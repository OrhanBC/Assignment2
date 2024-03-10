from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return "<h1>Welcome to my CSCB20 website!</h1>"

@app.route('/<name>')
def greet(name):
    return user(name)

def user(name):
    new_name = "<h1>Welcome, "
    if name.isupper() and name.isalpha():
        new_name += name.lower()
    elif name.islower() and name.isalpha():
        new_name += name.upper()
    else:
        is_first = False
        for letter in name:
            if (letter.isalpha()):
                if (not is_first):
                    new_name += letter.upper()
                    is_first = True
                else:
                    new_name += letter.lower()
    new_name += ", to my CSCB20 website</h1>"
    print(new_name)
    return new_name

if __name__ == '__main__':
    app.run()