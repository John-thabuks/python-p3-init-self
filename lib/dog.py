#!/usr/bin/env python3

class Dog:
    #__init__
    #arguments: name, breed(optional) = "Mutt" of the dog
    #store the name in self.name
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed