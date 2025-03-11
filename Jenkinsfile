pipeline {

    agent any

    environment {
        VENV_DIR = "venv"  // Virtual environment directory
    }

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
                        sudo apt update
                        sudo apt install -y python3 python3-pip python3-venv
                    '''
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    sh '''
                        echo "Setting up virtual environment..."
                        python3 -m venv $VENV_DIR
                        source $VENV_DIR/bin/activate
                        pip install --upgrade pip
                    '''
                }
            }
        }

        stage('Install Python Dependencies') {
            steps {
                script {
                    sh '''
                        echo "Installing Python dependencies..."
                        source $VENV_DIR/bin/activate
                        pip install -r requirements.txt
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
                        source $VENV_DIR/bin/activate
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
