from Snake_game1 import gameboy
import tkinter as tk
import pygame as pg
import os
# path=os.path.abspath("gamebo1.mp3")
# pg.mixer.init()

def star():
    # pg.mixer.music.stop()
    menu.destroy()
    gameboy()
def leaf():
    # pg.mixer.music.stop()
    menu.destroy()
    # 

# pg.mixer.music.load("C:\Users\shriy\snake\gamebo1.mp3")
# pg.mixer.music.set_volume(0.5)
# pg.mixer.music.play(-1)
menu=tk.Tk()
menu.title("vegan snak lol")
menu.geometry("300x200")

st=tk.Button(menu, text="Play!",command=star,font=("Arial", 14),width=12)
st.pack(pady=20)

exit=tk.Button(menu, text="Leave\n (loser)",command=leaf,font=("Comic Sans",14),width=12)
exit.pack(pady=20)
menu.mainloop()