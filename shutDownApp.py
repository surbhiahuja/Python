from tkinter import *
import os 

def restart():
    os.system("shutdown /r /t 1")

def restart_wht_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

def close():
   #win.destroy()
   st.quit()

st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="Light Grey")


restart_button = Button(st, text="Restart", command=restart)
restart_button.place(x=20, y=20, height=40, width=150)

restart_schedued_button = Button(st, text="Restart Scheduled", command=restart_wht_time)
restart_schedued_button.place(x=20, y=70, height=40, width=150)

shutdown_button = Button(st, text="Shutdown Button", command=logout)
shutdown_button.place(x=20, y=120, height=40, width=150)

LogOff_button = Button(st, text="LogOff Button", command=shutdown)
LogOff_button.place(x=20, y=170, height=40, width=150)

Close_button = Button(st, text="Close Button", command=close)
Close_button.place(x=20, y=220, height=40, width=150)

st.mainloop()

