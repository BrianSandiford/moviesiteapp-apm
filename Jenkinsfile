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
            app.push("${env.GIT_COMMIT}")
            app.push("latest")
            } 
                echo "Trying to Push Docker Build to DockerHub"
       
    }
    stage("Deploy") {
            environment { 
                GIT_AUTH = credentials('git-pass-credentials-ID') 
            
            //steps {
                sh('''
                    rm -R -f moviesiteapp-helmcharts
                    git clone https://$GIT_AUTH_USR:$GIT_AUTH_PSW@github.com/BrianSandiford/moviesiteapp-helmcharts.git
                ''')
            dir("moviesiteapp-helmcharts"){
             //sh('echo \$BUILD_NUMBER > example-\$BUILD_NUMBER.md')
             sh "chmod +x changeTag.sh"
             sh "./changeTag.sh ${env.GIT_COMMIT}"
             sh "git add ."
             sh " git commit -am '[Jenkins CI] Add build file ${env.GIT_COMMIT}.' "
             sh " git remote show origin"
             sh "git push -u origin master"
            }
            //}
        } 
    }
}
