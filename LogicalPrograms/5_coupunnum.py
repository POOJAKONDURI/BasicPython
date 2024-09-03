
'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''

import random
class Coupunnum:
    @staticmethod
    def gen_random(N):
      """
        description:
            This method is to generate random number
        parameters:
            N : the number till which to geneerate random num
        return:
            Returns series of random numbers
     """
      
      return random.randint(1,N)
    

    @staticmethod
    def cuopun_gen(N):
       """
        description:
            This method is to generate N distinct couipuns
        parameters:
            N : distinct coupuns to generate
        return:
            Returns random nums needed to generate distinct coupuns
     """
       
       coulst = set()
       totalrandom_num  = 0
       while (len(coulst)<N):
          res = Coupunnum.gen_random(N)
          totalrandom_num += 1
          coulst.add(res)
       return totalrandom_num
    
def main():
    N = int(input("enter range of distincct coupuns : "))
    total_num = Coupunnum.cuopun_gen(N)
    print(f"the ranodm numbers needed to generate  distinct coupums are : {total_num}")


if __name__ == "__main__":
   main()

       

       
         
       
   
        
       
      

