Installed Plugins - 
    
    - Bitbucket
        - (git-indayush-password) credential in AMI
        - https://plugins.jenkins.io/bitbucket/
        - https://stackoverflow.com/questions/41455854/clone-from-bitbucket-private-repository-using-jenkins-pipeline-as-code        
    
    
    - Amazon Web Services SDK :: All
    - S3 Publisher
    - Pipeline: AWS Steps
        - (indayush-new) credential in AMI (Access Key & Secret Access Key)
        - https://stackoverflow.com/questions/68923918/jenkins-error-in-build-invalid-parameter-bucket-did-you-mean-entries
        - https://www.youtube.com/watch?v=EK0jjBCqz1A


    - Master Slave Setup
        - Create credentials in "SSH Username with private key" mode
        - Set the Host Key Verification Strategy = "Non verifying Verification Strategy"
        - Use Private IP for Instance
        - Specify label for addressing the Node

    - AWS CodeDeploy
        - Post Build Steps to CodeDeploy

    - Role Based Authorization Strategy
        - Create User/Groups according to reqs and assign permissions

    - build user vars
        - Get Current logged in User Name



For Slave EC2s Setup -
(No Plugins required)
- https://www.youtube.com/watch?v=B2YKzvNw_tE&t=1128s 
