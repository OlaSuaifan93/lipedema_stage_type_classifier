from src.cnnclassifier import logger
from src.cnnclassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnclassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnclassifier.pipeline.stage03_training import ModelTrainingPipeline
from src.cnnclassifier.pipeline.stage04_evaluation import EvaluationPipeline



STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="prepare base model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e