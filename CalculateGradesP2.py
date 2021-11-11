# Code assumes that data in CSV file is validated in terms of format. Therefore 
# the focus is on processing to produce the required output.
#
#The grading system will be reviewed in December 2021

import csv

StudentRecord = []
NewStudentRecord = []
filename = "C:\MUNDA\TestPython\StudentMarksFile.csv"
newfilename = ("C:\MUNDA\TestPython\StudentGradesFile.csv") 
newheader = ['Firstname','Surname','Average','Grade']

# Open and read input file
with open (filename, "r") as csvfile :
    InputData = csv.reader(csvfile)
    header = next(InputData)
    startidx = 2

 # Open Output file and prepare in for writing output recs

    with open(newfilename, 'w', newline="") as csvfileout:
         OutputData = csv.writer(csvfileout)
         OutputData.writerow(newheader)

         for row in InputData :
             StudentRecord.append(row)
             marks = row[startidx:]
             totalmark = 0
             rowsize = len(row)
             subjectcnt = len(marks)

# Calculate the total marks for a student
             for idx in range(startidx, rowsize) :
                 totalmark = totalmark + float(row[idx])

# Calculate the average mark for a student

                 avmark = totalmark/subjectcnt 

# Determine Student's grade 

                 if avmark>=80.0 and avmark<=100.0:
                    studentgrade = 'A' 
                 elif avmark>=70.0 and avmark<79.9:
                      studentgrade = 'B' 
                 elif avmark>=60.0 and avmark<69.9:
                      studentgrade = 'C'
                 elif avmark>=50.0 and avmark<59.9:
                      studentgrade = 'D'
                 elif avmark>=40.0 and avmark<49.9:
                      studentgrade = 'E' 
                 elif avmark>=0 and avmark<39.9:
                      studentgrade = 'F' 
                 else:
                      studentgrade = 'UNKNOWN' 

                
             row.append(avmark)
             row.append(studentgrade)

#       Write Output Record
             OutputData.writerow((row[0], row[1], avmark, studentgrade))
#  