from flexidb import get_database
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
db = get_database("mongodb", uri="mongodb://localhost:27017", database="Rdoc")


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == 'main':
    app.run(debug=True)
    
    
