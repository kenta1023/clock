import tkinter as tk
import datetime
import random
import glob


root =tk.Tk()
root.title("Clock")
canvas=tk.Canvas(width=1920,height=1060)#キャンバス作成
root.state('zoomed')#画面サイズ最大で表示
canvas.pack()#キャンバス表示

text_color="white"
bg_chg_time=1000 #3600000

img=tk.PhotoImage()
IMG_list=glob.glob("./Png_Image/*.png")#pngの写真のリストを作成
canvas.create_image(960,540,image=img,tags="BackgroundIMG")
canvas.create_text(960,540,text='',font=("Ink Free",350),fill=text_color,tags="MainTime")
canvas.create_text(1700,665,text='',font=("Ink Free",125),fill=text_color,tags="SubTime")
canvas.create_text(130,80,text='',font=("Ink Free",60),fill=text_color,tags="date")

def ChangeIMG():
    global root
    global img
    img=tk.PhotoImage(file=random.choice(IMG_list))
    canvas.itemconfig("BackgroundIMG",image=img)
    canvas.update()
    root.after(bg_chg_time,ChangeIMG) #壁紙の変更時間を指定
    

def MainClock():
    global root
    now=datetime.datetime.now()
    canvas.itemconfig("MainTime", text="{:02}:{:02}".format(now.hour,now.minute))
    canvas.itemconfig("SubTime",  text="{:02}".format(now.second))
    canvas.itemconfig("date",     text="1{}/{}".format(now.month,now.day))
    canvas.update()
    root.after(100,MainClock)

ChangeIMG()
MainClock()
root.mainloop()
