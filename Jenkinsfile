pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-alpine'
                }
            }
            steps {
                sh 'python -m py_compile blackjack.py ascii_msg.py deck_of_cards.py player.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml unittests.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
