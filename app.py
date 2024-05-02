from flask import Flask, request, jsonify
from PIL import Image
from pix2tex.cli import LatexOCR

app = Flask(__name__)

model = LatexOCR()

"""
    A function that serves as the home route for the application.
    Returns:
        str: A string indicating that the server is running.
"""
@app.route('/')
def home():
    return 'Server is running!'

"""
    A function that serves as the home route for the application. This function handles POST requests to the root URL.
    It expects an image file to be uploaded as part of the request. If the image file is not present, it returns a JSON response with an error message.
    If the image file is present but has no filename, it also returns a JSON response with an error message.
    If the image file is valid, it attempts to open the image using the PIL library and passes it to the model for OCR.
    If any exception occurs during the OCR process, it returns a JSON response with the error message.
    If the OCR process is successful, it returns a JSON response with the LaTeX response from the model.
    
    Returns:
        flask.Response: A JSON response with either the LaTeX response or an error message.
"""
@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image_file = request.files['image']
    
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        image = Image.open(image_file)
        latex_response = model(image)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify({'latex': latex_response}), 200

if __name__ == '__main__':
    app.run(debug=True)
