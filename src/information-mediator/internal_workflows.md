## 8. Internal Workflows

### 8.1 Service onboarding workflow
1. An administrator authenticates to the IM administrative interface.
2. A Member is created or selected.
3. An Application is registered.
4. Service metadata and the interface contract are published.
5. Access policy is configured.
6. The service becomes discoverable to authorized participants.
7. An audit record is generated.

### 8.2 Synchronous service invocation workflow
1. A consumer application sends a request to the mediation gateway.
2. The IM authenticates the sender and evaluates policy.
3. The IM resolves the destination using registered metadata.
4. The IM forwards the request to the provider endpoint.
5. The provider returns a response.
6. The IM returns the response to the consumer.
7. The IM records transaction and operational metadata.

### 8.3 Event publication and delivery workflow
1. A Publisher emits an event to a Room.
2. The IM validates publisher authorization and event-schema conformance.
3. The IM persists event metadata required for delivery handling.
4. The IM identifies active Subscribers.
5. The IM attempts delivery to each eligible Subscriber.
6. Failed retriable deliveries are scheduled for retry.
7. Final delivery outcomes are logged and exposed to monitoring.

### 8.4 Federation workflow
1. A federation arrangement is established.
2. Relevant metadata is imported, synchronized, or resolved on demand.
3. Policy is evaluated for inter-domain exchange.
4. A request or event is routed across federated boundaries.
5. Correlation and audit metadata are preserved end-to-end.
6. The outcome is logged according to policy.

### 8.5 Administrative change workflow
1. An administrator authenticates.
2. The requested change is authorized.
3. Configuration, policy, or trust metadata is updated.
4. Resulting metadata is versioned or otherwise recorded.
5. The change becomes effective according to the relevant propagation model.
6. An audit record is stored.
