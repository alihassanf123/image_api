from flask import Flask, render_template, request,jsonify
# from tensorflow.keras.preprocessing.image import load_img,img_to_array
# print("hELLO")
# from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file_():
   return "Hello"

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']

#       return jsonify({"message":f.filename})