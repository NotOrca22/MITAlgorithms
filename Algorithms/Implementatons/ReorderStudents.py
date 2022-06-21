def reorderStudents(studentList):
    centerIndex = len(studentList)//2
    section1 = studentList[:centerIndex+1]
    section2 = studentList[centerIndex+1:]
    return section1 + list(reversed(section2))
print(reorderStudents([5,3,12,5,20,51,1]))