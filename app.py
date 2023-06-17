from flask import Flask, render_template, request, redirect
from pdf_reader import process

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        result = process(query)  # Call the process function from "query.py"
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()