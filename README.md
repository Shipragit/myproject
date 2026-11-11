# Python Docker Demo

This is a minimal Python application that demonstrates:

- building and testing a Python app
- creating a Docker image
- pushing the image to Docker Hub using GitHub Actions

## Project structure

- `app.py` - simple Python application
- `tests/test_app.py` - unit tests
- `Dockerfile` - container definition
- `.github/workflows/docker-publish.yml` - CI/CD pipeline

## Run locally

```bash
python3 app.py
```

Expected output:

```bash
Hello, World!
```

Run tests:

```bash
python3 -m unittest discover -s tests -v
```

Build the Docker image locally:

```bash
docker build -t python-demo-app .
```

Run the container:

```bash
docker run --rm -e APP_NAME=Alice python-demo-app
```

## GitHub Actions setup

Add these GitHub repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Then push to the `main` branch or run the workflow manually from the GitHub Actions tab.
