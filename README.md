# DevOps CLI Game Project

## Description

This project is a comprehensive DevOps assignment that involves creating a Python CLI game, end-to-end (e2e) tests using Selenium, and a Flask server to serve the Selenium tests. Additionally, the project is containerized using Docker, managed with Docker Compose, and automated with a Jenkins CI/CD pipeline.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Docker](#docker)
- [CI/CD with Jenkins](#cicd-with-jenkins)

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Docker:**
    Make sure you have Docker and Docker Compose installed on your system.

## Usage

1. **Run the CLI game:**
    ```bash
    python MainGame.py
    ```

2. **Run the Flask server for Selenium tests:**
    ```bash
    python MainScores.py
    ```

## Testing

To run the end-to-end tests using Selenium:

1. Ensure the Flask server is running:
    ```bash
    python MainScores.py
    ```

2. Execute the Selenium tests:
    ```bash
    python e2e.py
    ```

## Docker

### Dockerfile

The Dockerfile is used to build a Docker image for the application. It includes the main game and the Flask server for testing.

### Building and Running with Docker Compose

1. **Build the Docker image:**
    ```bash
    docker-compose build
    ```

2. **Run the Docker container:**
    ```bash
    docker-compose up
    ```

## CI/CD with Jenkins

This project uses Jenkins to automate the CI/CD pipeline. The `Jenkinsfile` includes the following stages:

1. **Checkout:** Checkout the repository.
2. **Build:** Build the Docker image.
3. **Run:** Run the Dockerized application.
4. **Test:** Execute the Selenium tests.
5. **Finalize:** Terminate the container and push the Docker image to Docker Hub.