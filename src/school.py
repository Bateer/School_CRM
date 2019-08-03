# -*- Coding: utf-8 -*-
# Author: Yu
from src.classroom import Classroom
from src.course import Course
from src.student import Student
from src.teacher import Teacher

class School(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.sch_course = {}
        self.sch_classroom = {}
        self.sch_teacher = {}
        self.sch_student = {}

    def create_course(self, course_name, course_price, course_time):
        # 1. 创建可成对象
        # 2. 根据课程名称为key， 课程对象为valve来建立对应的关系
        course_obj = Course(course_name, course_price, course_time)
        self.sch_course[course_name] = course_obj

    def show_course(self):
        for course_key in self.sch_course:
            course_infor = self.sch_course[course_key]
            print("课程名称为%s\t 课程价格为%s\t 课程的时间为%s" % (
            course_infor.course_name, course_infor.course_price, course_infor.course_time))

    def modify_course(self):
        modify_course_name = input("请输入你要更改的课程名字:")
        for course_key in self.sch_course:
            modify_course_obj = self.sch_course[course_key]
            if course_key == modify_course_name:
                print("请选择你要修改的选项：1. 课程名字\t 2. 课程价格\t 3. 课程时间\t")
                input_num = input("请输入你的选择：")
                if input_num == "1":
                    modify_name = input("请输入你修改之后的名字:")
                    modify_course_obj.course_name = modify_name
                elif input_num == "2":
                    modify_price = input("请输入你修改之后的价格:")
                    modify_course_obj.course_price = modify_price
                elif input_num == "3":
                    modify_time = input("	请输入你修改之后的时间:")
                    modify_course_obj.course_time = modify_time
            else:
                print("该学校没有这个课程")

    def create_classroom(self, classroom_name, course_obj):
        classroom_obj = Classroom(classroom_name, course_obj)
        self.sch_classroom[classroom_name] = classroom_obj

    def show_classroom(self):
        for classroom_key in self.sch_classroom:
            classroom_infor = self.sch_classroom[classroom_key]
            print("该班级名字: %s  该班级的课程有: %s" % (classroom_infor.classroom_name,
                                              classroom_infor.course_obj))

    def modify_classroom(self):
        modify_classroom_name = input("请输入你要修改的班级名字")
        for modify_classroom_key in self.sch_classroom:
            modify_classroom_infor = self.sch_classroom[modify_classroom_key]
            if modify_classroom_name == modify_classroom_key:
                print("请输入你要选择修改的选项：1. 班级名字；2. 课程名称")
                input_num = input("请输入的选择：")
                if input_num == '1':
                    af_modify_classroom_name = input("输入你修改之后的班级名字：")
                    modify_classroom_infor.classroom_name = af_modify_classroom_name
                elif input_num == '2':
                    af_modify_course = input("输入你修改之后的课程名字")
                    modify_classroom_infor.course_obj = af_modify_course

    def create_student(self, student_name, student_age, student_gender, class_name):
        student_obj = Student(student_name, student_age, student_gender)
        self.sch_student[student_name] = student_obj
        class_obj = self.sch_classroom[class_name]
        class_obj.class_student[student_name] = student_obj
        self.sch_classroom[class_name] = class_obj

    def show_student(self, student_name):
        stu_obj = self.sch_student[student_name]
        print("姓名：%s 年龄:%s 年级:%s 成绩:%s" % (stu_obj.student_name, stu_obj.student_age,
                                     stu_obj.student_gender, stu_obj.student_score))

    def create_teacher(self, teacher_name, teacher_age, teacher_salary, class_name):
        teacher_obj = Teacher(teacher_name, teacher_age, teacher_salary)
        self.sch_teacher[teacher_name] = teacher_obj
        class_obj = self.sch_classroom[class_name]
        teacher_obj.add_teach_classroom(class_name, class_obj)

    def show_teacher(self):
        for teacher_key in self.sch_teacher:
            teacher_obj = self.sch_teacher[teacher_key]
            for class_name_key in teacher_obj.teacher_classroom:
                print("老师的名字：%s 年龄：%s 工资：%s 所教班级：%s" % (teacher_obj.teacher_name,
                                                        teacher_obj.teacher_age, teacher_obj.teacher_salary,
                                                        class_name_key))

    def show_tech_stu_info(self, teacher_name):
        teacher_obj = self.sch_teacher[teacher_name]
        for classroom_key in teacher_obj.teacher_classroom:
            classroom_obj = self.sch_classroom[classroom_key]
            stu_list = []
            for stu_key in classroom_obj.class_student:
                stu_list.append(stu_key)
            print("班级：%s  课程：%s \n"
                  "该班级有学生：%s" % (classroom_obj.classroom_name, classroom_obj.course_obj.course_name,
                                 stu_list))

    def modify_student_score(self, teach_name, stu_name, new_score):
        teach_obj = self.sch_teacher[teach_name]
        for clroom_key in teach_obj.teacher_classroom:
            class_obj = self.sch_classroom[clroom_key]
            for stu_key in class_obj.class_student:
                if stu_key == stu_name:
                    stu_obj = class_obj.class_student[stu_name]
                    stu_obj.modify_score(new_score)
                else:
                    print("找不到这个学生")

# school_1 = School("yu", "chengdu")
# school_1.create_course("python", "456", "1 monthes")
# school_1.create_classroom("二班", "python")
# school_1.show_classroom()
# school_1.show_course()
# # school_1.modify_course()
# # school_1.show_course()
# school_1.create_student("yu", "20", "二年级", "二班")
#
# school_1.create_teacher("Mr Li", "20", "58000", "二班")
# school_1.show_teacher()
#
# school_1.show_tech_stu_info("Mr Li")
# school_1.modify_student_score("Mr Li", "yu", "100")
# school_1.show_student("yu")