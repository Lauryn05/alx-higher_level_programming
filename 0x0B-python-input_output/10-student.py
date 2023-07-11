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

   def to_json(self, attrs=None):
       """Return dictionary rep of the Student

       If attrs is a list of strings, represents only those attributes
       included in the list

       Args:
           attrs (list): (Optional) The attributes to represent
       """
       if (type(attrs) == list and
               all(type(ele) == str for ele in attrs)):
           return{k: getattr(self, k) for k in attrs if hasattr(self, k)}
       return self.__dict__
