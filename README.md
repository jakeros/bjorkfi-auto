# bjorkfi-auto
bjorkfi-auto

<h2> Bjorkfi Trader App Documentation</h2>
The Bjorkfi Trader app is a native desktop application built using Python and the Tkinter library. 
It allows users to log in with their credentials, access the main trading window, and submit trading data.

First off: This repo does not include an virtual environment.

Here are the steps you can follow in Visual Studio Code (VS Code):

Install the Python extension for Visual Studio Code: If you haven't already, install the Python extension from the Visual Studio Marketplace. This extension provides enhanced Python language features, including linting, IntelliSense, code formatting, refactoring, debugging, interactive notebooks, and more.

Create a New Folder for Your Project: This can be done through VS Code or using your OS file explorer. Open this folder in VS Code.

Create a Virtual Environment: Open the terminal in VS Code (View > Terminal). Navigate to your project directory, if you're not already there, and create a new virtual environment:


For macOS and Linux:
python3 -m venv env


This will create a new virtual environment in a folder named "env" within your project directory.

Activate the Virtual Environment:

For macOS and Linux:

source env/bin/activate
You should see (env) at the beginning of your terminal line, indicating that you are working inside the env virtual environment.

Install Necessary Libraries: Now, you can install the necessary libraries for your project. For your project, you might need to install the tkinter library. However, tkinter comes pre-installed with Python, so you may not need to install it separately.

Start Coding: Now you can start writing your Python code. Create a new Python file (.py) in VS Code and start writing your application. VS Code should automatically use the Python interpreter from your virtual environment. You can confirm this by looking at the Python version displayed in the status bar (it should point to the Python in your virtual env).

Remember to keep the virtual environment activated whenever you're working on the project. Whenever you open a new terminal in VS Code, you'll need to activate the environment again.

<h2> Files and Structure </h2>
The application is structured into the following files:

database.py: Contains functions for creating the user database, inserting a test user, and checking user credentials.
gui.py: Contains the GUI-related functions and windows for the application.
main.py: The main entry point of the application, where the program is executed.
Functionality
The app provides the following functionality:

<h2> Database Management</h2>
The database.py file handles the creation of the user database, including the necessary tables. It also provides functions to insert a test user and check user credentials.

Login Window: The create_login_window() function in gui.py creates a login window where users can enter their email and password. The login() function verifies the entered credentials against the database and opens the main window if the login is successful.

Main Window: The MainWindow class in gui.py creates the main trading window. It includes fields for Binance API and secret key, as well as a submit button. The submit() function is called when the submit button is clicked, and it retrieves the entered data, performs an API call (placeholder), and displays a success or error message using the messagebox module.

<h2> Usage </h2>

To run the Bjorkfi Trader app:

Make sure you have Python and the necessary dependencies installed.
Run the main.py file using the Python interpreter.
The login window will appear. Enter valid login credentials to access the main window.
In the main window, enter the Binance API and secret key.
Click the submit button to trigger the API call (placeholder) and display a success or error message.
Additional Features
To enhance the app, you can consider adding the following features:

Validation of user input: Implement input validation to ensure that the entered data meets the required criteria.
Error handling: Improve error handling by displaying more informative error messages and handling exceptions gracefully.
Improved styling: Customize the app's appearance by using CSS or a theming library for Tkinter.
Real API integration: Replace the API call placeholder with actual API integration to perform real trading operations.
Feel free to expand the functionality and improve the user experience of the Bjorkfi Trader app based on your requirements.

Remember to update the documentation as you add new features or modify existing functionality.

<h2>Here's a suggestion for managing the API:</h2>

Create a new file named api.py in your project directory.

In the api.py file, define functions or classes to handle the API operations. For example, you can have a function called execute_trade(api_key, secret_key, trade_data) that performs the actual trade execution based on the provided API key, secret key, and trade data.

Implement the necessary API integration logic within the functions or classes in api.py. This can include making HTTP requests, processing API responses, and handling errors.

Once you have implemented the API functionality in api.py, you can import and use it in your main_window.py file. For example, you can import the execute_trade function from api.py and call it in the submit() method of the MainWindow class

from api import execute_trade

# ...

def submit(self):
    api_key = self.e1_main.get()
    secret_key = self.e2_main.get()
    trade_data = # Get the trade data from the UI elements
    
    # Call the API function
    result = execute_trade(api_key, secret_key, trade_data)

    if result:  # If the API call was successful
        messagebox.showinfo("Success", "Your trade was executed successfully!")
    else:  # If the API call failed
        messagebox.showerror("Error", "An error occurred. Please contact support.")


By separating the API-related code into a dedicated module, you can keep your codebase organized and maintain a clear separation of concerns. It also allows for easier testing and maintenance of the API functionality.

