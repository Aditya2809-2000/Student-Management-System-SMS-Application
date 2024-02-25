# Student Management System (SMS) Application

## Overview
The Student Management System (SMS) is a comprehensive testing application designed to manage student records efficiently. It allows users to add, view, update, and delete student records. Additionally, it features a chart display for visual representation of student marks and integrates weather and quote of the day functionalities to provide users with additional useful information.

## Features
- **Add Student Records**: Allows the addition of student details including roll number, name, and marks.
- **View Student Records**: Enables users to view all the student records in a scrollable format.
- **Update Student Records**: Facilitates the modification of existing student records.
- **Delete Student Records**: Permits the deletion of specific student records based on the roll number.
- **Charts**: Graphically displays the marks of students in a bar chart format for easy comparison.
- **Weather Information**: Shows the current temperature and location information to the user.
- **Quote of the Day**: Displays a motivational quote of the day.

## Installation
To run the Student Management System application, ensure you have the following prerequisites installed on your system:
- Python 3.x
- Tkinter library for Python (usually comes with Python installation)
- SQLite3 for database management
- Matplotlib for generating charts
- Requests and Beautiful Soup (bs4) libraries for fetching weather information and quote of the day.

You can install the necessary Python libraries using pip:
```
pip install matplotlib requests beautifulsoup4
```

## Usage
To start the application, execute the Python script from your command line or IDE:
```
python sms_application.py
```

Once the application starts, you'll be presented with the main window containing the following options:
- **Add**: To add a new student record.
- **View**: To view existing student records.
- **Update**: To modify an existing student record.
- **Delete**: To remove a student record.
- **Charts**: To view a graphical representation of student marks.
- **Weather and Quote**: Displays on the main window as additional information.

Each action (add, view, update, delete) opens in a new window where you can enter the required information and submit or go back to the main menu.

## Database Setup
The application uses SQLite database named `stu.db` with a table `student` for storing student records. The database and table are automatically created if they do not exist when adding the first student record.

### Student Table Schema
- **rno**: Roll Number (Integer, Primary Key)
- **name**: Name (Text)
- **marks**: Marks (Integer)


## Contributing
Contributions to the Student Management System application are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## Support
For support, please open an issue in the GitHub repository, and we will try to address it as soon as possible.

---
This README provides a basic overview and setup instructions for the Student Management System application. For detailed documentation on the code or further assistance, please refer to the comments within the codebase or contact the maintainers.
