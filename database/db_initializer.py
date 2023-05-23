from database import db_config
from model.proposal_model import ProposalModel


def init_db():
    db_config.db.connect()

    if not ProposalModel.table_exists():
        ProposalModel.create_table()
        pass
    pass
