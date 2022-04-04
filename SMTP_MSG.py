from tkinter import *
import tkinter
from PIL import ImageTk,Image,ImageFilter
from tkinter import filedialog
import numpy as np
import cv2
import PIL.Image, PIL.ImageTk
import tkinter.font as font
import smtplib, ssl
import conf
def send ():
    
    server=smtplib.SMTP('64.233.184.108',587)
    server.starttls()
    server.login(email_sender.get(),Email_password.get())
    message='subject:'+Email_subject.get()+'\n'+Email_message.get(1.0,END)
    server.sendmail(email_sender.get(), email_Reciever.get(),message)
    server.close()
root=Tk()
root.title("SMTP")
root.geometry("790x680")
root['background']='#2C313C' 
myFont = font.Font(size=13)
###################### import image 
image1 = Image.open("icons8-email-open-48.png")
image1=image1.resize((30, 30), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test,background="#2C313C")
label1.image=test
label1.place(x=100,y=150)
######################### End of import 
###################### import image 
image1 = Image.open("Graphicloads-100-Flat-Email-2.ico")
image1=image1.resize((60, 60), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test,background="#2C313C")
label1.image=test
label1.place(x=150,y=35)
######################### End of import 
###################### import image 
image1 = Image.open("icons8-email-open-48.png")
image1=image1.resize((30, 30), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test,background="#2C313C")
label1.image=test
label1.place(x=100,y=200)
######################### End of import 
###################### import image 
image1 = Image.open("icons8-new-topic-48.png")
image1=image1.resize((30, 30), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test,background="#2C313C")
label1.image=test
label1.place(x=100,y=250)
######################### End of import 
###################### import image 
image1 = Image.open("icons8-topic-48.png")
image1=image1.resize((30, 30), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test,background="#2C313C")
label1.image=test
label1.place(x=100,y=300)
######################### End of import 
###################### import image 
image1 = Image.open("icons8-show-password-48.png")
image1=image1.resize((30, 30), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test,background="#2C313C")
label1.image=test
label1.place(x=100,y=500)
######################### End of import 
label=Label(root,text='SMTP SERVER',background="#1B1D23",fg='white',width='20',font=("Courier", 20)).place(x=230,y=50)
email_sender = Entry(root,width = 30,font=("Courier", 20),fg='white',bd=0.5,background='#1B1D23')
email_sender.insert(0,'Email Of Sender')
email_sender.place(x=150, y=150)
email_Reciever = Entry(root,width = 30,font=("Courier", 20),fg='white',bd=0.5,background='#1B1D23')
email_Reciever.insert(0,'Email Of Reciever')
email_Reciever.place(x=150, y=200)
Email_subject = Entry(root, width = 30,font=("Courier", 20),fg='white',bd=0.5,background='#1B1D23')
Email_subject.insert(0,'Subject')
Email_subject.place(x=150, y=250)
Email_message = Text(root, height = 6, width = 30,font=("Courier", 20),fg='white',bd=0.5,background='#1B1D23')
Email_message.insert(0.1,'Message')
Email_message.place(x=150, y=300)
Email_password = Entry(root, width = 30,font=("Courier", 20),fg='white',bd=0.5,background='#1B1D23')
Email_password.insert(0,'password')
Email_password.place(x=150, y=500)
Button10=Button(root,text="Send Message",padx=50,pady=20,font=myFont,fg='black',bd=0.5,background='#52A3B6',command=send)
Button10.place(x=280, y=580)



root.mainloop()
