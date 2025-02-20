from tkinter import *
import random
import ctypes
import tkinter.font
from turtledemo.penrose import start

ctypes.windll.shcore.SetProcessDpiAwareness(1)
# Start the Tkinter main loop


WIDTH = 700
HEIGHT = 400

# Set up the window
window = Tk()
comic_font = tkinter.font.Font(family="consolas", size=30, weight="bold")
window.title("Typing Test")
window.geometry(f"{WIDTH}x{HEIGHT}")
bg_colour = "#323437"
window.configure(bg = bg_colour)
orange = "#bc9b1b"
white = "#cecdc2"
grey = "#545659"
red = "#913f49"

def start_screen():
    global started
    started = True

    global startLabel
    startLabel = Label(window, text = "Welcome To Axle's Typing Test" , font = comic_font , fg = orange , bg = bg_colour)
    startLabel.place(relx = 0.5 , rely = 0.2 , anchor = CENTER)

    global startButton
    startButton = Button(window, text = "Test Your Skills" , command = generate_new_test, font = comic_font , fg = bg_colour ,activeforeground=grey, bg = white)
    startButton.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

def generate_new_test():
    global prompt_choices
    global prompt

    global started

    if started:
        startLabel.destroy()
        startButton.destroy()
        started = False

    prompt_choices= ["The Great Wall of China stretches over thirteen thousand miles and was built to protect Chinese states from invasions. Constructed over centuries, it is a testament to human determination and engineering. Though some parts have crumbled, much of the wall remains intact and attracts millions of visitors annually. The structure winds through mountains, deserts, and grasslands, offering breathtaking views and a glimpse into China's rich history.",
                        "Artificial intelligence is revolutionizing industries worldwide. From self-driving cars to medical diagnostics, AI systems are capable of processing vast amounts of data with incredible speed and accuracy. However, concerns about ethics and job displacement remain topics of debate. As technology advances, society must strike a balance between innovation and responsibility to ensure that AI benefits humanity as a whole.",
                        "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his chest to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him. The hallway smelt of boiled cabbage and old rag mats. At one end, a colored poster, too large for indoor display, had been tacked to the wall. It depicted simply an enormous face, more than a meter wide:",
                        "The vastness of space has intrigued humankind for centuries. With every new mission, we uncover more about our universe, from distant exoplanets to the mysteries of black holes. The Apollo 11 mission in 1969 marked a historic milestone when humans first set foot on the Moon. Today, scientists are working on sending astronauts to Mars, a journey that presents both technical and psychological challenges. The dream of interplanetary travel is slowly becoming a reality.",
                        "The concept of time has fascinated philosophers for millennia. Is time an absolute, unchanging entity, or is it merely a human construct? Einstein's theory of relativity suggests that time is fluid, stretching and contracting depending on speed and gravity. This challenges our everyday perception of time as a constant march forward. If time is not as rigid as it seems, could it be possible to travel through it? The idea remains one of the great mysteries of science and philosophy.",
                        "Rainforests are often called the lungs of the Earth, producing oxygen and absorbing carbon dioxide. These dense forests are home to more than half of the world’s species, including rare and undiscovered plants and animals. However, deforestation threatens these ecosystems at an alarming rate. If left unchecked, habitat destruction could lead to the extinction of countless species. Conservation efforts aim to protect these vital forests and preserve biodiversity for future generations."]
    prompt = random.choice(prompt_choices).lower()

    global split
    split = 0

    global leftLabel
    leftLabel = Label(window, text = prompt[0:split], font = comic_font, fg = white, bg = bg_colour)
    leftLabel.place(relx = 0.5, rely = 0.5 , anchor = E)

    global rightLabel
    rightLabel = Label(window, text = prompt[split:],font = comic_font, fg = grey, bg = bg_colour)
    rightLabel.place(relx = 0.5, rely = 0.5 , anchor = W)

    global currentLetterLabel
    currentLetterLabel = Label(window, text = prompt[split], font = comic_font, fg = orange, bg = bg_colour)
    currentLetterLabel.place(relx= 0.5, rely = 0.8 , anchor = CENTER)

    global currentTimeLabel

    currentTimeLabel = Label(window, text = "0", font = comic_font, fg = orange, bg = bg_colour)
    currentTimeLabel.place(relx = 0.1 ,rely = 0.2, anchor = W)

    global AbleToWrite
    AbleToWrite = True
    window.bind("<Key>", keyPress)

    global seconds_passed
    seconds_passed = 0

    window.after(30000,stopTest)
    window.after(1000, addSecond)


def addSecond():
    global seconds_passed
    seconds_passed += 1

    currentTimeLabel.config(text = f"{seconds_passed}")

    if AbleToWrite:
        window.after(1000,addSecond)

def stopTest():
    global AbleToWrite
    AbleToWrite = False

    words_typed = len(leftLabel.cget("text").split(" "))
    wpm = words_typed * 2

    leftLabel.destroy()
    rightLabel.destroy()
    currentTimeLabel.destroy()
    currentLetterLabel.destroy()

    global wpmLabel

    wpmLabel = Label(window, text = f"wpm {wpm}" , fg = orange, font = comic_font, bg = bg_colour,)
    wpmLabel.place(relx = 0.3, rely = 0.4 , anchor = CENTER)

    global restartButton

    restartButton = Button(window, text = "Retry" , command = restart, font = comic_font , fg = bg_colour ,activeforeground=grey, bg = white)
    restartButton.place(relx = 0.6, rely = 0.4, anchor = CENTER)

def restart():
    wpmLabel.destroy()
    restartButton.destroy()

    generate_new_test()

def keyPress(event = None):
    try:
        if event.char.lower() == rightLabel.cget("text")[0].lower():
            rightLabel.config(text = rightLabel.cget("text")[1:])
            leftLabel.config(text = leftLabel.cget("text") + event.char.lower())
            currentLetterLabel.config(text = rightLabel.cget("text")[0])
    except tkinter.TclError:
        pass

# Generate the first prompt
start_screen()

window.mainloop()