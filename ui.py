THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self,true_image,false_image,quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.canvas = Canvas()
        self.canvas.config(height=250,width=300)
        self.question_text= self.canvas.create_text(
            150,
            125,
            width= 280,
            text="This is a Sample Question",
            fill=THEME_COLOR,
            font=('Arial',18,'italic')
        )
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="White")
        self.score_label.grid(row=0,column=1)

        true_image = PhotoImage(file=true_image)
        self.true_btn = Button(image=true_image,highlightthickness=0,command=self.true_answer)
        self.true_btn.grid(column=0,row=2)

        false_image = PhotoImage(file=false_image)
        self.false_btn = Button(image=false_image,highlightthickness=0,command=self.false_answer)
        self.false_btn.grid(column=1,row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=question)

    def true_answer(self):
        score = self.quiz.check_answer("true")
        self.score_label.config(text=f"Score: {score}")
        self.get_next_question()

    def false_answer(self):
        self.quiz.check_answer("false")
        self.get_next_question()