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
                        echo "Installing system dependencies..."
                        echo "jenkins" | sudo -S apt update  # Run sudo in non-interactive mode
                        sudo apt install -y python3 python3-pip
                        python3 -m pip install --upgrade pip
                    '''
                }
            }
        }

        stage('Install Python Dependencies') {
            steps {
                script {
                    sh '''
                        echo "Installing Python dependencies..."
                        sudo pip3 install -r requirements.txt
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh '''
                        echo "Stopping old process..."
                        pkill -f app.py || true

                        echo "Starting application..."
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
