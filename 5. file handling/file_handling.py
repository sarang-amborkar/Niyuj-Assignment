"""
time interval, provide exception word lists.
Screen output: Display total and incremental number of words written to
target file. Total Exception words and words in incremental data.
Show incremental content written to target file
"""
import glob
from time import sleep

counter = 0
def file_op():
    exception_list = ["error" , "warm"]
    list_of_files = glob.glob('./*.txt')  # create the list of file

    total_words = 0
    total_exceptions = 0
    incremental_words = 0
    incremental_exceptions = 0
    for file_name in list_of_files:          #iterating on  files
        f2 = open(file_name, 'r')
        temp = f2.read()
        incremental_words = len(temp)
        
        for word in temp.split():
            if word in exception_list:
                incremental_exceptions += 1

        with open('output/output.txt', 'a') as f1:            # writing to one file
            f1.write(temp)
        f2.close()
        total_words += incremental_words
    total_exceptions += incremental_exceptions
        


        
    print("Incremental Words: ", incremental_words)
    print("Incremental Exception: ", incremental_exceptions)    
    print("Total Words: ", total_words)
    print("Total Exception: ", total_exceptions)
    print("###############################")
    global counter
    with open("output/output.txt", "r") as file:
        counter = file.tell()
            


def time_interval():
    while True:
        file_op()
        sleep(10)      #pause the program for 10 seconds on each iteration

if __name__=="__main__":
    time_interval()
    
    

