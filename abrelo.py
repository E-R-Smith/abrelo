from json.encoder import INFINITY
from operator import truediv
from textwrap import fill
from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from tokenize import Double
from turtle import back, left
from urllib.parse import urldefrag
import webbrowser

# -- globals -- #
chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

now = 0
timeUntilOpen = INFINITY;

# -- functions -- #
def registerBrowsers():
    #register Firefox
    webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser(firefox_path))
    #register Chrome
    webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser(chrome_path))
    #register Edge
    webbrowser.register('edge',
    None,
    webbrowser.BackgroundBrowser(edge_path))
def openBrowsers():
    print('opening...')
    print(url.get())
    webbrowser.get('firefox').open_new(url.get())
    webbrowser.get('chrome').open(url.get())
    webbrowser.get('edge').open(url.get())
    print('done')  
def waitUntilTime(hour:IntVar, minute:IntVar):
    global now
    now = datetime.now()
    print(hour.get())
    print(minute.get())
    while (now.hour != hour.get()):
        print("waiting for hour")
        now = datetime.now()       
    while (now.minute != minute.get()):
        print("waiting for minute")
        now = datetime.now()
def validateSpinbox(input, widgetname):
    # check to see if numeric
    if input.isdigit():
        # fetch spinbox min/max
        minval = int(root.nametowidget(widgetname).config('from')[4])
        maxval = int(root.nametowidget(widgetname).config('to')[4])
        # check if input is within min/max range
        if int(input) not in range(minval, maxval):
            print("out of range")
            return False
        print(input)
        return True
    
    # if input is empty string
    elif input is "":
        print(input)
        return True
    
    # input is not numeric
    else:
        print("not numeric")
        return False
def beginScheduledLaunch():
    if url.get() == "":
        return
    waitUntilTime(hour, minute)
    registerBrowsers()
    openBrowsers()
    
# -- main -- #
root = Tk()
root.title("Schedule webpage launch")
root.minsize(400, 200)
root.maxsize(600, 300)

mainframe = ttk.Frame(root)
mainframe.pack(fill=BOTH, expand=TRUE) #place it in the window



urlFrame = Frame(mainframe, bg="cyan", padx=20, pady=10)
urlFrame.pack(expand=FALSE, fill=BOTH)

ttk.Label(urlFrame, text="URL to open: ").pack(side=LEFT, fill="x")

url = StringVar()
urlInput = ttk.Entry(urlFrame, textvariable=url)
urlInput.pack(expand=TRUE, fill=X)



timeframe = Frame(mainframe, bg="pink")
timeframe.pack(expand=FALSE, fill=NONE)
ttk.Label(timeframe, text="Open at (24h time):").pack()
hour = IntVar()
minute = IntVar()
rangeValidation = root.register(validateSpinbox)
ttk.Label(timeframe, text="Hour: ").pack(side=LEFT)
hourInput = ttk.Spinbox(timeframe,
                        width=4,
                        from_=0,
                        to=23,
                        textvariable=hour,
                        validate="key",
                        validatecommand=(rangeValidation, "%P", "%W")).pack(side=LEFT)
ttk.Label(timeframe, text="Minute: ").pack(side=LEFT)
minuteInput = ttk.Spinbox(timeframe,
                          width=4,
                          from_=0,
                          to=59,
                          textvariable=minute,
                          validate="key",
                          validatecommand=(rangeValidation, "%P", "%W")).pack(side=LEFT)

feedbackFrame = Frame(mainframe, bg="yellow", padx=20, pady=30)
feedbackFrame.pack(expand=FALSE, fill=BOTH)
submitButton = ttk.Button(feedbackFrame, text="Schedule", command=beginScheduledLaunch)
submitButton.pack()

root.mainloop()