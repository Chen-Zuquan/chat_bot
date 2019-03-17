import spacy
nlp = spacy.load('en_core_web_md')
include_entities = ['ORG']

# Define extract_entities()
def extract_entities(message):
    # Create a dict to hold the entities
    ents = dict.fromkeys(include_entities)
    # Create a spacy document
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            return ent.text
    return ""
