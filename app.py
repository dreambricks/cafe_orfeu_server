from flask_socketio import SocketIO
from flask import Flask, url_for, send_file, render_template, redirect, request, abort

import parameters
import utils
from qrcodeaux import generate_qr_code
from udp_sender import UDPSender
import uuid
import os
import time
import shutil
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = 'dbsupersecretkey'
socketio = SocketIO(app)

udp_sender = UDPSender()

valid_links = {}

MAX_LINKS = 5

IMAGE_BASE_FOLDER = os.path.join(app.root_path, 'static', 'download_images')


def remove_old_folders():
    current_time = time.time()
    directory = 'static/download_images'
    minutes = 10

    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)

        if os.path.isdir(folder_path):
            creation_time = os.path.getctime(folder_path)
            time_difference = (current_time - creation_time) / 60

            if time_difference > minutes:

                shutil.rmtree(folder_path)
                print(f'A pasta "{foldername}" foi excluída.')
            else:
                print(f'A pasta "{foldername}" foi criada há menos de {minutes} minutos.')


scheduler = BackgroundScheduler()
scheduler.add_job(remove_old_folders, 'interval', minutes=2)
scheduler.start()


@app.route('/')
def index():
    return "Alive"


@app.route('/alive')
def alive():
    return "Alive"


@app.route('/generate', methods=['GET'])
def generate():
    if len(valid_links) >= MAX_LINKS:
        valid_links.clear()
        print("Lista de links esvaziada para evitar sobrecarga.")

    link_id = str(uuid.uuid4())
    link = url_for('terms', link_id=link_id, _external=True)

    valid_links[link_id] = True

    qr_img = generate_qr_code(link)

    return send_file(qr_img, mimetype='image/png')


@app.route('/qrcode-images', methods=['GET'])
def qrcode_images():
    cod = request.args.get('cod')
    if not cod:
        abort(400, description="O parâmetro 'cod' é obrigatório.")

    url = f"{parameters.BASE_URL}/download-images?cod={cod}"

    img_bytes = generate_qr_code(url)

    socketio.emit('render_images')

    return send_file(img_bytes, mimetype='image/png')


@app.route('/download-images')
def download_images():
    cod = request.args.get('cod')
    folder_path = os.path.join(IMAGE_BASE_FOLDER, cod)

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        abort(404, description="Folder not found.")

    zip_buffer = utils.create_zip_of_images(folder_path)

    zip_filename = f"{cod}_images_cafeorfeu.zip"
    return send_file(zip_buffer, mimetype='application/zip', as_attachment=True, download_name=zip_filename)


@app.route('/terms/<link_id>')
def terms(link_id):
    if valid_links.get(link_id):
        return render_template('terms.html', link_id=link_id)
    else:
        return redirect(url_for('error'))


@app.route('/accept/<link_id>', methods=['POST'])
def accept(link_id):
    if valid_links.get(link_id):
        valid_links[link_id] = False
        socketio.emit('invalidate_link', {'link_id': link_id}, to='/')

        return redirect(url_for('play'))
    else:
        return redirect(url_for('error'))


@app.route('/deny', methods=['POST'])
def deny_btn():
    return redirect(url_for('deny'))


@app.route('/play')
def play():
    return render_template("play.html")


@app.route('/deny')
def deny():
    return render_template("deny.html")


@app.route('/error')
def error():
    return render_template("error.html")


@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')


@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', allow_unsafe_werkzeug=True)
