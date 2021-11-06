from bot import *
import tkinter as tk

window = tk.Tk()

status_text = tk.Label(window, text="ON", foreground="green", font="TimesNewRoman 18 bold")
bot = Builder(status_text)

window.title("Easy Building")
window.geometry("200x200+0+100")
window.resizable(0, 0)

def button(text):
	return tk.Button(window, text=text, width=10, height=2)

button_start = button("Start")
button_stop = button("Stop")

button_start.grid(column=1, row=1)
button_stop.grid(column=1, row=2)
status_text.grid(column=2, row=1)

button_start.config(command=bot.start)
button_stop.config(command=bot.stop)

keyboard.add_hotkey("Ctrl+Num 1", bot.start)
keyboard.add_hotkey("Ctrl+Num 2", bot.stop)

bot.stop()
window.mainloop()
bot.active = False

