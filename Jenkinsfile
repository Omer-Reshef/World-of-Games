properties([pipelineTriggers([pollSCM('*/5 * * * *')])])
pipeline {
    agent any

    stages {
    stage('Checkout') {
            steps {
                echo 'Checking Out..'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
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