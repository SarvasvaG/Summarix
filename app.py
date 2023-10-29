from flask import Flask,render_template,request,redirect,url_for
import summariser
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input',methods = ['GET','POST'])
def input():
    if request.method == 'POST':
        size = request.form['summarySize']
        s = request.form['inputText']
        f = request.files['documentUpload']
        summary = ""
        
        if(s):
            summary += summariser.funSum(s,size)
            return render_template('output.html',out = summary, inp = s)

        if(f):
            text = f.read().decode('utf-8')
            summary += summariser.funSum(text,size)
            return render_template('output.html',out = summary, inp = text)
                
    return render_template('input.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True,port=8080)