properties([pipelineTriggers([pollSCM('*/5 * * * *')])])
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                docker compose build
                '''
            }
        }
        stage('Run') {
            steps {
                echo 'Running..'
                sh '''
                docker compose run -d app
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                 sh '''
                    pip install -r requirements.txt --break-system-packages
                    python3 MainScores.py &
                    ls -ltra
                    python3 tests/e2e.py > test_result.log
                    cat test_result.log
                    '''

            }

        }
        stage('Finalize') {
            steps {
                echo 'Finalizing....'
            }
        }
    }
}