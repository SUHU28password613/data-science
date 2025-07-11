from flask import Flask, render_template

app =  Flask(__name__)
app.secret_key = 'supersecretmre'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicepage')
def servicepage():
    return render_template('servicepage.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/registerpage')
def registerpage():
    return render_template('registerpage.html')


if __name__ =='__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)