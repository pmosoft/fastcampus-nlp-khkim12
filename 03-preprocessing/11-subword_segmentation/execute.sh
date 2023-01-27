cut -f2 ./review.sorted.uniq.refined.tsv > ./review.sorted.uniq.refined.tsv.text
cat ./review.sorted.uniq.refined.tsv.text | mecab -O wakati >  review.sorted.uniq.refined.tsv.text.tok
cat ./review.sorted.uniq.refined.tsv.text | mecab -O wakati | python post_tokenize.py ./review.sorted.uniq.refined.tsv.text > ./review.sorted.uniq.refined.tsv.text.tok2
python ./subword-nmt/learn_bpe.py --input ./review.sorted.uniq.refined.tsv.text.tok2 --output ./model --symbols 30000
# python ./subword-nmt/learn_bpe.py --input D:/lge/pycharm-projects/fastcampus-nlp-khkim12/03-preprocessing/11-subword_segmentation/review.sorted.uniq.refined.tsv --output D:/lge/pycharm-projects/fastcampus-nlp-khkim12/03-preprocessing/11-subword_segmentation/model --symbols 30000

python ./subword-nmt/apply_bpe.py --codes ./model < ./review.sorted.uniq.refined.tsv.text.tok2 > ./review.sorted.uniq.refined.tsv.text.tok.bpe
# python ./subword-nmt/apply_bpe.py --codes D:/lge/pycharm-projects/Fastcampus-NLP12/03-preprocessing/11-subword_segmentation/model < D:/lge/pycharm-projects/Fastcampus-NLP12/03-preprocessing/11-subword_segmentation/review.sorted.uniq.refined.tsv.text.tok > D:/lge/pycharm-projects/Fastcampus-NLP12/03-preprocessing/11-subword_segmentation/review.sorted.uniq.refined.tsv.text.tok.bpe

apply_bpe.py model 내에 HF(09h) 값은 공백으로 보이나 처리가 되지 않으므로 . 으로 변경하여 처리