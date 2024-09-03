'''

    @Author:pooja
    @Date:27-08-2024
    @last modified by:pooja
    @last modified time:27-08-2024
    @title:program to find head and tail percentage on flip 

'''

def harmnum(N):
     """
        description:
            This prog to find harmonic value
        parameters:
            N: till which harmonic value to be found
        return:
            Returns Hamonic value
    """
     
     harm = 0
     for i in range(1,N+1):
        harm += 1/i
     print(f"nth harmonic value is: {harm}:.2f")


def main():
    N = int(input("enter N till wichto find harmonic value:"))
    if N>0:
        harmnum(N)
    else:
        print("please enter a positive value")

if __name__ =="__main__":
    main()