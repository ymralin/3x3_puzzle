import tkinter as tk
from tkinter import messagebox
from random import sample
from random import randint

window = tk.Tk()
window.title("Puzzle")

window.geometry("300x400")

color1="red"
color2="green"
move_counter=0


#region define color changes

def change_b11():
    if button_11.cget("bg") == color1:
        button_11.config(bg=color2)
    else:
        button_11.config(bg=color1)

def change_b12():
    if button_12.cget("bg") == color1:
        button_12.config(bg=color2)
    else:
        button_12.config(bg=color1)

def change_b13():
    if button_13.cget("bg") == color1:
        button_13.config(bg=color2)
    else:
        button_13.config(bg=color1)

def change_b21():
    if button_21.cget("bg") == color1:
        button_21.config(bg=color2)
    else:
        button_21.config(bg=color1)

def change_b22():
    if button_22.cget("bg") == color1:
        button_22.config(bg=color2)
    else:
        button_22.config(bg=color1)

def change_b23():
    if button_23.cget("bg") == color1:
        button_23.config(bg=color2)
    else:
        button_23.config(bg=color1)

def change_b31():
    if button_31.cget("bg") == color1:
        button_31.config(bg=color2)
    else:
        button_31.config(bg=color1)

def change_b32():
    if button_32.cget("bg") == color1:
        button_32.config(bg=color2)
    else:
        button_32.config(bg=color1)

def change_b33():
    if button_33.cget("bg") == color1:
        button_33.config(bg=color2)
    else:
        button_33.config(bg=color1)

#endregion

#region define click effects

def click_b11():
    global move_counter
    change_b11()
    change_b12()
    change_b21()
    move_counter +=1
    color_check()

def click_b12():
    global move_counter
    change_b11()
    change_b12()
    change_b13()
    change_b22()
    move_counter +=1
    color_check()

def click_b13():
    global move_counter
    change_b12()
    change_b13()
    change_b23()
    move_counter +=1
    color_check()

def click_b21():
    global move_counter
    change_b11()
    change_b21()
    change_b22()
    change_b31()
    move_counter +=1
    color_check()

def click_b22():
    global move_counter
    change_b12()
    change_b21()
    change_b22()
    change_b23()
    change_b32()
    move_counter +=1
    color_check()

def click_b23():
    global move_counter
    change_b13()
    change_b22()
    change_b23()
    change_b33()
    move_counter +=1
    color_check()

def click_b31():
    global move_counter
    change_b21()
    change_b31()
    change_b32()
    move_counter +=1
    color_check()

def click_b32():
    global move_counter
    change_b22()
    change_b31()
    change_b32()
    change_b33()
    move_counter +=1
    color_check()

def click_b33():
    global move_counter
    change_b23()
    change_b32()
    change_b33()
    move_counter +=1
    color_check()

#endregion

#region changes
# list of possible changes
changes = [change_b11,change_b12,change_b13,change_b21,change_b22,change_b23,change_b31,change_b32,change_b33
]
#endregion

#region restart
# changes all buttons to red and randomly changes 3 to 7 of them to green
def restart():
    global move_counter
    button_11.config(bg=color1),
    button_12.config(bg=color1),
    button_13.config(bg=color1),
    button_21.config(bg=color1),
    button_22.config(bg=color1),
    button_23.config(bg=color1),
    button_31.config(bg=color1),
    button_32.config(bg=color1),
    button_33.config(bg=color1),
    sampled_changes = sample(changes,randint(0,8))
    for change in sampled_changes:
        change()
    move_counter = 0
#endregion


#region color check
# checks if all buttons are green and if they are, shows victory message
color_list=[]
a=1

def color_check():
    buttons = [button_11, button_12, button_13,
               button_21, button_22, button_23,
               button_31, button_32, button_33]
    color_list.clear()
    a=1
    for but in buttons:
        #color_list.append(but.cget("bg"))
        a= a* but.cget("bg")=="green"
    if a==1:
        messagebox.showinfo("Victory", "Victory in " + str(move_counter) + " moves")
        if_retry=messagebox.askquestion("Restart", "Do you want to restart the game?")
        if if_retry=="yes":
            restart()
        else:
            window.destroy()

#endregion

#region define buttons

frame_11 = tk.Frame(window, width = 100, height = 100)

button_11 = tk.Button(
    frame_11,
    bg=color1,
    command = click_b11)

frame_11.grid_propagate(False)
frame_11.columnconfigure(0,weight=1)
frame_11.rowconfigure(0,weight=1)
frame_11.grid(row=0,column=0)
button_11.grid(sticky="wens")

frame_12 = tk.Frame(window, width = 100, height = 100)

button_12 = tk.Button(
    frame_12,
    bg=color1,
    command = click_b12)

frame_12.grid_propagate(False)
frame_12.columnconfigure(0,weight=1)
frame_12.rowconfigure(0,weight=1)
frame_12.grid(row=0,column=1)
button_12.grid(sticky="wens")

frame_13 = tk.Frame(window, width = 100, height = 100)

button_13 = tk.Button(
    frame_13,
    bg=color1,
    command=click_b13)

frame_13.grid_propagate(False)
frame_13.columnconfigure(0,weight=1)
frame_13.rowconfigure(0,weight=1)
frame_13.grid(row=0,column=2)
button_13.grid(sticky="wens")

frame_21 = tk.Frame(window, width = 100, height = 100)

button_21 = tk.Button(
    frame_21,
    bg=color1,
    command=click_b21)

frame_21.grid_propagate(False)
frame_21.columnconfigure(0,weight=1)
frame_21.rowconfigure(0,weight=1)
frame_21.grid(row=1,column=0)
button_21.grid(sticky="wens")

frame_22 = tk.Frame(window, width = 100, height = 100)

button_22 = tk.Button(
    frame_22,
    bg=color1,
    command=click_b22)

frame_22.grid_propagate(False)
frame_22.columnconfigure(0,weight=1)
frame_22.rowconfigure(0,weight=1)
frame_22.grid(row=1,column=1)
button_22.grid(sticky="wens")

frame_23 = tk.Frame(window, width = 100, height = 100)

button_23 = tk.Button(
    frame_23,
    bg=color1,
    command=click_b23)

frame_23.grid_propagate(False)
frame_23.columnconfigure(0,weight=1)
frame_23.rowconfigure(0,weight=1)
frame_23.grid(row=1,column=2)
button_23.grid(sticky="wens")

frame_31 = tk.Frame(window, width = 100, height = 100)

button_31 = tk.Button(
    frame_31,
    bg=color1,
    command=click_b31)

frame_31.grid_propagate(False)
frame_31.columnconfigure(0,weight=1)
frame_31.rowconfigure(0,weight=1)
frame_31.grid(row=2,column=0)
button_31.grid(sticky="wens")

frame_32 = tk.Frame(window, width = 100, height = 100)

button_32 = tk.Button(
    frame_32,
    bg=color1,
    command=click_b32)

frame_32.grid_propagate(False)
frame_32.columnconfigure(0,weight=1)
frame_32.rowconfigure(0,weight=1)
frame_32.grid(row=2,column=1)
button_32.grid(sticky="wens")

frame_33 = tk.Frame(window, width = 100, height = 100)

button_33 = tk.Button(
    frame_33,
    bg=color1,
    command=click_b33)

frame_33.grid_propagate(False)
frame_33.columnconfigure(0,weight=1)
frame_33.rowconfigure(0,weight=1)
frame_33.grid(row=2,column=2)
button_33.grid(sticky="wens")

frame_bottom = tk.Frame(window, width = 300, height = 100)
button_restart = tk.Button(
    frame_bottom,
    text = "RESTART",
    bg="blue",
    fg = "white",
    command = restart)

frame_bottom.grid_propagate(False)
frame_bottom.columnconfigure(0,weight=1)
frame_bottom.rowconfigure(0,weight=1)
frame_bottom.grid(row=4, column=0, columnspan = 3)
button_restart.grid(sticky="wens")

#endregion

# buttons have random colors on start
restart()


window.mainloop()
