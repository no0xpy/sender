import customtkinter as Ctk
import requests
import sys
import subprocess

Ctk.set_appearance_mode('dark')

def home():
    homee.pack_forget()
    gett.pack_forget()
    dell.pack_forget()
    homee.pack()
def rel():
    subprocess.Popen([sys.executable, __file__])
    w.destroy()
    sys.exit()

def get():
    homee.pack_forget()
    gett.pack_forget()
    dell.pack_forget()
    gett.pack()
    label = Ctk.CTkLabel(gett, text="Enter target URL... ", font=("Segoe UI", 20), text_color="white")
    label.pack()
    global target, txt
    target = Ctk.CTkEntry(gett)
    target.pack()
    btn = Ctk.CTkButton(gett, text="Send", text_color="white", command=envoyerg)
    btn.pack(pady=10)
    backtohome = Ctk.CTkButton(gett, text="Back to home", text_color="white", command=rel)
    backtohome.pack(pady=10)
def envoyerg():
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
    dell.pack()
    label = Ctk.CTkLabel(dell, text="Enter target URL... ", font=("Segoe UI", 20), text_color="white")
    label.pack()
    global target, txt
    target = Ctk.CTkEntry(dell)
    target.pack()
    btn = Ctk.CTkButton(dell, text="Send", text_color="white", command=envoyerd)
    btn.pack(pady=10)
    backtohome = Ctk.CTkButton(dell, text="Back to home", text_color="white", command=rel)
    backtohome.pack(pady=10)

def envoyerd():
    url = target.get()
    if not url.startswith("http"):
        url = "https://" + url
    rep = requests.delete(url)
    txt = Ctk.CTkTextbox(dell)
    txt.delete("1.0", "end")
    txt.insert("end", rep.status_code)
    txt.pack()


w = Ctk.CTk()
w.geometry("1000x1000")
w.title("Sender")
w.configure(bg="black")

homee = Ctk.CTkFrame(w)
gett  = Ctk.CTkFrame(w)
dell = Ctk.CTkFrame(w)
label = Ctk.CTkLabel(homee, text="What do you want to do, today ?", font=("Segoe UI", 20), text_color="white")
label.pack(pady=10)
pub = Ctk.CTkLabel(w, text="Made by Nox (https://nox.ct.ws/)", font=("Segoe UI", 20), text_color="white")
pub.pack(pady=(90, 90))
btnget = Ctk.CTkButton(homee, text="GET REQUESTS", font=("Segoe UI", 13), text_color="white", command=get)
btndel = Ctk.CTkButton(homee, text="DELETE REQUESTS", font=("Segoe UI", 13), text_color="white", command=delete)
btnget.pack(pady=10)
btndel.pack(pady=10)
homee.pack()


w.mainloop()
