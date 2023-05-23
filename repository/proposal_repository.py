from _datetime import datetime

from domain.proposal import Proposal
from model.proposal_model import ProposalModel


def save_to_db(proposal: Proposal):
    proposal_model: ProposalModel = ProposalModel.create(
        title=proposal.title,
        price=proposal.price,
        description=proposal.description,
        link=proposal.link,
        additional_info_tags=proposal.additional_info_tags,
        date=datetime.now()
    )

    return proposal_model.save()
    pass


def is_exists_by_link(link: str):
    query = ProposalModel.select().where(ProposalModel.link == link)
    return query.execute()
    pass
