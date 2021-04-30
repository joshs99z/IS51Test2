"""
The program is trying to display the number of grades, average grade and the percentage that are above average grade, using 
the Final.txt file. We first read in the text file Final.txt. then 
from the text file, we create a list of strings from each lines in the text file. Then, we create a dictionary the list. Once the text file 
has been read into memory, we close the file.To Start, we will assign the grades to list of integers between 1 and 24, and we can check to see
how many grades are above average i.e. 83.25. We intialize integer count to count the number of grades above average. If the grade is less 
than 83.25, then we do nothing. Otherwise if the grade is greater than 83.25, then add 1 to count. After we finish all 24, we divide the value
of count by 24 and multiply the answer with 100 and the result will be the percentage of grades above average.


"""
"""
main():
Set dictionary = open(infile)
calculate_percentage_above_average(percentage,dictionary)

open(infile):
read in Final.txt
create list = each line from file
close the file
create a dictionary of the list 
return the dictionary

calculate_percentage_above_average(percentage,dictionary):
percentage = percentage of grades above average.
number = for each of the grade in the percentage
M = the total of grade above average divide by total grades for each grade,
if grade < 83.25:
    the return 
otherwise if grade > 83.25,
then num=num+1
return num
otherwise if grade = 83.25
then return.
if (num=0)
 then return num
otherwise if (num>0)
M = num / 24
 percentage = M * 100
return percentage


"""

