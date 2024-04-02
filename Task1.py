def odd(a):
    if a%2 ==0:
        print("the number is even")
    else:
        print("the number is odd")

def prime(a):
    if a%a == 0 and a%2 != 0 :
        print("the number is prime number")
    else:
        print("the number is not prime")

def main():
    a = int(input("enter number:"))
    odd(a)
    prime(a)

if __name__=="__main__":
    main()