# Examples

## Server

A simple Nginx server.

Steps:
1. `kubectl apply -f examples/server/nginx-deployment.yaml`.
2. `kubectl apply -f examples/server/nginx-service.yaml`.

Go to: `http://<node-ip>:30080`.

`node-ip` can be found by running `minikube ip`.

Note: If that doesn't work, try this: `minikube service nginx-service`. It will display the URL with the correct `port` in the terminal.

Or, alternatively: `kubectl port-forward service/nginx-service 8080:80`. Then you can access it from `http://localhost:8080`.
