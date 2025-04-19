pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/chaitanyasonaje/CryptoScan.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("cryptoscan-image")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run("-p 5000:5000")
                }
            }
        }
    }
}
