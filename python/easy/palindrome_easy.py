def isPalindrome(x: int) -> bool:
    # cant be a palindrome if its a:
    # - negative
    # - zero
    # - ends with a zero
    if (x < 0 or x % 10 == 0 and x != 0):
        return False


    reverse = 0
    temp = x
    while temp > 0:
        rem = temp % 10
        reverse = reverse * 10 + rem
        temp =  temp // 10

    if reverse - x == 0:
        return True
    return False


if  __name__ == "__main__":
    print(isPalindrome(12321))  # True
    print(isPalindrome(1221))  # True
    # print(isPalindrome(-121))  # False
    # print(isPalindrome(10))  # False
    # print(isPalindrome(12321))  # True
    # print(isPalindrome(0))  # False