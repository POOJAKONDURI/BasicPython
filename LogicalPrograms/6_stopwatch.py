'''

    @Author: Pooja 
    @Date: 27-08-2024
    @Last Modified by: Pooja 
    @Last Modified time: 27-08-2024
    @Title : Python p
    rogram to 

'''
import time
class Stopwatch:
    @staticmethod
    def start_stopwatch():
        """
            description:
                This prog if num is a perfect square
            parameters:
                num : which is to be checked
            return:
                Returns mesage saying its a perfect num
        """
        
        start_time = time.time()
        print("stopwatch started")
        return start_time

    @staticmethod
    def stop_stopwatch(start_time):
        """
            description:
                This prog if num is a perfect square
            parameters:
                num : which is to be checked
            return:
                Returns mesage saying its a perfect num
        """

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("stopwatch stopped")
        return elapsed_time


def main():
    print("press enter start time")
    start_time = Stopwatch.start_stopwatch()
    print("press enter stop time")
    elapsed_time= Stopwatch.stop_stopwatch(start_time)
    print(f"time in between is {elapsed_time:.2f}")


if __name__ == "__main__":
    main()
        