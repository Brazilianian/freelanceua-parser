from peewee import AutoField, CharField, ForeignKeyField

from model.base_model import BaseModel
from model.category.category_model import CategoryModel


class SubcategoryModel(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    category = ForeignKeyField(CategoryModel, backref="category")

    def __str__(self):
        return f"id - {self.id} " \
               f"name - {self.name} " \
               f"category - {self.category}"

    class Meta:
        table_name = "subcategories"
