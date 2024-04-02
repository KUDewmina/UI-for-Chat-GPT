import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk,Image
import os
from tkinter import messagebox
import openai
import sys

openai.api_key = "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"  # "Replace Your API Key Here"
script_directory = os.path.dirname(__file__)

root = ctk.CTk()
ctk.set_appearance_mode("light")
root.geometry('700x500')
root.title("Chat GPT")
root.configure(fg_color="#0c2340") 
root.iconbitmap(script_directory+"\\icon.ico")

def on_enter_press(event):
    Button.invoke()
def clear_all():
    Text_Box.delete(1.0,tk.END)

def send():

    if Entry_Field.get() == "" :
        messagebox.showinfo("Chat GPT" ,"Please Enter Your Message")
    else:
        try:
            Text_Box.insert(tk.END ,"\n"+"\n" + "You : " +Entry_Field.get())
            Entry_Field.delete(0, tk.END)

            response = openai.ChatCompletion.create(
               model = "gpt-3.5-turbo",
               messages = [
             {"role" : "user" , "content" : Entry_Field.get()}
             ]
               )
            answer = response.choices[0].message.content
            Text_Box.insert(tk.END ,"\n"+"\n" + "Chat GPT : " + answer)

        except    openai.error.RateLimitError :
             Text_Box.insert(tk.END ,"\n"+"\n" + "Chat GPT : " + "You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.")
        
        except    openai.error.AuthenticationError :
             Text_Box.insert(tk.END ,"\n"+"\n" + "Chat GPT : " + "Incorrect API key provided.You can find your API key at https://platform.openai.com/account/api-keys.")
        except    SyntaxError :
             Text_Box.insert(tk.END ,"\n"+"\n" + "Chat GPT : " + "Please Enter Your API Key"+ "\n" + "You can find your API key at https://platform.openai.com/account/api-keys." )

Frame_1 = ctk.CTkFrame(root, width=600, height= 50, fg_color="#DDDEE5", corner_radius=15)
Frame_1.place(relx=0.02, rely=0.87)

Entry_Field = ctk.CTkEntry(Frame_1,width = 590, height=40, placeholder_text="Enter Your Message Here",corner_radius=10, fg_color="#eef0f2",text_color="#0c2340")
Entry_Field.place(relx=0.009, rely=0.1)

Frame_2 = ctk.CTkFrame(root, width = 670, height=400, fg_color="white",corner_radius=15)
Frame_2.place(relx= 0.02, rely=0.02)

Text_Box = ctk.CTkTextbox(Frame_2, width = 650, height=380, fg_color="#DDDEE5",corner_radius=15,border_width=2 ,border_color="#D5D5D5" ,text_color="#0c2340" )
Text_Box.place(relx=0.015 ,rely=0.02)
Text_Box.insert(tk.END, "Only Supported for Texts.Go to https://chat.openai.com for advanced options")

Frame_3 = ctk.CTkFrame(root, width=50 ,height=48 , corner_radius=10,border_width=2 ,border_color="white")
Frame_3.place(relx=0.9, rely=0.87)

root.bind('<Return>', on_enter_press)

img_path = os.path.join(script_directory+ "\\logo.png")
btn_icon = tk.PhotoImage(file = img_path)
Button = ctk.CTkButton(Frame_3, image= btn_icon,text="", width=40 ,height=40 ,corner_radius=8, fg_color="transparent" ,command = send,hover_color="white")
Button.place(relx=0.06,rely=0.09)

Frame_4 = ctk.CTkFrame(root, width=60 ,height=48 , corner_radius=10,border_width=2 ,border_color="white", bg_color="#DDDEE5")
Frame_4.place(relx=0.86, rely=0.06)

img_path = os.path.join(script_directory+ "\\clear.png")
btn1_icon = tk.PhotoImage(file = img_path)
Button1 = ctk.CTkButton(Frame_4, image= btn1_icon,text="", width=30 ,height=30 ,corner_radius=10,fg_color="transparent",bg_color="#DDDEE5",hover_color="white" ,command= clear_all)
Button1.place(relx=0.05,rely=0.1)


root.mainloop()