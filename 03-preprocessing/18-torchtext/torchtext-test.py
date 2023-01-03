import sys
sys.path.insert(0,'D:/lge/pycharm-projects/fastcampus-nlp-khkim12/03-preprocessing/18-torchtext/')
# %%
from data_loader import DataLoader

# %% md
## Load TSV data
# %%
loaders = DataLoader(
    train_fn='D:/lge/pycharm-projects/fastcampus-nlp-khkim12/03-preprocessing/18-torchtext/review.sorted.uniq.refined.tok.shuf.train.tsv',
    batch_size=256,
    valid_ratio=.2,
    device=-1,
    max_vocab=999999,
    min_freq=5,
)
# %% md
### Check loader
# %%
print("|train|=%d" % len(loaders.train_loader.dataset))
print("|valid|=%d" % len(loaders.valid_loader.dataset))
# %%
print("|vocab|=%d" % len(loaders.text.vocab))
print("|label|=%d" % len(loaders.label.vocab))
# %% md
### Get mini-batch tensors
# %%
data = next(iter(loaders.train_loader))

print(data.text.shape)
print(data.label.shape)
# %% md
### Use vocab
# %%
dir(loaders.text.vocab)
# %%
loaders.text.vocab.stoi['배송']
# %%
loaders.text.vocab.itos[16]
# %% md
#### Check most frequent words
# %%
for i in range(50):
    word = loaders.text.vocab.itos[i]
    print('%5d: %s\t%d' % (i, word, loaders.text.vocab.freqs[word]))
# %% md
#### Restore text from tensor
# %%
print(data.text[-1])
# %%
x = data.text[-1]
line = []
for x_i in x:
    line += [loaders.text.vocab.itos[x_i]]

print(' '.join(line))
# %%