# Imports go at the top
from microbit import *

squareroot = Image(
   '00999:'
   '00900:'
   '00900:'
   '90900:'
   '09000')

opts = [ 
    ".",
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,  
    
]

# number input stage
entering = True
i = 0
button_a.was_pressed()
button_b.was_pressed()
digits = ""
while entering:
    
    if opts[i] == "s":
        display.show(squareroot)
    else:       
        display.show(opts[i])

    if button_b.was_pressed():
        if i < len(opts)-1:
            i+=1
        else:
            i=0
    elif button_a.was_pressed():
        if opts[i] != "s":
            digits += str(opts[i])
            if opts[i] == ".":
                opts.pop(i)
            if len(digits) == 1:
                opts = ["s"] + opts
            i = 0
        else:
            entering = False

# turn digits list into number n
n = float(digits)

# process and show square root
rt = n**0.5
if rt == rt // 1:
    rt = int(rt)
print(rt)
display.scroll(rt)
