from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot('Minor Selection Bot')

convo = [
    'Hey',
    'Hello, I am here to answer all your queries regarding minor elective.',
    'How many minor electives do we have?',
    'We have Data Science, Cyber Security, Machine Learning, Mean Stack '
    'Development and Software Engineering.',
    'How the minors will be allocated to us?',
    'We will conduct a polling in which you have to select any three minors '
    'with respect to your preference and it will '
    'be allocated to us.',
    'How many seats do we have for ML?',
    '720',
    'How many seats do we have for Data Science?',
    '1120',
    'How many seats do we have for Cyber Security?',
    '760',
    'How many seats do we have for Mean Stack Development?',
    '920',
    'How many seats do we have for Software Engineering?',
    '540',
    'What are the career opportunities for the persuaded minor?',
    'All the information regarding minor careers are uploaded on your UMS, you '
    'can download all the files regarding '
    'every minor.',
    'If we face any doubt regarding minor whom to approach?',
    'If you face any doubt you can ask to your teacher or can RMS regarding '
    'any further query.',
    'What prior knowledge do we need if our preference is Data Science?',
    'For Data Science:Know the basics of programming, Know the basics of SQL, '
    'Be familiar with the basics of maths,'
    ' probability and statistical concepts',
    'What prior knowledge do we need if our preference is ML?',
    'For ML:Statics, Linear Algebra, Calculus, Probability, Programming '
    'Languages.',
    'What prior knowledge do we need if our preference is Mean Stack Development?',
    'For MSD: Javascript /typescript and basics of Nosql database, some '
    'Programming also.',
    'What prior knowledge do we need if our preference is Cyber Security?',
    'For Cyber Security: Java, PHP, Perl, Ruby, Python) Understanding '
    'architecture, administration and operating systems.',
    'When polling is to be conducted?',
    'Any further information regarding polling will be informed through your UMS.',
]

trainer = ListTrainer(bot)

trainer.train(convo)

main = Tk()

main.geometry("800x650")

main.title("Minor Selection Helper")
img = PhotoImage(file="bot2.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=150, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=X)

frame.pack()

# creating text field

textF = Entry(main, font={"Google Sans", 20})
textF.pack(fill=X, pady=10)

btn = Button(main, text="Enter", font={"Google Sans", 20}, command=ask_from_bot)
btn.pack()


# creating a function

def enter_function(event):
    btn.invoke()

# going to bind main window with enter key...


main.bind('<Return>', enter_function)

main.mainloop()

