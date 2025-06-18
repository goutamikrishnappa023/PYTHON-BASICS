def generate_fibonacci(n):
    a=0
    b=1
    count=0

    if n<=0:
        print("Enter a positive number")
    elif n==1:
        print("Fibonacci sequence up to 1 term")
        print(a)
    else:
        print(f"Fibonacci sequence up to {n} termss:")
        while(count<n):
            print(a, end=" ")
            a,b=b,a+b
            count+=1

num=int(input(" Fibonacci upto which term "))
generate_fibonacci(num)
