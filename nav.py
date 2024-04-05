def findSubjectIndex(listOfSubjects, numSubjects, subjectName):
    subjectIndex = -1
    for i in range(numSubjects):
        if listOfSubjects[i]["name"] == subjectName:
            subjectIndex = i
            break
    return subjectIndex