

'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''

def reversenum(num):

    """
        description:
            This prog if num is a prime
        parameters:
            num : which is to be checked
        return:
            Returns mesage saying its a prime num
    """
    rev_num = 0 
    while num > 0:
        rem = num%10
        rev_num = rev_num * 10 + rem
        num //= 10
    return rev_num

def main():
    num = int(input("enter number: "))
    res = reversenum(num)
    print(f"{num} after reversing is {res}")


if __name__ == "__main__":
    main()

       