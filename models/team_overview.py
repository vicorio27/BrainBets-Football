"""
Team Object
"""


class TeamOverview:
    name: str
    """
    {
        "goals": 0,
        "corners": 2,
        "fouls": 0,
        "offsides": 0,
        "possesion": 0,
        "goalkeeper_saves": 0,
        "passes": {"total": 0, "accurate": "10%"},
        "shots": 
        {
            "total": 3,
            "on_goal": 4,
            "off_goal": 0,
            "blocked": 0,
            "insidebox": 0,
            "outsidebox": 0,
        },
        "cards": 
        {
            "red": 3,
            "yellow": 2,
        },
        matches:
        {          
            "total_played_games": 0,
            "total_wins": 9,           
            "total_draws": 5,
            "total_loses": 9
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
          "played_games": 4,
          "wins": 9,
          "draws": 0,
          "loses": 0,
		  "best_win": '2-0',
		  "worst_lost": '0-5',
		  "biggest_goals_for": 2,
          "biggest_goals_against": 4,
          "worst_goals_for": 4,
          "worst_goals_against": 5,
          "clean_sheet": 6,
          "failed_to_score": 8
	}
    """
    home: dict
    """
    {
          "played_games": 4,
          "wins": 9,
          "draws": 0,
          "loses": 0,
		  "best_win": '2-0',
		  "worst_lost": '0-5',
		  "biggest_goals_for": 2,
          "biggest_goals_against": 4,
          "worst_goals_for": 4,
          "worst_goals_against": 5,
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
    totals: dict

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
        "to_get_cards":
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
    percentages: dict

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
