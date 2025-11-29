pipeline {
    agent {
        docker { 
            image 'python:3.10-slim' 
            workingDirectory '/var/jenkins_home/workspace/Python-App-CI'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Código descargado correctamente del repositorio.'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                
                sh 'python task_manager.py'
            }
        }
        
        stage('Reporte') {
            
            steps {
                echo 'El pipeline ha finalizado con éxito.'
            }
        }
    }
}