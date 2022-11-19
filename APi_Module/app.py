from flask import Flask, request

database = {'wahid': '100', 'ahmed': '141'}

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '1'


# initialize flask app

if __name__ == '__main__':
    app.run()


@app.route('/getdata/', methods=['GET'])
def getdata():
    return database

# api/adddata?name=id


@app.route('/adddata/', methods=['PUT'])
def add_data():
    key, value = list(request.args.items())[0]
    print("Key is ", key)
    return f"{key} added "


# api/deletedata?user=name
@app.route('/deletedata/', methods=['DELETE'])
def delete_data():
    _, value = list(request.args.items())[0]
    print(value)
    database.pop(value)
    return f"{value} deleted.."


if __name__ == '__main__':
    app.run()
