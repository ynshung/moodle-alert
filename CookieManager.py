import os

class CookieManager:
    """Manages cookie storage and retrieval."""

    def __init__(self, filename="temp/cookie.txt"):
        self.filename = filename

    def exists(self):
        """Checks if cookie file exists."""
        return os.path.exists(self.filename)

    def get_cookie(self):
        """Reads and returns the cookie from file, if present."""
        if not self.exists():
            print("Cookie not found")
            return None
        with open(self.filename, "r") as f:
            cookie = f.read()
        return cookie

    def store_cookie(self, cookie):
        """Stores the cookie in a file."""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "w") as f:
            f.write(cookie)
