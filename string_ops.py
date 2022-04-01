# Is it a palindrome ?
# Write a function that checks if a given string (case insensitive) is a palindrome.

def is_palindrome (text):
    try:
        if text.lower() == (text[::-1]).lower():
            return True
        else:
            return False
    except:
        print ("You Enter Wronge Input. Please Enter a String")
  

# Simple String Matching


def solve(strng1,strng2):
    try:
        if "*" in strng1:
            return strng2.startswith(strng1.split("*")[0]) and strng2.endswith(strng1.split("*")[1])

        if strng1 == strng2:
            return True

        if "*" not in strng1:
            return False
    except:
        print("You Enter Wronge Input. Please Enter a String")

# Find the nth Occurrence of a word in a string!


def find_nth_occurrence(substring, string, occurrence=1):
    try:
        x = string.find(substring) 
        y = string.find(substring, x+1)
        z = string.find(substring, y+1)
        r = string.find(substring, z+1)

        if occurrence == 1:
            return x
        elif occurrence == 2 :
            return y
        elif occurrence == 3 :
            return z
        elif occurrence > 3 :
            return r
    except:
        print("You Enter Wronge Input. Please Enter a String")



# Repeated Substring 


def find_repetition(txt):
    try:
        for i in range (1, len(txt)+1):
            substr = txt[:i]
            if substr * (len(txt) // i ) == txt:
                return substr , txt.count(substr)
        return txt , txt.count(txt)
    except:
        print("You Enter Wronge Input. Please Enter a String")
