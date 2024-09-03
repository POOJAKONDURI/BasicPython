'''

    @Author: Pooja 
    @Date: 29-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 29-08-2024
    @Title : Python program to 

'''


def tobinary(n):
      """
        description:
            This method is to generate square root of number using newton raphons method
        parameters:
            C : the number to find square root
        return:
            Returns square root of number
     """
      binary = bin(n)[2:]
      binary32bit = binary.zfill(32)
      return binary32bit


def main():
      n = int(input("enter integer number: "))
      res = tobinary(n)
      print(f"decimal of number in 32bit is : {res}")
      


if __name__ == "__main__":
      main()
      