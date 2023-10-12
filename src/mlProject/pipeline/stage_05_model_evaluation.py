from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation


STAGE_NAME = "Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()