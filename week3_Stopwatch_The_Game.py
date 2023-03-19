# template for "Stopwatch: The Game"
import simplegui as sg

# define global variables
counter = 0
stop_times = 0
score = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return str(t/600) + ":" + str((t / 100) % 6) + str((t / 10) % 10) + "." + str(t % 10)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    
    global score
    global stop_times
    
    timer.stop()
    stop_times += 1
    if counter % 10 == 0:
        score += 1
    
def reset_handler():
    global counter
    global stop_times
    global score
    
    counter = 0
    stop_times = 0
    score = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), [160, 150], 35, 'White')
    canvas.draw_text(str(score) +  '/' + str(stop_times) , [340, 40], 30, 'Red')
    
# create frame
fm = sg.create_frame("Stopwatch: The Game", 400, 300)

# register event handlers

timer = sg.create_timer(100, timer_handler)
fm.set_draw_handler(draw_handler)

btn_start = fm.add_button('Start', start_handler, 150)
btn_stop = fm.add_button('Stop', stop_handler, 150)
btn_reset = fm.add_button('Reset', reset_handler, 150)




# start frame
fm.start()

# Please remember to review the grading rubric
