"""
File: question_model.py
"""

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_q = Question("Hello ", "goodbye")
print(new_q.answer)