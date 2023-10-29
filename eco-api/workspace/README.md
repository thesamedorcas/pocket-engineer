Based on the requirements, the following core functions will be necessary:

1. `add_points_to_user(url: str, email: str) -> None`: Accepts a URL and user email. If the URL is part of the list of green URLs, it adds 10 points to the user.
2. `get_user_points(email: str) -> int`: Returns the amount of points a particular user has.
3. `login_user(email: str, password: str) -> bool`: Validates the user's login credentials (email and password).
4. `get_user_info(email: str) -> dict`: Returns information about the user, including their email and points.

Now let's proceed with creating the necessary files and writing the code.

1. `main.py` - The entry point of the API.

