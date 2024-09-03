'''

    @Author:pooja
    @Date:27-08-2024
    @last modified by:pooja
    @last modified time:27-08-2024
    @title:program to find head and tail percentage on flip 

'''


def largestamongthree(n1,n2,n3):
    """
        description:
            This program finds largest among three"
        parameters:
            n1,n2,n3: three num
        return:
            Returns num which is largest
    """

    
    if n1>n2 and n2>n3:
        print(f"{n1} is largest")
    elif n2>n1 and n2>n3:
        print(f"{n2} is largest")
    else:
        print(f"{n3} is largest")


def main():
    n1 = input("enter num1 : ")
    n2 = input("enter num2 : ")
    n3 = input("enter num3 : ")
    largestamongthree(n1,n2,n3)

if __name__ == "__main__":
    main()