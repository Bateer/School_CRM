# -*- Coding: utf-8 -*-
# Author: Yu

class Teacher(object):
    def __init__(self, teacher_name, teacher_age, teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_age = teacher_age
        self.teacher_salary = teacher_salary
        self.teacher_classroom = {}

    def add_teach_classroom(self, class_name, class_obj):
        self.teacher_classroom[class_name] = class_obj
