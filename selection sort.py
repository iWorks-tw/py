num=[33,12,76,55,23,2,54]
#選擇排序Ｏ{n^2}
length=len(num)#取得串列列長度
for i in range(length): #雙迴圈排序出大小
	min_num=i#最小元素放置的串列索引值
	for j in range(i+1,length):#從i+1開始比
		if num[j]<num[min_num]:#最小的放入num[min_num]
			num[min_num],num[j]=num[j],num[min_num]#互換元素
print(num)#輸出排序結果		
