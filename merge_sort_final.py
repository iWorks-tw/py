number=[206,12,4,8,1,34,5,77,36,72,45,88,55,33,22]

def merge_sort(num):
	#宣告串列,
	list_spilt_L=[];list_spilt_R=[];merge_num=[];tempL=[];tempR=[];merge=[]
	#拆分待排序串列
	length=len(num)#取得串列長度
	middle=int(length/2)#取得串列長度中間值
	list_spilt_L=num[:middle]#串列前半部拆分至左串列
	list_spilt_R=num[middle:]#串列後半部拆分至右串列
	lengthL=len(list_spilt_L);lengthR=len(list_spilt_R)#取得左右串列元素個數
	countL=lengthL;countR=lengthR#複製一份給合併用
	tempL=list_spilt_L;tempR=list_spilt_R#複製一份給合併用
#拆分
	if lengthL>1:#如果左串列有兩個元素含以上，再放入merge_sort做拆分到只剩下一個元素
		list_spilt_L=merge_sort(list_spilt_L)#遞迴合併排序
		tempL=list_spilt_L#將回傳串列複製給暫存串列，合併用
		
	
	if lengthR>1:#如果右串列有兩個元素含以上，再放入merge_sort做拆分到只剩下一個元素
		list_spilt_R=merge_sort(list_spilt_R)#遞迴合併排序
		tempR=list_spilt_R#將回傳串列複製給暫存串列，合併用
		
	
	if lengthL==1 and lengthR==1:#單位元素比較，當左右串列都只有一個元素時，小的放入左串列，大的放入又串列
		if list_spilt_L[0]>list_spilt_R[0]:
			list_spilt_L[0],list_spilt_R[0]=list_spilt_R[0],list_spilt_L[0]
			
	#合併
	while countL>0 and countR>0:#此時以暫存串列進行合併程序，當左右串列都有元素時進行左右比較數值，最小的元素放入合併串列merge的第一個，後依序置入已完成合併程序
		
		if tempL[0]<tempR[0]:#比兩邊串列的首位元素，左邊小時處理下列程序
			merge.append(tempL[0])#小的加入合併串列merge後並刪除
			countL-=1#串列元素個數減1
			if countL>0:#若串列還存在就將放入merge的元素刪除，第二個元素的索引值變成0
				tempL.remove(tempL[0])
			if countL==0:#左暫存串列完全放入merge後成mull，串列元素＝0
				for c in range(countR):#右串列剩餘的元素依序合併到merge
					merge.append(tempR[c])
										
		else:#右邊串列首位元素小時執行下列程序，原理同上
			merge.append(tempR[0])#
			countR-=1#
			if countR>0:#
				tempR.remove(tempR[0])
			
			if countR==0:#
				for d in range(countL):
					merge.append(tempL[d])
		
	return merge#傳回合併後串列

number=merge_sort(number)
print(number)


			
		
