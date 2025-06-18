def is_palindrome(text):
    cleaned_text=text.replace(" "," ").lower()

    if cleaned_text==cleaned_text[::-1]:
        return True
    else:
        return False

user_input=input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("Not a palindrome")
