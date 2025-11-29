node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        // Mantenemos los argumentos de permisos y mapeo de volumen
        docker.image('python:3.10-slim').inside("--user root -v ${WORKSPACE}:/app --workdir /app") {
            
            echo 'Iniciando pruebas Python...'
            
            // --- CAMBIO CRUCIAL: Ejecutamos el script usando su ruta absoluta dentro del contenedor ---
            // El archivo está en /app (gracias a -v), así evitamos el error de directorio de trabajo (-w)
            sh 'python /app/task_manager.py' 
        }
    }
    
    // Etapa 3: Reporte
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
    }
}