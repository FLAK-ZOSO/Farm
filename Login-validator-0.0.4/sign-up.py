#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import exceptions as e
import process as p


class SignUp(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master.title("Sign-up form")
        self.master.geometry('190x100')
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
        
        tk.Label(self, text='Confirm').grid(row=2, column=0)
        self.confirm = tk.StringVar()
        self.confirmInput = tk.Entry(self, textvariable=self.confirm, justify='center', show='*')
        self.confirmInput.grid(row=2, column=1)

        self.btn = tk.Button(self, text="Submit", command=self.submit)
        self.btn.grid(row=4, column=1)
    
    def submit(self) -> None:
        try:
            p.signUp(self.name.get(), self.password.get(), self.confirm.get())            
        except e.AccountException:
            messagebox.showwarning("Sign In", "Username already taken")
        except e.PasswordException:
            messagebox.showerror("Sign In", "Confirmed password doesn't match")
        self.master.destroy()


if __name__ == '__main__':
    w = SignUp()
    w.mainloop()