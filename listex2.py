s=input("ENter a string to check whether it is a palindrome")
c=s[::-1]
if c==s:
    print("Yes! it is a Palindrome")
else:
    print("It is not a palindrome")