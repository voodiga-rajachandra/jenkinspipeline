pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/voodiga-rajachandra/jenkinspipeline.git'
                }
            }
        }

        stage('Install System Dependencies') {
            steps {
                script {
                    sh '''
                        # Update package list
                        sudo apt update

                        # Install Python and pip if not already installed
                        sudo apt install -y python3 python3-pip

                        # Upgrade pip
                        python3 -m pip install --upgrade pip
                    '''
                }
            }
        }

        stage('Install Python Dependencies') {
            steps {
                script {
                    sh '''
                        # Install dependencies globally
                        sudo pip3 install -r requirements.txt
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh '''
                        # Stop old process if running
                        pkill -f app.py || true

                        # Start the application in the background
                        nohup python3 app.py > app.log 2>&1 &
                    '''
                }
            }
        }

    }

    post {

        success {
            echo 'Deployment successful! ✅'
        }

        failure {
            echo 'Deployment failed! ❌'
        }

    }

}
