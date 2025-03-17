from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/check_palindrome', methods=['POST'])
def check_palindrome():
   data = request.get_json()
   string = data.get('string', '')
   if string == string[::-1]:
       return jsonify({'result': 'Palindrome'}), 200
   else:
       return jsonify({'result': 'Not a palindrome'}), 200
