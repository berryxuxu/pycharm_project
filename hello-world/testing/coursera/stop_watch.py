# http://www.codeskulptor.org/#user41_j0fVoRHPhw_0.py
# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    if t < 10:
        return '0:00.' + str(t)
    elif t < 100:
        return '0:0' + str(t/10) + '.' +  str(t%10)
    elif t < 600:
        return '0:' + str(t/10) + '.' + str(t%10)
    else:
        nt = format(t%600)
        nt1 = nt.replace('0',str(t/600),1)
        return nt1


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    timer.stop()
    global time
    time = 0

# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1

timer = simplegui.create_timer(100,time_handler)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time),[10,170],90,'Red')


# create frame
frame = simplegui.create_frame('Stopwatch',300,300)
button1 = frame.add_button('Start', start)
button2 = frame.add_button('Stop', stop)
button3 = frame.add_button('Reset',reset)
# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

## Please remember to review the grading rubric
