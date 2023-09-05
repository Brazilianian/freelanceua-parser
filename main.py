import time

import schedule

from database.db_initializer import init_db
from domain.proposal import Proposal
from domain.proposal_type_enum import ProposalType
from logger_configuration import logger
from logger_configuration.log_config import init_logger
from service import proposal_service
from service.freelancehunt import freelancehunt_projects_parser, freelancehunt_service
from service.freelanceua import freelanceua_parser, freelanceua_service


def parce_freelanceua():
    soup = freelanceua_parser.get_beautiful_soap()
    proposals: [Proposal] = freelanceua_service.get_proposals_from_soup(soup)

    for proposal in proposals:
        if not proposal_service.is_proposal_exists(proposal):
            logger.info(f"Found new proposal on {proposal.freelance_site.name} with link - {proposal.link}")
            proposal_service.save_proposal(proposal)


def parse_freelancehunt():
    # Parse Projects
    soup = freelancehunt_projects_parser.get_beautiful_soap()
    proposals: [Proposal] = freelancehunt_service.get_proposals_from_soup(soup, ProposalType.PROJECT)

    for proposal in proposals:
        if not proposal_service.is_proposal_exists(proposal):
            logger.info(f"Found new proposal on {proposal.freelance_site.name} with link - {proposal.link}")
            proposal_service.save_proposal(proposal)

    # Parse Orders


def parse_orders_and_save():
    parce_freelanceua()
    parse_freelancehunt()


def start_scheduling():
    parse_orders_and_save()

    schedule.every(20).seconds.do(parse_orders_and_save)

    logger.info("Starting scheduler")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    init_logger()
    init_db()
    start_scheduling()
    print("Parser started")
