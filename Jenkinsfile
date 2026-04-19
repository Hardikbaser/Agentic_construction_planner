pipeline {
    agent any

    environment {
        IMAGE_NAME = "hb7960/myapp"
        DOCKER_CREDENTIALS = "dockerhub-creds"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'cd backend && docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKER_CREDENTIALS,
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([string(
                    credentialsId: 'groq-api-key',
                    variable: 'GROQ_API_KEY'
                )]) {
                    sh '''
                    docker stop myapp || true
                    docker rm myapp || true
                    docker run -d -p 8000:8000 \
                      -e GROQ_API_KEY=$GROQ_API_KEY \
                      --name myapp $IMAGE_NAME
                    '''
                }
            }
        }
    }
}
