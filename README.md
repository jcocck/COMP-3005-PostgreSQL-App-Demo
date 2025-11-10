COMP 3005 query program demo

This demo works with the Python library psycopg2 which it uses to communicate with the PostgreSQL db.
Documentation can be found here: https://pypi.org/project/psycopg2

Run Instructions:

- Make sure your machine has Python 3.4 or later installed along with pgAdmin4
- Open pgAdmin4 and create a new database according to the requirements of the spec. Make sure that the table is named "students" and that all of the columns are correctly named. When prompted, input your username, password and the name of the database.
- Ensure fields in the connection tab are as follows:
- 
		host="localhost",       
		port="5432"
- Download the python file from the repository and make note of where you store it
- Open a command prompt and install the psycopg library by running: pip install psycopg2
- Once installed, navigate to the directory where the COMP3005A3Q1.py file is stored
- Run with: python COMP3005A3Q1.py

Use instructions:
- Once running, input the correct data into each field as you are prompted
- Select any of the options provided to run queries to alter the "students" table in the PostgreSQL db.

Video link: https://www.dropbox.com/scl/fi/9j257i6n7ryies6epsdky/2025-11-09-20-45-55.mp4?rlkey=l1kb4nk9hmajmn0pwgpity8d5&st=khofeij0&dl=0








