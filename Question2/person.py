# ------------------------------
# Person Entity Class
# ------------------------------


class Person:
    def __init__(self, name, gender, biography, privacy="public"):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy  # "public" or "private"

    def __str__(self):
        # Return a readable representation of the person.
        return self.name
