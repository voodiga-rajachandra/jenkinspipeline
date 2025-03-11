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
 
        stage('Setup Python Environment') {

            steps {

                script {

                    sh '''

                        python3 -m venv $VENV_DIR  # Create virtual environment

                        source $VENV_DIR/bin/activate  # Activate venv

                        pip install --upgrade pip  # Upgrade pip

                        pip install -r requirements.txt  # Install dependencies

                    '''

                }

            }

        }
 
        stage('Deploy Application') {

            steps {

                script {

                    sh '''

                        pkill -f app.py || true  # Stop old process if running

                        nohup $VENV_DIR/bin/python app.py > app.log 2>&1 &  # Run app in the background

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

 
