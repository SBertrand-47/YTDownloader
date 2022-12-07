import tkinter
from tkinter import *
import youtube_dl


class YouTubeDownloaderGUI:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Downloader")

        self.label = Label(master, text="Enter the URL of the YouTube video you want to download")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.download_button = Button(master, text="Download", command=self.download)
        self.download_button.pack()

    def download(self):
        video_url = self.entry.get()

        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])


root = Tk()
my_gui = YouTubeDownloaderGUI(root)
root.mainloop()