class Category:
    id: int
    name: str

    def __init__(self, category_id: int, name: str):
        self.id = category_id
        self.name = name

    def __str__(self):
        return f"id - {self.id} " \
               f"name - {self.name} "
