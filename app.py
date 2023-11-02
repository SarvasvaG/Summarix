from flask import Flask,render_template,request
import io
import PyPDF2
from docx import Document
from flask_sqlalchemy import SQLAlchemy
import datetime

import extractive
import Email
# from transformers import pipeline,AutoModelForSeq2SeqLM
# model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# model_ckpt = "google/flan-t5-base"
# pipe = pipeline('summarization', model=model_ckpt)


# import model
# import testm

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DocSummary.db"
db.init_app(app)


class Inst(db.Model):
    name = db.Column(db.String, primary_key=True)
    email = db.Column(db.String,nullable = False)
    message = db.Column(db.String,nullable = False)
    time_created = db.Column(db.DateTime, default=datetime.datetime.now())


@app.route('/',methods = ['GET','POST'])
def index():
    with app.app_context():
        db.create_all()
    if(request.method == 'POST'):
        name = request.form['name']
        message = request.form['message']
        email = request.form['email']
        inst_first = Inst(name= name,message = message,email = email)
        db.session.add(inst_first)
        db.session.commit()

        Email.transfer(email)
    return render_template('index.html')

@app.route('/input',methods = ['GET','POST'])
def input():
    if request.method == 'POST':
        size = request.form['summarySize']
        s = request.form['inputText']
        f = request.files['documentUpload']
        summary = ""
        
        if(not s and not f):
            return render_template('output.html', out = summary,inp = s,size = size) 
        
        # Priority given to Document
        if(f):
            uploaded_file_contents = f.read()

            if (f.filename.endswith('.pdf')):
                text = extract_text_from_pdf(uploaded_file_contents)
            elif f.filename.endswith('.docx'):
                text = extract_text_from_docx(uploaded_file_contents)
            else:
                text = extract_text_from_txt(uploaded_file_contents)
            
            summary += extractive.summarize(text,size,"para")
            print(summary)
            return render_template('output.html',out = summary, inp = text,size = size)

        if(s):
            summary += extractive.summarize(s,size,"para")
            print(summary)
            return render_template('output.html',out = summary, inp = s,size = size)
        
        summary = ""
        f = None
    return render_template('input.html')

@app.route('/about')
def about():
    return render_template('about.html')

def extract_text_from_pdf(pdf_content):
    text = ""
    pdf_file = io.BytesIO(pdf_content)  # Create an in-memory file-like object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_content):
    text = ""
    doc = Document(io.BytesIO(docx_content)) 
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def extract_text_from_txt(txt_content):
    return txt_content.decode('utf-8')  


if __name__ == "__main__":
    app.run(debug=True,port=8000)