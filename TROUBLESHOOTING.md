# Troubleshooting

## ImagePullBackOff

Tried to deploy a Redis guestbook based on a code example (see: `examples/README.md`).

Cmd: `kubectl port-forward service/guestbook-service 8080:3000`.

Result: `error: unable to forward port because pod is not running. Current status=Pending`.

Cmd: `kubectl get pods`.

Result:
```shell
NAME                                    READY   STATUS             RESTARTS      AGE
guestbook-deployment-54b9954bd4-b4jfw   0/1     ImagePullBackOff   0             14m
```

Cmd: `kubectl describe pod guestbook-deployment-54b9954bd4-b4jfw`.

```shell
Name:         guestbook-deployment-54b9954bd4-b4jfw
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Fri, 10 Jan 2025 10:01:31 -0800
Labels:       app=guestbook
              pod-template-hash=54b9954bd4
Annotations:  <none>
Status:       Pending
IP:           172.17.0.6
IPs:
  IP:           172.17.0.6
Controlled By:  ReplicaSet/guestbook-deployment-54b9954bd4
Containers:
  guestbook:
    Container ID:   
    Image:          prakhar1989/guestbook
    Image ID:       
    Port:           3000/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:
      REDIS_HOST:  redis-service
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2rnw9 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-2rnw9:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                   From               Message
  ----     ------     ----                  ----               -------
  Normal   Scheduled  7m4s                  default-scheduler  Successfully assigned default/guestbook-deployment-54b9954bd4-b4jfw to minikube
  Normal   Pulling    5m37s (x4 over 7m3s)  kubelet            Pulling image "prakhar1989/guestbook"
  Warning  Failed     5m36s (x4 over 7m2s)  kubelet            Failed to pull image "prakhar1989/guestbook": rpc error: code = Unknown desc = Error response from daemon: pull access denied for prakhar1989/guestbook, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
  Warning  Failed     5m36s (x4 over 7m2s)  kubelet            Error: ErrImagePull
  Warning  Failed     5m12s (x6 over 7m2s)  kubelet            Error: ImagePullBackOff
  Normal   BackOff    117s (x20 over 7m2s)  kubelet            Back-off pulling image "prakhar1989/guestbook"
```

## CrashLoopBackOff

Cmd: `kubectl port-forward service/guestbook-service 8050:3000`.

Result:
```shell
Forwarding from 127.0.0.1:8050 -> 3000
Forwarding from [::1]:8050 -> 3000
Handling connection for 8050
E0110 10:15:10.859690   41116 portforward.go:406] an error occurred forwarding 8050 -> 3000: error forwarding port 3000 to pod 9386a6c187c3858793ea1288723af17167f971c1ff10757093cf720a5edc216d, uid : exit status 1: 2025/01/10 18:15:10 socat[701018] E connect(5, AF=2 127.0.0.1:3000, 16): Connection refused
E0110 10:15:10.860209   41116 portforward.go:234] lost connection to pod
Handling connection for 8050
E0110 10:15:10.861240   41116 portforward.go:346] error creating error stream for port 8050 -> 3000: EOF
```

Cmd: `kubectl get pods`.

Result:
```shell
NAME                                    READY   STATUS             RESTARTS      AGE
guestbook-deployment-6f46475f98-w7jh7   0/1     CrashLoopBackOff   3 (39s ago)   93s
```

Cmd: `kubectl describe pod guestbook-deployment-6f46475f98-w7jh7`.

Result:
```shell
Name:         guestbook-deployment-6f46475f98-w7jh7
Namespace:    default
Priority:     0
Node:         minikube/192.168.49.2
Start Time:   Fri, 10 Jan 2025 10:14:22 -0800
Labels:       app=guestbook
              pod-template-hash=6f46475f98
Annotations:  <none>
Status:       Running
IP:           172.17.0.7
IPs:
  IP:           172.17.0.7
Controlled By:  ReplicaSet/guestbook-deployment-6f46475f98
Containers:
  guestbook:
    Container ID:   docker://c95da696463049e5dcebe919ae68c392f68e369e265b774760cf4f676529f73b
    Image:          google/guestbook-python-redis
    Image ID:       docker-pullable://google/guestbook-python-redis@sha256:650e0f7833a1614eaa94b8ff5dbeeed3461e7ff66060e4f0e945da091b70be5a
    Port:           3000/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       CrashLoopBackOff
    Last State:     Terminated
      Reason:       Error
      Exit Code:    139
      Started:      Fri, 10 Jan 2025 10:17:38 -0800
      Finished:     Fri, 10 Jan 2025 10:17:38 -0800
    Ready:          False
    Restart Count:  5
    Environment:
      REDIS_HOST:  redis-service
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4bkhx (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-4bkhx:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                    From               Message
  ----     ------     ----                   ----               -------
  Normal   Scheduled  3m57s                  default-scheduler  Successfully assigned default/guestbook-deployment-6f46475f98-w7jh7 to minikube
  Normal   Pulled     3m48s                  kubelet            Successfully pulled image "google/guestbook-python-redis" in 8.279774679s
  Normal   Pulled     3m46s                  kubelet            Successfully pulled image "google/guestbook-python-redis" in 1.258867235s
  Normal   Pulled     3m29s                  kubelet            Successfully pulled image "google/guestbook-python-redis" in 1.186579032s
  Normal   Created    3m3s (x4 over 3m47s)   kubelet            Created container guestbook
  Normal   Started    3m3s (x4 over 3m47s)   kubelet            Started container guestbook
  Normal   Pulled     3m3s                   kubelet            Successfully pulled image "google/guestbook-python-redis" in 1.192609675s
  Warning  BackOff    2m26s (x8 over 3m45s)  kubelet            Back-off restarting failed container
  Normal   Pulling    2m13s (x5 over 3m56s)  kubelet            Pulling image "google/guestbook-python-redis"
```

Checking the logs: `kubectl logs guestbook-deployment-6f46475f98-w7jh7`.

Result was empty. Perhaps the container immediately crashed before it could log any of the traceback.

### Building a Custom Guestbook Image

#### Troubleshooting Failure to Connect with Redis

I defined a custom image with some simple Python code.

However, it failed to connect to the Redis service when initially tested.

Result (from Docker logs): `redis.exceptions.ConnectionError: Error -2 connecting to redis-service:6379. Name or service not known.`.

Cmd: `kubectl get pods`.

Result:
```shell
NAME                                    READY   STATUS             RESTARTS         AGE
guestbook-deployment-9d99f8fb7-rfkrn    0/1     ImagePullBackOff   0                3m34s
redis-deployment-57cc4b4ddd-cbkpk       1/1     Running            0                49m
```

It appears to be running.

Cmd: `kubectl get svc`.

Result:
```shell
NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
guestbook-service   NodePort    10.100.102.3    <none>        3000:30001/TCP   52m
kubernetes          ClusterIP   10.96.0.1       <none>        443/TCP          22h
nginx-service       NodePort    10.99.83.162    <none>        80:30080/TCP     22h
redis-service       ClusterIP   10.101.77.229   <none>        6379/TCP         52m
```

Checking the namespace to make sure they're in the same one:

Cmd: `kubectl get deployments -n default`.

Result:
```shell
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
guestbook-deployment   0/1     1            0           58m
nginx-deployment       2/2     2            2           22h
redis-deployment       1/1     1            1           58m
```

And then it occurs to me... I ran the container using regular old Docker, so it is not going to be in the same namespace.

Time to test them from the same Docker network:

Cmd: `docker network create guestbook-net`.

Cmd: `docker run -d --name redis-service --network guestbook-net redis:6.2`.

Cmd: `docker run -d --name guestbook --network guestbook-net -p 3000:3000 -e REDIS_HOST=redis-service my-guestbook:latest`.

It turned out that there was host name mismatch.

Fixed it, and proceeded to try again via Kubernetes.

...

imagePullPolicy: IfNotPresent

## Minikube

Cmd: `minikube status`.

Result:
```shell
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
docker-env: in-use
```
