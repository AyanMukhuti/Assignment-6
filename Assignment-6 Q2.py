def palindrome(string):
    string1=string[ : :-1]
    if string1==string:
        print("The given word is a palindrome.")
    else:
        print("The given word is not a palindrome.")
a=input("Enter any word:")
palindrome(a)
