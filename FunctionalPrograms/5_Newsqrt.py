'''

    @Author: Pooja 
    @Date: 28-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 28-08-2024
    @Title : Python program to 

'''

def Newtonsqrt(C):
      """
        description:
            This method is to generate square root of number using newton raphons method
        parameters:
            C : the number to find square root
        return:
            Returns square root of number
     """
      
      epsilon = 1e-15
      t = C
      while abs(t - C/t) > epsilon * t:
            t = (t+C/t)/2
      return t
    

def main():
      C = int(input("enter number to find sqrt"))
      res = Newtonsqrt(C)
      print(f"square root of given number using newton raphons:{res:.2f}")

if __name__ == "__main__":
      main()
      
      