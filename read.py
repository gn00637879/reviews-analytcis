data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完畢,留言共計有', len(data), '筆資料')

sum_len = 0
for d in data :
	sum_len += len(d)
print('留言總字數', sum_len)
print('每筆平均留言字數', int(sum_len/len(data)),'個字' )