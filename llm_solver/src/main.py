import logging
import pathlib
from logs.logs import setup_logging, flush_logger

def main():
    logs_dir = pathlib.Path(__file__).parent.parent.resolve() / "logs"
    setup_logging(log_dir="logs", log_level=logging.DEBUG)
    
    try:
        logging.info("Starting the LLM Solver application")
        
        
        logging.info("LLM Solver application completed successfully")
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)
    
    finally:
        flush_logger()

if __name__ == "__main__":
    main()
