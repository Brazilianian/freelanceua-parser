from datetime import datetime

from domain.proposal import Proposal
from model.proposal_model import ProposalModel
from service import freelance_site_service


def save_to_db(proposal: Proposal):
    freelance_site = freelance_site_service.get_site_by_id(proposal.freelance_site.id)

    proposal_model: ProposalModel = ProposalModel.create(
        title=proposal.title,
        price=proposal.price,
        description=proposal.description,
        link=proposal.link,
        additional_info_tags=proposal.additional_info_tags,
        posted_date=datetime.now(),
        freelance_site=freelance_site
    )

    return proposal_model.save()


def is_exists_by_link(link: str):
    query = ProposalModel.select().where(ProposalModel.link == link)
    return query.execute()
