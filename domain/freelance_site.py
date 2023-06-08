class FreelanceSite:
    id: int
    name: str
    link: str

    def __init__(self, site_id: int, name: str, link: str):
        self.id = site_id
        self.name = name
        self.link = link

    def __str__(self):
        return f"id - {self.id} " \
               f"name - {self.name} " \
               f"link - {self.link} "

