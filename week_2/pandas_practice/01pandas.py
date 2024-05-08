# Pandas: 
#    0) Pandas Installation , Importing into Python file
#    1) Series [Columns]
#    2) Data Frames [Combination of Multiple Series]
#    3) Reading Data from Excel Sheet
#    3) Reading Data from CSV File [Comma Separate Values]
#    4) Pandas Inbuilt Fns : count(),head(),tail(),value_counts(),sum(),max(),min(),mean()
#    4) Pandas attributes : shape,columns


import pandas as pd
import numpy as np

dict1={
    "name":["mohsin","devanshu","mohsin","harsh","faizan"],
    "age":[21,23,21,25,19],
    "address":["narol","kalupur","narol","CTM","Juhapura"],
}
# To get the Data / to Display the Datas
d=pd.DataFrame(dict1)
print(d)

#to convert into csv file 
d.to_csv('data.csv')#to remove the index number we use d.to_csv('data.csv',index=false)

#to see paticular line 
d1=d.head(2) #it will only show starting 2 rows
print("the starting 2 rows are :\n",d1)

d2=d.tail(2)#it will only show the last 2 elements
print("the last 2 rows is :\n",d2)

# To Read Data from excel file 
data=pd.read_excel('data.xlsx')
print("The Excel Files are :\n",data)

#to Read csv file
data1=pd.read_csv('data.csv')
print("The csv file are :\n",data1)

#to see the info and data type 
print(data1.info())
#to Access the sum of number or charcter 
print("the sum of value :\n",data1['age'].sum())
#to see value count
print(data1['age'].value_counts())

#to See Max value
print("the max value is:\n",data1['age'].max())

#minium value 
print("the minimum value :\n",data1['age'].min())

#mean()
print("the mean :\n",data1['age'].mean())

# to see any Duplicated value 
print(data1.duplicated())
#before duplicate removed
print("Before Duplicate remove:\n",data1)
#to remove duplictae value
print("after Duplicate remove :\n",data1.drop_duplicates('name'))

#to repalce duplicate items 
data['Age']=data['Age'].replace(np.nan,29)
print("The mean value is :\n",data['Age'].mean())
print(data)

# forward fill and Backward fill 
print("forward fill :\n",data.fillna(method="ffill"))
#backward fill 
print("the Backward fill :\n",data.fillna(method='bfill'))

#group by
gp=data.groupby(["Name","Location","Gender"]).agg({"Age":"count"})
gp1=data.groupby("Location").agg({"Age":"mean"})
print(gp)
print(gp1)
print()
print()

print()

data1={"Emp Id":['Emp01',"Emp02","Emp03","Emp04","Emp05"],
"name":["mohsin","dev","devanshu","abhishek","Harsh"],
"age":[25,23,28,31,38]}

data2={"Emp Id":["Emp01",'Emp02','Emp03','Emp04','Emp05','Emp06','Emp07'],
"Salary":[29000,23000,34000,21000,66000,25000,30000]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print()

print(df2)

d3=pd.merge(left=df1,right=df2,on = "Emp Id",how = "right").fillna(method="ffill")
print(d3)
#copy one element from other and chnaging value
d4=d3.copy()
d4.loc[6,"name"]="dev"

print(d4)
