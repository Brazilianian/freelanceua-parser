from domain.freelance_sites_enum import FreelanceSitesEnum


class FreelanceSite:
    id: int
    name: FreelanceSitesEnum
    link: str

    def __init__(self, site_id: int, name: FreelanceSitesEnum, link: str):
        self.id = site_id
        self.name = name
        self.link = link

    def __str__(self):
        return f"id - {self.id} " \
               f"name - {self.name} " \
               f"link - {self.link} "

