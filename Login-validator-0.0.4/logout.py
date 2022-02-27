#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import exceptions as e
import process as p


class Logout(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master.title("Logout form")
        self.master.geometry('190x60')
        self.master.resizable(0, 0)
        self.grid()
        self.makeWidgets()

    def makeWidgets(self) -> None:
        tk.Label(self, text='Username').grid(row=0, column=0)
        self.name = tk.StringVar()
        self.nameInput = tk.Entry(self, textvariable=self.name, justify='center')
        self.nameInput.grid(row=0, column=1)

        self.btn = tk.Button(self, text="Submit", command=self.submit)
        self.btn.grid(row=2, column=1)
    
    def submit(self) -> None:
        try:
            if (not p.logout(self.name.get())):
                messagebox.showwarning("Logout", "Already logged out")
        except e.AccountException:
            messagebox.showwarning("Logout", "Account doesn't exist")
        self.master.destroy()


if __name__ == '__main__':
    w = Logout()
    w.mainloop()