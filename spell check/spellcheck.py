from tkinter import*
from textblob import TextBlob

#create the API windows or frame
app=Tk()
app.configure(background="grey")
app.geometry('750x350')
app.resizable(0,0)
app.title('spell checker and corrector app')

#create the text and  words  entry link widgets
heading_text=Label(app,text="Welcome to spell checker and spell corrector app",font='Arial 15 bold',fg="blue",bg="grey")
lbl_input=Label(app,text="input word",font='Arial 14 bold',fg='white',bg='navyblue')
lbl_corrected=Label(app,text="correct word",font='Arial 14 bold',fg='white',bg='navyblue')

heading_text.grid(row=0,column=1,pady=20)
lbl_input.grid(row=1,column=0,padx=10)
lbl_corrected.grid(row=3,column=0,padx=10)

#creare text entry widgets here
input_word_box=Entry(app,width=40,font='Arial 14 bold')
corrected_word_box=Entry(app,width=40,font='Arial 14 bold')

input_word_box.grid(row=1,column=1,pady=10)
corrected_word_box.grid(row=3,column=1,pady=10)

#creating the function
def spellCorrection():
 word_input=input_word_box.get()
 text=TextBlob(word_input)
 corrected_word=str(text.correct())
    #insert the value in the text entry box
 corrected_word_box.insert(10,corrected_word)
    #a function to clear the texts found inside box the entry boxes
def clearAllWords():
     input_word_box.delete(0,END)
     corrected_word_box.delete(0,END)
 
#Create a correction button
btn1=Button(app,text="Correction",font='Arial 14 bold',fg='black',bg='lightblue',border=5,command=spellCorrection)
btn1.grid(row=2,column=1)

#Create button that enbles to clear the word entered in the entry box
btn1=Button(app,text="Clear All",font='Arial 14 bold',fg='black',bg='lightblue',border=5,command=clearAllWords)
btn1.grid(row=4,column=1)
app.mainloop()
