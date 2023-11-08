from datetime import datetime


class CheckedHistoryRecord:
    """
    This class represents one record in habit checked-off history
    """
    def __init__(self, streak: int):
        """
        Constructor of the CheckedHistoryRecord class.

        :param streak: The streak or number of days a habit has been successfully checked off.
        """
        # Generate the current date and time and store it in ISO 8601 format as the occurred_at attribute.
        self.occurred_at = datetime.now().isoformat()
        self.streak = streak  # Assign the provided streak to the object's streak attribute.

