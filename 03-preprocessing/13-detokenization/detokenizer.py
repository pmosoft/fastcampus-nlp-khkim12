import sys

STR = '▁'
TWO_STR = '▁▁'


def detokenization(line):
    if TWO_STR in line:
        line = line.strip().replace(' ', '').replace(TWO_STR, ' ').replace(STR, '').strip()
    else:
        line = line.strip().replace(' ', '').replace(STR, ' ').strip()

    return line


if __name__ == "__main__":
    # python. / detokenizer.py <./ review.sorted.uniq.refined.tok.bpe.tsv > review.sorted.uniq.refined.tok.bpe.detok.tsv

    fr = open('review.sorted.uniq.refined.tok.bpe.tsv', "r", encoding='utf-8')
    fw = open('review.sorted.uniq.refined.tok.bpe.detok.tsv', "w", encoding='utf-8')
    # for line in sys.stdin:
    for line in fr:
        if line.strip() != "":
            buf = []
            for token in line.strip().split('\t'):
                buf += [detokenization(token)]

            # sys.stdout.write('\t'.join(buf) + '\n')
            fw.write('\t'.join(buf) + '\n')
        else:
            # sys.stdout.write('\n')
            fw.write('\n')
