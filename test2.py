"""
The program is trying to display the number of grades, average grade and the percentage that are above average grade, using 
the Final.txt file. We first read in the text file Final.txt. then 
from the text file, we create a list of strings from each lines in the text file. Then, we create a dictionary the list. Once the text file 
has been read into memory, we close the file.To Start, we will assign the grades to list of integers between 1 and 24, and we can check to see
how many grades are above average i.e. 83.25. We intialize integer count to count the number of grades above average. If the grade is less 
than 83.25, then we do nothing. Otherwise if the grade is greater than 83.25, then add 1 to count. After we finish all 24, we divide the value
of count by 24 and multiply the answer with 100 and the result will be the percentage of grades above average.


"""