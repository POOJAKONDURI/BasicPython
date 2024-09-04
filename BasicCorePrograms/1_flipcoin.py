'''

    @Author:pooja
    @Date:27-08-2024
    @last modified by:pooja
    @last modified time:27-08-2024
    @title:program to find head and tail percentage on flip 

'''


import random
def findheadtailper(flips):
    """
        description:
            This program gives head and tail percentage"
        parameters:
            Takes number of flips as parameter
        return:
            Returns haed and tail percentage on flips
    """

    

    heads = 0
    tails = 0
    val = random.randint(0,1)
    if val <0.5:
        heads += 1
    else:
        tails += 1
    headper = (heads/flips)*100
    tailper = (tails/flips)*100

    return headper,tailper


def main():
    flips = int(input("enter number of flips :"))
    headper,tailper = findheadtailper(flips)
    print(f"head percentage is {headper:.2f}")
    print(f"tail percentage: {tailper:.2f}")
    

if __name__ =="__main__":
    main()


    
    
