from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from os import path
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from os import listdir
from os.path import isfile, join
from tkinter import Tk
from tkinter.filedialog import askdirectory
from moviepy.editor import *
from moviepy.editor import VideoFileClip
import moviepy.editor as mpe
import moviepy.editor as mp

#functions

#select folder and files
def clicked():
    global videos
    global images
    FileExtension =selected.get()
    if FileExtension == 1:

       videos = filedialog.askopenfilenames(filetypes = (("Video files","*.mp4"),("all files","*.*")))
       images = []

    if FileExtension == 2:

       videos = []
       images = filedialog.askopenfilenames(filetypes = (("Images","*.jpg"),))

    if FileExtension == 3:

       videos = filedialog.askopenfilenames(filetypes = (("Video files","*.mp4"),("all files","*.*")))
       images = filedialog.askopenfilenames(filetypes = (("Images","*.jpg"),))
       print(videos)
       print(images)
       #videovagas(videos, images, pictureduration)

def startEdit():
    global path
    path = askdirectory(title='Chose the folder with the video files to be joined!')
    print(path)

#set picture duration
def clickedPicDur():

    if len(images) > 0:
        for i in images:
            #if i.endswith(".png"):
            clips.append(ImageClip(i).set_duration(pictureduration))

        print(clips)
        global BackgDurPics
        global BackgroundPics
        BackgDurPics = 0



        global videoImage
        #global videoImage_resized
        videoImage = concatenate(clips, method="compose")
        #videoImage_resized = videoImage.resize( (540, 960) )
        videoImage.write_videofile('kepek1.mp4', fps=36)

        BackgDurPics = videoImage.duration

        BackgroundPics = ColorClip([960, 540], color=[1,1,1], duration=BackgDurPics)
        BackgroundPics.write_videofile("Frame.mp4", fps=36)

        global vidImBG

        vidImBG = CompositeVideoClip([BackgroundPics, videoImage.set_pos("center")], size=(960,540))
        vidImBG.write_videofile("MyImVidBG.mp4", fps=36)




#combine videos, add background
def videovagas():
    global BackgDur
    global Background
    BackgDur = 0


    global myclip
    global myclip_resized
    myclip = VideoFileClip(videos[0])
    #myclip_resized = myclip.resize( (540, 960) )
    #myclip_resized.write_videofile("movie_resized.mp4")


    if len(videos) > 1:
        bar['value'] = 0
        for i in range(1, len(videos)):
            nextClip = VideoFileClip(videos[i])
            #nextClip_resized = nextClip.resize( (540, 960) )
            #myclip_resized = VideoFileClip("movie_resized.mp4")
            myclip = concatenate_videoclips([myclip, nextClip])
            #myclip_resized.write_videofile("movie_resized.mp4")

            bar['value'] = (i+1)*(90/len(videos))
            window.update()

    myclip.write_videofile("VideosJoined.mp4")
    bar['value'] = 100

    BackgDur = myclip.duration

    Background = ColorClip([960, 540], color=[1,1,1], duration=BackgDur)
    Background.write_videofile("Frame.mp4", fps=36)

    global final_video22

    final_video22 = CompositeVideoClip([Background, myclip.set_pos("center")], size=(960,540))
    final_video22.write_videofile("MyVidwBG.mp4", fps=36)

#join video and image clip, add background
def compose():


    clipIm = VideoFileClip("MyImVidBG.mp4")
    clipVid = VideoFileClip("MyVidwBG.mp4")

    clipAll = concatenate_videoclips([clipIm, clipVid])
    clipAll.write_videofile("MyMovie.mp4", fps=36)


#choose folder and file for audio
def selectSong():
    global pathMusic
    pathMusic = askdirectory(title='Chose the folder with the music files!')
    print(pathMusic)
    global fileMusic
    fileMusic = filedialog.askopenfilename()

    #global res
    #res = messagebox.askyesno('Audio setting','Do you want to keep the original audio of your video?')
#add audio to the video
def addSong():

    clip = VideoFileClip("MyMovie.mp4")
    #songdur = clip.duration
    bgmusic = AudioFileClip(fileMusic)
    bgmusicCut = bgmusic.subclip(0, clip.duration)
    bgmusicCut.write_audiofile("CutAudio.mp3")
    #print(songdur)
    #insertdur = round(songdur)
    #print(insertdur)
    FinalVideo = clip.set_audio(bgmusicCut)
    FinalVideo.write_videofile("output.mp4")

#Window

window = Tk()
window.title('Make a movie')

window.geometry('1200x800')

#choose folder and files
lbl = Label(window, text=('I. Choose a folder and select files to make a short movie'), font=('Arial_bold', 10))
lbl.grid(column=0, row=0)


#select file extension
selected = IntVar()

rad1 = Radiobutton(window, text='videos', value=1, variable=selected)
rad2 = Radiobutton(window, text='images', value=2, variable=selected)
rad3 = Radiobutton(window, text='both images and videos', value=3, variable=selected )


FileExtension = 0

btnExt = Button(window, text="Done", command=clicked)

rad1.grid(column=0, row=2)

rad2.grid(column=0, row=3)

rad3.grid(column=0, row=4)

btnExt.grid(column = 0, row = 5)

lblempty = Label(window, text=" ")
lblempty.grid(column=0, row=6)

#start the program
btnFirst = Button(window, text=("Start"), command=startEdit)
btnFirst.grid(column=0, row=1)

#II. convert pictures to picture clip

lblPicDur = Label(window, text="II. Set the duration of the images", font=('Arial_bold', 10))
lblPicDur.grid(column=0, row=7)
var =IntVar()

#set picture duration
var.set(3)

spin = Spinbox(window, values=(3, 4, 5, 6), width=5, textvariable=var)
spin.grid(column=0, row=8)
pictureduration = spin.get()
clips = []

#gets selected picture duration, starts to create image clip!
btnPicDur = Button(window, text="OK", command=clickedPicDur)
btnPicDur.grid(column=0, row=9)


#join selected videos, join picture and videoclip, adds background



btnStart = Button(window, text="Join videos", command=videovagas)
btnStart.grid(column=0, row=10)
bar = Progressbar(window, length=200)
bar.grid(column=0, row = 11)

btnJoin = Button(window, text="join images and videos", command=compose)
btnJoin.grid(column=0, row=12)

lblName = Label(window, text=(' IV. Add music to your video'), font=('Arial_bold', 10))
lblName.grid(column=1, row=10)

btnmusic = Button(window, text=("select music"), command=selectSong)
btnmusic.grid(column=1, row=11)
btnAddMusic = Button(window, text=("Add song"), command=addSong)
btnAddMusic.grid(column=1, row=12)


window.mainloop()
