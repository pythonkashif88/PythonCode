# PythonAssignment5
# Get the student Record details

def getStudentDetails():
    vStudentDetails = {
        "Kashif": [45, 50, 60],
        "Roshan": [40, 35, 50],
        "John":   [20, 35, 45]
    }
    vSubjects = ["English", "Maths", "Science"]
    print("Please Select the Students Name from below List:")
    print()
    for id, student in enumerate(vStudentDetails.keys(), start=1):
        print(f"{id}. {student}")
    print()
    vInput = input("Enter the Student Name: ")

    if vInput in vStudentDetails:
        marks = vStudentDetails[vInput]
        
        for subjects in vSubjects:
            print(f"{subjects:<10}",end = ' ')
        print()    
        for vMarks in marks:
            print(f"{vMarks:<10}",end = ' ')
        print()    
        
    else:
        print(f"Sorry the student {vInput} is not found in our records")

getStudentDetails()


# 2 Creating Dynamic number list, extracting 5 elements and reverse the elements
def listSlicing():
    vList = []
    for newList in range(1,11):
        vList.append(newList)
    print(f"Original List\n {vList}")
    vList = vList[0:5]
    print(f"Extracting first five elemets from above dynamic list:\n {vList}")
    #vList = vList[::-1] # OR
    vList.reverse()
    print(f"Reverse the elemets from above list:\n {vList}")
        
listSlicing() 