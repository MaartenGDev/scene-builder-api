import spacy
import pprint
from classifiers import attribute_classifier, entity_type_classifier

nlp = spacy.load("en_core_web_sm")
doc = nlp("Marcel drove to the big market with his pink car.")

models = list()

entities = {}

for token in doc:
    if token.pos_ == "VERB":
        actions = list()
        source = None
        target = None

        for child in token.children:
            if child.pos_ == "NOUN" or child.pos_ == "PRON" or child.pos_ == "PROPN":
                source = child
            for childTwo in child.children:
                if child.pos_ == "ADP" and source is not None:
                    actions.append({"approach": child.text, "action": token.lemma_, "source": source.idx, "target": childTwo.idx})
                if child.pos_ == "VERB" and source is not None:
                    if target is None:
                        target = childTwo
                    for childThree in childTwo.children:
                        actions.append({"approach": childTwo.text, "action": child.lemma_, "source": source.idx, "target": target.idx})

        if source is not None:
            entities[source.idx] = {"id": source.idx, "label": source.text, "attributes": list(), "actions": actions}

    if token.pos_ == "NOUN":
        if token.idx not in entities:
            entities[token.idx] = {"id": token.idx, "label": token.text, "attributes": list(), "actions": []}

    if token.pos_ == "ADJ":
        if token.head.idx not in entities:
            entities[token.head.idx] = {"id": token.head.idx, "label": token.head.text, "attributes": list(), "actions": []}

        entities[token.head.idx]["attributes"].append(token.text)

type_classifier = entity_type_classifier.EntityTypeClassifier()
attribute_classifier = attribute_classifier.AttributeClassifier()

for entity in entities.values():
    model = {
        "id": entity["id"],
        "name": entity["label"],
        "type": type_classifier.get_type(entity["label"]),
        "properties": list(),
        "actions": entity["actions"]
    }

    for attribute_label in entity["attributes"]:
        model["properties"].append(attribute_classifier.get_as_property(attribute_label))
    models.append(model)

pprint.pprint(models)
