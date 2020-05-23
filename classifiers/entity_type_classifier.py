import classifiers.type_classes as types


class EntityTypeClassifier:
    def get_type(self, name):
        for category in types.classes:
            for possible_name in types.classes[category]:
                if name == possible_name:
                    return category

        return "entity"
