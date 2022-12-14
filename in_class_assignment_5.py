#Problem 1:
#References (if any):
#https://realpython.com/python-recursion/ (P.S. Thanks Brianna)
#https://vegibit.com/how-to-read-and-write-files-in-python/
#https://www.geeksforgeeks.org/reading-writing-text-files-python/

import re

#GIVEN: quicksort function
def quicksort(numbers_in_a_list):
    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list
    
    else:
        numArray = numbers_in_a_list[0]
        num1 = []
        num2 = []
        
        for x in range(1, len(numbers_in_a_list)):
            if numbers_in_a_list[x] < numArray:
                num1.append(numbers_in_a_list[x])
                
            if numbers_in_a_list[x] > numArray:
                num2.append(numbers_in_a_list[x])
                
    #GIVEN: Return statement
    return quicksort(num1) + [numArray] + quicksort(num2)

#Reads in numbers.txt
def read_numbers_txt(readNumbers):
    nums = []
    with open(readNumbers) as file_object:
        numLine = file_object.readLine()
        fileNumbers = re.findall("[0-9]+", numLine)
        
        for y in fileNumbers:
            y = int(y)
            nums.append(y)
    return nums

#Writes the resulting output into sorted.txt
def write_sorted_txt(writeSorted, fileNumbers):
    with open(writeSorted, "w") as sorted_numbers:
        for b in quicksort(fileNumbers):
            b = str(b)
            sorted_numbers.write(f"{b}\n")
            
#GIVEN: main function
def main():
    fileNumbers = read_numbers_txt("C:\Users\Ky-long-PC\INFO450\numbers.txt") #Calls the read function for numbers.txt
    
    #GIVEN: Return statement
    return write_sorted_txt("C:\Users\Ky-long-PC\INFO450\sorted.txt", fileNumbers) #Calls the write function for sorted.txt

#GIVEN:
if __name__ == "__main__":
    main()
