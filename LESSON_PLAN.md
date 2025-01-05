# Lesson Plan

Below is a **concise, “Pareto principle”–oriented lesson plan** focused on the Certified Kubernetes Administrator (CKA) exam. The idea is to cover **the most critical 20% of concepts** (i.e., those most likely to yield 80% of exam success) while still providing enough context and hands-on practice. The relative weightings provided (in parentheses) guide where to spend the most time.

---

## 1. Troubleshooting (30%)

### 1.1 Conceptual Foundations

- **Importance of Observability**
    - Role of logs (cluster, node, application logs)
    - Monitoring strategies (metrics, dashboards)
- **Troubleshooting Mindset**
    - Systematic approach (check logs, events, resource statuses)
    - Common failures (PodCrashLoopBackOff, NodeNotReady, DNS misconfigurations, networking issues)

### 1.2 Hands-On Practice Objectives

1. **Inspect Logs**
    - Use `kubectl logs` to retrieve container logs.
    - Practice filtering logs (e.g., `kubectl logs mypod --tail=20`).
2. **Check Pod & Node Status**
    - Use `kubectl describe pod`, `kubectl describe node`, and `kubectl get events`.
    - Identify misconfigurations or resource constraints (e.g., insufficient CPU/memory).
3. **Network Troubleshooting**
    - Verify Pod connectivity using `kubectl exec` to ping other Pods or Services.
    - Investigate Service/Ingress misconfiguration or DNS issues (`dig`, `nslookup`).
4. **Application Failure Diagnosis**
    - Induce a failure scenario (e.g., incorrect image, missing ConfigMap) and resolve it.
    - Practice analyzing error messages in logs and events.
5. **Cluster Component Failure**
    - Check `kubelet` status on nodes (`systemctl status kubelet`).
    - Understand how to investigate `etcd`, `kube-apiserver`, `kube-controller-manager`, and `kube-scheduler` logs (if needed).

---

## 2. Cluster Architecture, Installation & Configuration (25%)

### 2.1 Conceptual Foundations

- **Core Components**
    - etcd, API Server, Controller Manager, Scheduler, Kubelet, Kube-Proxy
- **High Availability & RBAC**
    - Multiple master nodes, etcd redundancy
    - Role-Based Access Control basics (Roles, ClusterRoles, RoleBindings, ClusterRoleBindings)

### 2.2 Hands-On Practice Objectives

1. **Basic Cluster Installation with kubeadm**
    - Initialize cluster with `kubeadm init` and join worker nodes with `kubeadm join`.
    - Inspect generated manifest files in `/etc/kubernetes/manifests/`.
2. **RBAC Configuration**
    - Create a Role and RoleBinding for a namespace.
    - Confirm restricted user’s privileges using a test user context.
3. **Cluster Upgrades**
    - Use `kubeadm upgrade plan` and `kubeadm upgrade apply` to simulate an upgrade process.
    - Verify the cluster is fully functional post-upgrade.
4. **etcd Backup & Restore**
    - Snapshot etcd with `etcdctl snapshot save`.
    - Restore etcd from snapshot and verify cluster state is correct.

---

## 3. Services & Networking (20%)

### 3.1 Conceptual Foundations

- **Networking Models**
    - Pod-to-Pod communication (CNI plugins: Calico, Flannel, etc.)
    - Node-to-Pod and external connectivity
- **Service Types**
    - ClusterIP, NodePort, LoadBalancer, ExternalName (basic awareness)
- **Ingress & DNS**
    - The role of Ingress controllers (Nginx, HAProxy, Traefik)
    - CoreDNS configuration

### 3.2 Hands-On Practice Objectives

1. **Configure Basic Services**
    - Deploy a simple application (e.g., Nginx) with a Service (ClusterIP).
    - Expose the application externally using a NodePort Service.
2. **Deploy an Ingress**
    - Install an Ingress controller (e.g., Nginx).
    - Create an Ingress resource routing traffic to multiple Services.
3. **Validate Networking**
    - Confirm Pod-to-Pod communication with `kubectl exec`.
    - Use commands like `curl`, `dig` inside Pods to test DNS resolution.
4. **CoreDNS Testing**
    - Update a CoreDNS ConfigMap to add a custom domain.
    - Validate resolution of custom domain from inside a Pod.

---

## 4. Workloads & Scheduling (15%)

### 4.1 Conceptual Foundations

- **Controller Primitives**
    - Deployments, ReplicaSets, DaemonSets, StatefulSets (basic awareness)
    - Rolling updates vs. rollbacks
- **Application Configuration**
    - Using ConfigMaps and Secrets to decouple config from images
    - Resource requests/limits and scheduling implications
- **Autoscaling & Self-Healing**
    - Horizontal Pod Autoscaler (HPA) basics
    - Liveness & Readiness probes

### 4.2 Hands-On Practice Objectives

1. **Deploy & Update an Application**
    - Create a Deployment with multiple replicas.
    - Perform a rolling update and rollback (`kubectl rollout history`, `kubectl rollout undo`).
2. **Use ConfigMaps & Secrets**
    - Store environment variables in a ConfigMap.
    - Store sensitive info (e.g., database password) in a Secret.
    - Mount them into a running container.
3. **Resource Requests & Limits**
    - Assign CPU and memory requests/limits in a Pod spec.
    - Observe scheduling behavior when resources are constrained.
4. **Basic Autoscaling**
    - Deploy the Kubernetes Metrics Server (if not present).
    - Configure a Horizontal Pod Autoscaler (`kubectl autoscale`).

---

## 5. Storage (10%)

### 5.1 Conceptual Foundations

- **Persistent Volumes & Persistent Volume Claims**
    - Volume modes, access modes, reclaim policies
    - StorageClasses for dynamic provisioning
- **Application Configuration with Persistent Storage**
    - Relationship between PVC and Pod usage

### 5.2 Hands-On Practice Objectives

1. **Set Up StorageClass & PVC**
    - Create a StorageClass (if cluster supports dynamic provisioning).
    - Create a PersistentVolumeClaim and verify PVC binding to a PersistentVolume.
2. **Mounting Persistent Storage in a Pod**
    - Deploy a simple stateful application (e.g., MySQL or a file-based app) that uses a PVC.
    - Observe data persistence after Pod restarts.
3. **Reclaim Policy Testing**
    - Set reclaim policy to Retain, Delete, or Recycle and observe the effect after a PVC is released.

---

# Putting It All Together

Below is a suggested **study/workflow** to optimize your preparation:

1. **Day 1: Quick Setup & Architecture**
    - Build a small cluster using `kubeadm` (practice the commands).
    - Review **Cluster Architecture** (etcd, API Server) and minimal **RBAC** tasks.
2. **Day 2: Workloads & Networking**
    - Create a simple Deployment with a Service.
    - Add an **Ingress** resource.
    - Introduce **ConfigMaps** and **Secrets**.
    - Practice scaling (HPA), rolling updates, and rollbacks.
3. **Day 3: Troubleshooting Deep Dive**
    - Intentionally break the cluster (wrong image, misconfigured Ingress, out-of-resources Pods).
    - Practice `kubectl logs`, `kubectl describe`, events, etc.
    - Investigate node conditions (e.g., mark node as unschedulable and fix it).
4. **Day 4: Storage & Final Review**
    - Deploy a stateful application with a PVC/StorageClass.
    - Experiment with reclaim policies.
    - Perform an **etcd backup and restore** as final cluster administration practice.
    - Summarize key commands, ensure understanding of high-level concepts.

---

## Final Tips
- **Focus on Troubleshooting & Installation**: These carry the heaviest exam weight and also reinforce fundamental Kubernetes knowledge.
- **Hands-On is Key**: Spin up a cluster (in the cloud or using local tools like Minikube/kind) and break/fix it.
- **Memorize Key Commands**: Know your `kubectl` commands, logs, and main configuration files by heart.
- **Time Management**: The CKA exam is time-bound and tasks are scenario-based. Speed at troubleshooting and writing YAML manifests is crucial.

By adhering to this minimal yet powerful lesson plan, you’ll cover the **vital 20%** of Kubernetes concepts and tasks that will drive the **majority of your success** on the CKA exam. Good luck!

