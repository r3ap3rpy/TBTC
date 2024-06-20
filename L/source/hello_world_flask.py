from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello!"

@app.route("/world")
def world():
    return "World!"

@app.route("/items")
def items():
    item_id = request.args.get('id')
    return f"This is item: {item_id}"

@app.route("/user/<int:user_id>", methods = ["POST"])
def users(user_id):
    return f"User with ID: {user_id}"

if __name__ == '__main__':
    app.run("0.0.0.0", port = 8000)
