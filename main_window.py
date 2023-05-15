from tkinter import Tk, Label, Entry, Button, Frame, messagebox

class MainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bjorkfi Auto")

        # Create frames
        frame1 = Frame(self.window)
        frame1.pack()
        frame2 = Frame(self.window)
        frame2.pack()
        frame3 = Frame(self.window)
        frame3.pack()

        # Frame 1: Binance API
        Label(frame1, text="Binance API:").pack(side="left")
        self.e1_main = Entry(frame1)
        self.e1_main.pack(side="left")

        # Frame 2: Secret Key
        Label(frame2, text="Secret key:").pack(side="left")
        self.e2_main = Entry(frame2, show="*")
        self.e2_main.pack(side="left")

        # Frame 3: Submit button
        Button(frame3, text='Submit', command=self.submit).pack()

    def submit(self):
        field1 = self.e1_main.get()
        field2 = self.e2_main.get()
        print("Binance API:", field1)
        print("Secret key:", field2)
        # Do something with field1 and field2

        # Call your API here and get the result
        # result = call_api(field1, field2)  # This is a placeholder, replace it with your actual API call
        result = True  # Just for testing

        if result:  # If the API call was successful
            messagebox.showinfo("Success", "Your trade was executed successfully!")
        else:  # If the API call failed
            messagebox.showerror("Error", "An error occurred. Please contact support.")


        # If you want to clear the input fields after submitting, you can do this:
        self.e1_main.delete(0, 'end')
        self.e2_main.delete(0, 'end')

    def run(self):
        self.window.mainloop()
