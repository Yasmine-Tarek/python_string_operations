
from string_ops import is_palindrome, solve, find_nth_occurrence, find_repetition

# To test the function with all test cases : Is it a palindrome

print(is_palindrome('a'))
print(is_palindrome('aba'))
print(is_palindrome('Abba'))
print(is_palindrome('malam'))
print(is_palindrome('walter'))
print(is_palindrome('kodok'))
print(is_palindrome('Kasue'))

# to test error block
print(is_palindrome(1))

print ("")

# To test the function with all test cases : Simple String Matching

print(solve("code*s", "codewars"))
print(solve("codewar*s", "codewars"))
print(solve("code*warrior", "codewars"))
print(solve("c", "c"))
print(solve("*s", "codewars"))
print(solve("*s", "s"))
print(solve("s*", "s"))
print(solve("aa", "aaa"))
print(solve("aa*", "aaa"))
print(solve("aaa", "aa"))
print(solve("aaa*", "aa"))
print(solve("*", "codewars"))
print(solve("*bc", "abcd"))

# to test error block
print(solve(1, "abcd"))

print ("")


# To test the function with all test cases : Find the nth Occurrence of a word in a string!

string = "This is an example. Return the nth occurrence of example in this example string."

print(find_nth_occurrence("example", string, 1))
print(find_nth_occurrence("example", string, 2))
print(find_nth_occurrence("example", string, 3))
print(find_nth_occurrence("example", string, 4))
print ("")
print(find_nth_occurrence("TestTest", "TestTestTestTest", 1))
print(find_nth_occurrence("TestTest", "TestTestTestTest", 2))
print(find_nth_occurrence("TestTest", "TestTestTestTest", 3))
print(find_nth_occurrence("TestTest", "TestTestTestTest", 4))

# to test error block
print(find_nth_occurrence(1, 1, 1))

print ("")

# To test the function with all test cases : Repeated Substring
print (find_repetition("ababab"))
print (find_repetition("abcde"))
print (find_repetition("abceeeabc"))

# to test error block
print (find_repetition(1))