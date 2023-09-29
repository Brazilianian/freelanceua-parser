from database import db_config
from logger_configuration import logger
from model.category.category_model import CategoryModel
from model.category.proposals_subcategories_model import ProposalsSubcategoriesModel
from model.category.subcategory_model import SubcategoryModel
from model.freelance_site_model import FreelanceSiteModel
from model.proposal_model import ProposalModel


def init_db():
    if db_config.db.is_closed():
        db_config.db.connect()

    logger.info("Db connected")

    if not ProposalModel.table_exists():
        ProposalModel.create_table()
        logger.info("Proposals table created")

    if not FreelanceSiteModel.table_exists():
        FreelanceSiteModel.create_table()
        logger.info("FreelanceSites table created")

    if not CategoryModel.table_exists():
        CategoryModel.create_table()
        logger.info("Category table created")

    if not SubcategoryModel.table_exists():
        SubcategoryModel.create_table()
        logger.info("Subcategory table created")

    if not ProposalsSubcategoriesModel.table_exists():
        ProposalsSubcategoriesModel.create_table()
        logger.info("ProposalsSubcategories table created")
