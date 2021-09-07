from tkinter import *
root = Tk()

def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: kya be lwre kaisa h")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == "thik hun tu bta kaha hai"):
        text.insert(END, "\n" + "Bot: chand pe hai apun")
    elif (e.get() == "ja na lwre"):
        text.insert(END, "\n" + "Bot: apna kaam kr na apsbd")
    else:
        text.insert(END, "\n" + "Bot: Muh se supari nikal k bat kr btc.")
text = Text(root,bg='light blue')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root = Tk()
root.title('IT SOURCCODE SIMPLE CHATBOT')
root.mainloop()
