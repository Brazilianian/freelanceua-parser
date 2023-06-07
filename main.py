from logger_configuration import logger
import time

import schedule

from database.db_initializer import init_db
from domain.proposal import Proposal
from logger_configuration import logger
from logger_configuration.log_config import init_logger
from service import proposal_service
from service.freelanceua import freelanceua_parser, freelanceua_service


def main():
    init_logger()
    init_db()
    start_scheduling()


pass


def parce_freelanceua():
    soup = freelanceua_parser.get_beautiful_soap()
    proposals: [Proposal] = freelanceua_service.get_proposals_from_soup(soup)

    for proposal in proposals:
        if not proposal_service.is_proposal_exists(proposal):
            logger.info(f"Found new proposal on {proposal.freelance_site.name} with link - {proposal.link}")
            proposal_service.save_proposal(proposal)
            pass
        pass
    pass


def parse_orders_and_save():
    parce_freelanceua()


pass


def start_scheduling():
    parse_orders_and_save()

    schedule.every(1).minute.do(parse_orders_and_save)

    logger.info("Starting scheduler")

    while True:
        schedule.run_pending()
        time.sleep(1)
        pass
    pass


if __name__ == '__main__':
    main()
