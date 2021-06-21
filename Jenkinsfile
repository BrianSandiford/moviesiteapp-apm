node {
    def app
    //environment {
    //    registry = "655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repoo"
    //}
   
    
        stage('Cloning Git') {
            
              checkout scm     
            
        }
        // Building Docker images
        stage('Building image') {
            
                script {
                  dockerImage = docker.build "655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repo:"+env.BUILD_NUMBER
        }
      
    }
      // Uploading Docker images into AWS ECR
    stage('Pushing to ECR') {
      
         script {
                sh 'aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 655895384845.dkr.ecr.us-east-2.amazonaws.com'
                sh 'docker push 655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repo:'+env.BUILD_NUMBER
         }
        
      }
    
    stage("Deploy") {  
        
            withCredentials([usernameColonPassword(credentialsId: 'git-pass-credentials-ID', variable: 'USERPASS')]) {
            
            
         
            sh('''
                rm -R -f moviesiteapp-helmcharts
                git clone https://$USERPASS@github.com/BrianSandiford/moviesiteapp-helmcharts.git
                ''')
                }
         
            dir("moviesiteapp-helmcharts"){
             sh('echo \$BUILD_NUMBER > example-\$.mdBUILD_NUMBER')
             sh "chmod +x changeTag.sh"
             sh "./changeTag.sh $BUILD_NUMBER"
             sh "git add ."
             sh " git commit -am '[Jenkins CI] Add build file $BUILD_NUMBER.' "
             sh " git remote show origin"
             sh "git push -u origin master"
            
          
        } 
    }  
}node {
    def app
    //environment {
    //    registry = "655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repoo"
    //}
   
    
        stage('Cloning Git') {
            
              checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/BrianSandiford/moviesiteapp.git']]])     
            
        }
        // Building Docker images
        stage('Building image') {
            
                script {
                  dockerImage = docker.build "655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repo:"+env.BUILD_NUMBER
        }
      
    }
      // Uploading Docker images into AWS ECR
    stage('Pushing to ECR') {
      
         script {
                sh 'aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 655895384845.dkr.ecr.us-east-2.amazonaws.com'
                sh 'docker push 655895384845.dkr.ecr.us-east-2.amazonaws.com/docker-private-repo:'+env.BUILD_NUMBER
         }
        
      }
    
    stage("Deploy") {  
        
            withCredentials([usernameColonPassword(credentialsId: 'git-pass-credentials-ID', variable: 'USERPASS')]) {
            
            
         
            sh('''
                rm -R -f moviesiteapp-helmcharts
                git clone https://$USERPASS@github.com/BrianSandiford/moviesiteapp-helmcharts.git
                ''')
                }
         
            dir("moviesiteapp-helmcharts"){
             sh('echo \$BUILD_NUMBER > example-\$.mdBUILD_NUMBER')
             sh "chmod +x changeTag.sh"
             sh "./changeTag.sh $BUILD_NUMBER"
             sh "git add ."
             sh " git commit -am '[Jenkins CI] Add build file $BUILD_NUMBER.' "
             sh " git remote show origin"
             sh "git push -u origin master"
            
          
        } 
    }  
}