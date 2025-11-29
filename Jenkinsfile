node('') { 
    // Etapa 1: Checkout del código
    stage('Checkout SCM') {
        echo 'Descargando código del repositorio...'
        checkout scm
    }

    // Etapa 2: Ejecución de Pruebas dentro del contenedor Docker
    stage('Test') {
        echo 'Ejecutando pruebas en contenedor Docker...'
        
        // Mantenemos la configuración robusta de Docker
        docker.image('python:3.10-slim').inside("--user root -v ${WORKSPACE}:/app --workdir /app") {
            
            // Establecemos PYTHONPATH para que Python sepa buscar módulos en la carpeta 'src'
            // Esto es crucial para la ejecución de proyectos estructurados.
            withEnv(['PYTHONPATH=/app/src']) {
                
                echo 'Iniciando la ejecución del script con PYTHONPATH configurado...'
                
                // 🚨 SOLUCIÓN FINAL: Ejecutamos el archivo usando su ruta absoluta confirmada: /app/src/task_manager.py
                sh 'python /app/cli_task_manager/src/main.py' 
            }
        }
    }
    
    // Etapa 3: Reporte
    stage('Reporte') {
        echo 'Generando reporte (simulado)...'
    }
}