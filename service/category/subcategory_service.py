from domain.category.category import Category
from domain.category.subcategory import Subcategory
from model.category.subcategory_model import SubcategoryModel
from repository import subcategory_repository


def get_subcategory_by_name(subcategory_name: str):
    subcategory_model: SubcategoryModel = subcategory_repository.find_by_name(subcategory_name)

    return Subcategory(subcategory_model.id, subcategory_model.name,
                       Category(subcategory_model.category.id,
                                subcategory_model.category.name))
