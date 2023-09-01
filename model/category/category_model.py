from peewee import AutoField, CharField

from model.base_model import BaseModel


class CategoryModel(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()

    def __str__(self):
        return f"id - {self.id} " \
               f"name - {self.name} "

    class Meta:
        table_name = "categories"
