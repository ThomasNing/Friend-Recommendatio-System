import numpy as np
import pandas as pd
from array import array
import xlrd

def compareSchool(rows,size,numberCol,numberRows,friend,a,i):
	

	b=2
	#i=0
	j=0
	k=0

	while b<size:
		if rows[a]==rows[b]:
			
	   		friend[i][j]=rows[b-2]+rows[b-1]
	   		b=b+numberCol
	   		j=j+1

		else:
			b=b+numberCol
	
	for k in range(numberRows):
		#print(k)
	   	if (rows[a-2]+rows[a-1])==friend[i][k]:
	   		#print(k)
	   		friend[i][k]=0
	if a==(len(rows)-4):
		print('I have finished your friend recommendation based on your school')
	else:
		a=a+numberCol
		i=i+1
		
		
		return compareSchool(rows,size,numberCol,numberRows,friend,a,i)
	
	return friend

def printout(friend,numberRows,numberCol,choice2):
	print('Here are the recommendations:')
	j=0
	for j in range(numberCol):
		if friend[choice2-1][j]!=0:
			print(friend[choice2-1][j])

def printName(rows,numberCol):
	number=0


	for t in range(0,len(rows),numberCol):
		number=number+1
		
		print(number,'.',rows[t],' ',rows[t+1],'\n')
			
			

def compareIncome(rows,size,numberCol,numberRows,friend,a,i):
	

	b=3
	#i=0
	j=0
	k=0

	while b<size:
		if rows[a]-rows[b]<=20000 and rows[a]-rows[b]>=(-20000) and rows[a]-rows[b]!=0:
			
			
	   		friend[i][j]=rows[b-3]+rows[b-2]
	   		b=b+numberCol
	   		j=j+1

		else:
			b=b+numberCol
	
	for k in range(numberRows):
		#print(k)
	   	if (rows[a-3]+rows[a-2])==friend[i][k]:
	   		#print(k)
	   		friend[i][k]=0
	if a==(len(rows)-3):
		print('I have finished your friend recommendation based on your school')
	else:
		a=a+numberCol
		i=i+1
		
		
		return compareIncome(rows,size,numberCol,numberRows,friend,a,i)
	
	return friend

def compareState(rows,size,numberCol,numberRows,friend,a,i):
	

	b=4
	#i=0
	j=0
	k=0

	while b<size:
		if rows[a]==rows[b]:
			
			
	   		friend[i][j]=rows[b-4]+rows[b-3]
	   		b=b+numberCol
	   		j=j+1

		else:
			b=b+numberCol
	
	for k in range(numberRows):
		#print(k)
	   	if (rows[a-4]+rows[a-3])==friend[i][k]:
	   		#print(k)
	   		friend[i][k]=0
	if a==(len(rows)-2):
		print('I have finished your friend recommendation based on your school')
	else:
		a=a+numberCol
		i=i+1
		
		
		return compareState(rows,size,numberCol,numberRows,friend,a,i)
	
	return friend

def comparePhone(rows,size,numberCol,numberRows,friend,a,i):
	

	b=5
	#i=0
	j=0
	k=0
	
	while b<size:
		if (round(rows[a]/10**8))-round((rows[b]/10**8))==0:
			print(rows[a])
			
	   		friend[i][j]=rows[b-5]+rows[b-4]
	   		b=b+numberCol
	   		j=j+1

		else:
			b=b+numberCol
	
	for k in range(numberRows):
		#print(k)
	   	if (rows[a-5]+rows[a-4])==friend[i][k]:
	   		#print(k)
	   		friend[i][k]=0
	if a==(len(rows)-1):
		print('I have finished your friend recommendation based on your school')
	else:
		a=a+numberCol
		i=i+1
		
		
		return comparePhone(rows,size,numberCol,numberRows,friend,a,i)
	print(friend)
	return friend

loc = ("/home/student/ee355/PA3/workbook.xlsx") 
  	
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
  
# Extracting number of rows 
numberRows=sheet.nrows
numberCol=sheet.ncols


rows=list()
#the friend recommendation list
friend = [[0 for i in range(numberRows)] for j in range(numberRows)] 

#print(numberRows)
for i in range (numberRows):
	for j in range(numberCol):
		rows.append(sheet.cell_value(i,j))
	#rows=map(rows,sheet.row_values(i))

size1=len(rows)
#When the users preference is for the school
a=2


print('There are a few options of friend recommendations for you to choose:\n 1. based on your school\n 2. based on the income\n 3. based on State \n 4. based on phone number\n 5. automatic friend recommendation')
choice=input('Please give me your choice: ')
if choice==1:
	compareSchool(rows,size1,numberCol,numberRows,friend,a,0)
	
	print('Here is the name list\n')
	printName(rows,numberCol)
	choice2=input('give me the number that you want to see his/her friend recommendation list: ')
	printout(friend,numberRows,numberCol,choice2)

if choice==2:
	a=3
	compareIncome(rows,size1,numberCol,numberRows,friend,a,0)
	printName(rows,numberCol)
	choice2=input('give me the number that you want to see his/her friend recommendation list: ')
	printout(friend,numberRows,numberCol,choice2)
	
if choice==3:
	a=4
	compareState(rows,size1,numberCol,numberRows,friend,a,0)
	printName(rows,numberCol)
	choice2=input('give me the number that you want to see his/her friend recommendation list: ')
	printout(friend,numberRows,numberCol,choice2)
if choice==4:
	a=5
	comparePhone(rows,size1,numberCol,numberRows,friend,a,0)
	printName(rows,numberCol)
	choice2=input('give me the number that you want to see his/her friend recommendation list: ')
	printout(friend,numberRows,numberCol,choice2)

#for the last function if the data size is large enough I could combine all the previous conditions together or select some of those conditions out