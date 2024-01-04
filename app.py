from flask import Flask, render_template, request, send_file
from stegano import lsb
from PIL import Image

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk proses penyisipan pesan
@app.route('/encrypt', methods=['POST'])
def encrypt():
    text_message = request.form['message']
    cover_image = request.files['cover_image']
    
    cover_image.save('static/cover.png')

    secret_image = lsb.hide('static/cover.png', text_message)
    secret_image.save('static/secret.png')

    return render_template('index.html', message="Pesan berhasil disisipkan!")

# Route untuk halaman ekstraksi
@app.route('/extract')
def extract():
    return render_template('extract.html')

# Route untuk proses ekstraksi pesan
@app.route('/extract', methods=['POST'])
def extract_message():
    uploaded_image = request.files['upload_image']
    uploaded_image_path = 'static/uploaded_image.png'
    uploaded_image.save(uploaded_image_path)

    # Ekstrak pesan dari gambar yang diunggah
    extracted_message = lsb.reveal(uploaded_image_path)

    return render_template('extract.html', extracted_message=extracted_message)

# Route untuk mengunduh gambar hasil penyisipan pesan
@app.route('/download')
def download():
    return send_file('static/secret.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    
