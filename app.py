from flask import Flask
from flask import request, jsonify
from flask_mongoengine import MongoEngine
import jwt
from flask_sslify import SSLify


key_value = '000000111111'
api_keys = {
    'api_key': key_value
}

def validate_api_key(api_key):
    for key in api_keys:
        if api_keys[key] == api_key:
            return True
        else:
            return False


# function to verify token that return true or false
def verify_token(token, level_access):
    try:
        decoded = jwt.decode(token, 'lespapus', algorithms=['HS256'])
        print(decoded)
        if decoded['api_key'] == level_access:
            return True
        else:
            return False
    except:
        return False

app = Flask(__name__)
# HTTPS to secure communication client-server
sslify = SSLify(app)

@app.route('/group01')
def group01():
    # get token from header authorization
    token = request.headers.get('Authorization')
    # verify token
    if verify_token(token, 'basic'):
        return jsonify({'result': 'este es el grupo 01'})
    else:    
        return jsonify({'result': 'access denied'})

@app.route('/group02')
def group02():
    # get token from header authorization
    token = request.headers.get('Authorization')
    # verify token
    if verify_token(token, 'advanced'):
        return jsonify({'result': 'este es el grupo 02'})
    else:    
        return jsonify({'result': 'access denied'})

@app.route('/group03')
def group03():
    # get token from header authorization
    token = request.headers.get('Authorization')
    # verify token
    if verify_token(token, 'advanced'):
        return jsonify({'result': 'este es el grupo 03'})
    else:    
        return jsonify({'result': 'access denied'})

@app.route('/group04')
def group04():
    # get token from header authorization
    token = request.headers.get('Authorization')
    # verify token
    if verify_token(token, 'advanced'):
        return jsonify({'result': 'este es el grupo 04'})
    else:    
        return jsonify({'result': 'access denied'})

# get route to validate api key
@app.route('/validate_api_key')
def validate_api_key_route():
    api_key = request.args.get('api_key')
    print(api_key)
    if validate_api_key(api_key):
        # return jwt token
        print('create token')
        encoded_jwt = jwt.encode({'api_key': 'basic'}, 'lespapus', algorithm='HS256')
        print('return token')
        return jsonify({'result': 'valid', 'token': encoded_jwt})
    else:
        return jsonify({'result': 'invalid gg'})


if __name__ == "__main__":
    app.run(ssl_context='adhoc', debug=True, port=5000)

# readme 
# pip install flask
