import json


def max_value_from_json_array(json_data, key):
    """
    Finds the maximum value associated with a specific key in a JSON array.

    Args:
        json_data: A JSON string or a Python list of dictionaries.
        key: The key to search for within each dictionary.

    Returns:
        The maximum value found, or None if the key is not found or the data is invalid.
    """
    try:
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data

        if not isinstance(data, list):
            return None, None

        max_value = None
        key_v = None
        for item in data:
            if isinstance(item, dict) and key in item:
                if max_value is None or item[key] > max_value:
                    max_value = item[key]
                    key_v = key
        return key_v, max_value
    except json.JSONDecodeError:
        return None, None
