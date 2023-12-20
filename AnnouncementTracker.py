import os

class AnnouncementTracker:
    """Tracks the last announcement ID seen."""

    def __init__(self, filename="temp/last_announcement_id.txt"):
        self.filename = filename
    
    def exists(self):
        """Checks if the file exists."""
        return os.path.exists(self.filename)

    def get_last_announcement_id(self):
        """Reads and returns the last announcement ID from the file, handling initialization if needed."""
        if not os.path.exists(self.filename):
            # Initialize file with default value
            with open(self.filename, "w") as f:
                f.write("0")
            return 0
        else:
            with open(self.filename, "r") as f:
                return int(f.read())

    def store_last_announcement_id(self, last_announcement_id):
        """Stores the provided ID as the last announcement ID seen."""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "w") as f:
            f.write(str(last_announcement_id))

