
class Question(object):
    """
    This class defines Question Model
    """

    def __init__(self, title, body, tag):
        self.id = 0
        self.title = title
        self.body = body
        self.tag = tag
        self.answers = []

    def jsonify(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "tag": self.tag,
            "answers": self.answers
        }


class Answer(object):
    """
    Answer Model
    """
    def __init__(self, ans_id, body):
        self.id = ans_id
        self.body = body

    def make_json(self):
        return {
            "id": self.id,
            "body": self.body,
        }
