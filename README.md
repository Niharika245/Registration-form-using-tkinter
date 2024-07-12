# Registration-form-using-tkinter

Creating a simple registration form using Tkinter in Python involves the following steps:

1.Setting Up the Tkinter Environment: This includes importing the Tkinter module and setting up the main application window.

2.Creating the Form Fields: Adding labels and entry widgets for the user to input their information.

3.Adding Functionality: Implementing functions to handle the form submission.

4.Running the Application: Setting up the main event loop to keep the application running.

Here is an example of how to create a basic registration form using Tkinter in Python:

First, create a file with name “form.py” and add the code

Explanation:

Importing Tkinter and Setting Up:

import tkinter as tk: Imports the Tkinter module.


Running the Application:

root.mainloop(): Starts the main event loop, which waits for user interaction and updates the GUI accordingly.

Validations:

Check if all fields are filled.

Validate email format using a regular expression.

Ensure passwords match.

Validate that the age is a positive integer.

Validate that the phone number is a 10-digit number.

Steps to Run the project:

Open Command Prompt (Windows) or Terminal (macOS/Linux).

Use the cd command to navigate to the directory where you saved the form.py file.

Execute the project by typing python followed by the project name.

Ex: Python form.py

· The Tkinter window should open, displaying the registration form.

· Fill out the form fields and click the "Submit" button to test the validation and form submission functionality.
