# NLP for scene-builder
Parses text to determine the scene with the entities and associated actions.

## Setup
1. `pip install -r requirements.txt`

## Example
### Input
> Marcel drove to the big market with his pink car.
### Output:
```json
[
  {
    "id": 0,
    "name": "Marcel",
    "type": "entity",
    "actions": [
      {
        "action": "drive",
        "approach": "to",
        "source": 0,
        "target": 24
      },
      {
        "action": "drive",
        "approach": "with",
        "source": 0,
        "target": 45
      }
    ],
    "properties": []
  },
  {
    "id": 24,
    "name": "market",
    "type": "entity",
    "actions": [],
    "properties": [
      {
        "category": "size",
        "source_value": "big",
        "value": 130
      }
    ]
  },
  {
    "id": 45,
    "name": "car",
    "type": "entity",
    "actions": [],
    "properties": [
      {
        "category": "color",
        "source_value": "pink",
        "value": "#ffc0cb"
      }
    ]
  }
]
```