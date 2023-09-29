from bs4 import BeautifulSoup, Tag

from domain.freelance_sites_enum import FreelanceSitesEnum
from domain.proposal import Proposal
from service import freelance_site_service
from service.category import subcategory_service
from service.freelanceua import freelanceua_parser

ignore_tags = ['пропозиц',
               'сьогодні',
               'вчора']
freelance_site = freelance_site_service.get_site_by_name(FreelanceSitesEnum.FREELANCE_UA)


def get_subcategories_of_proposal(proposal_link: str):
    soup: BeautifulSoup = freelanceua_parser.get_soap_of_subcategories(proposal_link)
    subcategory = get_subcategory_from_soup(soup)
    subcategories_db = subcategory_service.get_subcategory_by_freelance_site_name(freelance_site.name)
    return [sub for sub in subcategories_db if sub.name == subcategory]


def get_subcategory_from_soup(soup: BeautifulSoup):
    div_container: Tag = soup.find_all('div', class_='container')[2]
    ol: Tag = div_container.find_all('ol', class_='breadcrumb')[0]
    li: Tag = ol.find_all('li')[2]
    return li.find('a').text


def get_proposals_from_soup(soup: BeautifulSoup) -> [Proposal]:
    proposals: [Proposal] = []

    li_list = soup.find_all('li', class_='j-order')
    for li in li_list:
        proposal: Proposal = Proposal()

        header: Tag = li.find('header', class_='l-project-title')
        a: Tag = header.find('a')
        proposal.title = a.text.strip()
        proposal.link = a['href'].strip()

        proposal.price = li.find('span', class_='l-price').text.strip()

        article = li.find('article')

        proposal.description = article.find('p').text.strip()

        ul = li.find('ul')
        additional_info_tags = ""
        for li_element in ul:
            additional_info_tag: str = li_element.text.strip()
            if additional_info_tag != '':
                is_ignore = False
                for ignore_tag in ignore_tags:
                    if additional_info_tag.__contains__(ignore_tag):
                        is_ignore = True
                        break

                if not is_ignore:
                    additional_info_tags += (additional_info_tag + ',')

        proposal.additional_info_tags = additional_info_tags[:-1]

        subcategories_db = subcategory_service.get_subcategory_by_freelance_site_name(freelance_site.name)
        proposal.subcategories = [subcategory for subcategory in subcategories_db if
                                  subcategory.name in additional_info_tags.split(',')]

        proposal.freelance_site = freelance_site

        for sub in get_subcategories_of_proposal(proposal.link):
            proposal.subcategories.append(sub)

        proposals.append(proposal)

    return proposals
