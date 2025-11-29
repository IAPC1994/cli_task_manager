node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        // --- CAMBIO CRUCIAL: Agregar --user root al argumento 'inside' ---
        // Esto le da permisos de escritura al proceso de Jenkins dentro del volumen montado.
        docker.image('python:3.10-slim').inside("--user root -v ${WORKSPACE}:/app") {
            
            // Cambiamos el directorio de trabajo DENTRO del contenedor a /app
            // El comando 'dir' ahora funcionará gracias a los permisos de root.
            dir('/app') {
                echo 'Iniciando pruebas Python...'
                
                // Ejecutamos el script
                sh 'python task_manager.py' 
            }
        }
    }
    
    // Etapa 3: Reporte
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
    }
}