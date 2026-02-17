from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Face Recognition attendance system'

if __name__ == '__main__':
    app.run(debug=True)