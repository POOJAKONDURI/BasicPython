'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python program to 

'''

def qorem(dividend,divisor):

     """
        description:
            This prog to find quotient and reminder
        parameters:
            divident and divisor
        return:
            Returns quotient and reminder
    """
     quotient = dividend//divisor
     reminder = dividend%divisor
     return quotient,reminder


def main():
     dividend = int(input("enter dividend:"))
     divisor  = int(input("enter divisor:"))
     if divisor != 0:
        quotient,reminder = qorem(dividend,divisor)
        print(f"quotient is {quotient}")
        print(f"reminder is {reminder}")
     else:
        print("enter positive number")


if __name__ == "__main__":
    main()
   
