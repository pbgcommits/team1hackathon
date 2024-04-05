"""Test data for app."""

numSubjects = 4
listOfSubjects = []
tmpImageURI = "img/unimelblogo.png"
for i in range(1, numSubjects + 1):
    subject = "Subject " + str(i)
    listOfSubjects.append({
        "name": subject, 
        "code": "COMP1000" + str(i), 
        "teachingPeriod": {
            "year": 2024, "semester": 1
            },
        "imgURI": tmpImageURI
        })