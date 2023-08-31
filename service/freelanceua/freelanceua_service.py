from bs4 import BeautifulSoup, Tag

from domain.freelance_sites_enum import FreelanceSitesEnum
from domain.proposal import Proposal
from service import freelance_site_service

ignore_tags = ['пропозиц',
               'сьогодні',
               'вчора']


def get_proposals_from_soup(soup: BeautifulSoup) -> [Proposal]:
    proposals: [Proposal] = []
    freelance_site = freelance_site_service.get_site_by_name(FreelanceSitesEnum.FREELANCE_UA)

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
        proposal.freelance_site = freelance_site
        proposals.append(proposal)

    return proposals
