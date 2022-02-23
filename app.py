from urllib import response
from flask import Flask,render_template,request,redirect,flash, send_file
# from music import *
from utils import *
import os
from werkzeug.utils import secure_filename

def generate(x):
    from magenta.models.melody_rnn import melody_rnn_generate
    melody_rnn_generate.main.config="basic_rnn"
    melody_rnn_generate.FLAGS.bundle_file="basic_rnn.mag"
    melody_rnn_generate.FLAGS.output_dir="./tmp/melody_rnn/generated"
    melody_rnn_generate.FLAGS.num_outputs=1
    melody_rnn_generate.FLAGS.num_steps=150
    melody_rnn_generate.FLAGS.primer_midi="./uploads/"+x
    melody_rnn_generate.console_entry_point()


app=Flask(__name__)
app.config['UPLOADS_FOLDER']=UPLOADS_FOLDER
app.config['SECRET_KEY'] = 'gaurav'


@app.route("/", methods=["GET","POST"])
def hello():
    if request.method=="GET":
        return render_template("index.html")

    if not 'file' in request.files:
        flash("No FIle")
        return redirect(request.url)

    file = request.files.get('file')
    if file.filename == '':
        flash('No file uploaded')
        return redirect(request.url)

    if file_valid(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
        try:
            generate(file.filename)
        except:
            # flash('Uploaded Succesfully')
            path="tmp/melody_rnn/generated/"+file.filename[0:-4]+"_converted_1.mid"
            return send_file(path,as_attachment=True)
        
    else:
        flash('File type not supported')
        return redirect(request.url)
   
    

# @app.route("/generate_melody",methods=["GET","POST"])
# def generatemusic():
        
#     p="tmp/melody_rnn/generated/"+"2_converted_1.mid"
#     return send_file(p,as_attachment=True)
    
    
    
    
    




if __name__=="__main__":
    app.run(debug=True)


