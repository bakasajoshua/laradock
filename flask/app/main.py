import pymysql
from app import app
from config import mysql
from flask import jsonify, request
# from flask import flash, request
		
@app.route('/', methods=['GET'])
def fetch():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, surname, email, telephone, username FROM users")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/records', methods=['POST'])
def query():
	try:
		conn = mysql.connect()
		cursor = conn.curson(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * from users")
		rows = cursor.fetchall()
		respone = jsonify(rows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)