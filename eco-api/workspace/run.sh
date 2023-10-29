from api import add_points_to_user

def generate_startup_actions():
    # Add points to users for green URLs
    green_urls = [
        'https://example.com',
        'https://example.org',
        'https://example.net'
    ]
    users = [
        {'email': 'user1@example.com', 'points': 0},
        {'email': 'user2@example.com', 'points': 0}
    ]

    for url in green_urls:
        for user in users:
            add_points_to_user(url, user['email'])

if __name__ == '__main__':
    generate_startup_actions()
