from model.freelance_site_model import FreelanceSiteModel


def find_by_name(name: str):
    query = FreelanceSiteModel.select().where(FreelanceSiteModel.name == name)
    return query.execute()[0]


def find_by_id(site_id: int):
    return FreelanceSiteModel.get_by_id(site_id)
