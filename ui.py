from tkinter import Tk
from tkinter import *
import quiz_brain
from quiz_brain import QuizBrain
import question_model

THEME_COLOR = "#375362"
CANVAS_COLOR = "#FFFFFF"
GREEN_COLOR = "#00ff00"
RED_COLOR = "#ff0000"
FONT = ("Arial", 20, "italic")


class QuizUi:
    def __init__(self, quiz_brain_instance: QuizBrain):
        self.window = Tk()
        self.window.title("Quizz Buzz")
        self.quiz_brain = quiz_brain_instance
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg=CANVAS_COLOR)
        self.question_text = self.canvas.create_text(150, 125, width=250, text="", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        right_image = PhotoImage(file="./images/true.png")
        wrong_image = PhotoImage(file="./images/false.png")
        self.right_button = Button(self.window, image=right_image, highlightthickness=0, command=self.right_answer)
        self.wrong_button = Button(self.window, image=wrong_image, highlightthickness=0, command=self.wrong_answer)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)
        # self.score = QuizBrain.get_score()
        self.score_label = Label(self.window, text=f"Score : {0}", font=FONT, bg=THEME_COLOR, highlightthickness=0,
                                 fg="white")
        self.score_label.grid(row=0, column=1)
        self.get_question()

        self.window.mainloop()

    def get_question(self):
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.score_label.config(text=f"Score : {self.quiz_brain.get_score()}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text= "You have Reached the end of the Quiz")
            self.canvas.config(bg=CANVAS_COLOR)
            self.right_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)

    def right_answer(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.window.after(1000, self.reset_canvas_and_next_question)

    def reset_canvas_and_next_question(self):
        self.canvas.config(bg=CANVAS_COLOR)
        self.get_question()