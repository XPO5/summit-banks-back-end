# Build the Docker container
build:
	docker build -t bank-app .

# Run the Docker container and enter a bash shell
run:
	docker run -it --rm -p 8000:8000 bank-app

# Shortcut to build, run, install, and start the app in development mode
start: build run