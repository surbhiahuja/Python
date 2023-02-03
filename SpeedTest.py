from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    up = str(round(sp.upload()/(10**6),3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("SpeedTest")
sp.geometry("500x500")
sp.config(bg= "light grey")
lab = Label(sp, text="Internet Speed Test")
lab.place(x=40, y=40, width=200)

lab = Label(sp, text="Downloading Speed", fg="blue")
lab.place(x=40, y=90, width=200)

lab_down = Label(sp, text="00")
lab_down.place(x=40, y=140, width=200)

lab = Label(sp, text="Uploading Speed")
lab.place(x=40, y=190, width=200)

lab_up = Label(sp, text="00")
lab_up.place(x=40, y=240, width=200)

button = Button(sp,text="CHECK SPEED", relief=RAISED, command=speedCheck)
button.place(x=40, y=290, width=200)


sp.mainloop()  