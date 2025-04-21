"""
Team Object
"""

class TeamOverview:
    name: str
    """
    {
		"goal": 4,
		"assists": 2,
        "corners": 2,
        "shots":{
            "value": 3,
            "on_target": 4
        }
        "cards": {
		  "red": 3,
		  "yellow": 2,
	    }
	}
    """
    averages: dict
    """
    {
		  "wins": 4,
		  "draws": 2,
		  "loses": 2
	}
    """
    streak: dict
    """
    {
		  "best_win": '2-0',
		  "wrost_lost": '0-5',
		  "biggest_goals_for": 2,
          "biggest_goals_against": 4,
          "wrost_goals_for": 4,
          "wrost_goals_against": 5,
          "clean_sheet": 6,
          "failed_to_score": 8
	}
    """
    home: dict
    """
    {
		  "best_win": '2-0',
		  "wrost_lost": '0-5',
		  "biggest_goals_for": 2,
          "biggest_goals_against": 4,
          "wrost_goals_for": 4,
          "wrost_goals_against": 5,
          "clean_sheet": 6,
          "failed_to_score": 8
	}
    """
    away: dict
    """ 
    {
	    "scored": 10,
		"missed": 2
        "percentage": 80%
	}
    """
    penalty: dict

    """
    {
        "to_score":
        {
            "61-75":
            {
                "total": 10,
                "percentage": "15.15%"
            }
	    },
        "to_cards":
        {
            "yellow":
            {
                "0-15": 
                {
                    "total": 5,
                    "percentage": "6.85%"
		        }
            },
            "red":
            {
                "31-45": 
                {
                    "total": null,
                    "percentage": null
		        }
            }
            
        }
    }
    
    """
    best_time: dict
    """
    {
        "over":
        {
            "0.5": 
            {
                "percentage": 20%
            },
            "1.5":
            {
                "percentage": 40%
            },
            "2.5":
            {
                "percentage": 40%
            },
            "3.5":
            {
                "percentage": 40%
            },
            "4.5":
            {
                "percentage": 40%
            }
        },
        "under":
        {
            "0.5": 
            {
                "percentage": 20%
            },
            "1.5":
            {
                "percentage": 40%
            },
            "2.5":
            {
                "percentage": 40%
            },
            "3.5":
            {
                "percentage": 40%
            },
            "4.5":
            {
                "percentage": 40%
            }
        }
    }
    
    """
    goal_percentage: dict




    def __init__(self, **kwargs):
        """
        Constructor.
        """
        self.__dict__.update(kwargs)
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__
