data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data)) 
print('檔案讀取完畢,留言共計有', len(data), '筆資料')

wc = {} #word_count 
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])
#print(len(wc))
#print(wc['Rex'])

while True:
	word = input('你想查什麼字: ')
	if word == 'q':
		print('感謝使用本查詢')
		break
	if word in wc:
		print(word,'出現過的次數為', wc[word], '次')
	else:
		print('沒有出現過')















# sum_len = 0
# for d in data :
# 	sum_len += len(d)
# print('留言總字數', sum_len)
# print('每筆平均留言字數', int(sum_len/len(data)),'個字' )


# nice = [d for d in data if'nice' in d]
# print('提到nice的留言共有', len(nice),'筆資料')

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('提到good的留言共有', len(good),'筆資料')

# bad = ['bad' in d for d in data]
# print(len(bad))





