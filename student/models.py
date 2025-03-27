import os

from django.db import models

# Create your models here.
class Clas(models.Model):
    name = models.CharField(max_length=32, verbose_name='班级名称')

    class Meta:
        db_table = 'db_class'


class Course(models.Model):
    title = models.CharField(max_length=32, verbose_name='课程名称')
    credit = models.IntegerField(verbose_name='学分', default=3)
    teacher = models.CharField(max_length=32, verbose_name='老师', null=True)
    classTime = models.CharField(max_length=32, verbose_name='上课时间', null=True)
    classAddr = models.CharField(max_length=32, verbose_name='地址', null=True)
    class Meta:
        db_table = 'db_course'

    def __str__(self):
        return self.title

    # students = models.ManyToManyField('Student', db_table='db_student2course')

from django.contrib.auth.models import AbstractUser
def user_directory_path(instance, filename):
    return os.path.join(instance.username, 'avatars', filename)

class UserInfo(AbstractUser):
    avatar = models.FileField(upload_to=user_directory_path, default='/avatar/default.jpg')
    stu = models.OneToOneField('Student', on_delete=models.CASCADE, unique=True, null=True)

class Student(models.Model):
    sex_choices = (
        (0, '女'),
        (1, '男'),
        (2, '保密'),
    )
    name = models.CharField(max_length=32, unique=True, verbose_name='姓名')
    age = models.SmallIntegerField(verbose_name='年龄', default=18)
    sex = models.SmallIntegerField(choices=sex_choices)
    birthday = models.DateField()

    # 一对多的关系 在多的表中创建关联的字段
    # 在数据库创建一个关联字段：clas_id
    clas = models.ForeignKey(to='Clas', related_name='student_list', on_delete=models.CASCADE, db_constraint=False)

    # 多对多的关系 创建第三张关系表
    courses = models.ManyToManyField('Course', related_name='stu_list', db_table='db_student2course')

    # 一对一的关系 创建关联字段 在数据库中生成关联字段：stu_detail_id
    stu_detail = models.OneToOneField('StudentDetail', related_name='stu', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'db_student'

    def __str__(self):
        return self.name


class StudentDetail(models.Model):
    tel = models.CharField(max_length=11)
    addr = models.CharField(max_length=32)

    class Meta:
        db_table = 'db_stu_detail'
