from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/api/v1.0/calculate', methods=['POST'])
    @cross_origin()
    def retrieve_calculation():
        body = request.get_json()

        operation_type = body.get('operation_type')
        firstInt = body.get('x')
        secondInt = body.get('y')

        result = 0
        
        if operation_type != None and firstInt != None and secondInt != None:
              operation_type = operation_type.lower()
              if (operation_type == "addition" or operation_type == "subtraction" or operation_type == "multiplication"):\
                        if operation_type == "addition":
                            result = firstInt + secondInt
                        elif operation_type == "subtraction":
                            result = firstInt - secondInt
                        elif operation_type == "multiplication":
                            result = firstInt * secondInt
                    else:
                        abort(400)
                else:
                    abort(400)
            else:
                abort(400)
        except Exception as e:
            abort(400)
        
        return jsonify({
            'slackUsername': 'laolu',
            'result': result,
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)