from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import os
from dotenv import load_dotenv


load_dotenv()

MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI')
MLFLOW_TRACKING_USERNAME = os.getenv('MLFLOW_TRACKING_USERNAME')
MLFLOW_TRACKING_PASSWORD = os.getenv('MLFLOW_TRACKING_PASSWORD')


STAGE_NAME = "DATA INGESTION"
try:
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Started! ===============")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Completed! ===============")
    print("\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA VALIDATION"
try:
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Started! ===============")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Completed! ===============")
    print("\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA TRANSFORMATION"
try:
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Started! ===============")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Completed! ===============")
    print("\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL TRAINER"
try:
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Started! ===============")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Completed! ===============")
    print("\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL EVALUATION"
try:
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Started! ===============")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"=============== Stage :: {STAGE_NAME} :: Completed! ===============")
    print("\n")
except Exception as e:
    logger.exception(e)
    raise e