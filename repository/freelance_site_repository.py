from model.freelance_site_model import FreelanceSiteModel


def find_by_name(name: str):
    return FreelanceSiteModel.get(name=name)
    pass


def find_by_id(site_id: int):
    return FreelanceSiteModel.get_by_id(site_id)
    pass
