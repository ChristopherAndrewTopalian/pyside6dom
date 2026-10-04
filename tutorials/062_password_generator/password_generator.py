# password_generator.py

from pyside6dom import *

init_window('OurApp', 700, 600)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')','_']

password = ce('div')
password.textContent = 'Password'
ba(password)

run_app()