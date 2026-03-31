import customtkinter as Ctk
import requests
import sys
import subprocess
import json as jsonlib

Ctk.set_appearance_mode('dark')

def home():
    homee.pack_forget()
    gett.pack_forget()
    dell.pack_forget()
    postjson.pack_forget()
    homee.pack()
def rel():
    subprocess.Popen([sys.executable, __file__])
    w.destroy()
    sys.exit()

def get():
    homee.pack_forget()
    gett.pack_forget()
    dell.pack_forget()
    postjson.pack_forget()
    gett.pack()
    label = Ctk.CTkLabel(gett, text="Enter target URL... ", font=("Segoe UI", 20), text_color="white")
    label.pack()
    global target, txt
    target = Ctk.CTkEntry(gett)
    target.pack()
    btn = Ctk.CTkButton(gett, text="Send", text_color="white", command=sendget)
    btn.pack(pady=10)
    backtohome = Ctk.CTkButton(gett, text="Back to home", text_color="white", command=rel)
    backtohome.pack(pady=10)
def sendget():
    url = target.get()
    if not url.startswith("http"):
        url = "https://" + url
    rep = requests.get(url)
    txt = Ctk.CTkTextbox(gett, width=500, height=250)
    txt.delete("1.0", "end") # Vider du début (debut = 1.0) a la fin (end)
    txt.insert("end", rep.text) # Ajouter a partir de la fin
    txt.pack(pady=10)    


def delete():
    homee.pack_forget()
    gett.pack_forget()
    dell.pack_forget()
    postjson.pack_forget()
    dell.pack()
    label = Ctk.CTkLabel(dell, text="Enter target URL... ", font=("Segoe UI", 20), text_color="white")
    label.pack()
    global target, txt
    target = Ctk.CTkEntry(dell)
    target.pack()
    btn = Ctk.CTkButton(dell, text="Send", text_color="white", command=senddelete)
    btn.pack(pady=10)
    backtohome = Ctk.CTkButton(dell, text="Back to home", text_color="white", command=rel)
    backtohome.pack(pady=10)

def senddelete():
    url = target.get()
    if not url.startswith("http"):
        url = "https://" + url
    rep = requests.delete(url)
    txt = Ctk.CTkTextbox(dell)
    txt.delete("1.0", "end")
    txt.insert("end", rep.status_code)
    txt.pack()

def post():
    homee.pack_forget()
    gett.pack_forget()
    dell.pack_forget()
    postjson.pack_forget()
    postjson.pack()
    label = Ctk.CTkLabel(postjson, text="Enter target URL... ", font=("Segoe UI", 20), text_color="white")
    label.pack()
    global targety, txt
    targety = Ctk.CTkEntry(postjson)
    targety.pack()
    label = Ctk.CTkLabel(postjson, text="Enter JSON... ", font=("Segoe UI", 20), text_color="white")
    label.pack()
    global json_entry, txt
    json_entry = Ctk.CTkEntry(postjson)
    json_entry.pack()
    btn = Ctk.CTkButton(postjson, text="Send", text_color="white", command=sendjson)
    btn.pack(pady=10)
    backtohome = Ctk.CTkButton(postjson, text="Back to home", text_color="white", command=rel)
    backtohome.pack(pady=10)
    global errorlabel
    errorlabel = Ctk.CTkLabel(postjson, text_color="red", text="")


def sendjson():
 try:
     raw = json_entry.get().strip()
     if not raw.startswith("{"):
         raw = "{" + raw
     if not raw.endswith("}"):
         raw = raw + "}"
     loadedjson = jsonlib.loads(raw)
     url = targety.get()
     if not url.startswith("http"):
        url = "https://" + url

     rep = requests.post(url, json=loadedjson)
     txt = Ctk.CTkTextbox(postjson)
     txt.delete("1.0", "end")
     txt.insert("end", str(rep.status_code))
     txt.pack()

 except jsonlib.decoder.JSONDecodeError:
    e =  "JSON entry error"
    errorlabel.configure(text=e)
    errorlabel.pack()
    
w = Ctk.CTk()
w.geometry("1000x1000")
w.title("Sender")
w.configure(bg="black")

homee = Ctk.CTkFrame(w)
gett  = Ctk.CTkFrame(w)
dell = Ctk.CTkFrame(w)
postjson = Ctk.CTkFrame(w)
label = Ctk.CTkLabel(homee, text="What do you want to do, today ?", font=("Segoe UI", 20), text_color="white")
label.pack(pady=10)
pub = Ctk.CTkLabel(w, text="Made by Nox (https://nox.ct.ws/)", font=("Segoe UI", 20), text_color="white")
pub.pack(pady=(90, 90))
btnget = Ctk.CTkButton(homee, text="GET REQUESTS", font=("Segoe UI", 13), text_color="white", command=get)
btndel = Ctk.CTkButton(homee, text="DELETE REQUESTS", font=("Segoe UI", 13), text_color="white", command=delete)
btnpost = Ctk.CTkButton(homee, text="POST REQUESTS (JSON)", font=("Segoe UI", 13), text_color="white", command=post)
btnget.pack(pady=10)
btndel.pack(pady=10)
btnpost.pack(pady=10)
homee.pack()


w.mainloop()
