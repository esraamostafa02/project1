Database Documentation

Online Public Library Management System

1. Overview

This project uses Django ORM with SQLite as the database system.

The database stores information about books, users, borrowings, and reservations.

2. Database Models

The database contains four main entities:

1. User

Uses Django's built-in authentication User model.

Stores user information such as username, password, and email.

2. Book

title: Book title.

author: Book author.

category: Book category.

description: Book description.

total_copies: Total number of copies.

available_copies: Number of available copies.

3. Borrowing

user: Foreign key referencing User.

book: Foreign key referencing Book.

borrowing_date: Date when the book was borrowed.

due_date: Expected return date.

return_date: Actual return date.

status: Borrowing status.

4. Reservation

user: Foreign key referencing User.

book: Foreign key referencing Book.

reservation_date: Date when the reservation was created.

status: Reservation status.

3. Relationships

One User can have multiple Borrowing records.

One Book can have multiple Borrowing records.

One User can have multiple Reservation records.

One Book can have multiple Reservation records.

4. Database Implementation

Django ORM was used to create the database models.

SQLite was used as the database.

Django migrations were created and applied.

All models were registered in Django Admin.

5. Sample Data

Sample data was added for testing purposes, including:

Sample books.

Test users.

Borrowing records.

Reservation records.

6. Testing

The database implementation was tested successfully.

The following checks were performed:

Django System Check

Executed python manage.py check.

No system issues were found.

Migration Check

Executed python manage.py makemigrations --check.

No missing model migrations were detected.

Executed python manage.py migrate successfully.

Database Records Check
The database contains:

3 Books.

2 Users.

1 Borrowing record.

1 Reservation record.

Relationship Testing

Verified that each Borrowing record is connected to an existing User and Book.

Verified that each Reservation record is connected to an existing User and Book.

All performed tests passed successfully.

7. Database Migrations

The following commands were used:

python manage.py makemigrations
python manage.py migrate

8. Conclusion

The database models were successfully implemented using Django ORM and SQLite. The database is ready to be integrated with the other components of the Online Public Library Management System.