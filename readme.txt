INSTALLATION PROCESS:
python3
pip install flask
pip install pymysql
pip install flask_httpauth

import sql\database.sql to mysql

Start python launcher.py
http://[SERVER]:[PORT]/login
Basic auth: admin\Super123

Before for use - you should get session from /login
Header Data:
Content-Type: application/json
Authorization: Session from /login
http://[SERVER]:[PORT]/api
{
	'FirstName' : "admin"
}

http://[SERVER]:[PORT]/create_account
{
	'login': "USER_NAME",
	'password': "USER_PASSWORD" ,
	'first_name': "USER_FIRST_NAME",
	'last_name1': "USER_LAST_NAME",
}
