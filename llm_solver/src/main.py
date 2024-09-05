import logging

import consts
import solver
from logs.logs import setup_logging, flush_logger


def main():
    setup_logging(log_dir=consts.LOGS_DIR, log_level=logging.DEBUG)

    try:
        logging.info("Starting the LLM Solver application")
        solver.solve_question()
        logging.info("LLM Solver application completed successfully")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)

    finally:
        flush_logger()


if __name__ == "__main__":
    main()
