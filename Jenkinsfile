node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        // Mantenemos la configuración robusta para permisos y mapeo a /app
        // Argumentos: --user root (permisos) -v ${WORKSPACE}:/app (mapeo) --workdir /app (directorio de trabajo)
        docker.image('python:3.10-slim').inside("--user root -v ${WORKSPACE}:/app --workdir /app") {
            
            echo 'Iniciando pruebas Python...'
            
            // 🚨 SOLUCIÓN FINAL: Ejecutamos el archivo desde la ruta CORRECTA: /app/src/
            sh 'python /app/src/task_manager.py' 
        }
    }
    
    // Etapa 3: Reporte
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
    }
}