from domain.freelance_site import FreelanceSite
from model.freelance_site_model import FreelanceSiteModel
from repository import freelance_site_repository


def get_site_by_name(site_name: str):
    freelance_site_model: FreelanceSiteModel = freelance_site_repository.find_by_name(site_name)
    return FreelanceSite(freelance_site_model.id, freelance_site_model.name, freelance_site_model.link)


def get_site_by_id(site_id: int):
    return freelance_site_repository.find_by_id(site_id)
