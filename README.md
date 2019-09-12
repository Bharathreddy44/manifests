# Task

Developed a hello-world web application with user authentication using python flask web framework.

Application source code can be found in GitHub.

https://github.com/Bharathreddy44/manifests

Deployed the application using command “kubectl create -f manifests.yaml” or “kubectl apply -f manifests.yaml” (manifests.yaml file contains application resources like deployment, service, secrets configuration which is inside the GitHub repo).

Once the command is executed it deploys web application with three replicas create secrets and exposes the application with an external IP address.

The login credentials for the web application are defined in the secrets. Currently 
Username: lastline
Password: Bharat

The secrets are volume mounted to the running pods. While testing the application locally the login credentials are set to username: admin & password: password.

High Availability of an application completely depends on the high availability of cluster.

The application replicas are set to 3 & If a node goes down the replication controller ensures to bring up the pods in a different node.
