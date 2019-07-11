from flask import Flask, Response, jsonify, request
import json
import psycopg2

app = Flask(__name__)

languages = []
connection = psycopg2.connect(user="postgres",
                                  password="7788",
                                  host="127.0.0.1",
                                  database="demodb")
cursor = connection.cursor()

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/person', methods=['GET'])
def returnAll():
	sql_select_query = """select * from person"""
	cursor.execute(sql_select_query)
	record = cursor.fetchall()
	print(record)

	return jsonify(record)



@app.route('/person', methods=['POST'])
def addOne():
	request_data = request.get_json()

	#id = request_data['id']
	firstName = request_data['firstname']
	lastName = request_data['lastname']
	mail = request_data['email']

	#print(id)
	print(firstName)
	print(lastName)
	print(mail)

	postgres_insert_query = """ INSERT INTO person (firstname, lastname, email) VALUES (%s,%s,%s)"""
	insert_tuple = (firstName, lastName, mail)
	cursor.execute(postgres_insert_query, insert_tuple)
	connection.commit()
	count = cursor.rowcount
	print(count, "Record inserted successfully into person table")

	return jsonify({'Person' : request_data})


if __name__ == '__main__':
	app.run(debug=True, port=8080)