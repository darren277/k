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

## Cron Job

An example cron job that runs every 5 minutes.

It merely displays the time to the console but could easily be adapted for any number of purposes, such as a data backup mechanism.

Steps:
1. `kubectl apply -f examples/cronjob/backup-cronjob.yaml`.

Also:
* Check the status: `kubectl get cronjob`.
* Check jobs: `kubectl get jobs`.
* Get list of pods: `kubectl get pods`.
* Check the logs (get the hash value from the list of pods): `kubectl logs -f db-backup-cron-<hash>`.
* To delete: `kubectl delete cronjob db-backup-cron`.

## Redis (Guest Book)

A simple guest book application that uses Redis as a database.

Steps:
1. `docker build -t my-guestbook examples/redis/src`.
2. ~~`minikube image load my-guestbook:latest`~~. Didn't work. Instead, trying the following:
   1. (Windows) `& minikube -p minikube docker-env --shell powershell | Invoke-Expression`.
   2. `docker build -t my-guestbook examples/redis/src`.
3. `kubectl apply -f examples/redis/redis-deployment.yaml`.
4. `kubectl apply -f examples/redis/guestbook-deployment.yaml`.

Go to: `http://<node-ip>:30001`.

Or: `kubectl port-forward service/guestbook-service 8082:3000`.
