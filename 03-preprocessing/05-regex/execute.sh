review.sorted.uniq.tsv 클린징 필요

# 아래 형식이어야 한다.
^(positive|negative)\t[^\t\n]+\t

# 클린징 대상 검색
^[^(positive|negative]+
\r

# 스페이스 검색
\s{1,}