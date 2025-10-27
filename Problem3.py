# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Rosland Problem 3

Indexes = [14, 21, 46, 53]
myString = "JN5AXBASdaOVZgLatastiakD5DmOt4meaXotpDq3xUMzRkcitreolaThuki9GbAUyuIUqL1iSn9hVZugLxbEB73ncLQmnOEYNGn9t6VcIMPhjAu6t4Nhm3aacTeivcDToECWKF4G8d1mQYwPlJJty2qicIJlk1p4vTAi3XthBPJGz6Rboi8MgLdZ8jIO7oV7NVHo."

newString = myString[Indexes[0]:Indexes[1]+1] + " " + myString[Indexes[2]:Indexes[3]+1]
print (newString)

