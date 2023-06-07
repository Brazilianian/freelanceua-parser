from model.freelance_site_model import FreelanceSiteModel


def find_by_name(name: str):
    sites = FreelanceSiteModel.select().where(FreelanceSiteModel.name == name).limit(1)
    return sites[0] if len(sites) > 0 else sites


def find_by_id(site_id: int):
    return FreelanceSiteModel.get_by_id(site_id)
    pass
