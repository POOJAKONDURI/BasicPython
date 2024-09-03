'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''

class MonthlypayUtils:
    """
      utility class 
    """

    @staticmethod
    def payment(P,R,Y):
         
         """
        description:
            This prog is to give day of particular date 
        parameters:
            d,m,y
        return:
            Returns day of particular date
    """
         
         n = 12 * Y
         r = R / (12 * 100)
         payment = (P*r) / (1 - (1 + r)** -n)
         return payment
    

def main():
     P = float(input("enter p: "))
     R = float(input("enter R: "))
     Y = float(input("enter Y: "))
     res = MonthlypayUtils.payment(P,R,Y)
     print(f"monthly payments u have to pay is:{res:.2f}")


if __name__ == "__main__":
     main()
     

