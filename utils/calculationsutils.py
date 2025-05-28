from utils.jsonutils import max_value_from_json_array

def calculate_best_minutes(minutes):
    key, max_value_item = max_value_from_json_array([minutes], "total")
    best_value = {"time": key, "value": max_value_item}

    return best_value


def calculate_best_under_over(under_over):
    key, max_under = max_value_from_json_array([under_over], "under")
    key_o, max_over = max_value_from_json_array([under_over], "over")
    best_under = {"value": key, "under": max_under}
    best_over = {"value": key_o, "under": max_over}

    return best_under, best_over


def calculate_best_lineup(lineups):
    formation, played = max_value_from_json_array(lineups, "played")
    best_lineup = {"formation": formation, "played": played}

    return best_lineup


def calculate_best_time_to_get_cards(cards):
    key, max_value_item = max_value_from_json_array([cards], "total")
    best_value = {"time": key, "value": max_value_item}

    return best_value