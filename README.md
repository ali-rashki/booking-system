# 🎓 سیستم رزرو کلاس

**Course Booking System v1.0**

یک API کامل برای مدیریت دوره‌های آموزشی، ثبت‌نام دانشجوها در کلاس‌ها و مدیریت ظرفیت، ساخته شده با **Django** و **Django
REST Framework**.

---

## 🚀 ویژگی‌ها

- 🔐 احراز هویت با JWT
- 👤 سیستم نقش‌ها (Admin, Instructor, Student)
- 📚 مدیریت دوره‌ها و جلسات
- ✅ ثبت‌نام و انصراف با مدیریت ظرفیت
- 📄 مستندسازی خودکار با Swagger
- 🐳 پشتیبانی از Docker
- 🧪 تست‌نویسی کامل

## 🛠️ تکنولوژی‌ها

`Django 6.0` `Django REST Framework` `Simple JWT` `PostgreSQL` `Docker & Compose` `Nginx + Gunicorn` `drf-spectacular`

## 📁 ساختار پروژه

```
booking-system/
├── apps/
│   ├── users/      # مدیریت کاربران
│   └── courses/    # مدیریت دوره‌ها و جلسات
├── config/
│   └── settings/   # تنظیمات (base, dev, production)
├── static/
├── media/
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

## ⚡ نصب و اجرا

```bash
# ۱. کلون کردن
git clone https://github.com/AliRashki/booking-system.git
cd booking-system

# ۲. ساخت محیط مجازی
python -m venv venv
source venv/bin/activate  # لینوکس/مک
# یا
venv\Scripts\activate     # ویندوز

# ۳. نصب وابستگی‌ها
pip install -r requirements.txt

# ۴. تنظیمات دیتابیس - فایل .env بسازید
DB_NAME=booking_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# ۵. اجرای مایگریشن‌ها
python manage.py migrate
python manage.py createsuperuser

# ۶. اجرا
python manage.py runserver
```

پروژه روی آدرس زیر در دسترس است:
`http://127.0.0.1:8000`

## 🐳 اجرا با Docker

```bash
docker-compose up --build
```

## 📖 مستندات API

- **Swagger UI:** `/api/docs/swagger/`
- **Redoc:** `/api/docs/redoc/`

### 🔑 احراز هویت

دریافت توکن:

```
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

ارسال توکن در درخواست‌ها:

```
Authorization: Bearer <your_access_token>
```

## 👥 نقش‌های کاربری

| نقش            | دسترسی‌ها                           |
|----------------|-------------------------------------|
| **Admin**      | دسترسی کامل به همه منابع            |
| **Instructor** | ایجاد و مدیریت دوره‌ها و جلسات خودش |
| **Student**    | مشاهده دوره‌ها و ثبت‌نام در کلاس‌ها |

## 📋 لیست Endpointها

| Method   | Endpoint                 | توضیح                        |
|----------|--------------------------|------------------------------|
| `POST`   | `/api/token/`            | دریافت توکن                  |
| `POST`   | `/api/token/refresh/`    | تمدید توکن                   |
| `GET`    | `/api/courses/`          | لیست دوره‌ها                 |
| `POST`   | `/api/courses/`          | ایجاد دوره (فقط Instructor)  |
| `GET`    | `/api/courses/{id}/`     | جزئیات دوره                  |
| `PUT`    | `/api/courses/{id}/`     | ویرایش دوره (فقط Instructor) |
| `DELETE` | `/api/courses/{id}/`     | حذف دوره (فقط Instructor)    |
| `GET`    | `/api/sessions/`         | لیست جلسات                   |
| `POST`   | `/api/sessions/`         | ایجاد جلسه (فقط Instructor)  |
| `POST`   | `/api/enrollments/`      | ثبت‌نام در کلاس              |
| `DELETE` | `/api/enrollments/{id}/` | انصراف از کلاس               |
| `GET`    | `/api/enrollments/my/`   | کلاس‌های من                  |

## 🧪 اجرای تست‌ها

```bash
python manage.py test
```

## 🤝 مشارکت

1. Fork کنید
2. Branch جدید بسازید: `git checkout -b feature/AmazingFeature`
3. Commit کنید: `git commit -m 'Add some AmazingFeature'`
4. Push کنید: `git push origin feature/AmazingFeature`
5. Pull Request باز کنید

## 📧 ارتباط با من

- **گیت‌هاب:** [AliRashki](https://github.com/AliRashki)
- **ایمیل:** kenway755@gmail.com

---

ساخته شده با ❤️ و جنگو
