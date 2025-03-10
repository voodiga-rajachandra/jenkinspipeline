from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    operation = request.args.get('operation', 'add')

    operations = {
        "add": num1 + num2,
        "subtract": num1 - num2,
        "multiply": num1 * num2,
        "divide": num1 / num2 if num2 != 0 else "Cannot divide by zero"
    }

    return jsonify({"result": operations.get(operation, "Invalid operation")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

