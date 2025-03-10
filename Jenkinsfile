pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/voodiga-rajachandra/jenkinspipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'pkill -f app.py || true'  // Stop old process
                sh 'nohup python app.py &'
            }
        }
    }
}

