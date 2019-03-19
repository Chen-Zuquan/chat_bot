from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

training_data = load_data('training_data\demo-rasa.json')
trainer = Trainer(config.load('config\config_spacy.yml'))
trainer.train(training_data)
model_directory = trainer.persist('./projects/')
print(model_directory)

with open('projects/model_path', 'w') as f:
    f.write(model_directory)