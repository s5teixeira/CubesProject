
 Run main.py to launch the program.

# Summary of Project:
The program is a GUI that allows users to claim CUBES projects. It uses the Wufoo API to download the entries data from a Wufoo form by sending an HTTP GET request, converting the HTTP GET response into JSON, and extracting the entries data from JSON. The entries data are saved to a database. The entries data from the database are displayed in the GUI. Users can fill in their own information to claim their selected entries. An entry can only be claimed once, but a user can claim multiple entries.

# Database Layout:
The database consists of 3 tables: entries, users, and claims.

# What opens on program launch:
-Prompts the user to choose to either update the data in the database or run the data visualization. The user should choose to update the data in the database at least once before running the data visualization. GUI remains running after updating the data in the database.

-Closes after the user chooses an option.

# GUI Layout:
Portrays the Entries List, Entry Data, Claim, and User Data. Click on one of these buttons and the data will appear on a pop up window. 

# Form:
 https://stepht15.wufoo.com/forms/cubes-project-proposal-submission

