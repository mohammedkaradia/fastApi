pipeline {
    agent any

    stages {
        stage('Build FastAPI Docker Image') {
            steps {
                script {
                    // Build FastAPI Docker image
                    docker.build('fastapi-image', './fastapi')
                }
            }
        }
        stage('Build MySQL Docker Image') {
            steps {
                script {
                    // Build MySQL Docker image
                    docker.build('mysql-image', './mysql')
                }
            }
        }
        stage('Run Docker Containers') {
            steps {
                script {
                    // Run MySQL container
                    docker.image('mysql-image').run('-p 3306:3306 --name mysql-container -d')

                    // Run FastAPI container
                    docker.image('fastapi-image').run('-p 8000:8000 --name fastapi-container --link mysql-container -d')
                }
            }
        }
    }
}
