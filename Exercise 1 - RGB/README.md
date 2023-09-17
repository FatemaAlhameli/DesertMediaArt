## Exercise 1 - RGB Hello World

As I sat to start this assignment, I first considered the ways color and light are used in a meaningful way. Color and light are powerful elements that if utilized smartly can have a great impact. The idea of Morse code came to me while I was debating what to do. Morse code is a form of communication that has been known for decades. It was primarily used for signaling short messages through dot and dash signals using audible beeps or lights. With the use of Morse code as a mode of communication, universal abbreviations to simplify words were created. For instance, in case of an emergency or cry for help “SOS” is commonly used to alert people. 

Therefore, I decided to create a script to depict the SOS message in Morse code through the onboard RGB using CircuitPython. I wanted to illustrate the message uniquely but clearly. I designed the script to start off with a bright blue where then the blue color slightly fades and disappears allowing the red-colored SOS message to begin. Ultimately, signaling that there is something wrong. I specifically chose red as it is constantly associated with emergency situations and alertness. I looked up a [Morse code translator](https://roboblocky.com/u/733.php#:~:text=a%20dot%20lasts%20for%20one,different%20letters%20is%20three%20seconds) that would assist me in spelling out “SOS” with the correct time and way. I learned that the dot's duration should last for one second and the dash should last for three seconds. The “SOS” message consists of three dots, three dashes, and three more dots. 

The “SOS” message begins in three stages, short duration of red LED blinking, long duration of red LED blinking, and again short duration of red blinking LED. The mechanism I used to create this series of signals to spell out the message was mainly through the attributes ```time.sleep``` and ```led.brightness```. 

  ``` led[0] = (255, 0, 0) #red, beginning of the SOS message,three secs to spell out S in short pulses
    time.sleep(1) 
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message 
    time.sleep(0.5) 
    led.brightness = 0
```


Above is a snippet of what the majority of the code looked like. I set the duration of the light based on the letter/signal and turned off the LED to create the blink effect by setting the brightness to 0. I continued by repeating the same pattern and adjusting the brightness and time until I spelled out the whole “SOS” message with the correct duration of blinks between letters. 

This assignment was definitely a learning experience as it was my first time coding Python. However, this exercise allowed me to understand the nature of programming and using CircuitPython. I am happy with the outcome I have achieved and the idea behind it. Although color may seem like a simple element it can have a lot of value to it. Experimenting CircuitPython with Morse code was very fun and helped me explore different attributes. I was able to learn how I can manipulate them to achieve what I want. A way I could further develop this work would be to add interactivity and allow user engagement. For instance, users could have the ability to input their own messages, and the program could convert them into Morse code and display them through an LED. There are many possibilities for taking this to the next level, I hope to reflect them in the main class project and other exercises this semester. 
