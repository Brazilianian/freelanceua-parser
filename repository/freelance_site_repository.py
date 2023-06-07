from model.freelance_site_model import FreelanceSiteModel


def find_by_name(name: str):
    query = FreelanceSiteModel.select().where(FreelanceSiteModel.name == name).limit(1)
    results = query.execute()
    return results[0] if len(results) > 1 else results


def find_by_id(site_id: int):
    return FreelanceSiteModel.get_by_id(site_id)
    pass
