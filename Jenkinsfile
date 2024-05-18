properties([pipelineTriggers([pollSCM('*/5 * * * *')])])
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                pwd
                ls -ltra
                whoami
                sudo apt install python
                pip install -r requirements.txt --break-system-packages
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