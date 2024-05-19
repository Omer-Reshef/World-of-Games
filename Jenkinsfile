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
                script{
                    sh '''
                    python3 MainScores.py &
                    python3 tests/e2e.py > test_result.log
                    '''
                    if(readFile('test_result.log').contains('-1')){
                        error 'tests failed'
                    }
            }

            }

        }
        stage('Finalize') {
            steps {
                echo 'Finalizing....'
            }
        }
    }
}