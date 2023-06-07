from peewee import *

from model.base_model import BaseModel
from model.freelance_site_model import FreelanceSiteModel


class ProposalModel(BaseModel):
    id = AutoField()
    title = TextField()
    price = TextField()
    posted_date = DateTimeField()
    description = TextField()
    link = TextField()
    additional_info_tags = TextField()
    freelance_site = ForeignKeyField(FreelanceSiteModel, backref="sites")

    def __str__(self):
        return f"id - {self.id}\n" \
               f"title - {self.title}\n" \
               f"price - {self.price}\n" \
               f"description - {self.description}\n" \
               f"link - {self.link}\n" \
               f"additional_info_tags: {self.additional_info_tags}\n " \
               f"freelance_site: {self.freelance_site.__str__()}"

    class Meta:
        table_name = 'proposals'


pass
