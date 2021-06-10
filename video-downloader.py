from tkinter import *
import os.path
import pytube

# Functions


def downlod():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        path = os.path.join(
            "UR DIRECTORY TO /videos")
        video.download(path)
        notif.config(fg="green", text="Video successfully downloaded!")

    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video could not be downloaded!")


# Main screen
master = Tk()
master.title("YouTube Video Downloader")

# Labels
Label(master, text="YouTube Video Converter", fg="blue",
      font=("Roboto", 15)).grid(sticky=N, padx=100, pady=8, row=0)

Label(master, text="Enter the link to your video below: ",
      font=("Roboto", 12)).grid(sticky=N, row=1, pady=15)

#  Notification if the video is downloaded.
notif = Label(master, font=("Roboto", 12))
notif.grid(sticky=N, pady=1, row=4)


url = StringVar()
# Entry
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2)

# Button
Button(master, width=20, bg="#555555", fg="white", text="Download", font=(
    "Roboto", 12), command=downlod).grid(sticky=N, row=3, pady=15)


photo = PhotoImage(file="logo.png")
master.iconphoto(False, photo)


master.title("wm min/max")

# this removes the maximize button
master.resizable(0, 0)
master.mainloop()
