import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

class PasswordManager(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk__init__(self, *args, **kwargs)
        self.wm_title("Password Manager")
        container = ctk.CTkFrame(self, height = 400, width = 600)
        container.pack(side='top', fill='both', exapnd=True)
        