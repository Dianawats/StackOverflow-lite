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
                'question_body': 'how to write a method using hibernate\
                                  which returns boolean',
                'question_tags': 'javascript', 
                'answer': [
                    {
                        'answer_id': 1,
                        'answer_body': 'for that debug and check what your query \
                                        exactly returns if true then here also\
                                        will return true only',

                    }
                ]
            },
            {
                'id': 2,
                'question_body': 'How is programming taking us',
                'question_tags': 'import',
                'answer': [
                    {
                        'answer_id': '',
                        'answer_body': '',
                    }
                ]
            }
        ]

        return self.questions

    def __str__(self):
        """String representation of the list returns
        """
        return str(self.list_of_question)

# Object class is instatianted
questions = Questions()

