# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
string = input("enter the word "))
ans = isPalindrome(string)
 
if ans:
    print("Yes")
else:
    print("No")