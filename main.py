import time

import schedule

from database.db_initializer import init_db
from service import parser
from service.proposal_service import *


def main():
    init_db()

    start_scheduling()


pass


def parse_orders_and_save():
    soup = parser.get_beautiful_soap()
    proposals: [Proposal] = get_proposals_from_soup(soup)

    for proposal in proposals:
        if not is_proposal_exists(proposal):
            print("Founded new proposal")
            save_proposal(proposal)
            pass
        pass


pass


def start_scheduling():
    parse_orders_and_save()

    schedule.every(1).minute.do(parse_orders_and_save)
    while True:
        schedule.run_pending()
        time.sleep(1)
        pass
    pass


if __name__ == '__main__':
    main()
