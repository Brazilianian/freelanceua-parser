from model.category.category_model import CategoryModel
from model.category.subcategory_model import SubcategoryModel
from model.freelance_site_model import FreelanceSiteModel


def find_by_name_and_freelance_site_name(subcategory_name: str,
                                         freelance_site_name: str):
    query = (SubcategoryModel
             .select()
             .join(CategoryModel)
             .join(FreelanceSiteModel)
             .where(SubcategoryModel.name == subcategory_name)
             .where(FreelanceSiteModel.name == freelance_site_name))

    return query.execute()[0]


def find_by_freelance_site_name(freelance_site_name):
    query = (SubcategoryModel
             .select()
             .join(CategoryModel)
             .join(FreelanceSiteModel)
             .where(FreelanceSiteModel.name == freelance_site_name))
    return query.execute()
