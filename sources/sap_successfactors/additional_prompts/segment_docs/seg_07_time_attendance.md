# SAP SuccessFactors API Documentation - Time & Attendance

## Segment Overview
- **Segment**: 7 - Time & Attendance
- **Files Processed**: 7
- **Entities Documented**: 13
- **Endpoints Documented**: 9

## API Summary

| Source File | API Type | Entities | GET Endpoints |
|-------------|----------|----------|---------------|
| ClockInClockOutIntegration.json | OData v4 | 2 | 2 |
| ClockInClockOutExternal.json | OData v4 | 2 | 1 |
| ClockInClockOut.json | REST | 4 | 0 (POST only) |
| ClockInClockOutTimeEventsRestAPI.json | REST | 5 | 0 (PATCH only) |
| Balances.json | REST | 9 | 3 |
| TimeOffEvents.json | REST | 1 | 1 |
| AvailableTimeTypes.json | REST | 2 | 1 |

---

## OData v4 APIs

---

### ClockInClockOutGroups
**Source File**: ClockInClockOutIntegration.json
**API Type**: OData v4
**Base Path**: `/odatav4/timemanagement/timeeventprocessing/ClockInClockOutIntegration.svc/v1`

#### Description
Clock In Clock Out Groups configuration entity for time event type management.

#### Schema
| Field | Type | Required | Key | Filterable | Description |
|-------|------|----------|-----|------------|-------------|
| code | string | Yes | Yes | Yes | Unique code of the Clock In Clock Out Group |
| createdAt | date-time | Yes | No | No | Date and time at which the Clock In Clock Out Group was created |
| createdBy | string | Yes | No | No | Assignment ID of the user who created the Clock In Clock Out Group |
| lastChangedAt | date-time | Yes | No | No | Date and time at which the Clock In Clock Out Group was last modified |
| lastChangedBy | string | Yes | No | No | Assignment ID of the user who last modified the Clock In Clock Out Group |
| name | string | No | No | No | Name of the Clock In Clock Out Group |
| timeEventTypeNav | array[TimeEventTypes] | No | No | No | Time Event Types associated with the Clock In Clock Out Group |

#### Primary Keys
- `code` (string)

#### Ingestion Type
- **Type**: `cdc`
- **Cursor Field**: `lastChangedAt`
- **Rationale**: Entity has `lastChangedAt` timestamp field for tracking modifications with a unique `code` key field.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ClockInClockOutGroups | Read all Clock In Clock Out Groups configured | `$skip`, `$top`, `@odata.count` |
| GET | /ClockInClockOutGroups('{code}') | Read a Clock In Clock Out Group using its code | N/A (single entity) |

#### Query Parameters
- `$filter` - Filter items by property values
- `$orderby` - Order items (code, createdAt)
- `$select` - Select properties (code, createdAt, createdBy, lastChangedAt, lastChangedBy, name)
- `$expand` - Expand related entities (timeEventTypeNav)
- `$count` - Include count of items

---

### TimeEventTypes
**Source File**: ClockInClockOutIntegration.json
**API Type**: OData v4
**Base Path**: `/odatav4/timemanagement/timeeventprocessing/ClockInClockOutIntegration.svc/v1`

#### Description
Time Event Types definition entity, nested within ClockInClockOutGroups.

#### Schema
| Field | Type | Required | Key | Description |
|-------|------|----------|-----|-------------|
| code | string | Yes | Yes | Unique code of the Time Event Type |
| active | boolean | Yes | No | Specifies whether a Time Event Type is active or inactive |
| event | TimeEventTypeEnum (START\|STOP) | Yes | No | Specifies whether it is a START or a STOP Time Event Type |
| name | string | No | No | Name of the Time Event Type |
| description | string | No | No | Description of the Time Event Type |

#### Primary Keys
- `code` (string)

#### Ingestion Type
- **Type**: `snapshot`
- **Rationale**: No timestamp fields for tracking changes. Accessible only through expansion on ClockInClockOutGroups.

#### Endpoints
This entity is accessed via `$expand=timeEventTypeNav` on ClockInClockOutGroups endpoints.

---

### clockinclockout.timeevents
**Source File**: ClockInClockOutExternal.json
**API Type**: OData v4
**Base Path**: `/odatav4/timemanagement/timeeventprocessing/clockinclockout/v1`

#### Description
Time events export entity for external customers. Provides time event details with filters. Maximum of 1000 records per request.

#### Schema
| Field | Type | Required | Key | Filterable | Description |
|-------|------|----------|-----|------------|-------------|
| externalId | string | No | Yes | Yes | Unique alphanumeric id for the Time Event |
| approvalStatusCode | string | No | No | Yes | Approval Status of the Time Event |
| comments | string | No | No | Yes | Additional information for creation of Manual Time Event |
| createdAt | date-time | No | No | Yes | Created Date |
| createdBy | string | No | No | Yes | Created User |
| creationSourceCode | string | No | No | Yes | Source of created Time Event |
| lastChangedAt | date-time | No | No | Yes | Last Modified Date |
| lastChangedBy | string | No | No | Yes | Last Modified User |
| pairingStatusCode | string | No | No | Yes | Pairing Status of the Time Event |
| reasonForManualTimeEventCode | string | No | No | Yes | Reason for creation of Manual Time Event |
| terminalId | string | No | No | Yes | Terminal id of the Time Event |
| timeEventTypeCode | string | No | No | Yes | Unique alphanumeric code for the Time Event Type |
| timeTypeCode | string | No | No | Yes | Time Type Code |
| timeZoneOffset | string | No | No | Yes | Time Zone Offset |
| timestampUTC | date-time | No | No | Yes | Timestamp at which Time Event was created |
| validationMessages | array[Message] | No | No | Yes | Validation messages |
| validationStatusCode | string | No | No | Yes | Validation Status of the Time Event |
| workAssignmentId | string | No | No | Yes | Assignment id of the user |

#### Primary Keys
- `externalId` (string)

#### Ingestion Type
- **Type**: `append`
- **Cursor Field**: `lastChangedAt` or `timestampUTC`
- **Rationale**: Time events are log/event records. Once created, they represent immutable records of clock in/out actions. Append mode is appropriate for event logging.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /timeevents | Export Time Events information for external customers | `$skip`, `$top`, `@odata.count` |

#### Query Parameters
- `$filter` - Filter items by property values
- `$orderby` - Order items by multiple fields
- `$select` - Select properties to return
- `$count` - Include count of items

---

### clockinclockout.Message
**Source File**: ClockInClockOutExternal.json
**API Type**: OData v4
**Base Path**: `/odatav4/timemanagement/timeeventprocessing/clockinclockout/v1`

#### Description
Validation message structure for time events.

#### Schema
| Field | Type | Required | Key | Description |
|-------|------|----------|-----|-------------|
| additionalTargets | array[string] | No | No | Additional target fields |
| code | string | No | No | Message code |
| longtextUrl | string | No | No | URL for long text description |
| message | string | No | No | Message text |
| numericSeverity | integer (uint8) | No | No | Numeric severity level |
| target | string | No | No | Target field |
| transition | boolean | No | No | Transition indicator |

#### Primary Keys
- None (nested structure)

#### Ingestion Type
- **Type**: N/A
- **Rationale**: This is a nested complex type within timeevents, not a standalone entity.

---

## REST APIs

---

### TimeEvents (Create)
**Source File**: ClockInClockOut.json
**API Type**: REST
**Base Path**: `/rest/timemanagement/timeeventprocessing/v1`

#### Description
REST API for creating time events to track employee time punches with external time tracking services.

#### Schema (Request)
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| id | string | Yes | 36 | Unique ID of the item in the API call, used to map the response later to request items |
| assignmentId | string | Yes | 100 | Assignment ID of the employee whose time event is recorded |
| typeCode | string | Yes | 20 | The code of the time event type that was used for the time event |
| timestamp | string | Yes | - | The date and time of the time event in ISO format (yyyy-MM-dd'T'HH:mm:ssZ) |
| terminalId | string | No | 30 | Identifier of the terminal at which the time event was recorded |
| timeTypeCode | string | No | 128 | The external code of a time type available in Time Tracking |

#### Primary Keys
- `id` (string) - request mapping identifier
- `UUID` (string) - system-generated identifier in response

#### Ingestion Type
- **Type**: N/A (write-only API)
- **Rationale**: This is a POST-only endpoint for creating time events. No GET endpoint available for data ingestion.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| POST | /TimeEvents | Create time events for employee's time tracking | N/A |

---

### TimeEvents (Delete)
**Source File**: ClockInClockOutTimeEventsRestAPI.json
**API Type**: REST
**Base Path**: `/rest/timemanagement/timeeventprocessing/clockinclockout/v1`

#### Description
REST API for mass deletion of Clock In Clock Out time events.

#### Schema (Request)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| value | array[IdAndDeleteRequest] | Yes | List of time event IDs to be deleted |

#### IdAndDeleteRequest Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Time Event id to be deleted |
| deleted | boolean | Yes | Parameter that defines if a time event should be deleted (true for deletion) |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: N/A (write-only API)
- **Rationale**: This is a PATCH-only endpoint for deleting time events. No GET endpoint available for data ingestion.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| PATCH | /timeevents | Delete time events of employees | N/A |

---

### TimeAccountBalanceResponse
**Source File**: Balances.json
**API Type**: REST
**Base Path**: `/rest/timemanagement/absence/v1`

#### Description
Time accounts with their respective balances for a user at a specific date.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| timeAccount | TimeAccountResponse | No | Time account information |
| balances | DetailedBalanceResponse | No | Detailed balance breakdown |

#### Nested Schema: TimeAccountResponse
| Field | Type | Description |
|-------|------|-------------|
| timeAccountType | TimeAccountTypeResponse | Time account type information |
| externalCode | string | External code of the time account |
| bookableStartDate | string (date) | Start date when account can be booked |
| bookableEndDate | string (date) | End date when account can be booked |
| nextTransferDate | string (date) | Next transfer date |

#### Nested Schema: TimeAccountTypeResponse
| Field | Type | Description |
|-------|------|-------------|
| externalCode | string | External code (e.g., "VAC-DAYS") |
| externalName | string | External name (e.g., "Leave Account for Vacation") |
| unit | string | Unit of measurement (e.g., "DAYS") |

#### Nested Schema: DetailedBalanceResponse
| Field | Type | Description |
|-------|------|-------------|
| available | SimpleBalanceResponse | Available balance |
| accrued | SimpleBalanceResponse | Accrued balance |
| earned | SimpleBalanceResponse | Earned balance |
| paidOut | SimpleBalanceResponse | Paid out balance |
| planned | SimpleBalanceResponse | Planned balance |
| taken | SimpleBalanceResponse | Taken balance |

#### Nested Schema: SimpleBalanceResponse
| Field | Type | Description |
|-------|------|-------------|
| value | number | Balance value |
| formattedWithUnit | string | Balance with unit in user's language format |
| formattedWithUnitRoundedDown | string | Balance rounded down to 2 decimal places |

#### Primary Keys
- Composite: `timeAccount.externalCode` + `$at` (date parameter)

#### Ingestion Type
- **Type**: `snapshot`
- **Cursor Field**: N/A
- **Rationale**: Balance values are point-in-time calculations based on the `$at` date parameter. Each query returns current state rather than change history.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /timeAccountBalances | Gets time accounts with their respective balances | None |

#### Query Parameters
- `$at` (required) - Date for which balances are requested (YYYY-MM-DD)
- `assignmentId` (optional) - Assignment UUID of the user

---

### TimeTypeBalanceResponse
**Source File**: Balances.json
**API Type**: REST
**Base Path**: `/rest/timemanagement/absence/v1`

#### Description
Time types with their respective balances for the active user.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| mainAbsenceTimeType | boolean | No | Indicates if this is the main absence time type |
| timeType | TimeTypeResponse | No | Time type information |
| balance | SimpleBalanceResponse | No | Balance information |

#### Nested Schema: TimeTypeResponse
| Field | Type | Description |
|-------|------|-------------|
| externalCode | string | External code (e.g., "VAC") |
| externalName | string | External name (e.g., "Vacation") |
| unit | string | Unit of measurement (e.g., "DAYS") |
| leaveOfAbsence | boolean | Indicates if this is a leave of absence type |
| undeterminedEndDateAllowed | boolean | Whether undetermined end date is allowed |

#### Primary Keys
- Composite: `timeType.externalCode` + `$at` (date parameter)

#### Ingestion Type
- **Type**: `snapshot`
- **Cursor Field**: N/A
- **Rationale**: Balance values are calculated at the specified date. No change tracking available.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /timeTypeBalances | Gets time types with their respective balances | None |

#### Query Parameters
- `$at` (required) - Date for which balances are requested (YYYY-MM-DD)
- `mainAbsenceTimeTypeBalanceOnly` (optional) - Return only main absence time type balances
- `favoriteTimeTypeBalances` (optional) - Filter by favorite time types

---

### TerminationTimeAccountBalanceResponse
**Source File**: Balances.json
**API Type**: REST
**Base Path**: `/rest/timemanagement/absence/v1`

#### Description
Time accounts with their respective termination balances for a user.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| timeAccount | TerminationTimeAccountResponse | No | Time account information |
| balance | AvailableBalanceResponse | No | Available balance at termination |
| accrualSeparatedBalance | AvailableBalanceResponse | No | Accrual balance not yet transferred (only for "Entitled as Transferred" method) |

#### Nested Schema: TerminationTimeAccountResponse
| Field | Type | Description |
|-------|------|-------------|
| timeAccountType | TimeAccountTypeResponse | Time account type information |
| externalCode | string | External code of the time account |
| bookableStartDate | string (date) | Start date when account can be booked |
| bookableEndDate | string (date) | End date when account can be booked |

#### Nested Schema: AvailableBalanceResponse
| Field | Type | Description |
|-------|------|-------------|
| value | number | Balance value |
| formattedWithUnit | string | Balance with unit formatted |
| formattedWithUnitRoundedDown | string | Balance rounded down to 2 decimals |
| payable | boolean | Indicates if the balance can be paid out |

#### Primary Keys
- Composite: `timeAccount.externalCode` + `assignmentId` + `$at` (date)

#### Ingestion Type
- **Type**: `snapshot`
- **Cursor Field**: N/A
- **Rationale**: Termination balances are calculated based on termination date. Point-in-time calculation.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /terminationTimeAccountBalances | Gets time accounts with termination balances | None |

#### Query Parameters
- `$at` (optional) - Termination date (YYYY-MM-DD). If not provided, system derives it
- `assignmentId` (optional) - Assignment UUID of the user
- `preview` (optional) - Simulate termination if user not terminated (requires `$at` parameter)

---

### TimeOffEventResponse
**Source File**: TimeOffEvents.json
**API Type**: REST
**Base Path**: `/rest/timemanagement/absence/v1`

#### Description
Returns a list of absences, public holidays, and non-working days for a specified duration (up to 12 months).

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | No | External code identifier |
| title | string | No | Event title (e.g., "VACATION", "Good Friday") |
| startDate | string (date) | No | Start date of the event |
| endDate | string (date) | No | End date of the event |
| startTime | string | No | Start time (nullable for full-day events) |
| endTime | string | No | End time (nullable for full-day events) |
| duration | number | No | Duration value |
| timeUnit | string | No | Time unit (e.g., "DAYS") |
| durationFormatted | string | No | Formatted duration (e.g., "2 days") |
| crossMidnight | boolean | No | Whether event crosses midnight |
| type | string | No | Event type: ABSENCE, PUBLIC_HOLIDAY, NON_WORKING_DAY |
| typeFormatted | string | No | Formatted event type |
| status | string | No | Status: PENDING, CANCELLED, APPROVED, REJECTED, PENDING_CANCELLATION |
| statusFormatted | string | No | Formatted status |
| absenceDurationCategory | string | No | Category: MULTI_DAY, SINGLE_FULL_DAY, etc. (nullable) |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: `snapshot`
- **Cursor Field**: N/A
- **Rationale**: Events are queried by date range parameters. No incremental change tracking available. The API requires explicit start and end dates.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /events | Returns absences, public holidays, and non-working days | `$skip`, `$top` |

#### Query Parameters
- `assignmentId` (required) - Assignment UUID or userId of the user
- `types` (required) - Event types to retrieve: ABSENCE, PUBLIC_HOLIDAY, NON_WORKING_DAY
- `startDate` (required) - Start date (YYYY-MM-DD)
- `endDate` (required) - End date (YYYY-MM-DD)
- `includePartialDayAbsences` (optional) - Include partial-day absences (default: false)
- `excludeAbsencesStartingBeforeSelectionPeriod` (optional) - Exclude absences starting before start date
- `absenceStatus` (optional) - Filter by status: PENDING, CANCELLED, APPROVED, REJECTED, PENDING_CANCELLATION

---

### AvailableTimeType
**Source File**: AvailableTimeTypes.json
**API Type**: REST
**Base Path**: `/rest/timemanagement/absence/v1`

#### Description
Available time types for the login user based on their Time Profile in Job Information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| externalCode | string | No | External code (e.g., "VAC-DAYS") |
| externalName | string | No | External name (e.g., "Vacation (Days)") |
| unit | string | No | Unit of measurement (e.g., "Day(s)") |
| undeterminedEndDateAllowed | boolean | No | Whether undetermined end date is allowed |
| leaveOfAbsence | boolean | No | Whether this is a leave of absence type |
| mainAbsenceTimeType | boolean | No | Whether this is the main absence time type |
| flexibleRequestingAllowed | boolean | No | Whether flexible requesting is allowed |
| allowedFractions | AllowedFraction | No | Allowed fractions: FULL_DAY, HALF_DAY, QUARTER_DAY, FULL_HOURS, HOURS_MINUTES |

#### Primary Keys
- `externalCode` (string)

#### Ingestion Type
- **Type**: `snapshot`
- **Cursor Field**: N/A
- **Rationale**: Configuration data for available time types. No modification tracking available.

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /availableTimeTypes | Gets available time types for the login user | None |

#### Query Parameters
- `$at` (required) - Date for which available time types are requested (YYYY-MM-DD)
- `absenceRequestCode` (optional) - External code of existing absence to filter time types

---

## Ingestion Type Summary

| Entity | API Type | Ingestion Type | Cursor Field | Rationale |
|--------|----------|----------------|--------------|-----------|
| ClockInClockOutGroups | OData v4 | `cdc` | lastChangedAt | Has timestamp tracking and unique key |
| TimeEventTypes | OData v4 | `snapshot` | N/A | Nested entity, no timestamp tracking |
| clockinclockout.timeevents | OData v4 | `append` | lastChangedAt | Event log records |
| TimeEvents (Create) | REST | N/A | N/A | Write-only API (POST) |
| TimeEvents (Delete) | REST | N/A | N/A | Write-only API (PATCH) |
| TimeAccountBalanceResponse | REST | `snapshot` | N/A | Point-in-time calculation |
| TimeTypeBalanceResponse | REST | `snapshot` | N/A | Point-in-time calculation |
| TerminationTimeAccountBalanceResponse | REST | `snapshot` | N/A | Point-in-time calculation |
| TimeOffEventResponse | REST | `snapshot` | N/A | Date range query, no change tracking |
| AvailableTimeType | REST | `snapshot` | N/A | Configuration data |

---

## Authentication

### OData v4 APIs
- **Type**: API Key (Bearer token)
- **Header**: `Authorization: Bearer <token>`

### REST APIs
- **Type**: OAuth 2.0 Client Credentials
- **Token URL**: `https://{api-server}/oauth/token`
- **Header**: `Authorization: Bearer <token>`

---

## Pagination Summary

| API | Pagination Method |
|-----|-------------------|
| ClockInClockOutIntegration (OData v4) | `$skip`, `$top`, `@odata.count` |
| ClockInClockOutExternal (OData v4) | `$skip`, `$top`, `@odata.count` |
| TimeOffEvents (REST) | `$skip`, `$top` |
| Balances APIs (REST) | None (single response) |
| AvailableTimeTypes (REST) | None (single response) |

---

## Notes

1. **Clock In Clock Out APIs**: Split across multiple files with different purposes:
   - Integration API (OData v4): Configuration and group management
   - External API (OData v4): Export time events for external systems
   - REST Create API: Create time events from external terminals
   - REST Delete API: Mass delete time events

2. **Balance APIs**: Point-in-time calculations requiring date parameter. Not suitable for incremental ingestion.

3. **Time Events Export**: Best candidate for incremental ingestion using `lastChangedAt` or `timestampUTC` as cursor fields.

4. **RBP Permissions**: Time Events export API respects Role-Based Permissions. Empty response with 200 status indicates missing permissions.

5. **Rate Limits**: Time events export limited to 1000 records per request. Implement pagination for full data extraction.
