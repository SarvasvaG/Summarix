### What is Summarix?
"Summarix" or "AI Powered Document Summarizer" is a website for instant summary generation of any textual content, articles, research papers etc. It also allows to set size, type (paragraph or key points) and quality of summary to generate.

### Why Summarix?
In today's information-driven landscape, individuals and organizations grapple with the overwhelming influx of textual content, spanning research papers, articles, legal documents, and reports. This deluge of data presents a formidable challenge—how to discern and extract vital insights from extensive documents swiftly. The "AI-Powered Document Summarizer" seeks to address this challenge by offering an automated solution for distilling essential information into coherent, easily digestible summaries.

### Get Started
Before starting the below requirements, install python>=3.8.0 and pip from https://www.python.org/downloads/

1. Clone the repository https://github.com/SarvasvaG/Summarix by using the following bash command:
   
   ```console
   git clone https://github.com/SarvasvaG/Summarix
   ```

2. Install all the required packages by pip install command, as given in requirements.txt file. Alternatively, use the following command to install all the packages in the python environment:

   ```python
   pip install -r requirements.txt
   ```
   
3. After installing all the packages, add a python file, named ***secretsEmail.py***, in the same directory as app.py, containing email and password of the sender, through with the email will be sent to the respective user on submission of the contact form. For example,

   ```python
   password = "AG@123"
   email = "anvit_g@cs.iitr.ac.in"
   ```
   
4. Finally, run the application by the following python command:

   ```python
   python app.py
   ```
   The server will start running on the specified 8000 port. Open any browser and type  "http://localhost:8000/".
   **Congratulations! You have started the Summarix.** Try summarizing some documents and texts.

6. **About the contact form**
   The email, message and name of the user will be stored in a file named "Document.db" in "instance" folder in the same working directory as app.py.  

In case of any problem faced in Summarix, feel free to contact any member on the about page, either via email or any professional social media application. We are always there to help you.
