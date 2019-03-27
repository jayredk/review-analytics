
# Read file
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('讀取完畢，總共有', len(data), '筆資料')

# Build dictionary
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

# Average length
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

while True:
	word = input('請輸入想找的字： ')
	if word == 'q':
		print('感謝使用查詢服務')
		break
	if word in wc:
		print(word, '一共出現了', wc[word], '次')
	else:
		print('找不到這個字哦！')






