pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Jenkins will automatically use the repository where this Jenkinsfile is located
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Run the Python script
                echo 'Running the Python script...'
                sh 'python3 sum.py'
            }
        }

        stage('Test') {
            steps {
                // Run tests using pytest
                echo 'Running tests...'
                sh 'pytest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
