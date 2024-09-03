'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python program to 

'''

def evenodd(num):
    """
        description:
            This prog to check if num is even or odd
        parameters:
            num : to check
        return:
            Returns if num is even or odd
    """

    if num % 2 == 0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")


def main():
    num = int(input("enter num to check even odd: "))
    evenodd(num)

if __name__ == "__main__":
    main()