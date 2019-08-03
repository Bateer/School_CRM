# -*- Coding: utf-8 -*-
# Author: Yu
import os
import shelve

from conf import setings
from src.classroom import Classroom
from src.course import Course
from src.school import School
from src.student import Student
from src.teacher import Teacher

class Center(object):

    def run(self):
        exit_flag = False
        menu = u'''
            \033[32;1m
            1. 学生视图
            2. 讲师视图
            3. 学校视图
            4. 退出 \n\033[om'''

        while not exit_flag:
            print(menu)
            user_option = input("请输入要进入的管理的视图:")
            if user_option == '1':
                Student_view()
            elif user_option == '2':
                Teacher_view()
            elif user_option == '3':
                School_view()
            elif user_option == '4':
                break
            else:
                print("你输入的选项错误，请重新输入")

class School_view(object):
    def __init__(self):
        if os.path.exists(setings.school_file+'.dat'):
            self.school_file = shelve.open(setings.school_file)
            self.school_manager()
            self.school_file.close()
        else:
            print("没有该学校信息和数据，请先创建")
            self.init_school()
            self.school_manager()
            self.school_file.close()

    def init_school(self):
        self.school_file = shelve.open(setings.school_file)
        self.school_file["北京"] = School("余家培训机构", "成都")
        self.school_file["宜宾"] = School("李家考研班", "宜宾")

    def school_manager(self):
        while True:
            for sch_name in self.school_file:
                print("这儿有的学校有：%s" % sch_name)

            sch_option = input("请输入你要管理的学校：").strip()
            if sch_option in self.school_file:
                self.sch_option = sch_option
                self.school_obj = self.school_file[sch_option]

                menu = u'''            
                        \033[32;1m
                        欢迎来到 %s 学校：
                        1. 添加课程 add_course
                        2. 添加班级 add_classroom
                        3. 添加讲师 add_teacher
                        4. 查询课程 show_course
                        5. 查询班级 show_classroom
                        6. 查询讲师 show_teacher
                        7. 退出 exit
                        \033[om''' % sch_option
                while True:
                    print(menu)
                    user_choice = input("请输入你的选择：")
                    if hasattr(self, user_choice):
                        getattr(self, user_choice)()

    def add_course(self):
        course_name = input("请输入你的需要填写的课程的名字：")
        course_price = input("请输入该课程的价格：")
        course_time = input("请输入该课程的学习时间：")
        if course_name in self.school_obj.sch_course:
            print("该课程已经存在了！")
        else:
            self.school_obj.create_course(course_name, course_price, course_time)
            print("%s课程，已经添加成功！" % course_name)
            self.school_file.update({self.sch_option:self.school_obj})

    def add_classroom(self):
        class_name = input("请输入班级名字：").strip()
        class_course = input("请输入课程名字：").strip()
        if class_name not in self.school_obj.sch_classroom:
            if class_course in self.school_obj.sch_course:
                course_obj = self.school_obj.sch_course[class_course]
                self.school_obj.create_classroom(class_name, course_obj)
                self.school_file.update({self.sch_option: self.school_obj})
                print("班级创建成功")
            else:
                print("课程不存在")
        else:
            print("该班级已经存在")

    def add_teacher(self):
        teacher_name = input("请输入老师名字").strip()
        teacher_age = input("请输入老师的年龄").strip()
        teacher_salary = input("请输入老师的工资").strip()
        teach_class = input("请输入班级名字").strip()

        if teach_class in self.school_obj.sch_classroom:
            class_obj = self.school_obj.sch_classroom[teach_class]
            if teacher_name not in self.school_obj.sch_teacher:
                self.school_obj.create_teacher(teacher_name, teacher_age, teacher_salary, teach_class)
                print("创建教师成功！")
            else:
                print("该教师已经存在")
            self.school_file.update({self.sch_option: self.school_obj})
        else:
            print("请先创建班级")
            class_name = input("请输入班级名字：").strip()
            class_course = input("请输入课程名字：").strip()
            if class_course in self.school_obj.sch_course:
                course_obj = self.school_obj.sch_course[class_course]
                self.school_obj.create_classroom(class_name, course_obj)
                self.school_file.update({self.sch_option: self.school_obj})
                print("班级创建成功")
            else:
                print("课程不存在")

    def show_course(self):
        course_name = input("请输入你要查询课程名字")
        if course_name in self.school_obj.sch_course:
            course_infor = self.school_obj.sch_course[course_name]
            print("课程名称为%s\t 课程价格为%s\t 课程的时间为%s" % (
                course_infor.course_name, course_infor.course_price, course_infor.course_time))
        else:
            print("找不到该课程，请先创建课程")

    def show_classroom(self):
        classroom_name = input("请输入要查询的班级名字")
        if classroom_name in self.school_obj.sch_classroom:
            classroom_infor = self.school_obj.sch_classroom[classroom_name]
            print("该班级名字: %s  该班级的课程有: %s" % (classroom_infor.classroom_name,
                                              classroom_infor.course_obj.course_name))
        else:
            print("找不到该班级，请先去创建班级")

    def show_teacher(self):
        teacher_name = input("请输入你要查询的讲师名字")
        if teacher_name in self.school_obj.sch_teacher:
            teacher_infor = self.school_obj.sch_teacher[teacher_name]
            for class_name_key in teacher_infor.teacher_classroom:
                print("老师的名字：%s 年龄：%s 工资：%s 所教班级：%s" % (teacher_name,teacher_infor.teacher_age,
                                                    teacher_infor.teacher_salary, class_name_key))
        else:
            print("找不到该讲师，请先创建讲师")

    def exit(self):
        exit()

class Teacher_view(object):
    def __init__(self):
        if os.path.exists(setings.school_file +'.dat'):
            self.school_file = shelve.open(setings.school_file)
            self.teacher_manager()
            self.school_file.close()
        else:
            print("讲师数据不存在，请先创建学校或者创建教师数据")
            self.school_file.close()

    def teacher_manager(self):
        while True:
            for sch_name in self.school_file:
                print("这儿的学校有：%s" %(sch_name))
            sch_option = input("请输入你要进入管理的学校:")
            if sch_option in self.school_file:
                self.sch_option = sch_option
                self.sch_obj = self.school_file[sch_option]
                for teach_name in self.sch_obj.sch_teacher:
                    print("该学校有的老师有：%s" %(teach_name))
                teach_option = input("请输入你的姓名：")
                if teach_option in self.sch_obj.sch_teacher:
                    self.teach_option = teach_option
                    self.teach_obj = self.sch_obj.sch_teacher[teach_option]

                    menu = u'''            
                        \033[32;1m
                        欢迎来到 %s 学校 %s老师：
                        1. 查询所在班级 show_classroom
                        2. 查询所在班级的学生 show_student
                        3. 修改学生成绩 modify_score
                        4. 退出 exit
                        \033[om''' % (sch_option, teach_option)
                    while True:
                        print(menu)
                        user_choice = input("请输入你的选择：")
                        if hasattr(self, user_choice):
                            getattr(self, user_choice)()
            else:
                print("该学校不存在")

    def show_classroom(self):
        for classroom_name in self.teach_obj.teacher_classroom:
            print("该老师管理的班级有 %s" % classroom_name)

    def show_student(self):
        self.sch_obj.show_tech_stu_info(self.teach_option)
        # for classroom_name in self.teach_obj.teacher_classroom:
        #     classroom_obj = self.teach_obj.teacher_classroom[classroom_name]
        #     for student_name in classroom_obj.class_student:
        #         print("该班级有的学生：%s" % student_name)

    def modify_score(self):
        student_name = input("请输入你要修改的学生名字：")
        if student_name in self.sch_obj.sch_student:
            student_obj = self.sch_obj.sch_student[student_name]
            print("该学生的分数是 %s" % student_obj.student_score)
            new_score = input("请输入你要修改的新的分数: ")
            student_obj.modify_score(new_score)
            print("该学生的分数是 %s" % student_obj.student_score)
        else:
            print("找不到该学生，请先进入创建")
        self.school_file.update({self.sch_option: self.sch_obj})

    def exit(self):
        exit()

class Student_view(object):
    def __init__(self):
        if os.path.exists(setings.school_file+'.dat'):
            self.school_file = shelve.open(setings.school_file)
            self.student_manager()
            self.school_file.close()
        else:
            print("学生数据找不到，请先创建学校或者创建学生数据")
            self.school_file.close()

    def student_manager(self):
        while True:
            for sch_name in self.school_file:
                print("目前的学校有 %s " % sch_name)
            sch_option = input("请输入你要进去管理的学校：")
            if sch_option in self.school_file:
                self.sch_option = sch_option
                self.sch_obj = self.school_file[sch_option]
                class_name = input("请输入你所在的班级：")
                if class_name in self.sch_obj.sch_classroom:
                    self.class_name = class_name
                    self.class_obj = self.sch_obj.sch_classroom[class_name]
                    student_name = input("请输入你的名字：")
                    if student_name in self.class_obj.class_student:
                        self.studen_name = student_name
                        student_obj = self.class_obj.class_student[student_name]
                        print("-----welcome %s------\n"
                              "姓名: %s\n"
                              "年龄: %s\n"
                              "年级: %s\n" % (student_obj.student_name, student_obj.student_name,
                                           student_obj.student_age, student_obj.student_gender))

                        menu = u'''            
                            \033[32;1m
                            欢迎来到 %s 学校 %s学生：
                            1. 查询分数 show_score
                            2. 退出 exit
                            \033[om''' % (sch_option, student_name)

                        while True:
                            print(menu)
                            user_choice = input("请输入你的选择")
                            if hasattr(self, user_choice):
                                getattr(self, user_choice)()

                    else:
                        print("找不到该学生，请先完成注册")
                        menu_regist = u'''
                            \033[32:1m\n
                            1. 进入注册 regist
                            2. 返回 return
                            \033[om'''
                        print(menu_regist)
                        user_choose = input("请输入你的选择：")
                        if user_choose == '1':
                            student_name = input("请输入你要注册学生的名字:")
                            student_age = input("请输入你的年龄：")
                            student_gender = input("请输入你的年级：")
                            self.sch_obj.create_student(student_name, student_age, student_gender, class_name)
                            print("注册成功")
                            self.school_file.update({self.sch_option: self.sch_obj})
                        elif user_choose == '2':
                            break
                else:
                    print("该班级不存在，请输入正确的班级")
            else:
                print("暂时没有开放该学校")

    def show_score(self):
        student_obj = self.sch_obj.sch_student[self.studen_name]
        print("你的分数是：%s" % student_obj.student_score)

    def exit(self):
        exit()