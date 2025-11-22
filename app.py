from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return jsonify(message="welcome to the home page!")

if __name__ == '__main__':
    # app.run()# production mode
    app.run(debug=True)  # development mode