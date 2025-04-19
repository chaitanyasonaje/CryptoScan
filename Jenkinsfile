pipeline {
    agent any

    environment {
        // Optional: specify Python path if needed
        PYTHON = 'python'
        PIP = 'pip'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/chaitanyasonaje/CryptoScan.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "${PIP} install -r requirements.txt"
            }
        }

        stage('Run App') {
            steps {
                bat "${PYTHON} app.py"
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Please check the logs above.'
        }
        success {
            echo '✅ Pipeline completed successfully.'
        }
    }
}
