from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME_1 = "Data Ingestion Stage"
STAGE_NAME_2 = "Data Validation Stage"
STAGE_NAME_3 = "Data Transformation"

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

        logger.info(f">>>> Stage '{STAGE_NAME_3}' started <<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>> Stage '{STAGE_NAME_3}' completed <<<<\n\nX================X\n")



    except Exception as e:
        logger.exception(e)
        raise e
