COMP 3005 query program demo

This demo works with the Python library psycopg2 which it uses to communicate with the PostgreSQL db.
Documentation can be found here: https://pypi.org/project/psycopg2

Run Instructions:

- Make sure your machine has Python 3.4 or later installed along with pgAdmin4
- Open pgAdmin4 and create a new database according to the requirements of the spec.
- Ensure reqs are as follows:
- 
    	dbname= "A2Q1",  
		user="postgres",   
		password= pw,  
		host="localhost",       
		port="5432"
- pw will be in the submission notes  
- Download the python file from the repository and make note of where you store it
- Open a command prompt and install the psycopg library by running: pip install psycopg2
- Once installed, navigate to the directory where the COMP3005A3Q1.py file is stored
- Run with: python COMP3005A3Q1.py

Use instructions:
- Once running, input the password indicated in the submission notes when prompted.

- Select any of the options provided to run queries to alter the "students" table in the PostgreSQL db.





