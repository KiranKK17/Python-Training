#Write a function to check whether a number is prime or not.
# some more functions
def check_prime():
    num=int(input("Enter a number:"))
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                print(num,"is not prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
check_prime()
