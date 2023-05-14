# bjorkfi-auto
bjorkfi-auto

Bjorkfi Trader App Documentation
The Bjorkfi Trader app is a native desktop application built using Python and the Tkinter library. It allows users to log in with their credentials, access the main trading window, and submit trading data.

Files and Structure
The application is structured into the following files:

database.py: Contains functions for creating the user database, inserting a test user, and checking user credentials.
gui.py: Contains the GUI-related functions and windows for the application.
main.py: The main entry point of the application, where the program is executed.
Functionality
The app provides the following functionality:

Database Management: The database.py file handles the creation of the user database, including the necessary tables. It also provides functions to insert a test user and check user credentials.

Login Window: The create_login_window() function in gui.py creates a login window where users can enter their email and password. The login() function verifies the entered credentials against the database and opens the main window if the login is successful.

Main Window: The MainWindow class in gui.py creates the main trading window. It includes fields for Binance API and secret key, as well as a submit button. The submit() function is called when the submit button is clicked, and it retrieves the entered data, performs an API call (placeholder), and displays a success or error message using the messagebox module.

Usage
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
