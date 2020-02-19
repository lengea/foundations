#!usr/bin/env python3

import cgi

form = cgi.FieldStorage()
username = form.getvalue("name")

print(f"""
	<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
  </head>
  <body>

  <h1>Hello {username}</h1>
    
  </body>
  
  </html>

 
	""")

'''

name = input("What is your name?")

print('Hello,' + ' ' + name + '!')

age = input("What is your age?")

print('You are' + ' ' + age + ' ' + 'years old!')

Print('Welcome to the platform!')
'''





