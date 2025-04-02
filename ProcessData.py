#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def makeID(first, last, num):
  while len(last) < 5:
    last = last + "x"
  last = last[0:5]

  last3 = num[-3:]

  id = first[0] + last + last3
  return id

def makeMajorYear(major, year):
  major3 = major[0:3]

  yearAbb = ""
  year = year.upper()
  if year == "FRESHMAN":
    yearAbb = "FR"
  elif year == "SOPHOMORE":
    yearAbb = "SO"
  elif year == "JUNIOR":
    yearAbb = "JR"
  elif year == "SENIOR":
    yearAbb = "SR"

  majorYear = major3 + yearAbb
  return majorYear

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for student in inFile:
    #student = "Antwan Dougherty AntwanDougherty@yahoo.com 443-13-3556 03/28/1996 Freshman Philosophy""""
    studentData = student.split()
    print(studentData)
    firstName = studentData[0]
    lastName = studentData[1]
    studentID = studentData[3]
    year = studentData[5]
    major = studentData[6]
    userID = makeID(firstName, lastName, studentID)
    majorYear = makeMajorYear(major, year)
    studentOutput = lastName + ","+ firstName + ","+ userID + majorYear + "\n"
    outFile.write(studentOutput)
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
