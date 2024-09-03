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
    binary32 = binary.zfill(8)
    return binary32

def swapnibble(n):
    binary = tobinary(n)
    swapped = binary[4:]+binary[:4]
    return swapped

def poweroftwo(n):
    return n>0 and (n & (n-1))


def main():
    n = int(input("enter integer: "))
    bina = tobinary(n)
    print(f"binary number is:{bina} ")
    swa = swapnibble(n)
    print(f"after swaping :{swa}")
    numpower = poweroftwo(n)
    print(f"cheking if number is power : {numpower}")


if __name__ == "__main__":
    main()

      

