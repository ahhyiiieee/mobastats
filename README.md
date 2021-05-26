# mobastats
Developer test project

# Setup:
1. Install Docker and Docker Compose: https://docs.docker.com/get-docker/
2. Run the project from your Terminal / Command Line: `docker-compose up`
3. If everything works, you'll be able to go to http://localhost:8000/ and log in with the test accounts below

# Test accounts:
1. player1 / password = your main account to develop for
2. player2 / password = another account, to test user filtering
3. admin / password = has access to Django admin (http://localhost:8000/admin/)

# Docker / Django basics:
- To connect to your Docker container and run commands against it: `docker-compose run web bash`
- (All commands below assume you're inside the Docker container)
- To open the Django shell: `python manage.py shell`
- To generate migrations: `python manage.py makemigrations` (you may need to specify the app if you're making migrations for a new app: `python manage.py makemigrations games`)
- To run the generated migrations: `python manage.py migrate`
