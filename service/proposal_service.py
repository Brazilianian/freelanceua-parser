from domain.proposal import Proposal
from logger_configuration import logger
from repository import proposal_repository, proposal_subcategory_repository
from repository.proposal_repository import is_exists_by_link


def save_proposal(proposal: Proposal):
    logger.info(f"Saved proposal with link - {proposal.link}")
    proposal_repository.save(proposal)


def is_proposal_exists(proposal: Proposal):
    result = is_exists_by_link(proposal.link)
    return len(result) > 0

