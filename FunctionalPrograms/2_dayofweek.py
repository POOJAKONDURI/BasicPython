
'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''

class DayofweekUtil:
    
    """ 
          utility class
    """
    def dayofweek(d,m,y):
         

      """
        description:
            This prog is to give day of particular date 
        parameters:
            d,m,y
        return:
            Returns day of particular date
    """
      
      y0 = y - (14 - m) // 12
      x = y0 + y0//4 - y0//100 + y0//400
      m0 = m + 12 * ((14 - m) // 12) - 2
      d0 = (d + x + 31*m0 // 12) % 7
      return d0

def main():
   d = 28
   m = 8
   y = 2024
   res = DayofweekUtil.dayofweek(d,m,y)
   print(f"the day on the given date month and year is,{res}")


if __name__ == "__main__":
   main()

