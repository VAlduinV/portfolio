# Login Management System

![Static Badge](https://img.shields.io/badge/C++-Solutions-blue.svg?style=flat&logo=c++)

This is a simple Login Management System implemented in C++. It allows users to register, login, view the list of registered users, search for a user, and delete a user.

![LG_PS](fon/lg_ps.png)

## How to Use

1. Upon running the program, a menu will be displayed with the following options:

- Register User
- Login
- Show User List
- Search User
- Delete User
- Exit

2. To perform an action, enter the corresponding number and press Enter.

### 1. Register User
When selecting option 1, the program will prompt you to enter a username and password. After entering the required information, the user will be successfully registered.

### 2. Login
Selecting option 2 will prompt you to enter a username and password for login. If the provided credentials match a registered user, the program will display "Login Successfully." Otherwise, it will show "Invalid User Name or Password."

### 3. Show User List
Option 3 allows you to view the list of all registered users.

### 4. Search User
By choosing option 4, you can search for a specific user by entering their username. If the user is found, the program will display "User Found."

### 5. Delete User
Selecting option 5 will enable you to delete a user from the system. You need to enter the username of the user you wish to delete. If the user is found, the program will remove them and display "User Removed Successfully."

### 6. Exit
Option 6 allows you to exit the program.

## Note
- The system uses a basic vector to store registered users. As this is a simple demonstration, no data persistence mechanisms like file storage or databases are used, meaning that all data will be cleared after the program is terminated.

---
Feel free to improve this system and add more functionalities as needed. Happy coding!
