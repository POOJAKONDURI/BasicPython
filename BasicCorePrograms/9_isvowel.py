'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python program to 

'''
def isvowel(s):
      """
        description:
            This prog to check if num is even or odd
        parameters:
            num : to check
        return:
           message saying character is a vowel
     """
      vowel = 'aeiou'
      if s in vowel:
            print(f"{s} is a vowel ")
      else:
            print(f"{s} is not a vowel")

        
def main():
      s = input("enter an alphabet: ")
      isvowel(s)


if __name__ == "__main__":
      main()
                  