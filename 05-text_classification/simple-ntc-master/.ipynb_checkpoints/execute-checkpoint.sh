head -1 ./review.sorted.uniq.refined.tok.shuf.train.tsv
cut -f2 ./review.sorted.uniq.refined.tok.shuf.train.tsv | shuf | head -10 | python ./classify.py --model_fn ./models/review.pyh --gpu_id -1
echo "배송이 늦게 왔지만 제품 자체는 괜챦은 것 같네요." | mecab -O wakati | python ./classify.py --model_fn ./models/review.pyh --gpu_id -1
echo "배송이 늦게 왔지만 제품 자체는 정말 좋네요." | mecab -O wakati | python ./classify.py --model_fn ./models/review.pyh --gpu_id -1
echo "배송이 늦게 왔지만 제품 자체는 정말 짱 좋네요." | mecab -O wakati | python ./classify.py --model_fn ./models/review.pyh --gpu_id -1

python train.py --model_fn ./models/review.pth --train_fn ./data/review.sorted.uniq.refined.tok.shuf.train.tsv --gpu_id -1 --batch_size 128 --n_epochs 10
--word_vec_size 256 --dropout .3 --rnn --hidden_size 512 --n_layers 4 --cnn --window_sizes 3 4 5 6 7 8 --n_filters 128 128 128 128 128 128

torchtext.legacy.data.iterator.py dev batch 274 line breakpoint data 소트 확인
rnn.py forward 662 line breakpoint

head ./data/review.sorted.uniq.refined.tok.shuf.test.tsv | awk -F'\t' '{ print $2 }' | python classify.py --model ./models/model.pth --gpu_id -1 --top_k 1