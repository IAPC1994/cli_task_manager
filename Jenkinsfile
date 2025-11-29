pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                echo 'Código descargado correctamente del repositorio.'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                
                sh 'python app.py' 
            }
        }
        
        stage('Reporte') {
            
            steps {
                echo 'El pipeline ha finalizado con éxito.'
            }
        }
    }
}