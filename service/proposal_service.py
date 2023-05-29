from bs4 import *

from repository.proposal_repository import *


def save_proposal(proposal: Proposal):
    save_to_db(proposal)
    pass


def is_proposal_exists(proposal: Proposal):
    result = is_exists_by_link(proposal.link)
    return len(result) > 0
    pass


ignore_tags = ['пропозиц',
               'сьогодні',
               'вчора']


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
        proposals.append(proposal)
    pass

    return proposals


pass
