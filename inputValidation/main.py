from tkinter import messagebox
from customtkinter import *
import http.client
import xml.etree.ElementTree as ET

app = CTk()
app.geometry("400x400")
app.title("Input Validation")

tc_entry = CTkEntry(master=app, placeholder_text="Enter your identification number", width=350, text_color="#FFFFFF")
tc_entry.place(relx=0.5, rely=0.4, anchor="center")

name_entry = CTkEntry(master=app, placeholder_text="Enter your name", width=350, text_color="#FFFFFF")
name_entry.place(relx=0.5, rely=0.1, anchor="center")

surname_entry = CTkEntry(master=app, placeholder_text="Enter your surname", width=350, text_color="#FFFFFF")
surname_entry.place(relx=0.5, rely=0.2, anchor="center")

birthday_entry = CTkEntry(master=app, placeholder_text="Enter year of birth", width=350, text_color="#FFFFFF")
birthday_entry.place(relx=0.5, rely=0.3, anchor="center")


def check_infos():
    name = str(name_entry.get().upper())
    surname = str(surname_entry.get().upper())
    birthday = (birthday_entry.get())
    tc = (tc_entry.get())
    birtdayInt = int(birthday)
    tcInt = int(tc)


    print(type(name), type(surname), type(birthday), type(tc))

    if not name or not surname or not birthday or not tc:
        messagebox.showerror("Error", "Please enter all the information")
        return

    if not name.isalpha():
        messagebox.showerror("Error", "Invalid name! Please enter only letters")
        return

    if not surname.isalpha():
        messagebox.showerror("Error", "Invalid surname! Please enter only letters")
        return

    if not birthday.isdigit() or len(birthday) != 4:
        messagebox.showerror("Error", "Invalid year of birth! Please enter 4-digit number")
        return

    if not tc.isdigit() or len(tc) != 11:
        messagebox.showerror("Error", "Invalid identification number! Please enter 11-digit number")
        return

    messagebox.showinfo("Success!","All information is valid.")

    #API

    from suds.client import Client

    client = Client("https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL")

    args = {
        "TCKimlikNo": tcInt,
        "Ad": name,
        "Soyad": surname,
        "DogumYili": birtdayInt
    }

    def tcKimlikDogrula(params):
        try:
            return client.service.TCKimlikNoDogrula(**params)
        except Exception as e:
            return False

    print(tcKimlikDogrula(args))

    if tcKimlikDogrula(args):
        messagebox.showinfo("Success", "Identification number verification successful")
    else:
        messagebox.showerror("Error", "Identification number verification failed")


verify_button = CTkButton(master=app, width=100, text="Verify", command=check_infos)
verify_button.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

