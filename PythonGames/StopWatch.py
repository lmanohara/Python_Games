# Stopwatch game
# Autor Lahiru Manohara

import simplegui
# define global variables
counter_win = 0
counter_time = 0
time = 0
interval = 100
tens = 0
# define helper function format that converts integer
def help_1(second):
    if(second < 10):
        return "0" + str(second)
    else:
        return str(second)
    
def help_2(second):
    global tens
    if(second < 10):
        return "0" + str(second) + ".0" 
    else:
        second = int(second / 10)
        tens = second % 10
        return help_1(second_1) + "." + str(tens)
    
# counting tenths of seconds into formatted string A:BC.D
def format(time):
    global tens
    if(time < 10):
        tens = time
        second = 0
        minutes = 0
        return str(minutes) + ":0" + str(second) + "." + str(tens)
    if(time == 10):
        tens = 0
        second = int(time / 10)
        minutes = 0
        return str(minutes) + ":0" + str(second) + "." + str(tens) 
    elif(time > 10 and time < 600):
        second = int(time / 10)
        tens = time % 10
        minutes = 0
        return str(minutes) + ":"  + help_1(second) + "." + str(tens)
    elif(time == 600):
        minutes = 1
        second = 0
        tens = 0
        return str(minutes) + ":" + str(second) + "." + str(tens)
    elif(time > 600):
        minutes = int(time / 600)
        second = time % 600
        return str(minutes) + ":" + help_2(second)
        
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    timer.start()
    
def winner():
    global counter_time
    global counter_win
    global tens
    counter_time = counter_time + 1
    if(tens == 0):
        counter_win = counter_win + 1
    
def button_stop():
    winner()
    timer.stop()

def button_reset():
    global counter_time
    counter_time = 0
    global counter_win
    counter_win = 0
    global time
    time = 0

# define event handler for timer with 0.1 sec interval
def draw(canvas):
    global counter_time
    global counter_win
    str_time = format(time)
    canvas.draw_text(str_time, (150, 150), 30, "white")
    canvas.draw_text(str(counter_win), (300,20), 20, "red")
    canvas.draw_text("/", (315,20), 15, "red")
    canvas.draw_text(str(counter_time), (325,20), 20, "red")
    
def timer():
    global time
    time = time + 1      
    format(time)
     
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, timer)
frame.add_button("Start", button_start, 100)
frame.add_button("Stop", button_stop, 100)
frame.add_button("Reset", button_reset, 100)

# start timer and frame
frame.start()



# remember to review the grading rubric