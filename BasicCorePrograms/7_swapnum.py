
'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python program to 

'''

def swap(a,b):
    """
        description:
            This prog to swap two numbers
        parameters:
            a and b : two numbers to swap
        return:
            Returns swapped numbers
    """
    a, b = b, a
    return a,b
    
    #  a = a + b
    #  b = a - b
    #  a = a - b
    #  return a, b


def main():
    a = int(input("enter num 1: "))
    b = int(input("enter num 2: "))
    a,b = swap(a,b)
    print(f"num1 becomes {a}")
    print(f"num2 becomes {b}")

if __name__ == "__main__":
    main()