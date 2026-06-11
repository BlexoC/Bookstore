#!/usr/bin/env python3

class Coffee:
    def __init__(self, size , price):
        self.size = size
        self.price = price

    size = input("Enter the Size You Want: ")
    price = int(input("Enter the Price Required: "))

    if  not size in ("small","large","medium"):
        print("size must be Small, Medium, or Large")

    def tip(self):
         print ("This coffee is great, here's a tip!\n")
         self.price += 1
        