Based on the requirements and assumptions, the following core functions will be necessary:

1. `add_points_to_user(url: str, email: str) -> int`: Accepts a URL and user email, checks if the URL is part of the list of green URLs, and adds 10 points to the user if it is. Returns the updated points of the user.
2. `get_user_points(email: str) -> int`: Returns the amount of points a particular user has.
3. `login_user(email: str, password: str) -> bool`: Validates the user's login credentials and returns True if the login is successful, False otherwise.
4. `get_user_info(email: str) -> dict`: Returns information about the user, including their email and points.
5. `register_user(email: str, password: str) -> bool`: Registers a new user with the provided email and password. Returns True if the registration is successful, False otherwise.

Now let's proceed with creating the necessary files and implementing the code.

1. `main.py` - The entry point of the API.

