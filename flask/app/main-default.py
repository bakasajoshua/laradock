# from flask import Flask, jsonify, request

# app = Flask(__name__)

# Student = [
# {
# 'id': 1,
# 'firstName': 'Aditya',
# 'lastName': 'Malviya',
# 'age': '24'
# },
# {
# 'id': 2,
# 'firstName': 'Aman',
# 'lastName': 'Mehta',
# 'age': '25'
# },
# {
# 'id': 3,
# 'firstName': 'Nuclear',
# 'lastName': 'Geeks',
# 'age': '26'
# }
# ]

# @app.route("/")
# def hello():
#     return "Hello World from Flask in a uWSGI Nginx Docker container with \
#      Python 3.7 (from the example template)"

# @app.route('/Student/', methods=['GET'])
# def students():
# 	return jsonify({'tasks': Student})

# @app.route('/Student/', methods=['POST'])
# def add_tasks():
# 	student = {
#      	'id': Student[-1]['id'] + 1,
# 		'firstName': request.json.get('firstName', ""),
#      	'lastName': request.json.get('lastName', ""),
#      	'age': request.json.get('age', 0)
# 		}
# 	Student.append(student)
# 	return jsonify({'student': student, 'all': Student}), 201

# if __name__ == "__main__":
#     # Only for debugging while developing
#     app.run(host="0.0.0.0", debug=True, port=80)
