properties([pipelineTriggers([pollSCM('*/5 * * * *')])])
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                pwd
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run') {
            steps {
                echo 'Running..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Finalize') {
            steps {
                echo 'Finalizing....'
            }
        }
    }
}