import psycopg2
import random
import hashlib

def main():
    
    #password validation to avoid publishing the postgreSQL password in the repository
    pw = input("enter the password indicated in the submission notes")
    
    validation_hash = "11e1dd56e313c7c3eccf7a30dbeaa98ae40f513a93fadddec7599cdcb58aedf4"   
    pw_hash = hashlib.sha256(pw.encode("utf-8")).hexdigest()

    if pw_hash != validation_hash:
        print("incorrect password")
        return
    
    #setting up the connection to the database using psycopg
    conn = psycopg2.connect(
		dbname= "A2Q1",  
		user="postgres",   
		password= pw,  
		host="localhost",       
		port="5432"  
	)
    cur = conn.cursor()
    
    #main event loop which sets up the CLI. you can execute any of the 4 functions in this loop. It works by parsing the user input for function parameters
    while True:
        print("1. getAllStudents")
        print("2. addStudent")
        print("3. updateStudent")
        print("4. deleteStudent")
        print("5. quit")
        choice = int(input("Select what function to call."))
        
        if choice == 1:
            getAllStudents(cur)
        elif choice == 2:
            params = input("enter a frist name, last name, email and enrollment_date all space separated to add a student")
            paramsList = params.split(" ")
            addStudent(cur, conn, paramsList[0], paramsList[1], paramsList[2], paramsList[3])
        elif choice == 3:
            params = input("enter the student ID and new email for the student whose email is to be updated all space separated")
            paramsList = params.split(" ")
            paramsList[0] = int(paramsList[0])
            updateStudentEmail(cur, conn, paramsList[0], paramsList[1])
        elif choice == 4:
            params = input("enter the ID of the student you want to remove")
            deleteStudent(cur, conn, int(params))
        elif choice == 5:
            break
            
        else:
            print("invalid  choice")
    
    cur.close()
    conn.close()
    
    print("done")

    #very simple query, just return everything from the students table and print it using a for loop. fetchall() gets everything from the query
def getAllStudents(curs):
    
    curs.execute("SELECT * FROM students;")
    rows = curs.fetchall()

    for row in rows:
        print(row)
    
def addStudent(curs, connec, fName, lName, e, ed):
    
    #input validation to ensure a properly formatted date is provided
    if ed.count("-") != 2:
        print("invalid date format")
        return
    
    #parse the date input
    year = ed.split("-")[0]
    month = ed.split("-")[1]
    day = ed.split("-")[2]
    
    illegalPairs = [(2, 30), (2, 31), (4, 31), (6, 31), (8, 31), (9, 31), (11, 30)]
    
    if year.isdigit() and month.isdigit() and day.isdigit():
        
        x = (month, day)
        
        if (int(day) < 32 and int(day) > 0) and (int(month) < 13 and int(month) > 0) and x not in illegalPairs:
            
            #once the date has been validated, the query can be created using placeholder variables
    
            query = '''INSERT INTO students (first_name, last_name, email, enrollment_date)
                            VALUES (%s, %s, %s, %s)'''

            #here, the user provided values are subbed into the query and the query is executed and committed
            curs.execute(query, (fName, lName, e, ed))
            connec.commit()
            
            print("Added the student")
    
    else:
        print("invalid date")

def updateStudentEmail(curs, connec, sID, sEmail):
    
    #a query is constructed to first check if a student with the given ID exists in the table
    
    checkQuery = "SELECT student_id FROM students WHERE student_id = %s LIMIT 1;"
    
    curs.execute(checkQuery, (str(sID),))
    
    result = curs.fetchone()
    
    #if the query returns nothing, result will be a nonetype and we exit the function
    if result is None:
        print("unable to update since student not found")
        return
    
    #otherwise, the first element of the result will be the ID we want and we construct a query to update that student with the email parameter
    if result[0] == sID:
    
        query = "UPDATE students SET email = %s WHERE student_id = %s"
        
        curs.execute(query, (sEmail, sID))
        connec.commit()
        print("updated")
        
    else:
        print("ID not in table")

def deleteStudent(curs, connec, sID):
    #same logic as update, only this we delete instead of update 
    
    checkQuery = "SELECT student_id FROM students WHERE student_id = %s LIMIT 1;"
    
    curs.execute(checkQuery, (str(sID),))
    
    result = curs.fetchone()
    
    if result is None:
        print("unable to delete since student not found")
        return
    
    if result[0] == sID:
    
        query = f"DELETE FROM students WHERE student_id = {sID}"
        
        curs.execute(query, (sID,))
        
        connec.commit()
    
    print("deleted")
    
main()   