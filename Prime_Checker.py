def is_prime(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
num=int(input("Enter a number to check whether it is prime: "))

if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


        
