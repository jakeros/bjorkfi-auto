from tkinter import *
from gui.main_window import MainWindow  # import the MainWindow class
import database.models as models  # import the database module

def create_login_window():
    root = Tk()
    root.title("Login")  # Set the title of the window

    Label(root, text="Email:").grid(row=1)
    Label(root, text="Password:").grid(row=2)

    e1 = Entry(root)
    e2 = Entry(root, show="*")

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    Button(root, text='Login', command=lambda: login(root, e1.get(), e2.get())).grid(row=3, column=1, sticky=W, pady=4)

    root.mainloop()

def login(root, email, password):
    if models.check_credentials(email, password):
        print("Login successful")
        root.destroy()  # Close the login window
        main_window = MainWindow()  # Create an instance of MainWindow
        main_window.run()  # Run the MainWindow instance
    else:
        print("Incorrect credentials")
