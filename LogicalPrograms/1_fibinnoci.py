
'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python program to 

'''

def fibbinocci(N):
    
     """
        description:
            This prog to find fibinocci series
        parameters:
            N: till whoch to find fibinocci
        return:
            Returns fibinocci series
    """
     lst = []
     a,b = 0,1
     for i in range(N+1):
        lst.append(a)
        a,b = b,a+b
     return  lst
    #  a, b = 0, 1
    #  print(a, end=" ")
    #  if n > 1:
    #     print(b, end=" ")
    #  for _ in range(2, n):
    #     a, b = b, a + b
    #     print(b, end=" ")


    # if n <= 1:
    #     return n
    # else:
    #     return fibonacci(n - 1) + fibonacci(n - 2)



    # a, b = 0, 1
    # while True:
    #     yield a
    #     a, b = b, a + b


def main():
    N = 5
    lst = fibbinocci(N)
    print(f"fibinoocu of {N} is {lst}")

if __name__ == "__main__":
    main()