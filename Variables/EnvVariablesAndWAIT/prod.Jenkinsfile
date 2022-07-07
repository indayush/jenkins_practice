pipeline {
    agent any

    environment{
        def sLocalString = "My Local String"
    }

    stages{
        stage("Demo"){
            steps{
                echo "Local String = ${sLocalString}"
                sleep(10)
                echo "Environmental String <BUILD ID> = ${env.BUILD_ID}"
                echo "Environmental String <BUILD NUMBER> = ${env.BUILD_NUMBER}"
                echo "Environmental String <JENKINS URL> = ${env.JENKINS_URL}"
            }
        }
    }
}