# %% md
# Based on Context Window (Co-occurrence)
# %%
import pandas as pd
from collections import defaultdict

# %% md
## Read text
# %%
with open('review.sorted.uniq.refined.tsv.text.tok', encoding='utf-8') as f:
    lines = [l.strip() for l in f.read().splitlines() if l.strip()]

# %%
def get_term_frequency(document):
    term_freq = {}

    words = document.split()

    for w in words:
        term_freq[w] = 1 + (0 if term_freq.get(w) is None else term_freq[w])

    return term_freq

# %%
def get_context_counts(lines, vocab, w_size=2):
    context_cnt = defaultdict(int)

    for line in lines:
        words = line.split()

        for i, w in enumerate(words):
            if w in vocab:
                for c in words[i - w_size:i + w_size]:
                    if w != c:
                        context_cnt[(w, c)] += 1

    return context_cnt

# %%
def get_co_occurrence_df(context_cnt, vocab):
    data = []

    for word1 in vocab:
        row = []

        for word2 in vocab:
            try:
                count = context_cnt[(word1, word2)]
            except KeyError:
                count = 0
            row.append(count)

        data.append(row)

    return pd.DataFrame(data, index=vocab, columns=vocab)

# %% md
## Call methods

term_freq = pd.Series(
    get_term_frequency(' '.join(lines))
).sort_values(ascending=False)

term_freq


# %%
vector_size = 800

term_freq.index[:vector_size]
# %% md

context_cnt = pd.Series(
    get_context_counts(
        lines,
        term_freq.index[:vector_size],
        w_size=4
    )
)

context_cnt
# %%
term_freq.index[:vector_size]
# %% md
df = get_co_occurrence_df(context_cnt, term_freq.index[:vector_size])
df
# %%
df.values.shape
# %%
import torch

# %%
def get_l1_distance(x1, x2):
    return ((x1 - x2).abs()).sum()


# %%
def get_l2_distance(x1, x2):
    return ((x1 - x2) ** 2).sum() ** .5


# %%
def get_infinity_distance(x1, x2):
    return ((x1 - x2).abs()).max()

# %%
def get_cosine_similarity(x1, x2):
    return (x1 * x2).sum() / ((x1 ** 2).sum() ** .5 * (x2 ** 2).sum() ** .5 + 1e-10)

# %%
def get_nearest(query, dataframe, metric, top_k, ascending=True):
    vector = torch.from_numpy(dataframe.loc[query].values).float()
    distances = dataframe.apply(
        lambda x: metric(vector, torch.from_numpy(x.values).float()),
        axis=1,
    )
    top_distances = distances.sort_values(ascending=ascending)[:top_k]

    print(', '.join([f'{k} ({v:.1f})' for k, v in top_distances.items()]))

# %% md
## Show nearest neighbor of given word for each metric.
# %%
print('L1 distance:')
get_nearest('반품', df, get_l1_distance, 10)
print('\nL2 distance:')
get_nearest('반품', df, get_l2_distance, 10)
print('\nInfinity distance:')
get_nearest('반품', df, get_infinity_distance, 10)
print('\nCosine similarity:')
get_nearest('반품', df, get_cosine_similarity, 10, ascending=False)