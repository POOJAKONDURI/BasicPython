'''

    @Author:pooja
    @Date:27-08-2024
    @last modified by:pooja
    @last modified time:27-08-2024
    @title:program to find head and tail percentage on flip 

'''

def primefactors(N):
     """
        description:
            This prog to find prime factors of given number
        parameters:
            N: number to find prime factorization
        return:
            Returns prime factors
    """
     fact = []
     for i in range(2,int(N**0.5)+1):
      while N%i == 0:
         fact.append(i)
         N //= i

     if N>2:
        fact.append(N)  
     return fact    


def main():
   N = int(input("eneter number :"))
   if N > 1:
      res = primefactors(N)
      print(f"prime factors of {N} are {res}")
   else:
      print("enter number greater than 1")
   


if __name__ == "__main__":
   main()
     
     
     
