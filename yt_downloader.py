import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from pytube import YouTube
import subprocess
import os

def choose_directory():
    download_path = filedialog.askdirectory()
    download_path_var.set(download_path)

def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path=download_path_var.get())
    
def download_audio():
    url = url_entry.get()
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=download_path_var.get())
    
    audio_file = download_path_var.get() + '/' + yt.title + '.' + audio_stream.subtype
    
    output_file = download_path_var.get() + '/' + yt.title + '.mp3'
    
    subprocess.run(['ffmpeg', '-i', audio_file, output_file])
    
    video_file = download_path_var.get() + '/' + yt.title + '.mp4'
    if os.path.exists(video_file):
        os.remove(video_file)
    
root = tk.Tk()
root.title("YouTube Downloader")

url_label = tk.Label(root, text="Insira a URL do YouTube:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

choose_directory_button = tk.Button(root, text="Escolha o diretório do donwload:", command=choose_directory)
choose_directory_button.pack()

download_path_var = tk.StringVar()
download_path_label = tk.Label(root, textvariable=download_path_var)
download_path_label.pack()

video_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
video_button.pack()

audio_button = tk.Button(root, text="Baixar Áudio (MP3)", command=download_audio)
audio_button.pack()

root.mainloop()
