from cProfile import label
from tkinter import *
import speedtest

print("you have to wait 1 min after clicking check now")
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6) ,3)) + "MBPS"
    up = str(round(sp.upload()/(10**6) ,3)) + "MBPS"
    lab_down.config(text=down)
    lab_up.config(text=up)





sp = Tk()
sp.title("Internet speed test by cyfix")
sp.geometry("500x650")
sp.config(bg = "red")


lab = Label(sp, text="speed test ", font=("Time New Roman" , 30 ,"bold" ))
lab.place(x = 60 , y = 60 ,height=50 , width=400)

lab = Label(sp, text="download speed", font=("Time New Roman" , 30 ,"bold" ))
lab.place(x = 60 , y = 130,height=50 , width=400) 

lab_down = Label(sp, text="00", font=("Time New Roman" , 30 ,"bold" ))
lab_down.place(x = 60 , y = 200,height=50 , width=400)

lab = Label(sp, text="upload speed", font=("Time New Roman" , 30 ,"bold" ))
lab.place(x = 60 , y = 290,height=50 , width=400)

lab_up = Label(sp, text="00", font=("Time New Roman" , 30 ,"bold" ))
lab_up.place(x = 60 , y = 360,height=50 , width=400)

lab = Button(sp, text="check speed", font=("Time New Roman" , 30 ,"bold"  ), relief=RAISED, command=speedcheck)
lab.place(x = 60 , y = 460,height=50 , width=400)

sp.mainloop()