'''
    checking the number is odd or even
'''
def odd(a):
    if a%2 ==0:
        print("the number is even")
    else:
        print("the number is odd")
'''
program of prime number or not
'''
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
    
'''
checking whether given is positive or negative
'''
def postive(a):
    if a>0 and a==0 :
        print("the number is positive ")
    else:
        print("the number is negative ")
 #======================================== palidrome ==============================================================   

def palidrome(b):
    if b == b[::-1]:
        print("word is palidrome")
    else:
        print("word is not palidrome")

#===========================================================================================================
'''
 another methode of checking the palidrome number 
'''
def is_pali(a):
    temp = a
    reverse = 0
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10
    return reverse == a


#=================================================================================================================
'''
main section where the each and every function has been called here
'''
def main():
    # a = int(input("enter number:"))
    #b=int(input("enter the word :"))
    a=5
    b=9
    odd(a)
    prime(a)
    postive(a)
    palidrome(b)
    if is_pali(a):
        print(" it is a palindrome!")
    else:
        print(" it's not a palindrome.")

if __name__=="__main__":
    main()