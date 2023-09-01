from datetime import datetime

from domain.proposal import Proposal
from model.proposal_model import ProposalModel
from repository import proposal_subcategory_repository
from service import freelance_site_service


def save(proposal: Proposal):
    freelance_site = freelance_site_service.get_site_by_id(proposal.freelance_site.id)

    proposal_model: ProposalModel = ProposalModel.create(
        title=proposal.title,
        price=proposal.price,
        description=proposal.description,
        link=proposal.link,
        additional_info_tags=proposal.additional_info_tags,
        posted_date=datetime.now(),
        freelance_site=freelance_site,
    )

    proposal_model.save()

    subcategories_id = list(subcategory.id for subcategory in proposal.subcategories)
    proposal_subcategory_repository.save(proposal_model, subcategories_id)


def is_exists_by_link(link: str):
    query = ProposalModel.select().where(ProposalModel.link == link)
    return query.execute()
