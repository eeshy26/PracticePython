import os
import platform

global studentlist
studentlist=["Paul","Ella","Jim","Naomi","Lily","Max"]

def studentmenu():
    print("### This is the student menu ###")
    print("Enter 1: Show list of students")
    print("Enter 2: Add a student")
    print("Enter 3: Delete a student")
    print("Enter 4: Search for a student")
    print("Enter 5: Add a surname to a student\n")

    try:
            a=int(input("Enter a number from the options above \n"))
    except ValueError:
            exit("That's not right")
    else:
            print("\n")

    if(a==1):
            print("Student list \n")
            for students in studentlist:
                print("{}".format(students))
    elif(a==2):
            newstudent=input("Enter new student: ")
            if(newstudent in studentlist):
                print("This student is already in the list".
                    format(newstudent))

            else:

                    studentlist.append(newstudent)
                    print("Student {} has been added to list".
                            format(newstudent))
                    for students in studentlist:
                            print("{}".format(students))

    elif(a==4):
            searchstudent=input("Enter student name to search:")
            if(searchstudent in studentlist):
                    print("\n There is a record of student {}".
                          format(searchstudent))

            else:
                    print("\n There is no record of the student {}".
                          format(searchstudent))
    elif(a==3):
            deletestudent=input("Enter student name to delete:")
            if(deletestudent in studentlist):
                    studentlist.remove(deletestudent)
                    for students in studentlist:
                            print("{}".format(students))

            else:
                    print("\n The student {} has not been found".
                          format(deletestudent))

    elif(a==5):
            student_forename=input("Enter student forename: \n")
            if(student_forename in studentlist):
                    student_surname=input("Enter a surname for student "+student_forename+"\n")
                    format(studentlist.remove(student_forename))
                    format(studentlist.append(student_forename+student_surname))
                    for students in studentlist:
                        print("{}".format(students))
                    
                          
    
    elif(a<1 or a>5):
        print("Enter valid option")

studentmenu()

def Again():
    run=input("\n Do want to end the program?")
    if(run.lower()=="no"):
        if(platform.system()=="Windows"):
            print(os.system("cls"))
        else:
                print(os.system("clear"))
        studentmenu()
        Again()

    else:
            quit()

Again()
