## 9. Testing

### 9.1 Verification principle

Every REQUIRED requirement in this specification SHALL be mapped to at least one
verification method.

### 9.2 Verification methods

Verification MAY include one or more of the following:

- black-box API testing for externally observable behavior;
- schema validation testing for API and event contracts;
- workflow testing for end-to-end mediation scenarios;
- operational observation for health, metrics, and trace outputs; and
- audit inspection for administrative, trust, and retention behavior.

### 9.3 Minimum compliance mapping

At minimum, conformance verification SHALL cover:

- `fr#req-1` to `fr#req-5`: API mediation behavior;
- `fr#req-7` to `fr#req-9`: administrative and audit behavior;
- `fr#req-10` to `fr#req-12`: discovery and metadata behavior;
- `fr#req-13` to `fr#req-18`: event publication, routing, delivery, and retry behavior;
- `fr#req-19` to `fr#req-21`: log generation and retrieval behavior;
- `fr#req-22` to `fr#req-24`: observability behavior;
- `fr#req-25` and `fr#req-27`: federation behavior where applicable; and
- `cfr#req-1` to `cfr#req-6`: IM-specific cross-functional obligations.

### 9.4 Mock and reference implementation guidance

A mock implementation, emulator, or conformance test harness SHOULD be provided
to support interoperability testing, automated compliance checks, and
procurement-time validation.
