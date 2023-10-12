from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer


STAGE_NAME = "Model Trainer"

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
