import sys
import mss
import time
import config
import keyboard
import threading
import numpy as np

from os import path as p # Ёлочка импортов :)

if p.isdir(sys.argv[0]):
	path = sys.argv[0]
else:
	path = f"{sys.argv[0]}\\.."

class Builder():

	def __init__(self,  status_text=None):

		self.status_text = status_text
		self.sct = mss.mss()
		self.active = False

	def start(self):

		if not self.active:
			
			if self.status_text:
				self.status_text.config(text="PROCESS", font="TimesNewRoman 14 bold", foreground="yellow")
				time.sleep(2)
				self.status_text.config(text="ON", font="TimesNewRoman 14 bold", foreground="green")
			self.active = True

			t1 = threading.Thread(target=self.building_cycle, daemon=True)
			t1.start()	

	def stop(self):

		self.active = False
		if self.status_text:
			self.status_text.config(text="OFF", font="TimesNewRoman 14 bold", foreground="red")

	def building_cycle(self):

		while self.active:

			img1 = np.asarray(self.sct.grab(config.mon1))
			data = []
			for i in img1:
				for j in i:
					if j[0] >= 200 and j[1] >= 200 and j[2] >= 200:
						data.append(j)

			if 75 < len(data) < 85:
				b = "y"
			elif 85 < len(data) < 100:
				b = "f"
			elif 135 > len(data) > 110:
				b = "e"
			else:
				continue

			for _ in range(25):
					keyboard.send(b)
