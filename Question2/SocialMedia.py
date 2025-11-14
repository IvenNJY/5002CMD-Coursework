# ------------------------------
# Social Media Application
# ------------------------------
from graph import Graph
from person import Person


class SocialMediaApp:
    def __init__(self):
        self.graph = Graph()
        self.people = {}

    def addPerson(self, person):
        # Adds a Person object to the app and graph.
        self.people[person.name] = person
        self.graph.addVertex(person.name)

    def _get_person(self, name):
        person = self.people.get(name)
        if not person:
            print(f"No user found with name '{name}'")
        return person

    def displayAllUsers(self):
        # Displays all user names.
        print("\n--- All Users ---")
        for name in self.graph.displayAllVertices():
            print(name)
        print("-----------------")

    def viewProfile(self, name):
        # View the profile of a person.
        person = self._get_person(name)
        if not person:
            return
        print("\n--- Profile ---")
        if person.privacy == "private":
            print(f"Name: {person.name}")
            print("(Private Profile: Other details hidden)")
        else:
            print(f"Name: {person.name}")
            print(f"Gender: {person.gender}")
            print(f"Biography: {person.biography}")
            print(f"Privacy: {person.privacy}")
        print("----------------")

    def viewFollowing(self, name):
        # Displays all accounts the person is following.
        if not self._get_person(name):
            return
        following = self.graph.listOutgoingAdjacentVertex(name)
        print(f"\n{name} follows:")
        if following:
            for f in following:
                print(f"- {f}")
        else:
            print("No following accounts.")

    def viewFollowers(self, name):
        # Displays all accounts following the person.
        if not self._get_person(name):
            return
        followers = self.graph.listIncomingAdjacentVertex(name)
        print(f"\nFollowers of {name}:")
        if followers:
            for f in followers:
                print(f"- {f}")
        else:
            print("No followers.")

    def followUser(self, from_name, to_name):
        # Allows a user to follow another.
        if self._get_person(from_name) is None or self._get_person(to_name) is None:
            print("Invalid user(s).")
            return
        self.graph.addEdge(from_name, to_name)
        print(f"{from_name} now follows {to_name}.")

    def unfollowUser(self, from_name, to_name):
        # Allows a user to unfollow another.
        if self._get_person(from_name) is None or self._get_person(to_name) is None:
            print("Invalid user(s).")
            return
        self.graph.removeEdge(from_name, to_name)
        print(f"{from_name} unfollowed {to_name}.")

    def displayGraph(self):
        print(self.graph)
        return

    # ------------------------------
    # Menu System
    # ------------------------------
    def menu(self):
        choice = ""
        while choice != "0":
            print("\n==== Social Media Menu ====")
            print("1. Display all users")
            print("2. View a user profile")
            print("3. View following list")
            print("4. View followers list")
            print("5. Add new user")
            print("6. Follow another user")
            print("7. Unfollow a user")
            print("8. Display Graph")
            print("0. Exit")

            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    self.displayAllUsers()
                case "2":
                    name = input("Enter the user's name: ")
                    self.viewProfile(name)
                case "3":
                    name = input("Enter the user's name: ")
                    self.viewFollowing(name)
                case "4":
                    name = input("Enter the user's name: ")
                    self.viewFollowers(name)
                case "5":
                    self._handle_add_user()
                case "6":
                    from_name = input("Enter your name: ")
                    to_name = input("Enter the name you want to follow: ")
                    self.followUser(from_name, to_name)
                case "7":
                    from_name = input("Enter your name: ")
                    to_name = input("Enter the name you want to unfollow: ")
                    self.unfollowUser(from_name, to_name)
                case "8":
                    self.displayGraph()
                case "0":
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid choice. Try again.")

    def _handle_add_user(self):
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        bio = input("Enter biography: ")
        privacy = input("Privacy (public/private): ").lower()

        newPerson = Person(name, gender, bio, privacy)
        self.addPerson(newPerson)

        print(f"User '{name}' added.")


# ------------------------------
# Main Function
# ------------------------------
def main():
    app = SocialMediaApp()

    # Create initial Person profiles (5-10 users)
    initial_users = [
        ("Alice", "Female", "Loves art and coffee", "public"),
        ("Bob", "Male", "Tech enthusiast and gamer", "public"),
        ("Charlie", "Male", "Private person", "private"),
        ("Diana", "Female", "Traveler and foodie", "public"),
        ("Eve", "Female", "Cybersecurity expert", "private"),
    ]

    # Add to app
    for name, gender, bio, privacy in initial_users:
        app.addPerson(Person(name, gender, bio, privacy))

    # Simulate follow connections
    app.followUser("Alice", "Bob")
    app.followUser("Alice", "Diana")
    app.followUser("Bob", "Alice")
    app.followUser("Diana", "Eve")
    app.followUser("Charlie", "Bob")

    # Start menu
    app.menu()


if __name__ == "__main__":
    main()
