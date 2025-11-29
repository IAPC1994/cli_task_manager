node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        // Ejecuta el contenedor 'python:3.10-slim'
        // CRUCIAL: Mapeamos el WORKSPACE del host a /app dentro del contenedor.
        // Esto resuelve el problema de visibilidad de archivos (AccessDenied/No such file)
        docker.image('python:3.10-slim').inside("-v ${WORKSPACE}:/app") {
            
            // Cambiamos el directorio de trabajo DENTRO del contenedor a /app
            dir('/app') {
                echo 'Iniciando pruebas Python...'
                
                // Ejecutamos el script desde /app (que es el custom workspace)
                sh 'python task_manager.py' 
            }
        }
    }
    
    // Etapa 3: Reporte (Manteniendo la estructura completa)
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
        // Puedes agregar aquí pasos futuros para generar reportes, enviar notificaciones, etc.
    }
}