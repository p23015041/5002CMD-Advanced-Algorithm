#---------- Q2 ----------#

# Define a class person for user profile info
class Person:
    def __init__(self, name, gender, bio, privacy):
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy  # 'public' or 'private'

# Define socialgraph for users and relationship
class SocialGraph:
    def __init__(self):
        self.graph = {}
        self.users = {}

    # Add new user
    def add_user(self, person):
        self.users[person.name] = person
        self.graph[person.name] = []

    # Create follow connection
    def follow(self, follower, followee):
        if followee not in self.graph[follower]:
            self.graph[follower].append(followee)

    # List of users that is following
    def get_following(self, name):
        return self.graph.get(name, [])

    # List of users who follow a user
    def get_followers(self, name):
        return [user for user in self.graph if name in self.graph[user]]

    # View user profile
    def view_profile(self, name):
        person = self.users[name]
        if person.privacy == 'private':
            return f"Name: {person.name}\n[Private Profile]"
        return (
            f"Name: {person.name}\n"
            f"Gender: {person.gender}\n"
            f"Bio: {person.bio}\n"
            f"Privacy: {person.privacy}"
        )

    # Return list
    def list_users(self):
        return list(self.users.keys())

# Main Function
def main():
    sg = SocialGraph()

    # Create users
    users = [
        Person("Ben", "Male", "Loves cars", "public"),
        Person("Ethan", "Male", "Enjoys hiking", "private"),
        Person("Preston", "Male", "Music lover", "public"),
        Person("Aaron", "Male", "Gamer", "public"),
        Person("Bob", "Male", "Photographer", "private")
    ]

    for user in users:
        sg.add_user(user)

    # Create relationships
    sg.follow("Ben", "Ethan")
    sg.follow("Ben", "Preston")
    sg.follow("Ethan", "Ben")
    sg.follow("Preston", "Bob")
    sg.follow("Aaron", "Ben")

    # Menu interface
    while True:
        print("\nProgram Main Menu:")
        print("1. View all profile names")
        print("2. View details for any profile")
        print("3. View followers for any profile")
        print("4. View followed accounts for any profile")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nAll Profiles:")
            for name in sg.list_users():
                print(f"- {name}")

        elif choice == "2":
            name = input("Enter profile name: ")
            if name in sg.users:
                print("\n" + sg.view_profile(name))
            else:
                print("Profile not found.")

        elif choice == "3":
            name = input("Enter profile name: ")
            if name in sg.users:
                followers = sg.get_followers(name)
                print(f"\nFollowers of {name}:")
                if followers:
                    for follower in followers:
                        print(f"- {follower}")
                else:
                    print("No followers.")
            else:
                print("Profile not found.")

        elif choice == "4":
            name = input("Enter profile name: ")
            if name in sg.users:
                following = sg.get_following(name)
                print(f"\n{name} is following:")
                if following:
                    for followee in following:
                        print(f"- {followee}")
                else:
                    print("Not following anyone.")
            else:
                print("Profile not found.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

# Run program
if __name__ == "__main__":
    main()
