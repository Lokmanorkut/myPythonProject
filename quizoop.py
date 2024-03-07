class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkanswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
        
    def getquestion(self):
        return self.questions[self.questionIndex]
    
    def displayquestion(self):
        question = self.getquestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")
        
        for q in question.choices:
            print("-"+q)
            
        answer=input("Cevap: ")
        
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self,answer):
        question=self.getquestion()
        
        if question.checkanswer(answer):
            self.score+=1
        self.questionIndex+=1
        
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showscore()
        else:
            self.displayproggress()
            self.displayquestion()
            
    def displayproggress(self):
        totalquesion=len(self.questions)
        questionNumber=self.questionIndex+1
        
        if questionNumber>totalquesion:
            print("Quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalquesion}")
            

    def showscore(self):
        print(f"Score:  {self.score}")
        
        
q1 = Question("En iyi programlama dili hangisidir?", ["C#", "Python", "PHP", "Java"], "PHP")
q2 = Question("En popüler programlama dili hangisidir?", ["C#", "Python", "PHP", "Java"], "Python")
q3 = Question("En sağlıklı programlama dili hangisidir?", ["C#", "Python", "PHP", "Java"], "Java")
questions = [q1, q2, q3]
quiz = Quiz(questions)

quiz.loadQuestion()
