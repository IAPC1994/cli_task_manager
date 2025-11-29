node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        // El argumento 'inside()' ahora contiene la solución triple:
        // 1. --user root: Para anular los problemas de permisos del host/kernel.
        // 2. -v ${WORKSPACE}:/app: Mapea el código del host a /app en el contenedor.
        // 3. --workdir /app: Le indica a Docker que el directorio de trabajo predeterminado es /app.
        //    (Esto reemplaza la necesidad del comando 'dir' de Jenkins, evitando el AccessDeniedException).
        docker.image('python:3.10-slim').inside("--user root -v ${WORKSPACE}:/app --workdir /app") {
            
            echo 'Iniciando pruebas Python...'
            
            // El comando sh se ejecuta directamente en /app (el working directory)
            sh 'python task_manager.py' 
        }
    }
    
    // Etapa 3: Reporte
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
    }
}