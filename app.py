from flask import Flask, request, jsonify

app = Flask(__name__)

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if the string is the same when reversed

@app.route("/check_palindrome", methods=["POST"])
def check_palindrome():
    data = request.get_json()
    if "input" not in data:
        return jsonify({"error": "Please provide an 'input' field in the request body."}), 400

    input_str = data["input"]
    if is_palindrome(input_str):
        return jsonify({"input": input_str, "is_palindrome": True, "message": "Yes, it's a palindrome!"})
    else:
        return jsonify({"input": input_str, "is_palindrome": False, "message": "No, it's not a palindrome."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
