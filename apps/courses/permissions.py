from rest_framework import permissions


class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ['instructor', 'admin']:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'


class IsEnrollmentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.student or request.user.role in ['admin', 'instructor']
