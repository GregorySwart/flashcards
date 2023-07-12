from bson import ObjectId


class StudySet:
    items: dict = {}
    owner: ObjectId = None

    def __init__(self, items):
        self.items = items
