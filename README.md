# jenkins-ci-lab

Learning CI/CD properly: a real Jenkins **declarative pipeline** that lints, tests, and smoke-checks actual code — not a hello-world echo.

The pipeline (`Jenkinsfile`) has 4 real stages against the tiny [`app/`](app/) Python package:

| Stage | What it does |
|---|---|
| **Setup** | Creates a venv, installs dev deps |
| **Lint** | `ruff check app/` |
| **Test** | `pytest` with JUnit reporting (visible in Jenkins) |
| **Smoke** | Import + behavior assertion as a final gate |

## Run Jenkins locally

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
# grab the initial admin password:
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

1. Open http://localhost:8080, install suggested plugins
2. New Item → **Pipeline** → point SCM at this repo
3. Build — watch Setup → Lint → Test → Smoke go green (or red, that's the point)

## Run the checks locally (no Jenkins)

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
ruff check app/
pytest app/ -v
```

## Why this exists

The old `Jenkinsfile` repo was a copy-paste of three `echo` statements. That teaches nothing. This repo teaches: virtualenvs in CI, failing stages, JUnit reports, and what "red build" actually means.
