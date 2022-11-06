#2.3: Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.

currentTime = int(input("What is the current time, in hours?"))

waitingHours = int(input("How many hours are left until your alarm goes off?"))

estimatedTime = (currentTime + waitingHours)%24; 
#mod 24 gives you the remaining hours left; 24 hours in a day
#e.g. the user inputs 13 for the current time and 50 for waiting hours
#13+50=63
#63/24= 2 and mod 15
#2= 2 full days(48 hours) and 15= remaining hours

print("Your alarm will go off at", estimatedTime, ".")