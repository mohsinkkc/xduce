# 1) Getting Data Using Single Condition
# 2) Getting Data Using Multiple Condition : use &(and),|(or)
# 3) Adding Column
# 4) Function : apply(your_function_name)  
# 5) Save the modified DataFrame into New_File and Original File
# 6) Droping(Deleting) Row,columns : drop()


import pandas as pd

data=pd.read_excel('data.xlsx')
print(data)

#adding coloumn from existing Coloumn

data.loc[(data['Age'] < 30 ), "Category"] = "younger"
data.loc[(data['Age']> 30 , "Category")]="Older"
print(data)



#saving dataframe into new file from  Orginal file
data.to_csv('New_File.csv', index=False)  

data.to_csv('data.csv', index=False)


#drop something 
data.drop(2, inplace=True) 
print(data)

#function using in pandas

def Salary(a):
    if a <= 30:
        return 30000
    else:
        return 20000

data['Salary'] =  data['Age'].apply(Salary)
print(data)