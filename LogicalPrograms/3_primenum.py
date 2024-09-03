
'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''

def primenum(num):
    """
        description:
            This prog if num is a prime
        parameters:
            num : which is to be checked
        return:
            Returns mesage saying its a prime num
    """
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
        return True
    
def main():
    num = int(input("enter the number: "))
    if primenum(num):
        print(f"{num} is prime number")
    else:
        print(f"{num} is not a prime number")



if __name__ == "__main__":
    main()

      
      