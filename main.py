import pyperclip
import pyautogui
import random
from time import sleep

def main():
	# print(pyautogui.position())
	# return

	# left bottom
	x = random.randint(800, 820)
	y = random.randint(560, 570)
	pyautogui.click(x, y)
	pause = random.randint(1, 5)
	# left top
	x = random.randint(800, 820)
	y = random.randint(360, 370)
	pyautogui.click(x, y)
	pause = random.randint(1, 5)
	# right top
	x = random.randint(1100, 1150)
	y = random.randint(335, 355)
	pyautogui.click(x, y)
	pause = random.randint(1, 5)
	# right bottom
	x = random.randint(1100, 1150)
	y = random.randint(560, 570)
	pyautogui.click(x, y)
	pause = random.randint(1, 5)





if __name__ == '__main__':
	print('Waiting 10 seconds...')
	sleep(10)
	print('Working...')
	for i in range(5):
		print('Round: ', i+1)
		main()
		# Waiting 45*60+1 seconds 
		sleep(45*60+1)