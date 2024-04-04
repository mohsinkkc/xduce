#==================== List =========================================

'''  
How do you iterate over elements in a list using loops in Python?
'''
list=[1,3,5,9,2,4,5,4]

for i in list:
    print(i)

''' 
 How do you sort a list in Python? Explain different sorting techniques available?
'''
list=[1,3,5,9,2,4,5,4]

list.sort()
print(list)

'''
Can you explain the difference between list.sort() and sorted() functions?


sort():method is a built-in method for lists in Python that sorts the elements of a list in place. It modifies the original list and doesn't return anything
sorted(): function takes a list and returns a new sorted list, leaving the original list unchanged
'''
'''
How do you find the length of a list in Python
'''
l1=[1,2,5,4,9,1,5,4,8,54]
print(len(l1))

#==================================== Tuple =================================================
'''
How do you create an empty tuple in Python
'''
l1=()

print(len(l1))

'''
Can you modify the elements of a tuple after it has been created? Why or why not?

No, we can't modified the tuple because the tuples are immutable 
'''

'''
 Explain the concept of indexing in tuples. How do you access elements in a tuple using indexing?
'''
l1=(1,2,5,1,2,4,'a','k','d')

print(l1[5])
print(l1[8])

'''
How do you convert a tuple into a list, and vice versa?
'''
l1=(1,2,5,4,2,54,1)
l2=list(l1)
print(l2)

#======================= Dictionary ==========================================
'''
dictionary-How do you create an empty dictionary in Python?
'''
l1={}

print(len(l1))

'''
Explain the difference between dict.keys() , dict.values() , and dict.items() methods.
'''

l1={"name":"mohsin","age":30,"address":"narol"}
#====keys======
print(l1)
print(l1.keys())
#=======values===
print(l1.values())
#=======items=====
print(l1.items())

'''
How do you iterate over key-value pairs in a dictionary using loops in Python?
'''
for key , values in l1.items():
    print(l1)
    break
'''
What are dictionary comprehensions? Provide an example
'''
d1={"gujrata":"ahmedabad","kerela":"kochi","goa":"bagha beach","maharastra":"mumbai"}
#dict={ key:experssion for in iterable}

d2={key:values for (key,values) in d1.items() }
print(d2)

# dict (if condtion) dict1={key: (condtion if/els) for (key,value) in dict }

l1={"kerela":60,"goa":55,"chennai":71,"gujarat":88,"maharastra":64}
l2={key: ("hot" if values>=60 else "cold") for (key,values) in l1.items()  }
print(l2)

# dict function dict1={key : funct for i in iterable}
def temp(values):
    if values > 80:
        return("hot")
    elif values<= 60 and values>=79:
        return("warm")
    else:
        return("cold")
l1={"kerela":60,"goa":55,"chennai":71,"gujarat":88,"maharastra":64}
l2={key:temp(values) for (key,values) in l1.items()}
print(l2)
#========================= Set ========================================

'''
How do you add elements to a set in Python?
'''
l1={'cat','dog','ant','elephant'}
l1.add("nine")
print(l1)

'''
Explain the difference between set.add() and set.update() methods.
'''
#==========.add() =========

l1.add("pq")
print(l1)

#========== .update() ============
l1.update("rabit")
print(l1)

'''
What are set comprehensions? Provide an example.
'''
l1={'cat','dog','ant','elephant'}
l2={i for i in l1}
print(l2)
