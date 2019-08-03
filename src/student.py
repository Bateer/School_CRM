# -*- Coding: utf-8 -*-
# Author: Yu

class Student (object):
    def __init__(self, student_name, student_age, student_gender):
        self.student_name = student_name
        self.student_age = student_age
        self.student_gender = student_gender
        self.student_score = 0

    def modify_score(self, new_score):
        self.student_score = new_score