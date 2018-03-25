# tex_assignment


Prerequisites:-
Need the following before running the code.
1. Python 3.5+
2. Postgresql 9.5
3. Install python dependencies from the requirements.txt file in the project using the command:-
>>>pip install -r requirements.txt

Steps:-
1. Create initial database:-
Edit the following line in alchemy.py to point to your installation of postgresql. Currently it has details of my user and database

   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gaurav:gaurav28@localhost/gaurav'

import the db object from an interactive Python shell and run the create_all() method to create the tables and database:
>>>from alchemy import db

>>>db.create_all()

2. read data from file and load into database:-
>>>python data_reader.py

3. Run Flask App:-
>>>python flask_api.py

4. To see the results with pagination, go to http://localhost:5000/
