from peewee import AutoField, TextField, CharField

from model.base_model import BaseModel


class FreelanceSiteModel(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(unique=True)
    link = TextField()

    def __str__(self):
        return f"id - {self.id} " \
               f"name - {self.name} " \
               f"link - {self.link} "

    class Meta:
        table_name = "freelance_sites"
