from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input',methods = ['GET','POST'])
def input():
    if request.method == 'POST':
        s = request.form['inputText']
        f = request.files['documentUpload']
        return render_template('output.html',st = s,file = f)
    return render_template('input.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True,port=8080)