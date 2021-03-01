from flask import Flask, render_template, request
from pytube import YouTube
from android.storage import primary_external_storage_path
from android.permissions import request_permissions, Permission

request_permissions([Permission.WRITE_EXTERNAL_STORAGE])

primary_ext_storage = primary_external_storage_path()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download', methods=['POST', 'GET'])
def download():
    global path
    url = request.form['link']
    ytd = YouTube(url)
    music1 = ytd.streams.filter(only_audio=True, file_extension='mp4').first().download(primary_ext_storage)
    return music1



if __name__ == '__main__':
    app.run(debug=True)