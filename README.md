# Coworking-center-api

1) Proyekt'ni ko'mpyuterga ko'chirib oling: git clone https://github.com/JavoxirOne/Coworking-center-api.git
2) Yangi environment yarating: python -m venv venv (for Windows); python3 -m venv venv (for Linux)
3) Environment'ni activate qiling: cd venv/Scripts/activate (for Windows); source venv/bin/activate (for Linux)
4) Kerakli kutbxonalarni yuklab oling: pip install -r requirements.txt
5) Proyekt'ni local server'da oching: python manage.py runserver (for Windows); python3 manage.py runserver (for Linux)
6) Local serverda websaytni ishlagandan so'ng /admin/ path'ga o'tib (username: admin | password: 123) shu ma'lumotlarni kiritgan holda Admin panel'ga kirishingiz mumkin bo'ladi

# API Endpoints
API so'nggi nuqtalarining ildizi: "api/"
Xonalar ro'yxati: "api/rooms/"
Ma'lum bir xona tafsilotlari: "api/rooms/<int:pk>/"
Ma'lum bir xona mavjudligi (vaqt oraliqlari): "api/rooms/<int:pk>/availability/"
Mavjud vaqt oralig'i uchun alohida xonani band qiling: "api/rooms/<int:pk>/book/"
Yagona bandlov: "api/bookings/<int:pk>/"
Bandlovlari ro'yxati: "api/bookings/"
