## 1. Title & Description

### 1.1 Purpose
The Information Mediator (IM) Building Block provides the secure, standardized, auditable, and interoperable communication layer through which GovStack Building Blocks, service applications, and other authorized digital service systems exchange data and functionality. It enables mediated service access, service discovery, event distribution, and traceability without requiring tightly coupled point-to-point integrations.

### 1.2 Scope
This specification defines the minimum technical capabilities, requirements, data structures, workflows, and verification expectations for a GovStack-compliant Information Mediator implementation. It covers:

- synchronous request-response mediation;
- asynchronous event publication and delivery;
- service and metadata discovery;
- trust, routing, and access-policy administration;
- transaction logging and auditability; and
- operational monitoring and observability.

### 1.3 Role in the GovStack ecosystem
The Information Mediator is a foundational Building Block in the GovStack ecosystem. It is strongly recommended for communication across network boundaries between Building Blocks and digital service systems. An IM deployment MAY operate in centralized, semi-decentralized, or federated topologies, provided that the interoperability, security, and compliance obligations defined in this specification are preserved.

### 1.4 System architecture scope
At system-architecture level, the Information Mediator functions as the interoperability backbone between service consumers and service providers. It enables mediated access to services, policy enforcement, trusted routing, asynchronous delivery patterns, and end-to-end traceability across organizational and technical boundaries.

### 1.5 Component architecture scope
At component-architecture level, an IM implementation MAY consist of one or more logical components, including:

- Security Server or Mediation Gateway;
- Directory Service;
- Event Distribution Service;
- Administrative Interface;
- Logging and Audit Service;
- Monitoring and Observability Service; and
- Federation Management Service.

A conformant implementation MAY realize these capabilities as a single deployable unit or as several cooperating components or microservices.

### 1.6 Out of scope
This specification does not define:

- the internal business logic of participating Building Blocks or service applications;
- a mandatory vendor, product, programming language, or hosting model;
- country-specific legal or regulatory compliance rules; or
- domain-specific business semantics beyond the minimum data structures and interface obligations required for interoperability.

Use of this specification does not by itself establish compliance with legal or regulatory frameworks such as data protection, digital identity, digital signature, or cross-border data-sharing regimes.

### 1.7 Relationship to GovStack Common Terminology
Terms defined in GovStack Common Terminology SHALL apply throughout this specification unless they are explicitly defined here as Information-Mediator-specific terms.
