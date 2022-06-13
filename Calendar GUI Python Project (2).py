#!/usr/bin/env python
# coding: utf-8

# In[7]:


from tkinter import * #import all methods and classes from the tkinter.
import calendar #import calendar module.
def showCalendar(): #function for calendar.
    W=Tk() #create a GUI window.
    W.title("CALENDAR") #to set the title of GUI.
    W.geometry("650x600") #to set the size of the window.
    W.config(bg="grey") #to set the background colour of the window.
    Y=int(ent.get()) #pass the enter method reference to year as an integer.
    
    c=calendar.calendar(Y) #calendar method of calendar module return the calendar of the given year.
    l3=Label(W,text=c,font="consolas 10 bold") #create a label for showing the content of the calendar.
    l3.grid(row=5,column=1,padx=50) #grid method is used for placing 
                                #the widgets at respective positionsin table like structure.
    
    W.mainloop() #start the GUI

root=Tk() #create a GUI window.
root.title("CALENDAR") #to set the title of tkinter GUI window.
root.geometry("350x250") #to set the size of GUI window.
root.config(bg="grey") #to set the background colour of GUI window.
l1=Label(root,text="CALENDAR",bg="black",fg="white",font=("Algerian",20,'bold')) 
      #creating label with specific font and size.
l2=Label(root,text="Enter year :- ",bg="black",fg="white",font=('algerian',10))#creating a label.
ent=Entry(root,borderwidth=10,width=18,bg="grey") #create entry button to take input.
button=Button(root,text="Show Calendar",font=('helvetica',10),command=showCalendar) #create a button and attached to show calendar.
exit=Button(root,text="Exit",font=('helvetica',8),command=root.destroy) #create a button and attached to exit.
l1.pack() #to pack the widgetsof of l1.
l2.place(x=6,y=45) #to set the position of l2.
ent.pack() #to pack the widgets of entry button.
button.pack() #to pack the widgets of button.
exit.pack() #to pack the widgets of exit.
root.mainloop() #start the GUI.


# In[ ]:




