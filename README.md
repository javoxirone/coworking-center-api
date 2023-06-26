# Coworking-center-api

1) Proyekt'ni ko'mpyuterga ko'chirib oling: git clone https://github.com/JavoxirOne/Coworking-center-api.git
2) Yangi environment yarating: python -m venv venv (for Windows); python3 -m venv venv (for Linux)
3) Environment'ni activate qiling: cd venv/Scripts/activate (for Windows); source venv/bin/activate (for Linux)
4) Kerakli kutbxonalarni yuklab oling: pip install -r requirements.txt
5) Proyekt'ni local server'da oching: python manage.py runserver (for Windows); python3 manage.py runserver (for Linux)
6) Local serverda websaytni ishlagandan so'ng /admin/ path'ga o'tib (username: admin | password: 123) shu ma'lumotlarni kiritgan holda Admin panel'ga kirishingiz mumkin bo'ladi

# API Endpoints
<b>API so'nggi nuqtalarining ildizi:</b> "api/" <br>
<b>Xonalar ro'yxati:</b> "api/rooms/"<br>
<b>Ma'lum bir xona tafsilotlari:</b> "api/rooms/<int:pk>/"<br>
<b>Ma'lum bir xona mavjudligi (vaqt oraliqlari):</b> "api/rooms/<int:pk>/availability/"<br>
<b>Mavjud vaqt oralig'i uchun alohida xonani band qiling:</b> "api/rooms/<int:pk>/book/"<br>
<b>Yagona bandlov:</b> "api/bookings/<int:pk>/"<br>
<b>Bandlovlari ro'yxati:</b> "api/bookings/"<br>
