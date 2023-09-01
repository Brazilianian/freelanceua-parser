from model.category.category_model import CategoryModel
from model.category.subcategory_model import SubcategoryModel


def find_by_name(subcategory_name: str):
    query = (SubcategoryModel
             .select()
             .join(CategoryModel)
             .where(SubcategoryModel.name == subcategory_name))

    return query.execute()[0]
