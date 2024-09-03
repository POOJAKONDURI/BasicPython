
'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''


def perfectnum(num):

    """
        description:
            This prog if num is a perfect square
        parameters:
            num : which is to be checked
        return:
            Returns mesage saying its a perfect num
    """


    res = 0
    for i in range(1,num):
        if num%i == 0:
            res += i
    if res == num:
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")


def main():
    num = int(input("enter number : "))
    perfectnum(num)

if __name__ == "__main__":
    main()
    

