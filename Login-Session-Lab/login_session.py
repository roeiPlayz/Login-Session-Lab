from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods = ['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'POST':
		authorage = request.form['authorage']
		authorname = request.form['authorname']
		authormessage = request.form['authormessage']
		try:
			login_session['authorage'] = authorage
			login_session['authorname'] = authorname
			login_session['authormessage'] = authormessage
			return redirect(url_for('thanks'))
		except:
			return redirectq(url_for('error'))
	return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', authorage = login_session['authorage'], authorname = login_session['authorname'], authormessage = login_session['authormessage']) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)