from flask import Flask, render_template, request

app = Flask(__name__)

#routes
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    pass

  if request.method == 'POST':
    request.form.get('name')

  return render_template('index.html')
