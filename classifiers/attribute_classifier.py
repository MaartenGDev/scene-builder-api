from classifiers import sizing_classes
import webcolors


class AttributeClassifier:
    color_classes = list(["big", "small", "massive", "tiny"])

    def get_as_property(self, raw_value):
        if raw_value in sizing_classes.classes:
            return {"category": "size", "value": sizing_classes.classes[raw_value], "source_value": raw_value}

        if raw_value in webcolors.CSS3_NAMES_TO_HEX:
            return {"category": "color", "value": webcolors.name_to_hex(raw_value), "source_value": raw_value}

        return {"category": "unknown", "value": 100, "source_value": raw_value}
