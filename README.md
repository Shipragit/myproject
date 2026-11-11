# Python Flask Docker Demo

This project is a simple real web application built with Flask. It demonstrates:

- testing a Python web app
- creating a Docker image
- pushing the image to Docker Hub using GitHub Actions
- tagging each image with the Git commit SHA

## Project structure

- `app.py` - Flask web application
- `requirements.txt` - Python dependencies
- `tests/test_app.py` - unit tests
- `Dockerfile` - container definition
- `.github/workflows/docker-publish.yml` - CI/CD pipeline

## Run locally

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Start the app:

```bash
python app.py
```

Open in a browser:

```bash
http://localhost:8081
```

Expected output:

```text
Hello, World!
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Build the Docker image locally

```bash
docker build -t shivakumara493/python-demo-app:local .
```

Run the container:

```bash
docker run --rm -p 8081:8081 -e APP_NAME=Alice shivakumara493/python-demo-app:local
```

Then open:

```bash
http://localhost:8081
```

## GitHub Actions setup

Add these GitHub repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

The workflow pushes the image using the Git commit SHA tag, for example:

```text
shivakumara493/python-demo-app:5eeb4fe6f9cdc9aed91801fc21c5f3ac75120505
```

Then push to the `main` branch or run the workflow manually from the GitHub Actions tab.
