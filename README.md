# Coworking-center-api

1) Copy the project to the computer: git clone https://github.com/JavoxirOne/Coworking-center-api.git
2) Create a new environment: python -m venv venv (for Windows); python3 -m venv venv (for Linux)
3) Activate Environment: cd venv/Scripts/activate (for Windows); source venv/bin/activate (for Linux)
4) Download required libraries: pip install -r requirements.txt
5) Open the project on the local server: python manage.py runserver (for Windows); python3 manage.py runserver (for Linux)
6) After running the website on the local server, go to /admin/ path (username: admin | password: 123) and enter the Admin panel.

# API Endpoints
<b>API endpoints root:</b> "api/" <br>
<b>List of rooms:</b> "api/rooms/"<br>
<b>Details of a specific room:</b> "api/rooms/<int:pk>/"<br>
<b>Availability of a specific room (time slots):</b> "api/rooms/<int:pk>/availability/"<br>
<b>Book a separate room for the available time slot:</b> "api/rooms/<int:pk>/book/"<br>
<b>Single booking:</b> "api/bookings/<int:pk>/"<br>
<b>List of bookings:</b> "api/bookings/"<br>
