#!/usr/bin/python3
import os
import sys
import tkinter as tk
from tkinter import messagebox
import process as p


# Thanks to Unbuntu from Stack Overflow at https://stackoverflow.com/a/7966437/15888601 for resizable screen
class Menu(tk.Frame):
    def __init__(self, master=None, user=None) -> None:
        super().__init__(master)
        self.user = '' if (user == None) else user
        self.master.title("Main menu")
        self.master.resizable(0, 0)
        self.grid()
        self.makeWidgets()
        self.master.bind('<Escape>', self.full_screen)

    def makeWidgets(self) -> None:
        if (self.user):
            self.btn = tk.Button(self, text="Logout", command=self.logout)
            self.btn.grid(row=1, column=1)
        else:
            self.btn = tk.Button(self, text="Login", command=self.login)
            self.btn.grid(row=0, column=1)        
            self.btn = tk.Button(self, text="Sign Up", command=self.sign_up)
            self.btn.grid(row=2, column=1)

        self.btn = tk.Button(self, text="Close", command=self.master.destroy)
        self.btn.grid(row=3, column=1)

    def toggle_geom(self, event=None) -> None:
        self.master.geometry(self._geom)
    
    def full_screen(self, event=None) -> None:
        self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}+0+0")

    def login(self) -> None:
        os.system('python login.py')
        self.master.destroy()
        if (p.isLogged(self.user)):
            os.system(f'python menu.py {self.user}')
        else:
            messagebox.showerror('Login', f'Couldn\'t log into {self.user}')
            os.system('python menu.py')

    def sign_up(self) -> None:
        os.system('python sign-up.py')
        self.master.destroy()
        os.system('python menu.py')
    
    def logout(self) -> None:
        os.system('python logout.py')
        self.master.destroy()
        os.system('python menu.py')


if __name__ == '__main__':
    # sys.argv[1] is the username
    try:
        w = Menu(None, sys.argv[1])
    except IndexError:
        w = Menu()
    w.mainloop()
