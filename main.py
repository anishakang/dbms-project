from flask import Flask, Response, render_template, jsonify
from backend import queries


from flask import Flask

app = Flask(__name__)
  

@app.route('/')

def index() :
   return render_template("index.html")

def hello_world():
    return 'Hello World'
  

if __name__ == '__main__':
  
    
    app.run()
