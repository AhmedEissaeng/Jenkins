pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'cd /var/lib/jenkins/workspace/pipe/'
                sh 'docker build -t myapp:v1 .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run -d myapp:v1 -p 5001:5001'
            }
        }
    }
}
