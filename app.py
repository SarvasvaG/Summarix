from flask import Flask,render_template,request
import summariser
import io
import PyPDF2
from docx import Document

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
            
            summary += summariser.funSum(text,size)
            return render_template('output.html',out = summary, inp = text,size = size)

        if(s):
            summary += summariser.funSum(s,size)
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
    app.run(debug=True,port=8080)