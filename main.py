from flask import Flask


# 3 ------------------------
app = Flask(__name__)

# 4 ----------------------------
@app.route('/')
def hello_flask():
    return 'Hello, Flask'

@app.route('/user/<name>')
def greet_user(name):
    return f'Hello, {name}!'

if __name__ == '__main__' :
    app.run(debug=True)

