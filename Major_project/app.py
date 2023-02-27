from flask import Flask,render_template,request,jsonify
import whisper
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/url',methods=['POST'])
def operation():
    if (request.method=='POST'):
        Upload_file=request.files['Upload_file']
        Upload_file.save(Upload_file.filename)
        model=whisper.load_model("base")
        result=model.transcribe(Upload_file.filename,fp16=False)
        text_result=result['text']
           
        return render_template('result.html',result=text_result)       











if __name__=='__main__':
    app.run(debug=True)