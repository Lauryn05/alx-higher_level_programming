#!/usr/bin/python3
"""Defines a Python class-to-JSON function"""


class Student:
    """represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize new Student

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self_age = age

   def to_json(self):
       """Return dictionary rep of a simple data structure"""
       return self.__dict__
