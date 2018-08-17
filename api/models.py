class Questions:
    """Defines questions class"""

    def list_of_question(self):
        """
        Initializes the questions object
        :args None
        :return Questions
        """
        self.questions = [
            {
                'id': 1,
                'title': 'Datatypes-boolean',
                'question_body': 'how to write a method using hibernate\
                                  which returns boolean',
                'question_tags': 'javascript'      
            },
            {
                'id': 2,
                'title': 'Programming in python',
                'question_body': 'How is programming taking us',
                'question_tags': 'imports'

            }]
            
        return self.questions

    def __str__(self):
        """String representation of the list returns
        """
        return str(self.list_of_question)


class Answers:
    """This class represents the answer list """

    def list_of_answer(self):
        self.answers = [
            {
                'answer_id': 2,
                'question_id': 1,
                'answer_body': 'Do more readings on oop that is\
                                when you will pick up something on methods '
            },
            {
                'answer_id': 3,
                'question_id': 3,
                'answer_body': 'So far programming is moving well,\
                                but we are catching up with python faster'
            }
            
        ]

        return self.answers


# Object class is being instatianted
questions = Questions()
answers = Answers()

