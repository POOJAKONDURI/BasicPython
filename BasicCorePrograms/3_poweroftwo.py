'''

    @Author:pooja
    @Date:27-08-2024
    @last modified by:pooja
    @last modified time:27-08-2024
    @title:program to find head and tail percentage on flip 

'''


def poweroftwo(N):

    """
        description:
            This program 2 to power table"
        parameters:
            N: power till which table of two exponent
        return:
            Returns table of powers of two
    """

    
    for i in range(0,N+1):
        res = 2**i
        print(f"2**{i}={res}")

def main():
    N = int(input("enter number till wich u want exp table"))
    poweroftwo(N)
    


if __name__ =="__main__":
    main()