import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

def add_points_to_user(url: str, email: str) -> int:
    # Check if the URL is part of the list of green URLs
    if url in green_urls:
        # Get the current points of the user
        points = get_user_points(email)
        # Add 10 points to the user
        points += 10
        # Update the user's points in the database
        update_points(email, points)
        return points
    else:
        return get_user_points(email)

def get_user_points(email: str) -> int:
    # Retrieve the user's points from the database
    cursor = db.cursor()
    query = "SELECT points FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        return 0

def update_points(email: str, points: int):
    # Update the user's points in the database
    cursor = db.cursor()
    query = "UPDATE users SET points = %s WHERE email = %s"
    cursor.execute(query, (points, email))
    db.commit()
    cursor.close()

def login_user(email: str, password: str) -> bool:
    # Validate the user's login credentials
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True
    else:
        return False

def get_user_info(email: str) -> dict:
    # Retrieve the user's information from the database
    cursor = db.cursor()
    query = "SELECT email, points FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return {'email': result[0], 'points': result[1]}
    else:
        return {}

def register_user(email: str, password: str) -> bool:
    # Register a new user in the database
    cursor = db.cursor()
    query = "INSERT INTO users (email, password, points) VALUES (%s, %s, 0)"
    try:
        cursor.execute(query, (email, password))
        db.commit()
        cursor.close()
        return True
    except mysql.connector.Error:
        cursor.close()
        return False
