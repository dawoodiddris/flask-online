from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('home.html',name= 'Dawood')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login')

@app.route('/about')
def about():
    return 'This is about us'   

@app.route('/your-url', methods=['POST','GET'])
def shorten():
    if request.method == 'POST':
        return render_template('customurl.html', shoten=request.form['shorturl'])
    elif request.method == 'GET':
        #return redirect('/')
        return redirect(url_for('home'))
        #return render_template('customurl.html', shoten=request.args['shorturl'])
    else:
        return render_template('404.html')
 

