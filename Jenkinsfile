pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // base image with Python
        }
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("cryptoscan-image")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("cryptoscan-image").run("-p 5000:5000")
                }
            }
        }
    }
}
