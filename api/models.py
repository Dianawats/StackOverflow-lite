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
                'question_tags': 'javascript',
                'answer': [
                    {
                        'answer_id': 1,
                        'answer_body': 'it is along one i will\
                                        send you the code.'
                    },

                    {
                        'answer_id': 2,
                        'answer_body': 'this is interpreted lang'
                    }]
            }, 
            {
                'id': 2,
                'title': 'Programming in python',
                'question_body': 'How is programming taking us',
                'question_tags': 'import',
                'answer': [
                    {'answer_id': '',
                     'answer_body': ''
                     }
                ]
            }]
            
        return self.questions
        
    def __str__(self):
        """String representation of the list returns
        """
        return str(self.list_of_question)

# Object class is being instatianted
questions = Questions()