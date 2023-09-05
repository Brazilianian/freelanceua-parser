from model.category.proposals_subcategories_model import ProposalsSubcategoriesModel
from model.proposal_model import ProposalModel


def save(proposal_model: ProposalModel, subcategories_id: [int]):
    for subcategory_id in subcategories_id:
        proposal_subcategory_model = ProposalsSubcategoriesModel.create(
            proposal_id=proposal_model.id,
            subcategory_id=subcategory_id)

        proposal_subcategory_model.save()
