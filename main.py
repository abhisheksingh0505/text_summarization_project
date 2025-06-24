from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME_1 = "Data Ingestion Stage"
STAGE_NAME_2 = "Data Validation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>> Stage '{STAGE_NAME_1}' started <<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>> Stage '{STAGE_NAME_1}' completed <<<<\n\nX================X\n")

        logger.info(f">>>> Stage '{STAGE_NAME_2}' started <<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>> Stage '{STAGE_NAME_2}' completed <<<<\n\nX================X\n")

    except Exception as e:
        logger.exception(e)
        raise e
