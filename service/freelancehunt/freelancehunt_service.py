import re

from bs4 import BeautifulSoup, Tag

from domain.freelance_sites_enum import FreelanceSitesEnum
from domain.proposal_type_enum import ProposalType
from domain.proposal import Proposal
from service import freelance_site_service
from service.category import subcategory_service


def get_proposals_from_soup(soup: BeautifulSoup, proposal_type: ProposalType):
    proposals: [Proposal] = []

    freelance_site = freelance_site_service.get_site_by_name(FreelanceSitesEnum.FREELANCE_HUNT)

    div_projects = soup.find('div', id='projects-html')
    tr_projects = div_projects.find_all('tr')

    for tr_project in tr_projects:
        proposal: Proposal = Proposal()

        td_list = tr_project.find_all('td')

        td_desc: Tag = td_list[0]
        div_list = td_desc.find_all('div')

        a_title = None
        additional_info_tags = ""

        # Premium
        if tr_project.has_attr('class') and tr_project['class'][0] == 'featured':
            a_title = div_list[0].find('a')
            additional_info_tags += "Преміум проєкт,"

        # Common
        else:
            td_desc = td_list[0]
            a_title = td_desc.find('a')

            small = td_desc.find('small')
            a_tags = small.find_all('a')
            for a_tag in a_tags:
                additional_info_tag = a_tag.text
                additional_info_tags += additional_info_tag + ','

        proposal.additional_info_tags = additional_info_tags[:-1]

        p_desc = td_desc.find('p')
        proposal.description = p_desc.text.strip()
        regexp = re.compile('.*price.*')
        div_price = tr_project.find('div', {"class": regexp})
        proposal.price = div_price.text.strip() if div_price is not None else ""

        proposal.title = a_title.text.strip()
        proposal.link = a_title['href'].strip()

        proposal.freelance_site = freelance_site
        # proposal.subcategories = [
        #     subcategory_service.get_subcategory_by_name_and_freelance_site_name(proposal_type.value,
        #                                                                         freelance_site.name)]

        subcategories_db = subcategory_service.get_subcategory_by_freelance_site_name(freelance_site.name)
        proposal.subcategories = [subcategory for subcategory in subcategories_db if
                                  subcategory.name in additional_info_tags.split(',')]

        proposals.append(proposal)
    return proposals


def get_beautiful_soap():
    return None
