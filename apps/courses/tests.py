from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.courses.models import Course

User = get_user_model()


# ==============================================
# تست شماره ۱: تست مدل Course
# ==============================================
class CourseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            role='instructor'
        )
        self.course = Course.objects.create(
            course_title='دوره تست',
            course_description='توضیحات تست',
            course_category='برنامه‌نویسی',
            course_instructor=self.user
        )

    def test_course_creation(self):
        self.assertEqual(self.course.course_title, 'دوره تست')

    def test_course_str(self):
        self.assertEqual(str(self.course), 'دوره تست')


# ==============================================
# تست شماره ۲: تست Serializer
# ==============================================
from rest_framework.test import APITestCase
from apps.courses.serializers import CourseSerializer


class CourseSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser2',
            password='12345',
            role='instructor'
        )
        self.course_data = {
            'course_title': 'دوره جدید',
            'course_description': 'توضیحات',
            'course_category': 'برنامه‌نویسی',
            'course_instructor': self.user.id
        }

    def test_serializer_valid(self):
        serializer = CourseSerializer(data=self.course_data)
        self.assertTrue(serializer.is_valid())


# ==============================================
# تست شماره ۳: تست API
# ==============================================
from rest_framework.test import APIClient
from rest_framework import status


class CourseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser3',
            password='12345',
            role='instructor'
        )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_title='دوره API',
            course_description='توضیحات',
            course_category='برنامه‌نویسی',
            course_instructor=self.user
        )

    def test_get_courses(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
