from database import db_config
from logger_configuration import logger
from model.proposal_model import ProposalModel


def init_db():
    db_config.db.connect()

    logger.info("Db connected")

    if not ProposalModel.table_exists():
        ProposalModel.create_table()
        logger.info("Table created")
        pass
    pass
