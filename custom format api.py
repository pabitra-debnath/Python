from flask import Flask, Response, jsonify, request
import json

app = Flask(__name__)

languages = []

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})

@app.route('/lan', methods=['POST'])
def addOne():
	request_data = request.get_json()
	'''language = {
		'name' : request_data['name']
	}
	languages.append(request_data)
	return jsonify({'languages' : languages})

	
	return Response(json.dumps(json_data).encode('UTF 8', 'strict'), mimetype='application/json')
	
	'''
	data_key = list(request_data.keys())
	data_value = list(request_data.values())

	json_data = {
		"key" : data_key,
		"data" : data_value
	}
	languages.append(json_data)
	return Response(json.dumps(json_data).encode('UTF 8', 'strict'), mimetype='application/json')


if __name__ == '__main__':
	app.run(debug=True, port=8080)