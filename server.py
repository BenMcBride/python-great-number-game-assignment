from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == session['random']:
        iscorrect = 'correct'
    elif int(request.form['guess']) > session['random']:
        iscorrect = 'high'
    else:
        iscorrect = 'low'
    return render_template('index.html', iscorrect = iscorrect)

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)