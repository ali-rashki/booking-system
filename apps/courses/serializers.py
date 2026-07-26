from rest_framework import serializers
from .models import Course, Session, Enrollment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate_course_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("عنوان دوره باید حداقل ۳ کاراکتر باشد")
        return value


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("زمان شروع باید قبل از زمان پایان باشد")
        return data


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

    def validate(self, data):
        session = data['session']
        if session.enrollments.count() >= session.capacity:
            raise serializers.ValidationError("ظرفیت کلاس پر شده است")
        return data
