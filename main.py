

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>> Stage '{STAGE_NAME}' started <<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>> Stage '{STAGE_NAME}' completed <<<<\n\nX================X\n")
    except Exception as e:
        logger.exception(e)
        raise e
