from flask import Flask

test = Flask(__name__)

@test.route('/')
def hello():
    return "Привет, мир!"


@test.route('/<name>')
def hello_name(name):
    return f"Привет, {name}!"


if __name__ == '__main__':
    test.run()
