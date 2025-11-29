node('') { 
    stage('Declarative: Checkout SCM') {
        checkout scm
    }

    stage('Test') {
        echo 'Ejecutando pruebas...'
        
        // --- CAMBIO CRUCIAL: Mapeamos el volumen al directorio de trabajo del contenedor ---
        // El directorio de trabajo por defecto del contenedor es el mismo que el del host: ${WORKSPACE}
        docker.image('python:3.10-slim').inside("-v ${WORKSPACE}:${WORKSPACE}") { 
            
            // Ya estamos en el directorio de trabajo del contenedor, no necesitamos 'dir'
            echo 'Código descargado correctamente del repositorio.'
            // Ejecutar la aplicación (está en la raíz del workspace)
            sh 'python task_manager.py'
        }
    }
    
    stage('Reporte') {
        echo 'Generando reporte...'
    }
}