import json


class Masuda:
    def __init__(self, masuda_id, title, content, bookmark_count, category):
        self.masuda_id = masuda_id
        self.title = title
        self.content = content
        self.bookmark_count = bookmark_count
        self.category = category

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)
