#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:37:43 2021
@author: slowhusky
github: slowhusky
"""
def percent_calc(bill, percentage):
    tip = (bill * percentage)/100
    print(f'\nThe percentage is {tip:.2f}')

if __name__ == "__main__":
    print("Tip calculator")
    bill = input("What was the total bill? ")
    percentage = input("What percentage tip whould you like to give? ")
    
    percent_calc(float(bill), float(percentage))