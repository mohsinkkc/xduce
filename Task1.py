def odd(a):
    if a%2 ==0:
        print("the number is even")
    else:
        print("the number is odd")

def prime(a):
    if a==1:
        print("the number is not prime number")
    elif a>1:
        for i in range(2,a):
            if (a%i) == 0:
                print("the number is not prime number")
                break
            else:
                print("the number is prime")
                break
    

def postive(a):
    if a>0 and a==0 :
        print("the number is positive ")
    else:
        print("the number is negative ")
    
def palidrome(b):
    if b == b[::-1]:
        print("it is palidrome")
    else:
        print("not palidrome")


def main():
    a = int(input("enter number:"))
    b=input("enter the word :")
    #odd(a)
    prime(a)
    #postive(a)
    palidrome(b)

if __name__=="__main__":
    main()