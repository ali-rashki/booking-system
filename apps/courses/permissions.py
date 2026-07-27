from rest_framework import permissions


class IsInstructorOrReadOnly(permissions.BasePermission):
    """
    دسترسی:
    - Instructor و Admin: همه کارها (ساخت، ویرایش، حذف)
    - دیگر کاربران (Student): فقط مشاهده (GET)
    """

    def has_permission(self, request, view):
        # ۱. کاربر باید لاگین باشه
        if not request.user.is_authenticated:
            return False

        # ۲. Instructor یا Admin باشه → اجازه کامل
        if request.user.role in ['instructor', 'admin']:
            return True

        # ۳. متد GET باشه → اجازه مشاهده
        if request.method in permissions.SAFE_METHODS:
            return True

        # ۴. هیچکدوم → عدم دسترسی
        return False

    def has_object_permission(self, request, view, obj):
        # ۱. همه می‌تونن بخونن (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # ۲. فقط خود Instructor یا Admin می‌تونن ویرایش/حذف کنن
        return obj.course_instructor == request.user or request.user.role == 'admin'


class IsStudent(permissions.BasePermission):
    """
    دسترسی: فقط Studentها
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'


class IsEnrollmentOwnerOrAdmin(permissions.BasePermission):
    """
    دسترسی روی یک ثبت‌نام خاص:
    - Admin: همه
    - Instructor: همه (برای مدیریت دانشجوها)
    - Student: فقط ثبت‌نام خودش
    """

    def has_object_permission(self, request, view, obj):
        # Admin یا Instructor → دسترسی کامل
        if request.user.role in ['admin', 'instructor']:
            return True

        # Student → فقط ثبت‌نام خودش
        return obj.student == request.user
