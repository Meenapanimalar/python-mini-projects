import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_var = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Counter")
window.config(padx= 100 , pady= 50, bg=YELLOW)
timer = Label(window, text="Timer" ,font = (FONT_NAME, 37,"bold"), bg= YELLOW, fg= PINK)
timer.grid(column= 1 , row= 0)


def count_down(count):
    global reps
    global timer_var
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_timer, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer_var =  window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps != 0 & reps % 2 == 0:
            checkmark.config(text = "✔️")
def reset_timer():
    global timer_var
    window.after_cancel(timer_var)
    timer.config(text="Timer")
    timer_var


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN* 60
    if reps == 8:
        timer.config(text="Time for a long break buddy",fg= YELLOW)
        count_down(long_break_sec)
    elif reps%2 == 1:
        timer.config(text="Time for Work!!", fg=GREEN)
        count_down(work_sec)
    elif reps%2 == 0:
        timer.config(text="Time for a short break buddy", fg=PINK)
        count_down(short_break_sec)



canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100 , 112, image= tomato_image)

text_timer = canvas.create_text(100,130, text = "00:00" ,fill = "white", font = (FONT_NAME, 35,"bold"))
canvas.grid(column=1, row=1)



start = Button(window, text= "Start" , command= start_timer)



start.grid(column = 0 , row = 2)

reset = Button(window, text= "Reset" , command= reset_timer)



reset.grid(column = 2 , row = 2)
checkmark = Label(window,font = (FONT_NAME, 10,"bold"), bg= YELLOW, fg= GREEN)
checkmark.grid(column=1, row=3)
window.mainloop()