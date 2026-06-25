<!-- 此文件由程序自动生成，请勿手动修改 -->

# CNCF Projects

> 数据来源: [CNCF Landscape](https://landscape.cncf.io/)
> 更新时间: 2026-06-26

## 项目统计

| 状态 | 数量 |
|------|------|
| [Graduated](#graduated) | 36 |
| [Incubating](#incubating) | 36 |
| [Sandbox](#sandbox) | 153 |
| [Archived](#archived) | 27 |
| **总计** | **252** |

---

## Graduated (36)

### App Definition and Development (7)

#### Application Definition & Image Build

- **[Dapr](https://dapr.io)** — The Distributed Application Runtime (Dapr) provides APIs that simplify microservice architecture development and increases developer productivity. Whether your communication pattern is service-to-service invocation or pub/sub messaging, Dapr helps you write resilient and secured microservices. By letting Dapr’s sidecar take care of the complex challenges such as service discovery, message broker integration, encryption, observability, and secret management, developers can focus on business logic and keep their code simple.
- **[Helm](https://helm.sh/)**

#### Continuous Integration & Delivery

- **[Argo](https://argoproj.github.io/)** — Kubernetes-native tools to run workflows, manage clusters, and do GitOps right.
- **[Flux](https://fluxcd.io/)** — Flux is a tool for keeping Kubernetes clusters in sync with sources of configuration (like Git repositories and OCI artifacts), and automating updates to configuration when there is new code to deploy. Flux is built from the ground up to use Kubernetes' API extension system, and to integrate with Prometheus and other core components of the Kubernetes ecosystem. Flux supports multi-tenancy and support for syncing an arbitrary number of Git repositories, among other long-requested features.

#### Database

- **[TiKV](https://tikv.org)** — A distributed transactional key-value database. Based on the design of Google Spanner and HBase, but simpler to manage and without dependencies on any distributed filesystem
- **[Vitess](https://vitess.io/)** — MySQL-compatible, horizontally scalable, cloud-native database solution.

#### Streaming & Messaging

- **[CloudEvents](https://cloudevents.io/)** — Standardizing common eventing metadata and their location to help with event identification and routing.

### Observability and Analysis (4)

#### Observability

- **[Fluentd](https://www.fluentd.org/)**
- **[Jaeger](https://www.jaegertracing.io/)** — tracing-based observability for distributed systems
- **[OpenTelemetry](https://opentelemetry.io/)** — Enabling built-in observability for cloud-native systems.
- **[Prometheus](https://prometheus.io/)** — metrics-based monitoring and alerting

### Orchestration & Management (9)

#### Coordination & Service Discovery

- **[CoreDNS](https://coredns.io/)**
- **[etcd](https://etcd.io/)** — Etcd is a distributed, reliable key-value store for the most critical data of a distributed system. By using etcd, developers can ensure that their applications have access to up-to-date configuration data, even as they scale up or down, and can maintain consistency, fault tolerance and coordination across multiple instances of the application.

#### Scheduling & Orchestration

- **[Crossplane](https://crossplane.io/)** — Crossplane is the cloud native control plane framework that allows you to build control planes without needing to write code. Crossplane has a highly extensible backend that enables you to orchestrate applications and infrastructure no matter where they run and a highly configurable frontend that lets you define the declarative API it offers.
- **[KEDA](https://keda.sh/)**
- **[Knative](https://knative.dev)** — Knative is a developer-focused serverless application layer which is a great complement to the existing Kubernetes application constructs. Knative consists of three components: an HTTP-triggered autoscaling container runtime called “Knative Serving”, a CloudEvents-over-HTTP asynchronous routing layer called “Knative Eventing”, and a developer-focused function framework which leverages the Serving and Eventing components, called "Knative Functions".
- **[Kubernetes](https://kubernetes.io/)** — Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications

#### Service Mesh

- **[Istio](https://istio.io/)** — Simplify observability, traffic management, security, and policy with the Istio service mesh.
- **[Linkerd](https://linkerd.io/)** — Ultra light, ultra simple, ultra powerful. Linkerd adds security, observability, and reliability to Kubernetes, without the complexity.

#### Service Proxy

- **[Envoy](https://www.envoyproxy.io)**

### Provisioning (11)

#### Automation & Configuration

- **[KubeEdge](https://kubeedge.io/en/)** — KubeEdge is an open source system for extending native containerized application orchestration capabilities to hosts at Edge.It is built upon kubernetes and provides fundamental infrastructure support for network, application deployment and metadata synchronization between cloud and edge. Our goal is to make an open platform to enable Edge computing, extending native containerized application orchestration capabilities to hosts at Edge

#### Container Registry

- **[Dragonfly](https://d7y.io/)** — Delivers efficient, stable, and secure data distribution and acceleration powered by P2P technology, with an optional content‑addressable filesystem that accelerates OCI container launch.
- **[Harbor](https://goharbor.io/)** — Harbor is an open source registry that secures artifacts with policies and role-based access control,  ensures images are scanned and free from vulnerabilities, and signs images as trusted. Can be installed on any Kubernetes environment or on a system with Docker support.

#### Key Management

- **[SPIFFE](https://spiffe.io/)** — The Secure Production Identity Framework For Everyone (SPIFFE) Project defines a framework and set of standards for identifying and securing communications between application services. At its core, SPIFFE is:  A standard defining how services identify themselves to each other. These are called SPIFFE IDs and are implemented as Uniform Resource Identifiers (URIs).  A standard for encoding SPIFFE IDs in a cryptographically-verifiable document called a SPIFFE Verifiable Identity Document or SVIDs.  An API specification for issuing and/or retrieving SVIDs. This is the Workload API.  The SPIFFE Project has a reference implementation, the SPIRE (the SPIFFE Runtime Environment), that in addition to the above, it:  - Performs node and workload attestation.  - Implements a signing framework for securely issuing and renewing SVIDs.  - Provides an API for registering nodes and workloads, along with their designated SPIFFE IDs.  - Provides and manages the rotation of keys and certs for mutual authentication and encryption between workloads.  - Simplifies access from identified services to secret stores, databases, services meshes and cloud provider services.  - Interoperability and federation to SPIFFE compatible systems across heterogeneous environments and administrative trust boundaries  The SPIFFE Workload API can attest running software systems and issue SPIFFE IDs and SVIDs to them. This in turn allows two workloads to establish trust between each other, for example by establishing an mTLS connection or by signing and verifying a JWT token. Use of SPIFFE can also enable workloads to securely authenticate to a secret store, a database, or a cloud provider service.
- **[SPIRE](https://spiffe.io/spire/)** — SPIRE implements the SPIFFE standards to provide cryptographic service identity (e.g. X.509 certificates and JWTs) and identity federation to workloads, independent of where those workloads are running. SPIRE provides secure attestation of both the workload itself and the environment it is running within and uses that information against custom defined policy to determine the identity of the workload and issue the appropriate credentials

#### Security & Compliance

- **[cert-manager](https://cert-manager.io/)** — cert-manager is a powerful and extensible X.509 certificate controller for Kubernetes and OpenShift workloads. It will obtain certificates from a variety of Issuers, both popular public Issuers as well as private Issuers, and ensure the certificates are valid and up-to-date, and will attempt to renew certificates at a configured time before expiry.
- **[Falco](https://falco.org/)** — Falco is a cloud-native runtime security project that makes it easy to consume kernel events. Falco enriches these events with additional information from the Kubernetes platform and ecosystem as well as the rest of the cloud native stack. Falco can also be extended to other data sources through the use of plugins. Falco offers a rich set of security rules designed for Kubernetes, Linux, and cloud native environments. When a rule is violated in the system, Falco alerts users with details about the violation and severity.
- **[in-toto](https://in-toto.io)** — in-toto provides security for the software supply chain.  It can cryptographically track  and validate the build, version control, testing, deployment, dependency, etc. actions that happen as you make your software.  in-toto also can enforce policies over these actions, so that your supply chain is performed in the way that you describe.
- **[Kyverno](https://kyverno.io/)** — Pod security,Policy-as-code,Governance,Software supply chain
- **[Open Policy Agent (OPA)](https://www.openpolicyagent.org/)**
- **[The Update Framework (TUF)](https://theupdateframework.github.io/)** — TUF secures container registries, package repositories, etc. so that the system resists successful attacks and can recover securely.  TUF uses a combination of security mechanisms and tooling to provide a strong root of trust used by other security projects as well, such as Sigstore.  It is easy to integrate and simple to manage; try it for yourself

### Runtime (5)

#### Cloud Native Network

- **[Cilium](https://cilium.io/)** — Cilium is a networking, observability, and security platform based on eBPF. As a CNI, it provides a flat Layer 3 network, even across clusters. Cilium enforces network policies on L3-L7 using an identity based security model.  Cilium implements distributed load balancing between pods and to external services by replacing kube-proxy. It also has advanced functionality like ingress and egress gateway, bandwidth management, service mesh, and deep network and security observability through Hubble and Tetragon.

#### Cloud Native Storage

- **[CubeFS](https://cubefs.io/)** — CubeFS is a distributed file system supports data access protocols such as S3, POSIX, HDFS. It supports multiple copies and erasure code storage engines, and provides users with multiple features such as multi-tenancy, multi-AZ deployment, and cross-regional replication.
- **[Rook](https://rook.io/)** — Rook is an open source cloud-native storage orchestrator, providing the platform, framework, and support for Ceph storage to integrate with cloud-native environments natively.  Ceph is a distributed storage system that provides block, file, and object storage and is deployed in large-scale production clusters.  Rook automates deployment and management of Ceph to provide self-managing, self-scaling, and self-healing storage services. The Rook operator builds on Kubernetes resources to deploy, configure, provision, scale, upgrade, and monitor Ceph.  The storage cluster can be run hyper-converged beside your applications, in a cloud, or on bare metal. Rook provides a consistent storage platform anywhere Kubernetes runs.

#### Container Runtime

- **[containerd](https://containerd.io/)** — containerd is available as a Linux and Windows daemon. It manages the complete container lifecycle of its host system, from image transfer and storage to container execution and supervision to low-level storage to network attachments and beyond.
- **[CRI-O](https://cri-o.io/)** — CRI-O is a secure, performant, and stable Container Runtime Interface (CRI) implementation for the Kubelet to orchestrate Open Container Initiative (OCI) containers in production Kubernetes environments. CRI-O's scope is only targeted at Kubernetes, and thus can be performance optimized, rigorously tested and securely tuned for running containers, pods and images in Kubernetes clusters.

---

## Incubating (36)

### App Definition and Development (10)

#### Application Definition & Image Build

- **[Artifact Hub](https://artifacthub.io)**
- **[Backstage](https://backstage.io/)** — Backstage is an open platform for building developer portals, which unify all your infrastructure tooling, services, and documentation with a single, consistent UI.
- **[Buildpacks](https://buildpacks.io/)**
- **[KubeVela](https://kubevela.io)** — KubeVela is a modern software delivery platform that makes deploying and operating applications across today's hybrid, multi-cloud environments easier, faster and more reliable.
- **[KubeVirt](https://kubevirt.io/)**
- **[Microcks](https://microcks.io)** — Microcks is a tool for mocking and testing your APIs and microservices. It leverages API standards to provide a uniform and multi-protocol approach for simulating complex distributed environments and validating service components in isolation.
- **[Operator Framework](https://operatorframework.io/)**

#### Continuous Integration & Delivery

- **[OpenKruise](https://openkruise.io/)**

#### Streaming & Messaging

- **[NATS](https://nats.io/)** — NATS.io is a connective technology for distributed systems and is a perfect fit to connect devices, edge, cloud or hybrid deployments. True multi-tenancy makes NATS ideal for SaaS and self-healing and scaling technology allows for topology changes anytime with zero downtime.
- **[Strimzi](https://strimzi.io/)** — Event streaming with Apache Kafka by providing Kubernetes-native Kafka deployments

### Inference (1)

#### Framework

- **[KServe](https://kserve.github.io/website/)** — Standardized Distributed Generative and Predictive AI Inference Platform for Scalable, Multi-Framework Deployment on Kubernetes

### Observability and Analysis (6)

#### Chaos Engineering

- **[Chaos Mesh](https://chaos-mesh.org/)**
- **[Litmus](https://litmuschaos.io/)**

#### Continuous Optimization

- **[OpenCost](https://www.opencost.io/)** — OpenCost provides visibility into current and historical Kubernetes spend and resource allocation.

#### Feature Flagging

- **[OpenFeature](https://openfeature.dev/)** — Standardizing Feature Flagging for Everyone

#### Observability

- **[Cortex](https://cortexmetrics.io/)** — Horizontally scalable, highly available, multi-tenant, long term storage for Prometheus.
- **[Thanos](https://thanos.io/)** — global scale metrics-based monitoring and alerting

### Orchestration & Management (8)

#### API Gateway

- **[Emissary-Ingress](https://emissary-ingress.dev/)** — Emissary-Ingress is a k8s-native, Envoy-based API gateway. It is designed to allow teams to work in a more decentralized way than the traditional Ingress object. Emissary-Ingress can scan for its CRDs across all namespaces, so development teams can deploy new network routing rules along with the apps that use them, increasing velocity. Emissary-Ingress can be extended via API calls with authentication and rate limiting services. It is compatible with all the CNCF service meshes, and facilitates canary deployments when integrated with Argo Rollouts.

#### Remote Procedure Call

- **[gRPC](https://grpc.io)** — A high performance, open source universal RPC framework.

#### Scheduling & Orchestration

- **[Fluid](https://fluid-cloudnative.github.io/)** — Fluid is an orchestration platform for elastic data abstraction and acceleration in cloud native environment.
- **[Karmada](https://karmada.io/)** — Karmada (Kubernetes Armada) is a Kubernetes management system that enables you to run your cloud-native applications across multiple Kubernetes clusters and clouds, with no changes to your applications. By speaking Kubernetes-native APIs and providing advanced scheduling  capabilities, Karmada enables truly open, multi-cloud Kubernetes. Karmada aims to provide turnkey automation for multi-cluster application management in multi-cloud and hybrid cloud scenarios, with key  features such as centralized multi-cloud management, high availability, failure recovery, and traffic scheduling.
- **[Kubeflow](https://kubeflow.org)** — Kubeflow is the foundation of tools for AI Platforms on Kubernetes.
- **[Volcano](https://volcano.sh/)**
- **[wasmCloud](https://wasmcloud.com)**

#### Service Proxy

- **[Contour](https://projectcontour.io)**

### Platform (1)

#### Certified Kubernetes - Distribution

- **[Flatcar Container Linux](https://www.flatcar.org/)** — A community Linux distribution designed for container workloads, with high security and low maintenance

### Provisioning (7)

#### Automation & Configuration

- **[Cloud Custodian](https://cloudcustodian.io/)**
- **[metal3-io](https://metal3.io/)** — Provision bare metal hardware via k8s-native APIs, including integration with the Cluster API.
- **[OpenYurt](https://openyurt.io/)** — An open platform that extends upstream Kubernetes to Edge.

#### Security & Compliance

- **[Keycloak](https://www.keycloak.org/)** — Keycloak is an open-source identity and access management solution for modern applications and services,  built on top of industry security standard protocols.
- **[Kubescape](https://kubescape.io/)** — Kubescape is an open source security and compliance platform that scans clusters, Kubernetes manifest files (YAML files, and Helm charts), code repositories, container registries and images. It detects misconfigurations according to frameworks such as the NSA-CISA,  MITRE ATT&CK® and CIS, as well as software vulnerabilities, and calculates risk scores.
- **[Notary Project](https://notaryproject.dev/)**
- **[OpenFGA](https://openfga.dev)** — OpenFGA is a high performance and flexible authorization/permission system built for developers and inspired by Google Zanzibar

### Runtime (3)

#### Cloud Native Network

- **[Container Network Interface (CNI)](https://www.cni.dev/)**

#### Cloud Native Storage

- **[Longhorn](https://longhorn.io/)** — Cloud-native distributed storage for Kubernetes

#### Container Runtime

- **[Lima](https://github.com/lima-vm/lima)** — Linux virtual machines, typically on macOS, for running containerd

---

## Sandbox (153)

### App Definition and Development (31)

#### Application Definition & Image Build

- **[Carvel](https://carvel.dev)** — Carvel provides a set of reliable, single-purpose, composable tools that aid in your application building, configuration, and deployment to Kubernetes.
- **[Dalec](https://project-dalec.github.io/dalec/)** — Dalec provides a declarative format for building system packages and containers from those packages in a secure way for supply chain security.
- **[Devfile](https://devfile.io)**
- **[DevSpace](https://devspace.sh)**
- **[ko](https://ko.build/)**
- **[Konveyor](https://www.konveyor.io/)** — Konveyor is an open-source application modernization platform that helps organizations safely and predictably modernize applications to new technologies, with an initial focus on accelerating the adoption of legacy applications to Kubernetes.
- **[KUDO](https://kudo.dev/)**
- **[ModelPack](https://github.com/modelpack/model-spec)** — The project establishes open standards for packaging, distributing and running AI artifacts in the cloud-native environment.
- **[ORAS](https://oras.land/)** — Multi-language OCI Registry SDKs and CLI
- **[Podman Desktop](https://podman-desktop.io/)** — An open-source tool for developers to work with containers and Kubernetes with an intuitive and user-friendly interface to effortlessly build, manage, and deploy containers and Kubernetes — all from the desktop.
- **[Porter](https://porter.sh/)**
- **[Radius](https://radapp.io/)** — Radius is a cloud-native application platform that enables developers and the platform engineers that support them to collaborate on delivering and managing cloud-native applications that follow organizational best practices for cost, operations and security, by default.
- **[Score](https://score.dev/)** — Score is an open-source workload specification designed to simplify development for cloud-native developers.
- **[Serverless Workflow](https://serverlessworkflow.io)**
- **[Shipwright](https://shipwright.io)**
- **[Stacker](https://stackerbuild.io)** — Stacker is a tool for building OCI images and related artifacts such as SBOMs natively via a declarative yaml format.
- **[Telepresence](https://www.telepresence.io/)** — Telepresence is a local-to-remote kubernetes debugging tool that creates a two-way proxy from your laptop to the cluster. You can access cluster resources as if they were local and intercept traffic to one or more services to develop in an integrated environment without the need for a container build-push-deploy loop.
- **[Visual Studio Code Kubernetes Tools](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools)** — The extension for developers building applications to run in Kubernetes clusters and for DevOps staff troubleshooting Kubernetes applications.
- **[xRegistry](https://xregistry.io)** — The xRegistry project defines an abstract model for managing metadata about resources and provides a REST-based interface to discover, create, modify and delete those resources.

#### Continuous Integration & Delivery

- **[Kube-burner](https://kube-burner.github.io/kube-burner/)**
- **[OpenChoreo](https://openchoreo.dev)** — A developer platform for Kubernetes that delivers higher-level abstractions with a Backstage-powered portal, CI/CD, GitOps, and built-in observability.
- **[OpenGitOps](https://opengitops.dev/)**
- **[PipeCD](https://pipecd.dev/)** — GitOps style continuous delivery platform that provides consistent deployment and operations experience for any applications
- **[werf](https://werf.io/)** — werf is a solution for implementing efficient and consistent software delivery to Kubernetes. It covers the entire CI/CD lifecycle and all related artifacts, glues commonly used tools (Git, Docker/Buildah, Helm, K8s) and facilitates best practices.

#### Database

- **[CloudNativePG](https://www.cloudnative-pg.io/)** — CloudNativePG is a comprehensive platform designed to seamlessly manage PostgreSQL databases within Kubernetes environments, covering the entire operational lifecycle from initial deployment to ongoing maintenance
- **[OpenEverest](https://openeverest.io/)** — The open-source platform for automated database provisioning and management. It supports multiple database technologies and can be hosted on any Kubernetes infrastructure, in the cloud or on-premises.
- **[openGemini](https://www.opengemini.org)** — openGemini is an open source distributed time series DBMS with high concurrency, high performance, and high scalability, focusing on the storage and analysis of massive observability data.
- **[SchemaHero](https://schemahero.io)**

#### Streaming & Messaging

- **[Apicurio Registry](https://www.apicur.io)** — Apicurio Registry is a runtime server system that stores a specific set of artifacts as files.
- **[Drasi](https://drasi.io)** — A data change processing platform to simplify change-driven systems that need to detect, evaluate, and react to data changes quickly and efficiently at scale.
- **[Tremor](https://www.tremor.rs/)**

### Inference (2)

#### Framework

- **[KAITO](https://kaito-project.netlify.app/)** — Kubernetes AI Toolchain Operator (KAITO) simplifies LLM inference, tuning, and RAG workloads on Kubernetes.
- **[llm-d](https://llm-d.ai/)** — llm-d is a Kubernetes-native, high-performance distributed LLM inference framework built on vLLM and the Kubernetes Gateway API Inference Extension, providing intelligent inference scheduling, prefix-cache-aware routing, prefill/decode disaggregation, hierarchical KV offloading, and traffic- and hardware-aware autoscaling across NVIDIA, AMD, Intel, and Google TPU accelerators.

### Observability and Analysis (12)

#### Chaos Engineering

- **[Chaosblade](https://chaosblade.io/)**
- **[Krkn](https://krkn-chaos.github.io/krkn)** — Chaos testing tool for Kubernetes to identify bottlenecks and improve resilience and performance under failure conditions.

#### Observability

- **[Headlamp](https://headlamp.dev)** — Extensible open source multi-cluster Kubernetes user interface
- **[HolmesGPT](https://holmesgpt.dev)** — HolmesGPT is an AI agent that automates cloud-native troubleshooting, bridging knowledge gaps by investigating alerts, executing runbooks, and correlating observability data in cloud-native platforms.
- **[Inspektor Gadget](https://inspektor-gadget.io/)** — Open source eBPF debugging and data collection tool for Kubernetes and Linux
- **[K8sGPT](https://www.k8sgpt.ai)**
- **[Kepler](https://sustainable-computing.io/)** — Kepler (Kubernetes-based Efficient Power Level Exporter) uses eBPF to probe energy related system stats and exports as Prometheus metrics.
- **[Kuberhealthy](https://github.com/kuberhealthy/kuberhealthy)**
- **[Logging Operator (Kube Logging)](https://kube-logging.dev/)**
- **[Perses](https://perses.dev)** — Perses is a dashboard tool to visualize observability data from Prometheus/Thanos/Jaeger.
- **[Pixie](https://px.dev/)** — Open source Kubernetes observability for developers
- **[Trickster](https://trickstercache.org)**

### Orchestration & Management (35)

#### API Gateway

- **[Easegress](https://megaease.com/easegress)**
- **[Higress](https://higress.io)**
- **[Kgateway](https://kgateway.dev/)** — An Envoy-powered, Kubernetes-native API Gateway that integrates Kubernetes Gateway API with a control plane for API connectivity in any cloud environment.
- **[Kuadrant](https://kuadrant.io)** — Kuadrant combines Gateway API and Istio-based gateway controllers to enhance application connectivity. It enables platform engineers  and application developers to easily connect, secure, and protect their services and infrastructure across multiple clusters  with policies for TLS, DNS, application authentication & authorization, and rate limiting.

#### Coordination & Service Discovery

- **[k8gb](https://www.k8gb.io)** — K8GB is a powerful tool for managing global Kubernetes deployments and provides features such as load balancing, failover, and intelligent routing. K8GB works by creating a set of custom resource definitions (CRDs) in the Kubernetes cluster, which define the global traffic routing policies. These policies are used by K8GB to configure the DNS servers to route traffic to the appropriate cluster or region.
- **[Oxia](https://oxia-db.github.io)** — Oxia is a scalable metadata store and coordination system

#### Remote Procedure Call

- **[Connect RPC](https://connectrpc.com/)** — Connect is a family of libraries for building browser and gRPC-compatible HTTP APIs.

#### Scheduling & Orchestration

- **[Agones](https://agones.dev/site/)** — Agones is a library for hosting, running, and scaling dedicated game servers on Kubernetes.
- **[Armada](https://armadaproject.io/)**
- **[Capsule](https://capsule.clastix.io)** — Capsule implements a multi-tenant and policy-based environment in your Kubernetes cluster. It is designed as a micro-services-based ecosystem with the minimalist approach, leveraging only on upstream Kubernetes.
- **[Clusternet](https://clusternet.io)** — [CNCF Sandbox Project] Managing your Kubernetes clusters (including public, private, edge, etc.) as easily as visiting the Internet
- **[Clusterpedia](https://clusterpedia.io)** — Clusterpedia is used for complex resources search across multiple clusters, support simultaneous search of a single kind of resource  or multiple kinds of resources existing in multiple clusters.
- **[CoHDI](https://github.com/CoHDI)** — CoHDI (Composable Hardware in Disaggregated Infrastructure) enables dynamic device scaling across next-generation architectures. As a community-driven, standards-based open ecosystem, CoHDI focuses on expanding cloud-native frameworks built on disaggregate infrastructure. Our core objective is to bridge the gap between Kubernetes and underlying hardware by actively collaborating with upstream projects to increase cloud native composability, specifically Dynamic Resource Allocation (DRA), Autoscaler, and Scheduling. By integrating these cloud-native capabilities, CoHDI empowers data center and infrastructure operators to maximize cost efficiency, achieve high availability, and drive sustainability through a seamlessly disaggregated computing system.
- **[Cozystack](https://cozystack.io)** — Cozystack is a free PaaS platform and framework for building private clouds and providing users/customers with managed Kubernetes,  KubeVirt-based VMs, databases as a service, NATS, message brokers, etc. with GPU support in VMs and Kubernetes clusters.
- **[Eraser](https://eraser-dev.github.io/eraser/)** — Eraser uses vulnerability data to remove non-running images from all Kubernetes nodes in a cluster.
- **[hami](https://project-hami.github.io/HAMi/)** — Heterogeneous AI Computing Virtualization Middleware
- **[k0s](https://k0sproject.io/)**
- **[KAI Scheduler](https://github.com/kai-scheduler/KAI-Scheduler)** — KAI Scheduler is a robust, efficient, and scalable Kubernetes scheduler that optimizes GPU resource allocation for AI workloads in large-scale clusters.
- **[kcp](https://kcp.io)**
- **[Koordinator](https://koordinator.sh)** — QoS based scheduling system for hybrid orchestration workloads on Kubernetes, bringing workloads the best layout and status.
- **[kube-rs](https://kube.rs)** — kube-rs is the core Rust ecosystem for building applications against Kubernetes
- **[KubeFleet](https://kubefleet.dev/)** — A multi-cluster solution that enables users to effectively manage their applications running in multiple Kubernetes clusters.
- **[KubeSlice](https://kubeslice.io)**
- **[KubeStellar](https://kubestellar.io)**
- **[Kured](https://kured.dev)** — Kured (KUbernetes REboot Daemon) is a Kubernetes daemonset that performs safe automatic node reboots when the need to do so is indicated by the package management system of the underlying OS
- **[Open Cluster Management](https://open-cluster-management.io/)**
- **[OpenFunction](https://openfunction.dev)** — Users can use OpenFunction in several different ways including building functions or applications only, running sync or async serverless functions or applications, building and then running serverless functions or applications, building and then running serverless wasm applications(In progress).  In all use cases, users can utilize Dapr to communicate with various backend services (BaaS).
- **[Serverless Devs](https://www.serverless-devs.com/)**

#### Service Mesh

- **[Aeraki Mesh](https://www.aeraki.net/)** — Aeraki Mesh allows you to manage any layer-7 traffic in a service mesh
- **[Kmesh](https://kmesh.net)** — Kmesh is a high-performance and low overhead service mesh data plane based on eBPF and programmable kernel. Kmesh brings traffic management, security and monitoring to service communication without needing application code changes. It is natively sidecarless, zero intrusion and without adding any resource cost to application container.
- **[Kuma](https://kuma.io)** — Kuma is a service mesh that combines the extensibility and performance of Envoy proxy with great UX and a powerful, yet flexible set of policies. It was built from the ground up to support Kubernetes, Docker, and VM environments seamlessly in a single deployment.
- **[Sermant](https://sermant.io/)** — Sermant a proxyless service mesh solution based on Javaagent.

#### Service Proxy

- **[BFE](https://www.bfe-networks.net)** — Open-source layer 7 load balancer derived from proprietary Baidu FrontEnd
- **[LoxiLB](https://loxilb.io)** — eBPF based cloud-native load-balancer. Powering Kubernetes|Edge|5G|IoT|XaaS Apps.
- **[MetalLB](https://metallb.universe.tf)**

### Platform (2)

#### Certified Kubernetes - Distribution

- **[k3s](https://k3s.io)** — Lightweight Kubernetes

#### Certified Kubernetes - Installer

- **[KubeClipper](https://www.kubeclipper.io/)** — Manage kubernetes in the most light and convenient way.

### Provisioning (40)

#### Automation & Configuration

- **[Akri](https://docs.akri.sh)**
- **[Atlantis](https://www.runatlantis.io/)** — Terraform Pull Request Automation for Teams
- **[Cadence Workflow](https://cadenceworkflow.io/)** — Cadence is a distributed, scalable, durable, and highly available fault-oblivious stateful code platform.
- **[CDK for Kubernetes (CDK8s)](https://cdk8s.io/)** — CDK8s lets you define Kubernetes apps and components using familiar programming languages and object-oriented APIs.
- **[kagent](https://kagent.dev/)** — Kagent is an open source programming framework designed for DevOps and platform engineers to run AI agents in Kubernetes
- **[Kairos](https://kairos.io)** — Transform any Linux system into a secure, customizable, and easily managed platform for edge computing with or without Kubernetes.
- **[KCL](https://kcl-lang.io/)** — A constraint-based record & functional language mainly used in configuration and policy scenarios.
- **[KitOps](https://kitops.org/)** — An open standard for packaging, managing, and deploying ML models and artifacts across different systems
- **[kpt](https://kpt.dev)**
- **[Kubean](https://kubean-io.github.io/kubean/)** — Product ready cluster lifecycle management toolchains based on kubespray and other cluster LCM engine.
- **[KusionStack](https://kusionstack.io/)**
- **[Meshery](https://meshery.io)** — As a self-service engineering platform, Meshery enables collaborative design and operation of cloud and  cloud native infrastructure.
- **[NMstate](https://nmstate.io/)** — NMstate is a library with an accompanying command line tool that manages host networking settings in a declarative manner. When used in the Kubernetes environment it allows for declarative node network configuration through the Kubernetes API.
- **[OpenTofu](https://opentofu.org/)** — OpenTofu is an open source infrastructure as code tool that enables users to safely and predictably provision and manage cloud and on-prem infrastructure. It's a community-driven fork of Terraform that maintains backward compatibility while offering enhanced features, stability.
- **[Runme Notebooks](https://runme.dev/)** — A toolchain that turns Markdown into interactive, cloud-native, runnable Notebook experiences for DevOps.
- **[Tinkerbell](https://tinkerbell.org/)**

#### Container Registry

- **[Distribution](https://github.com/distribution/distribution)**
- **[zot](https://zotregistry.dev/)** — Zot is an OCI-native container registry for distributing container images and OCI artifacts.

#### Key Management

- **[Athenz](https://www.athenz.io)** — Open source platform for X.509 certificate based service authentication and fine grained access control in dynamic infrastructures

#### Security & Compliance

- **[Bank-Vaults](https://bank-vaults.dev/)** — Bank-Vaults is a Vault swiss-army knife: a K8s operator, Go client with automatic token renewal, automatic configuration, multiple unseal options and more. A CLI tool to init, unseal and configure Vault (auth methods, secret engines). Direct secret injection into Pods.
- **[bpfman](https://bpfman.io/)** — An eBPF Manager for Linux and Kubernetes
- **[Cartography](https://cartography.dev)** — Cartography is a Python tool that consolidates infrastructure assets and the relationships between them in an intuitive graph view.
- **[Cedar](https://cedarpolicy.com)** — Cedar is an open source authorization policy language that enables developers to express fine-grained permissions as easy-to-understand policies enforced in their applications, and decouple access control from application logic. Cedar is designed to be ergonomic, fast, safe, and analyzable using automated reasoning. Cedar's simple and intuitive syntax supports common authorization use-cases with readable policies, naturally expressing concepts from role-based, attribute-based, and relation-based access control models. Cedar's policy structure enables authorization requests to be decided quickly. Its policy validator uses optional typing to help policy writers avoid mistakes, but not get in their way. Cedar's design has been finely balanced to allow for a sound, complete, and decidable logical encoding, which enables precise automated analysis of Cedar policies, e.g., to ensure that policy refactoring preserves existing permissions. Cedar's language specification has been formally verified using a theorem prover to satisfy key security properties like "deny trumps allow," and its implementation in Rust undergoes rigorous differential random testing against its formal specification. By combining mathematical rigor with developer-friendly design, Cedar offers a practical approach to secure, maintainable authorization for modern applications.
- **[Confidential Containers](https://confidentialcontainers.org/)** — Confidential Containers is an open source community working to enable cloud native  confidential computing by leveraging Trusted Execution Environments to protect  containers and data.
- **[ContainerSSH](https://containerssh.io)** — ContainerSSH launches a new container for each SSH connection in Kubernetes, Podman or Docker. The user is transparently dropped in the container and the container is removed when the user disconnects. Authentication and container configuration are dynamic using webhooks, no system users required.
- **[Copa](https://project-copacetic.github.io/copacetic/)** — CLI tool for directly patching container image vulnerabilities
- **[Dex](https://dexidp.io/)**
- **[external-secrets](https://external-secrets.io/)** — External Secrets Operator is a Kubernetes operator that integrates external secret management systems like AWS Secrets Manager, HashiCorp Vault, Google Secrets Manager, Azure Key Vault, IBM Cloud Secrets Manager, Akeyless, CyberArk Conjur and many more. The operator reads information from external APIs and automatically injects the values into a Kubernetes Secret. From there the secret can be consumed by a pod or used by other Kubernetes resources.
- **[Keylime](https://keylime.dev/)** — Bootstrap & Maintain Trust on the Edge / Cloud and IoT.
- **[KubeArmor](https://kubearmor.io/)** — Runtime protection for Kubernetes & other cloud Workloads. Kubearmor provides a observability and policy enforcement system to restrict any unwanted, malicious behaviour of cloud-native workloads at runtime.
- **[Kubewarden](https://www.kubewarden.io)** — Kubewarden is a Policy Engine powered by WebAssembly policies. Its policies can be written in CEL, Rego (OPA & Gatekeeper flavours), Rust, Go, YAML, and others. Kubewarden simplifies Policy-As-Code by allowing policy authors and consumers to use their preferred tooling and stack, develop and test policies out of cluster.
- **[OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/)** — A generic reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers.
- **[Open Policy Containers](https://openpolicycontainers.com)** — A docker-inspired CLI for building, tagging, pushing, pulling, and signing OPA policies to and from OCI-compliant registries.
- **[OSCAL-COMPASS](https://github.com/oscal-compass/community)** — The OSCAL COMPASS project is set of tools that enable the creation, validation, and governance of documentation artifacts for compliance needs. It leverages NIST's OSCAL (Open Security Controls Assessment Language) as a standard data format for interchange between tools and people, and provides an opinionated approach to OSCAL SDK and adoption by policy engines.
- **[Paralus](https://www.paralus.io/)** — Paralus is a free, open source tool that enables controlled, audited access to Kubernetes infrastructure and Zero trust Kubernetes with zero friction.
- **[Parsec](https://parsec.community/)**
- **[Ratify](https://ratify.dev/)** — A verification engine on Kubernetes which enables verification of artifact security metadata and admits for deployment only those that comply with policies you create.
- **[SlimToolkit](https://slimtoolkit.org/)** — Inspect, Optimize and Debug Your Containers
- **[SOPS](https://github.com/getsops)** — sops is an editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, age, and PGP.
- **[Tokenetes](https://tokenetes.io/)** — Tokenetes implements Transaction Tokens (TraTs) for microservices call chains.  It's a Kubernetes-native framework providing immutable identity and context in  service-to-service communication to prevent attacks like software supply chain  or privileged user compromise.

### Runtime (26)

#### Cloud Native Network

- **[Antrea](https://antrea.io/)** — Kubernetes networking based on Open vSwitch
- **[Kube-OVN](https://kube-ovn.io)**
- **[kube-vip](https://kube-vip.io)** — Kubernetes Virtual IP and Load-Balancer for both control plane and Kubernetes services
- **[Network Service Mesh](https://networkservicemesh.io/)**
- **[OVN-Kubernetes](https://ovn-kubernetes.io/)** — OVN-Kubernetes is a robust Kubernetes Networking platform, built from the ground up by leveraging Open vSwitch (OVS) as the data plane, and Open Virtual Network (OVN) as the SDN Controller.
- **[Spiderpool](https://spidernet-io.github.io/spiderpool/)** — Spiderpool is the underlay and RDMA network solution of the Kubernetes, for bare metal, VM and public cloud
- **[Submariner](https://submariner.io)** — Submariner enables direct networking between Pods and Services in different Kubernetes clusters, either on-premises or in the cloud.

#### Cloud Native Storage

- **[Carina](https://carina-io.github.io/)**
- **[HwameiStor](https://hwameistor.io/)** — Hwameistor is an HA local storage system for cloud-native stateful workloads
- **[K8up](https://www.k8up.io/)**
- **[Kanister](https://kanister.io)**
- **[OpenEBS](https://www.openebs.io/)**
- **[Piraeus Datastore](https://piraeus.io/)**
- **[Velero](https://velero.io)**
- **[Vineyard](https://v6d.io)** — Vineyard (v6d) is an in-memory immutable data manager.

#### Container Runtime

- **[bootc](https://bootc-dev.github.io)** — The bootc provides transactional, in-place operating system images and updates using OCI/Docker container images. This project applies the Docker container layering model to bootable host systems, using standard OCI/Docker containers as a transport and delivery format for base operating system updates.
- **[composefs](https://github.com/containers/composefs)** — A project that combines Linux kernel features to provide read-only mountable filesystem trees stacking on top of an underlying "lower" Linux filesystem, particularly useful for mounting container images.
- **[Hyperlight](https://github.com/hyperlight-dev/hyperlight)** — A lightweight, secure container runtime solution designed for modern cloud-native workloads
- **[Inclavare Containers](https://github.com/inclavare-containers/)**
- **[Interlink](https://interlink-project.dev)** — InterLink aims to provide an abstraction for the execution of a Kubernetes pod on any remote resource capable of managing a Container execution lifecycle thanks to the Virtual Kubelet interface. It allows you to extend your cloud environment anywhere by running Kubernetes workloads on various infrastructures, creating a seamless cloud-native experience across diverse environments.
- **[Kuasar](https://kuasar.io/)** — A multi-sandbox container runtime that provides cloud-native, all-scenario multiple sandbox container solutions.
- **[Podman Container Tools](https://podman.io/)** — A set of tools providing full management of container lifecycle, including Podman, Buildah, and Skopeo,  which manage containers and images without requiring a daemon or root privileges.
- **[urunc](https://urunc.io/)** — A CRI-compatible runtime for running unikernels and application kernels as containers.  urunc bridges the gap between unikernels and containerized environments, enabling seamless  integration with cloud-native architectures while maintaining OCI compatibility.
- **[Virtual Kubelet](https://virtual-kubelet.io/)**
- **[WasmEdge Runtime](https://wasmedge.org/)** — WasmEdge provides a high-performance, lightweight, secure, and extensible WebAssembly runtime for cloud-native applications. It is an OCI compliant container that is integrated into Docker, containerd, crun and many Kubernetes projects.  Compared with traditional Linux container apps, WasmEdge apps are more secure, more portable, cold-start 100x faster and only take 1/10 of the space.
- **[youki](https://youki-dev.github.io/youki/)**

### Serverless (2)

#### Framework

- **[KubeElasti](https://kubeelasti.dev)** — Auto scale-to-zero pods when idle and scale up pods when traffic arrives, without losing any requests. KubeElasti uses a smart proxy that queues incoming requests while scaling up targets, ensuring no request loss. It works with existing Kubernetes services and deployments without requiring code changes.

#### Installable Platform

- **[SlimFaaS](https://github.com/SlimPlanet/SlimFaas)** — The slimest and simplest Function As A Service

### Wasm (3)

#### Application Frameworks

- **[Spin](https://spinframework.dev)** — Spin is a framework for building and deploying serverless applications in WebAssembly.

#### Orchestration & Management

- **[container2wasm](https://github.com/container2wasm/container2wasm)** — A tool to run containers on Wasm-enabled environments.
- **[SpinKube](https://www.spinkube.dev/)** — Open source platform for efficiently running (containerless) Spin-based WebAssembly (Wasm) applications on Kubernetes.

---

## Archived (27)

### App Definition and Development (6)

#### Application Definition & Image Build

- **[Krator](https://docs.rs/crate/krator/latest)**
- **[Nocalhost](https://nocalhost.dev)**
- **[sealer](http://sealer.cool/)**

#### Continuous Integration & Delivery

- **[Brigade](https://brigade.sh/)**
- **[Keptn](https://www.keptn.sh)** — Cloud-native application life-cycle orchestration. Keptn automates your SLO-driven multi-stage delivery and operations & remediation of your applications.

#### Streaming & Messaging

- **[Pravega](https://cncf.pravega.io)**

### Observability and Analysis (4)

#### Observability

- **[Fonio](https://ingraind.org/)**
- **[OpenMetrics](https://openmetrics.io/)**
- **[OpenTracing](https://opentracing.io/)**
- **[Skooner](https://skooner.io/)**

### Orchestration & Management (6)

#### Coordination & Service Discovery

- **[Xline](https://www.xline.cloud)** — Xline is a high-performance geo-distributed metadata management system, which is compatible with the ETCD interface.

#### Service Mesh

- **[Merbridge](https://merbridge.io/)** — Use eBPF to speed up your Service Mesh like crossing an Einstein-Rosen Bridge.
- **[Open Service Mesh](https://openservicemesh.io/)**
- **[Service Mesh Interface (SMI)](https://smi-spec.io)**
- **[Service Mesh Performance](https://smp-spec.io/)**

#### Service Proxy

- **[OpenELB](https://openelb.github.io)** — In cloud-based Kubernetes clusters, Services are usually exposed by using load balancers provided by cloud vendors. However, cloud-based load balancers are unavailable in bare-metal environments. OpenELB allows users to create LoadBalancer Services in bare-metal, edge, and virtualization environments for external access, and provides the same user experience as cloud-based load balancers.

### Provisioning (6)

#### Automation & Configuration

- **[DevStream](https://www.devstream.io/)**
- **[KubeDL](https://kubedl.io)**
- **[SuperEdge](https://superedge.io/)** — An edge-native container management system for edge computing

#### Key Management

- **[Teller](https://tlr.dev)**

#### Security & Compliance

- **[Curiefense](https://www.curiefense.io/)**
- **[Hexa](https://hexaorchestration.org/)**

### Runtime (5)

#### Cloud Native Network

- **[CNI-Genie](https://cnigenie.netlify.app)**
- **[FabEdge](https://github.com/FabEdge/)**

#### Cloud Native Storage

- **[Curve](http://www.opencurve.io/)** — Curve is a distributed storage system designed and developed independently by NetEase,  featured with high performance, high availability, high reliability and well expansibility,  and it can serve as the basis for storage systems designed for different scenario.

#### Container Runtime

- **[Krustlet](https://krustlet.dev)**
- **[rkt](https://github.com/rkt/rkt)**

---

Data source: [CNCF Landscape](https://landscape.cncf.io/)
Updated: 2026-06-26