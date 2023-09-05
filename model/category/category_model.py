from peewee import AutoField, CharField, ForeignKeyField

from model.base_model import BaseModel
from model.freelance_site_model import FreelanceSiteModel


class CategoryModel(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    freelance_site = ForeignKeyField(FreelanceSiteModel, backref="freelance_site")

    def __str__(self):
        return f"id - {self.id} " \
               f"name - {self.name} " \
               f"freelance_site - {self.freelance_site}"

    class Meta:
        table_name = "categories"
