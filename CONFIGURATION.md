# Configuration

## Contexts

To view any currently configured Kubernetes contexts: `kubectl config get-contexts`.

To switch to another context: `kubectl config use-context <context-name>`.

For example, if you have `minikube` installed: `kubectl config use-context minikube`.

If you want to remove any existing contexts altogether:
1. `kubectl config delete-context <context-name>`.
2. `kubectl config delete-cluster <cluster-name>`.
3. `kubectl config unset users.<user-name>`.

To view (concise) details about the current context: `kubectl config view --minify`.

You'll see something like this:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority: C:\Users\<USER_PROFILE>\.minikube\ca.crt
    extensions:
    - extension:
        last-update: Fri, 14 Oct 2022 06:56:13 PDT
        provider: minikube.sigs.k8s.io
        version: v1.27.1
      name: cluster_info
    server: https://127.0.0.1:54217
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Fri, 14 Oct 2022 06:56:13 PDT
        provider: minikube.sigs.k8s.io
        version: v1.27.1
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: C:\Users\<USER_PROFILE>\.minikube\profiles\minikube\client.crt
    client-key: C:\Users\<USER_PROFILE>\.minikube\profiles\minikube\client.key
```

Mine turned out to be something I configured years ago and haven't seen since, so I tried running `minikube start` to rebuild the environment.

But I also actually encountered an error about expired certificates:
```shell
error execution phase certs/apiserver-kubelet-client: [certs] certificate apiserver-kubelet-client not signed by CA certificate ca: x509: certificate has expired or is not yet valid: current time 2025-01-09T19:57:14Z is after 2023-10-14T13:55:58Z
```

So I ended up removing the old cluster and creating a new one:
1. `minikube stop`.
2. `minikube delete`.
3. `minikube start`.
