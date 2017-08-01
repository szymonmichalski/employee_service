# employee_service

The app is available here:
https://szymon-employee-service.herokuapp.com/

This is simple demo of employee service. It is possible to add, get or delete
employee.

You can get all employees or filter them by email.

You can add employee giving all necessary data: name, surname, email.
Email cannot be duplicated in the database, and has to be in correct format 
(i.e. has to have domain, @ sign).

You can delete employee giving its database id or all correct data in order to
filter him out. Remember that id has higher priority if you give all the data.

All the parameters should be given as query params, i.e.

https://szymon-employee-service.herokuapp.com/employee?email=franek.kimono@wp.pl

Fell free to play.
