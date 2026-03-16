from tkinter import *
from PIL import ImageTk, Image


def open_dashboard():
    login_frame.pack_forget()

    dashboard_frame.pack(fill="both", expand=True)

    title = Label(dashboard_frame,
                  text="Welcome to GIET Dashboard",
                  font=("Arial", 20, "bold"),
                  bg="#1E1E2F",
                  fg="white")
    title.pack(pady=40)

    info = Label(dashboard_frame,
                 text="This is a dummy dashboard page",
                 font=("Arial", 14),
                 bg="#1E1E2F",
                 fg="white")
    info.pack(pady=10)

    logout_btn = Button(dashboard_frame,
                        text="Logout",
                        font=("Arial", 12, "bold"),
                        bg="white",
                        fg="#1E1E2F",
                        command=logout)
    logout_btn.pack(pady=20)


def confirm_login():
    email = email_entry.get()
    password = password_entry.get()

    print("Email:", email)
    print("Password:", password)

    open_dashboard()


def logout():
    dashboard_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)


root = Tk()
root.title("GIET Shopping")
root.geometry("600x550")
root.configure(bg="#1E1E2F")

icon = ImageTk.PhotoImage(Image.open("icon1.png"))
root.iconphoto(True, icon)


login_frame = Frame(root, bg="#1E1E2F")
login_frame.pack(fill="both", expand=True)

card = Frame(login_frame, bg="white", width=350, height=420)
card.pack(pady=60)
card.pack_propagate(False)


img = Image.open("star1.png")
img = img.resize((90,90))
logo = ImageTk.PhotoImage(img)

logo_label = Label(card, image=logo, bg="white")
logo_label.pack(pady=10)


title = Label(card,
              text="GIET Shopping",
              font=("Arial",20,"bold"),
              bg="white",
              fg="#6A0DAD")
title.pack(pady=5)


subtitle = Label(card,
                 text="Login to continue",
                 font=("Arial",11),
                 bg="white",
                 fg="grey")
subtitle.pack(pady=(0,20))


email_label = Label(card,
                    text="Email",
                    font=("Arial",12,"bold"),
                    bg="white")
email_label.pack(anchor="w", padx=40)

email_entry = Entry(card,
                    font=("Arial",12),
                    width=25,
                    bd=2,
                    relief="groove")
email_entry.pack(pady=5)


password_label = Label(card,
                       text="Password",
                       font=("Arial",12,"bold"),
                       bg="white")
password_label.pack(anchor="w", padx=40, pady=(10,0))

password_entry = Entry(card,
                       font=("Arial",12),
                       width=25,
                       bd=2,
                       relief="groove",
                       show="*")
password_entry.pack(pady=5)


login_btn = Button(card,
                   text="Login",
                   font=("Arial",13,"bold"),
                   bg="#6A0DAD",
                   fg="white",
                   width=18,
                   bd=0,
                   command=confirm_login)
login_btn.pack(pady=25)


footer = Label(card,
               text="GIET University System",
               font=("Arial",9),
               bg="white",
               fg="grey")
footer.pack(side="bottom", pady=10)


dashboard_frame = Frame(root, bg="#1E1E2F")


root.mainloop()