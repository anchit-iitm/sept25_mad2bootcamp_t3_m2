from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the LookBack App!"
    
@app.route('/about')
def about():
    return {"message": "This is the About page of the LookBack App!", "status": "success"}



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)