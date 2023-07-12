from user.user_models import User
from database import database as db


def main():
    # Create and save a user to the database
    my_user = User(email="test@flashcards.com")
    print(my_user.email)

    db.save(my_user)


if __name__ == "__main__":
    main()
