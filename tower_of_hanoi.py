#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:53:35 2021

Implemenetation of Tower of Hanoi Algorithm
@author: Saqlain
"""


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Moving disk 1 from source {} to destination {}.".format(source, destination))
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print("Move disk {} from source {} to destination {}.".format(n, source, destination))
    tower_of_hanoi(n-1, auxiliary, destination, source)
    
    
tower_of_hanoi(3, "A", "B", "C")