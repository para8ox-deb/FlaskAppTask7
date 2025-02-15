pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/para8ox-deb/FlaskAppTask7.git' 
            }
        }

        stage('Install Dependencies') {
            steps {
                 
            }
        }

        stage('Stop Previous Flask App') {
            steps {
                script {
                    bat '''
                    REM Find process ID (replace with a more robust method if needed)
                    for /f "tokens=2 delims=:" %%a in ('netstat -ano ^| findstr :5000') do (
                      set PID=%%a
                      goto :foundPID
                    )
                    :foundPID

                    if not defined PID (
                      echo "No Flask app found running on port 5000"
                    ) else (
                      echo "Stopping existing Flask app with PID %PID%"
                      taskkill /PID %PID% /F /T  // Force kill the process tree
                    )
                    '''
                }
            }
        }

        stage('Run Flask App') {
            steps {
                bat 'start python app.py' 
            }
        }
    }
}
