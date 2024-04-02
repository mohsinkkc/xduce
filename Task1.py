def odd(a):
    if a%2 ==0:
        print("the number is even")
    else:
        print("the number is odd")

def prime(a):
    if a%a==0  and a%2 != 0 :
        print("the number is prime number")
    else:
        print("the number is not prime")

def postive(a):
    if a>0 and a==0 :
        print("the number is positive ")
    else:
        print("the number is negative ")

def main():
    a = int(input("enter number:"))
    odd(a)
    prime(a)
    postive(a)

if __name__=="__main__":
    main()