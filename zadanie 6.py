#6. Ask the user for a string and print out whether this string is a palindrome or not.

string = input("Type a word and we will check if it's a palindrome")

if string[::-1] == string:
    print("This word is a palindrome")
else:
    print("Not a plindrome")
