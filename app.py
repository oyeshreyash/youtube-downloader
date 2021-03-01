from flask import Flask, render_template, request
import os
from pytube import YouTube

app = Flask(__name__)

user = os.getlogin()
path = r'c:\Users\{}\Downloads'.format(user)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download', methods=['POST', 'GET'])
def download():
    global path
    url = request.form['link']
    ytd = YouTube(url)
    music1 = ytd.streams.filter(only_audio=True, file_extension='mp4').first().download(path)
    return music1



if __name__ == '__main__':
    app.run(debug=True)