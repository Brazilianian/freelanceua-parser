from domain.freelance_site import FreelanceSite


class Proposal:
    id = ""
    title = ""
    price = ""
    description = ""
    link = ""
    additional_info_tags = ""
    posted_date = ""
    freelance_site: FreelanceSite = ""

    def __str__(self):
        return f"id - {self.id}\n" \
               f"title - {self.title}\n" \
               f"price - {self.price}\n" \
               f"description - {self.description}\n" \
               f"link - {self.link}\n" \
               f"additional_info_tags: {self.additional_info_tags}\n" \
               f"date: {self.posted_date}"
