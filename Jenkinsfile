// pipeline {
//     agent any
    
//     stages {
//         stage('Clone Repository') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/mohsinkkc/xduce.git'
//             }
//         }
//         stage('Run Python Script') {
//             steps {
//                 script {
//                     // Print out the current directory for debugging
//                     bat 'dir'
                    
//                     // Execute the Python script directly
//                     bat 'python week_1/2-april.py'
//                 }
//             }
//         }
//     }
// }
// ===================================From Git ===========================================================
pipeline {
    agent any

    stages {
        stage('scm') {
            steps {
                git branch: 'main', url: 'https://github.com/mohsinkkc/jenkins.git'
            }
        }
        stage('docker build & push') {
            steps {
                script {
                    bat 'docker build -t mohsinkkc/mohsin:tag123 .'
                }
            }
        }
        stage('push docker image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'mohsinkkc', variable: 'dockerhubpwd')]) {
                        bat "docker login -u mohsinkkc -p ${dockerhubpwd}"
                    }
                    bat 'docker push mohsinkkc/mohsin:tag123'
                }
            }
        }
        stage('run Python image') {
            steps {
                script {
                    bat 'docker run mohsinkkc/mohsin:tag123 python program.py'
                }
            }
        }
    }
}
