node('master') {
    // 1. Clonar el código primero
    stage('Declarative: Checkout SCM') {
        checkout scm
    }

    // 2. Usar un contenedor Docker para la etapa de prueba
    stage('Test') {
        echo 'Ejecutando pruebas...'
        
        // --- CAMBIO CRUCIAL: Uso de withDockerRegistry para inyectar la ruta ---
        // Se usa la variable WORKSPACE (disponible en el scope del nodo)
        // Se usa args para forzar el mapeo del volumen, que ahora sí se expandirá.
        docker.image('python:3.10-slim').inside("-v ${WORKSPACE}:/app") {
            // Entramos al directorio de la aplicación DENTRO del contenedor
            dir('/app') {
                echo 'Código descargado correctamente del repositorio.'
                // Ejecutar la aplicación (ahora está en /app)
                sh 'python task_manager.py'
            }
        }
    }
    
    // 3. Etapa de reporte
    stage('Reporte') {
        echo 'Generando reporte...'
        // Aquí irían pasos para generar reportes si existieran
    }
}