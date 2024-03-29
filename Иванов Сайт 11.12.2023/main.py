from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def register():
    return render_template('registration.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
