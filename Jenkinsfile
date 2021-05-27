node {
    
    def app

    stage('Clone repository') {

        /* Cloning the Repository to our Workspace */

        checkout scm
    }

    stage('Build image') {

        /* This builds the actual image */

        app = docker.build("briansandiford/moviesiteapp_x86")
      
    }

    stage('Push image') {
        
        /* 
			You would need to first register with DockerHub before you can push images to your account
		*/
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
            app.push("${env.BUILD_TAG}")
            app.push("latest")
            } 
                echo "Trying to Push Docker Build to DockerHub"
       
    }
    stage("Deploy") {
            //environment { 
            withCredentials([usernameColonPassword(credentialsId: 'git-pass-credentials-ID', variable: 'USERPASS')]) {
            //GIT_AUTH = credentials('git-pass-credentials-ID') 
            
            //steps {
            sh('''
                rm -R -f moviesiteapp-helmcharts
                git clone https://$USERPASS@github.com/BrianSandiford/moviesiteapp-helmcharts.git
                ''')
                }
            //}
            dir("moviesiteapp-helmcharts"){
             sh('echo \$BUILD_NUMBER > example-\$.mdBUILD_NUMBER')
             sh "chmod +x changeTag.sh"
             sh "./changeTag.sh $BUILD_TAG"
             sh "git add ."
             sh " git commit -am '[Jenkins CI] Add build file $BUILD_TAG.' "
             sh " git remote show origin"
             sh "git push -u origin master"
            
            //}
        } 
    }
}
