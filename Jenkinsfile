pipeline {
  agent any
  stages {
    stage('CI') {
      parallel {
        stage('CI') {
          steps {
            createSummary(text: 'hello', icon: 'hellow')
            timeout(unit: 'MINUTES', activity: true, time: 3)
          }
        }
        stage('unittest1') {
          steps {
            echo 'test1'
          }
        }
        stage('unittest2') {
          steps {
            echo 'test2'
          }
        }
      }
    }
    stage('Build') {
      agent any
      steps {
        echo 'build'
      }
    }
    stage('Deploy') {
      parallel {
        stage('Deploy') {
          steps {
            echo 'deploy'
          }
        }
        stage('check') {
          steps {
            echo 'check'
          }
        }
      }
    }
  }
}