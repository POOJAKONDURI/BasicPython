'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''


class TempconvUtils:
    """
        utility class
    """

    @staticmethod
    def tempcon(tempC):
        """
        description:
            This prog is to covert temp from cel to farenheoit
        parameters:
            tempC : temp in cels
        return:
            Returns temp in farenheit
    """
        tempF = (tempC * 9/5) + 32 
        return tempF
    

def main():
    temp = int(input("enter temperature in celsiuzs: "))
    converted  = TempconvUtils.tempcon(temp)
    print(f"temperature after conversion from celsius to farenheit is : {converted}")

    
if __name__ == "__main__":
    main()
