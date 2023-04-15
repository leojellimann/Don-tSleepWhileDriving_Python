# DontSleepWhileDriving_Python
This Python program detects if your eyes are closed using OpenCV

After falling asleep while driving in 2020, I decided to build a program to detect and prevent the driver if he falls asleep.

At this time, I didn't know how to analyze live cam and detect objects or shapes with a program.
I then discovered OpenCV could help me to do that.

I took my raspberry pi 4 and a webcam and I started coding.

I first built the program to detect my face and my two eyes separately.

![image](https://user-images.githubusercontent.com/93252510/232231344-9fb8f8b5-bce1-4ecd-8c75-d66e6012108b.png)

You can see on the top left of the window 4 different parameters:
- Frame Per Second of the camera
- Number of eyes detected by the camera
- Number of blink of my eyes (for the next part)
- Time of blink of my eyes (for the next part)

Once I was able to detect my face and my eyes, I tried to detect when one eyes is closed.

![image](https://user-images.githubusercontent.com/93252510/232232328-625241e5-b11e-40c5-8324-01c37fb8c08f.png)

Then, if I was able to detect a face but no eyes, that would mean eyes are closed.
No sooner said than done, here is the result :

![image](https://user-images.githubusercontent.com/93252510/232232463-111a7b0d-beba-43d0-ab3b-30d5a4bf513e.png)

Here we can see driver's eyes are closed so an alarm sounds and a message is written on the window.

This program is a test I built in 2020 and didn't work anymore on it after.
It would be great to come back on this program later and make it a mobile app.

This was a great time discovering nice tools like OpenCV while developing my Python skills for a personal project.

I hope you enjoy the project and would love to speak to you about it :)

