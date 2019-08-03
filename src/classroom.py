# -*- Coding: utf-8 -*-
# Author: Yu

class Classroom(object):
    def __init__(self, classroom_name, course_obj):
        self.classroom_name = classroom_name
        self.course_obj = course_obj
        self.class_student = {}