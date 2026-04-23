student = {}

while True:
    print("\n=====Student Manager App=====")
    print("\n1. Add Student")
    print("\n2. View Student")
    print("\n3. Check Result")
    print("\n4. Exit")

    choise = input("\nEnter your choise: ")

    # add students
    if choise =="1":
        name = input("Enter Student Name: ")
        marks = int(input("Enter Student Marks: "))
        student[name] = marks
        print(f"{name} Successfully Added !")


    # view result 
    elif choise == "2":
        if not student:
            print("No Student Found !")
        else:
            for name, marks in student.items():
                print(name, ":" ,marks)
    
    # check results 
    elif choise == "3":
        name = input("Enter Student Name: ")

        if name in student:
            marks = student[name]

            if marks >=40:
                print("Pass")
            else:
                print("Fail")
        
        else: 
            print(f"{name} Not Found !")


    # exit 
    elif choise == "4":
        print("Exiting.....")
        break

else:
    print("Invalid Input !")

