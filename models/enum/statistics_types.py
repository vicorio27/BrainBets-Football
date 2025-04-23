from enum import Enum

class StatisticsTypes(Enum):
    SHOTS_ON_GOAL = "Shots on Goal"
    SHOTS_OFF_GOAL = "Shots off Goal"
    TOTAL_SHOTS = "Total Shots"
    BLOCKED_SHOTS = "Blocked Shots"
    SHOTS_INSIDEBOX = "Shots insidebox"
    SHOTS_OUTSIDEBOX = "Shots outsidebox"
    FOULS = "Fouls"
    CORNER_KICKS = "Corner Kicks"
    OFFSIDES = "Offsides"
    BALL_POSSESSION = "Ball Possession"
    YELLOW_CARD = "Yellow Cards"
    RED_CARD = "Red Cards"
    GOALKEEPER_SAVES = "Goalkeeper Saves"
    TOTAL_PASSES = "Total passes"
    PASSES_ACCURATE = "Passes accurate"
