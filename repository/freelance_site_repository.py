from model.freelance_site_model import FreelanceSiteModel


def find_by_name(name: str):
    query = FreelanceSiteModel.select().where(FreelanceSiteModel.name == name)
    results = query.execute()
    for result in results:
        return result


def find_by_id(site_id: int):
    return FreelanceSiteModel.get_by_id(site_id)
    pass
