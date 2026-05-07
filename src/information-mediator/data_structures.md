## 7. Data Structures

### 7.1 Data-modeling rules

All externally exchanged text SHALL use UTF-8 encoding. All timestamps SHALL use
ISO 8601 in UTC unless a narrower exception is explicitly specified. JSON SHALL
be the default data representation for APIs unless another format is explicitly
required. Published schemas SHALL define validation rules and extension rules.

### 7.2 Core resource model

The core entities of the Information Mediator are:

- Member;
- Application;
- Service;
- Service Endpoint;
- Access Policy;
- Room;
- Event Type;
- Subscription;
- Transaction Log Entry; and
- Delivery Outcome.

### 7.3 Entity definitions

#### 7.3.1 Member

Minimum fields:
- `member_class`: string
- `member_code`: string
- `display_name`: string
- `status`: enum
- `signing_key_ref`: string
- `certificate_ref`: string
- `created_at`: datetime
- `updated_at`: datetime

#### 7.3.2 Application
Minimum fields:
- `application_id`: string
- `member_id`: string
- `display_name`: string
- `connection_type`: enum
- `base_url`: uri
- `certificate_ref`: string
- `status`: enum
- `created_at`: datetime
- `updated_at`: datetime

#### 7.3.3 Service
Minimum fields:
- `service_id`: string
- `application_id`: string
- `name`: string
- `version`: string
- `openapi_url`: uri
- `endpoint_url`: uri
- `access_policy_ref`: string
- `status`: enum
- `created_at`: datetime
- `updated_at`: datetime

#### 7.3.4 Room
Minimum fields:
- `room_id`: string
- `owner_member_id`: string
- `name`: string
- `description`: string
- `status`: enum
- `created_at`: datetime
- `updated_at`: datetime

#### 7.3.5 Event Type
Minimum fields:
- `event_type_id`: string
- `room_id`: string
- `name`: string
- `schema_ref`: uri
- `version`: string
- `sensitivity_classification`: string
- `created_at`: datetime
- `updated_at`: datetime

#### 7.3.6 Subscription
Minimum fields:
- `subscription_id`: string
- `subscriber_application_id`: string
- `room_id`: string
- `event_type_id`: string
- `delivery_endpoint`: uri
- `retry_policy_ref`: string
- `status`: enum
- `created_at`: datetime
- `updated_at`: datetime

#### 7.3.7 Transaction Log Entry
Minimum fields:
- `log_id`: string
- `timestamp`: datetime
- `correlation_data`: string
- `transaction_type`: enum
- `source_ref`: string
- `target_ref`: string
- `action`: string
- `outcome`: enum
- `sensitivity_classification`: string
- `retention_class`: string

#### 7.3.8 Delivery Outcome
Minimum fields:
- `delivery_id`: string
- `correlation_data`: string
- `subscription_id`: string
- `attempt_number`: integer
- `attempted_at`: datetime
- `outcome`: enum
- `error_code`: string
- `error_message`: string
- `next_retry_at`: datetime

### 7.4 Validation and extensibility rules

1. Every schema SHALL define required and optional fields.
2. Unknown fields MAY be ignored according to tolerant-reader behavior where backward compatibility is intended.
3. Breaking schema changes SHALL require a major version increment.
4. Sensitive fields SHALL be classified and protected according to inherited GovStack cross-functional requirements.
