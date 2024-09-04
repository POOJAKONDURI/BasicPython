'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python program to 

'''


def leapyear(year):
    """
    Description :
        This function is used to find leap year.
    Parameters :
        year : year to check if it is a leap
    Return:
         It prints year is a leapyear if yes else it prints saying its not
    """
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0 and year%100 == 0):
        return True
    return False


def main():
    year = input("enter a year")
    if len(year) == 4:
        if leapyear:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print("enter a four digit year")


if __name__ =="__main__":
    main()


