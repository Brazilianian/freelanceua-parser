from logger_configuration import logger
from repository.proposal_repository import *


def save_proposal(proposal: Proposal):
    logger.info(f"Saved proposal with link - {proposal.link}")
    save_to_db(proposal)
    pass


def is_proposal_exists(proposal: Proposal):
    result = is_exists_by_link(proposal.link)
    return len(result) > 0
    pass

