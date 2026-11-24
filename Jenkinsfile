pipeline {
    agent any

    tools {
        // Uses a Python installed on the Jenkins agent; adjust to your setup.
    }

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Creating virtualenv and installing dependencies...'
                sh '''
                    python3 -m venv $VENV
                    . ./$VENV/bin/activate
                    pip install --quiet -r requirements-dev.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Linting with ruff...'
                sh '''
                    . ./$VENV/bin/activate
                    ruff check app/
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest...'
                sh '''
                    . ./$VENV/bin/activate
                    pytest app/ -v --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'results.xml'
                }
            }
        }

        stage('Smoke') {
            steps {
                echo 'Import + behavior smoke test...'
                sh '''
                    . ./$VENV/bin/activate
                    python -c "from app.slugify import slugify; assert slugify('Hello, CI World!') == 'hello-ci-world'; print('smoke OK')"
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline passed.'
        }
        failure {
            echo '❌ Pipeline failed — check the stage that went red.'
        }
        always {
            echo 'Cleaning workspace venv...'
            sh 'rm -rf venv || true'
        }
    }
}
