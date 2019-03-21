data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('讀取完畢，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為：', sum_len / len(data))

new = []
for c in data:
	if len(c) < 100:
		new.append(c)
print('一共有', len(new), '筆資料小於100')

good = []
for g in data:
	if 'good' in g:
		good.append(g)
print('一共有', len(g), '筆留言說good')
