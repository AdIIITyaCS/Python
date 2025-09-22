import pyautogui as spam
import time
limit=int(input("Enter Your Limit::  "))   
Msg=input("Enter Your Message:: ")
i=0
time.sleep(2)
while i<int(limit):  
    spam.typewrite(Msg)  
    spam.press("Enter") 
    i+=1    
                 