node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        docker.image('python:3.10-slim').inside("--user root -v ${WORKSPACE}:/app --workdir /app") {
            
            echo 'Iniciando pruebas Python...'
            
            
            sh 'python /app/src/task_manager.py' 
        }
    }
    
    // Etapa 3: Reporte
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
    }
}