def isPalindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    return s == s[::-1]

if __name__ == "__main__":
    print("Q8 - Valid Palindrome Output:", isPalindrome("A man, a plan, a canal: Panama"))