from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'tries' not in session:
        session['tries'] = 0
    if 'random' not in session:
        session['random'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['tries'] += 1
    if int(request.form['guess']) == session['random'] and session['tries'] <= 5:
        iscorrect = 'correct'
    elif int(request.form['guess']) > session['random'] and session['tries'] <= 5:
        iscorrect = 'high'
    elif int(request.form['guess']) < session['random'] and session['tries'] <= 5:
        iscorrect = 'low'
    else:
        iscorrect = 'game_over'
    return render_template('index.html', iscorrect = iscorrect, tries = session['tries'])

@app.route('/leaderboard', methods=['POST'])
def addLeader():
    if 'leaders' not in session:
        session['leaders'] = {request.form['leader_name']: session['tries']}
    else:
        session['leaders'][request.form['leader_name']] = session['tries']
    return render_template('leaderboard.html', tries = session['tries'], leaders = session['leaders'])

@app.route('/reset', methods=['POST'])
def reset():
    if 'leaders' in session:
        leaders = session['leaders']
        session.clear()
        session['leaders'] = leaders
    else:
        session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)