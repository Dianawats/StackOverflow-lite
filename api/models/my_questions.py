from api import generate_id

questions_list = []

class Question:
     """Defines questions class
     """

     def __init__(self, user_id, title, body, tags):
         self.question_id = generate_id(questions_list)
         self.title = title
         self.body = body
         self.tags = tags
        
