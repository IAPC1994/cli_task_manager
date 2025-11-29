node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        // Mantenemos la configuración robusta para permisos y mapeo:
        // --user root: Para anular problemas de permisos.
        // -v ${WORKSPACE}:/app: Mapea el código del host a /app en el contenedor.
        // --workdir /app: Define el directorio de trabajo, evitando el error de 'dir'.
        docker.image('python:3.10-slim').inside("--user root -v ${WORKSPACE}:/app --workdir /app") {
            
            echo 'Iniciando pruebas Python...'
            
            // 🚨 SOLUCIÓN FINAL: Ejecutamos el archivo desde la ruta correcta, /app/src/
            sh 'python /app/src/task_manager.py' 
        }
    }
    
    // Etapa 3: Reporte
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
    }
}