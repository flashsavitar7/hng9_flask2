from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/', methods=['POST'])
def calculate():
    body = request.get_json()
    if body:
        operation_type = body.get('operation_type')
        x = body.get('x',)
        y = body.get('y',)
    else:
        operation_type = request.args.get('operation_type')
        x = request.args.get('x', type=int)
        y = request.args.get('y', type=int)

    result = 0
        
    if operation_type != None and x != None and y != None:
        operation_type = operation_type.lower()
        if (operation_type == "addition" or operation_type == "subtraction" or operation_type == "multiplication"):
                if operation_type == "addition":
                    result = x + y
                elif operation_type == "subtraction":
                        result = x - y
                elif operation_type == "multiplication":
                        result = x * y
                else:
                        abort(400)
        else:
            abort(400)
        
        return jsonify({
            'slackUsername': ' Triumph Edet',
            'result': result,
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)