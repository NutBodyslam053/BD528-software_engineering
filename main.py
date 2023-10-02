from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


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