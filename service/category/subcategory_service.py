from domain.category.category import Category
from domain.category.subcategory import Subcategory
from model.category.subcategory_model import SubcategoryModel
from repository import subcategory_repository


def get_subcategory_by_name_and_freelance_site_name(subcategory_name: str,
                                                    freelance_site_name: str):
    subcategory_model: SubcategoryModel = (subcategory_repository
                                           .find_by_name_and_freelance_site_name(subcategory_name,
                                                                                 freelance_site_name))

    return Subcategory(subcategory_model.id, subcategory_model.name,
                       Category(subcategory_model.category.id,
                                subcategory_model.category.name))


def get_subcategory_by_freelance_site_name(freelance_site_name: str):
    subcategories_model: [SubcategoryModel] = subcategory_repository.find_by_freelance_site_name(freelance_site_name)
    subcategories: [Subcategory] = []

    for subcategory_model in subcategories_model:
        subcategories.append(Subcategory(subcategory_model.id, subcategory_model.name,
                                         Category(subcategory_model.category.id,
                                                  subcategory_model.category.name)))
    return subcategories
