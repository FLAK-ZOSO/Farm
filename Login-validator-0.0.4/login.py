#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import exceptions as e
import process as p


class Login(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master.title("Login form")
        self.master.geometry('190x80')
        self.master.resizable(0, 0)
        self.grid()
        self.makeWidgets()

    def makeWidgets(self) -> None:
        tk.Label(self, text='Username').grid(row=0, column=0)
        self.name = tk.StringVar()
        self.nameInput = tk.Entry(self, textvariable=self.name, justify='center')
        self.nameInput.grid(row=0, column=1)

        tk.Label(self, text='Password').grid(row=1, column=0)
        self.password = tk.StringVar()
        self.passwordInput = tk.Entry(self, textvariable=self.password, justify='center', show='*')
        self.passwordInput.grid(row=1, column=1)

        self.btn = tk.Button(self, text="Submit", command=self.submit)
        self.btn.grid(row=3, column=1)
    
    def submit(self) -> None:
        try:
            if (not p.login(self.name.get(), self.password.get())):
                messagebox.showwarning("Login", "Already logged in")
        except e.PasswordException:
            messagebox.showerror("Login", "Password doesn't match")
        except e.AccountException:
            messagebox.showwarning("Login", "Account doesn't exist")
        self.master.destroy()


if __name__ == '__main__':
    w = Login()
    w.mainloop()