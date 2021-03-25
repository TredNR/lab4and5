import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

#Запросы к таблице с людьми
		
@app.route('/add_emp', methods=['POST'])
def add_emp():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_phone = _json['phone']
		_address = _json['address']
		if _name and _email and _phone and _address and request.method == 'POST':			
			sqlQuery = "INSERT INTO rest_emp(name, email, phone, address) VALUES(%s, %s, %s, %s, %s)"
			bindData = (_name, _email, _phone, _address)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('Employee added successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/emp')
def emp():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone, address FROM rest_emp")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/emp/<int:id>')
def emp_id(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone, address FROM rest_emp WHERE id =%s", id)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update_emp', methods=['PUT'])
def update_emp():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_email = _json['email']
		_phone = _json['phone']
		_address = _json['address']
		if _name and _email and _phone and _address and _id and request.method == 'PUT':			
			sqlQuery = "UPDATE rest_emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
			bindData = (_name, _email, _phone, _address, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('Employee updated successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
	#emp()

@app.route('/delete_emp/<int:id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM rest_emp WHERE id =%s", id)
		conn.commit()
		respone = jsonify('Employee deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

#Экран "привет"

@app.route('/')
def index():
    return "Last laboratory work by Ivanov, Lapenkov!"

#Запросы к таблице с файлами

@app.route('/file')
def file():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, file_name, data, extencion FROM file")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/file/<int:id>')
def file_id(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, file_name, data, extencion FROM file WHERE id =%s", id)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/add_file', methods=['POST'])
def add_file():
	try:
		_json = request.json
		_file_name = _json['file_name']
		_data = _json['data']
		_extencion = _json['extencion']
		if _file_name and _data and _extencion and request.method == 'POST':
			sqlQuery = "INSERT INTO file(file_name, data, extencion) VALUES(%s, %s, %s, %s)"
			bindData = (_file_name, _data, _extencion)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('Employee added successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/update_file', methods=['PUT'])
def update_file():
	try:
		_json = request.json
		_id = _json['id']
		_file_name = _json['file_name']
		_data = _json['data']
		_extencion = _json['extencion']
		if _file_name and _data and _extencion and _id and request.method == 'PUT':
			sqlQuery = "UPDATE rest_emp SET file_name=%s, data=%s, extencion=%s WHERE id=%s"
			bindData = (_file_name, _data, _extencion, _id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('Employee updated successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
	#emp()

@app.route('/delete_file/<int:id>', methods=['DELETE'])
def delete_file(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM file WHERE file_name =%s", id)
		conn.commit()
		respone = jsonify('Employee deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		
if __name__ == "__main__":
    app.run(debug=True)
