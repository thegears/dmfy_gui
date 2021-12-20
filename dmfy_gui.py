import youtube_dl;
from tkinter import *;

def dmfy():
	if len(link.get()) == 0:
		pass;
	else:
		video_url = link.get();
		
		video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False);

		file_name = video_info["title"]+".mp3";

		with youtube_dl.YoutubeDL({'format':'bestaudio/best','keepVideo':False,"outtmpl":file_name}) as ydl:
			ydl.download([video_info["webpage_url"]]);


master = Tk();
master.title("DMFY");
master.geometry("250x100");
Label(master,text="Video's Link").pack();
link = Entry(master,width=230);
link.pack();
Button(master,text="Download",command=dmfy).pack();

master.mainloop();
