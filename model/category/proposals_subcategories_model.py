from peewee import ForeignKeyField

from model.base_model import BaseModel
from model.category.subcategory_model import SubcategoryModel
from model.proposal_model import ProposalModel


class ProposalsSubcategoriesModel(BaseModel):
    proposal_id = ForeignKeyField(ProposalModel, backref="proposal")
    subcategory_id = ForeignKeyField(SubcategoryModel, backref="subcategory")

    class Meta:
        table_name = "proposals_subcategories"
