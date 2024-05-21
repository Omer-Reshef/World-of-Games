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
                script {
                    try {
                        sh '''
                        pip install -r requirements.txt --break-system-packages
                        python3 MainScores.py &
                        python3 tests/e2e.py
                        '''
//                         sh 'pip install -r requirements.txt --break-system-packages'
//                         sh 'python3 MainScores.py &'
//                         sh 'python3 tests/e2e.py'
                    } catch (Exception e) {
                        sh 'docker compose down'
                        error "Tests failed!"
                    }
                }
//                  sh '''
//                     pip install -r  --no-cache-dir requirements.txt --break-system-packages
//                     python3 MainScores.py &
//                     python3 tests/e2e.py > e2e.log
//                     cat test_result.log
//                     '''

            }

        }
        stage('Finalize') {
            steps {
                echo 'Finalizing....'
                sh '''
                docker compose down
                docker compose push
                '''

            }
        }
    }
}