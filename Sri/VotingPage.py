import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk, Image


def voteCast(root, frame1, vote, client_socket):
    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode())  # 4

    message = client_socket.recv(1024)  # Success message
    print(message.decode())  # 5
    message = message.decode()
    if message == "Successful":
        Label(
            frame1, text="Vote Casted Successfully", font=("Helvetica", 18, "bold")
        ).grid(row=1, column=1)
    else:
        Label(
            frame1,
            text="Vote Cast Failed... \nTry again",
            font=("Helvetica", 18, "bold"),
        ).grid(row=1, column=1)

    client_socket.close()


def votingPg(root, frame1, client_socket):
    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=("Helvetica", 18, "bold")).grid(
        row=0, column=1, rowspan=1
    )
    Label(frame1, text="").grid(row=1, column=0)

    vote = StringVar(frame1, "-1")

    Radiobutton(
        frame1,
        text="BJP\n\nMr.N.MODI",
        variable=vote,
        value="BJP",
        indicator=0,
        height=4,
        width=15,
        command=lambda: voteCast(root, frame1, "BJP", client_socket),
    ).grid(row=2, column=1)
    scLogo = ImageTk.PhotoImage(
        (Image.open("img/sc.jpg")).resize((45, 45), Image.Resampling.LANCZOS)
    )
    scImg = Label(frame1, image=scLogo).grid(row=2, column=0)

    Radiobutton(
        frame1,
        text="BRS\n\nMr.KCR",
        variable=vote,
        value="BRS",
        indicator=0,
        height=4,
        width=15,
        command=lambda: voteCast(root, frame1, "BRS", client_socket),
    ).grid(row=3, column=1)
    tcLogo = ImageTk.PhotoImage(
        (Image.open("img/tc.jpg")).resize((35, 48), Image.Resampling.LANCZOS)
    )
    tcImg = Label(frame1, image=tcLogo).grid(row=3, column=0)

    Radiobutton(
        frame1,
        text="TDP\n\nMr.NCB",
        variable=vote,
        value="TDP",
        indicator=0,
        height=4,
        width=15,
        command=lambda: voteCast(root, frame1, "TDP", client_socket),
    ).grid(row=4, column=1)
    crLogo = ImageTk.PhotoImage(
        (Image.open("img/cr.jpg")).resize((55, 40), Image.Resampling.LANCZOS)
    )
    crImg = Label(frame1, image=crLogo).grid(row=4, column=0)

    Radiobutton(
        frame1,
        text="YSR\n\nMr. JAGAN",
        variable=vote,
        value="YSR",
        indicator=0,
        height=4,
        width=15,
        command=lambda: voteCast(root, frame1, "YSR", client_socket),
    ).grid(row=5, column=1)
    etLogo = ImageTk.PhotoImage(
        (Image.open("img/et.jpg")).resize((50, 45), Image.Resampling.LANCZOS)
    )
    etImg = Label(frame1, image=etLogo).grid(row=5, column=0)

    Radiobutton(
        frame1,
        text="\nNOTA    \n  ",
        variable=vote,
        value="nota",
        indicator=0,
        height=4,
        width=15,
        command=lambda: voteCast(root, frame1, "nota", client_socket),
    ).grid(row=6, column=1)
    notaLogo = ImageTk.PhotoImage(
        (Image.open("img/nota.jpg")).resize((45, 35), Image.Resampling.LANCZOS)
    )
    notaImg = Label(frame1, image=notaLogo).grid(row=6, column=0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
