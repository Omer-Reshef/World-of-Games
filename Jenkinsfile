properties([pipelineTriggers([pollSCM('*/5 * * * *')])])
pipeline {
    agent any
    environment{
        DOCKERHUB_CREDENTIALS = credentials('omerr8-dockerhub')
    }

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
                script {
                    try {
                        sh '''
                        pip install -r requirements.txt --break-system-packages
                        python3 MainScores.py &
                        python3 tests/e2e.py
                        '''
                    } catch (Exception e) {
                        error "Tests failed!"
                    }
                }

            }

        }
        stage('Finalize') {
            steps {
                echo 'Finalizing....'
                sh '''
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker compose push
                '''

            }
        }
        post{
            always{
            sh '''
            docker logout
            docker compose down
            '''
            }
        }
    }
}
