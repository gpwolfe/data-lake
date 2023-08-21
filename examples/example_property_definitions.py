definition = {
    "property-id": "user-custom-property",
    "property-name": "user-custom-property-name",
    "property-title": "user short title",
    "property-description": "user example of a custom property definition",
    "user-custom-property-value": {
        "type": "float",
        "has-unit": True,  # or False
        "extent": [],
        "required": True,  #
        "description": "A single float value",
    },
    "user-custom-1d-array": {
        "type": "float",
        "has-unit": True,  # or False
        "extent": [":"],
        "required": False,
        "description": "An optional 1D vector of float values",
    },
    "user-custom-per-atom-array": {
        "type": "float",
        "has-unit": True,  # or False
        "extent": [":", 3],
        "required": True,
        "description": "2D array of float values in which second dimension is of length 3",
    },
}
