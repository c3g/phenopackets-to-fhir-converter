import json
import jsonschema
import os
import logging


logger = logging.getLogger(__name__)
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'schema')


def validate_schema(schema, data):
    with open(schema) as s:
        json_schema = json.loads(s.read())
    v = jsonschema.Draft7Validator(json_schema)
    try:
        jsonschema.validate(data, json_schema, format_checker=jsonschema.FormatChecker())
        logger.info('The file is valid. Validation passed.')
        return True
    except jsonschema.exceptions.ValidationError:
        errors = [e for e in v.iter_errors((data))]
        logger.info(f"The file is not valid. Total errors: {len(errors)}")
        for i, error in enumerate(errors, 1):
            logger.error(f"{i} Validation error in {'.'.join(str(v) for v in error.path)}: {error.message}")
        logger.info('Validation failed.')
        return False
