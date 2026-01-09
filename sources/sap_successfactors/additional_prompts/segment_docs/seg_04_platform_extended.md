# SAP SuccessFactors API Documentation - Platform Services Extended

## Segment Overview
- **Segment**: 4 - Platform Services Extended
- **Files Processed**: 5
- **Entities Documented**: 15
- **Endpoints Documented**: 26

## Files Processed
1. PLTTodo.json - Todo management APIs
2. PLTSuccessStore.json - Success Store content APIs
3. PLTExecutionManager.json - Execution Manager event APIs
4. PLTUserInterfaceThemes.json - UI theme configuration APIs
5. PLTCustomNavigation.json - Custom navigation APIs

---

## Objects

### Todo
**Source File**: PLTTodo.json
**API Type**: OData v2
**Base Path**: /odata/v2/Todo
**Description**: Legacy Todo API that allows querying to-do items of the logged-in user.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| categoryId | string | Yes | Category identifier (key field) |
| categoryLabel | string | No | Display label for the category |
| displayOrder | integer (int32) | No | Order in which to display the todo item |
| status | integer (int32) | No | Status of the todo item |

#### Primary Keys
- `categoryId` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime or createdDateTime field available for incremental tracking

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /Todo | Get entities from Todo | $skip, $top, $count |
| GET | /Todo('{categoryId}') | Get entity from Todo by key | N/A |

---

### TodoEntryV2
**Source File**: PLTTodo.json
**API Type**: OData v2
**Base Path**: /odata/v2/TodoEntryV2
**Description**: New TodoEntryV2 API allows querying to-do items of all users with proper permission, and creating/editing to-do items of selected categories.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| todoEntryId | string (decimal) | Yes | Unique identifier for the todo entry (key field) |
| categoryId | string | Yes | Category identifier |
| categoryLabel | string | No | Display label for the category |
| completedDateTime | datetime | No | Date/time when the todo was completed |
| createdDate | datetime | Yes | Date when the todo was created |
| dueDate | datetime | Yes | Due date for the todo item |
| formDataId | integer (int32) | No | Associated form data identifier |
| lastModifiedDateTime | datetime | Yes | Last modification timestamp |
| linkUrl | string (max 2000) | No | URL link associated with the todo |
| status | integer (int32) | Yes | Status of the todo entry |
| subjectId | string (max 100) | No | Subject identifier |
| todoEntryName | string | Yes | Name of the todo entry |

#### Primary Keys
- `todoEntryId` (string/decimal)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDateTime
- **Rationale**: Has lastModifiedDateTime field for tracking changes; no soft delete indicator for cdc_with_deletes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /TodoEntryV2 | Get entities from TodoEntryV2 | $skip, $top, $count |
| GET | /TodoEntryV2('{todoEntryId}') | Get entity from TodoEntryV2 by key | N/A |

---

### SuccessStoreContent
**Source File**: PLTSuccessStore.json
**API Type**: OData v2
**Base Path**: /odata/v2/SuccessStoreContent
**Description**: Access Success Store content including best practices and default content.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| contentId | string (int64) | Yes | Unique content identifier (key field) |
| bestPractice | boolean | No | Whether this is a best practice content |
| comments | string | No | Comments about the content |
| contentType | string | No | Type of content |
| customField | string | No | Custom field value |
| defaultContent | boolean | No | Whether this is default content |
| defaultContentName | string | No | Name of the default content |
| domain | string | No | Domain of the content |
| expiryOnDate | datetime | No | Expiration date |
| publishOnDate | datetime | No | Publication date |
| revisionNo | string | No | Revision number |
| status | string | No | Content status |
| wizardable | boolean | No | Whether content is wizardable |
| contentData | SuccessStoreContentBlob | No | Navigation to content blob data |

#### Primary Keys
- `contentId` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No lastModifiedDateTime field; publishOnDate and expiryOnDate are not modification timestamps

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /SuccessStoreContent | Get entities from SuccessStoreContent | $skip, $top, $count |
| GET | /SuccessStoreContent({contentId}) | Get entity from SuccessStoreContent by key | N/A |

#### Navigation Properties
- `contentData` -> SuccessStoreContentBlob

---

### SuccessStoreContentBlob
**Source File**: PLTSuccessStore.json
**API Type**: OData v2
**Base Path**: /odata/v2/SuccessStoreContentBlob
**Description**: Binary blob data for Success Store content.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| contentId | string | Yes | Content identifier (key field) |

#### Primary Keys
- `contentId` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking fields available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /SuccessStoreContentBlob | Get entities from SuccessStoreContentBlob | $skip, $top, $count |
| GET | /SuccessStoreContentBlob('{contentId}') | Get entity from SuccessStoreContentBlob by key | N/A |

---

### EMEventPayload
**Source File**: PLTExecutionManager.json
**API Type**: OData v2
**Base Path**: /odata/v2/EMEventPayload
**Description**: Execution Manager event payload data including file attachments.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string (int64) | Yes | Unique identifier (key field) |
| fileName | string | No | Name of the attached file |
| fileType | string | No | Type of the attached file |
| mimeType | string | No | MIME type of the payload |
| payload | string (base64url) | Yes | Base64 encoded payload data |
| type | string | Yes | Type of the event payload |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking fields available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EMEventPayload | Get entities from EMEventPayload | $skip, $top, $count |
| GET | /EMEventPayload({id}) | Get entity from EMEventPayload by key | N/A |

---

### EMMonitoredProcess
**Source File**: PLTExecutionManager.json
**API Type**: OData v2
**Base Path**: /odata/v2/EMMonitoredProcess
**Description**: Execution Manager monitored process information.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| processDefinitionId | string | Yes | Process definition identifier (key field) |
| processInstanceId | string | Yes | Process instance identifier (key field) |
| processType | string | Yes | Type of process (key field) |
| monitoredProcessId | string (int64) | Yes | Unique monitored process ID |
| coRelatorId | string | No | Correlator identifier for related processes |
| firstEventTime | datetime | Yes | Time of the first event |
| lastEventTime | datetime | Yes | Time of the last event |
| hasErrors | string | No | Whether process has errors |
| hasWarnings | string | No | Whether process has warnings |
| moduleName | string | No | Name of the module |
| processDefinitionName | string | No | Name of the process definition |
| processInstanceName | string | No | Name of the process instance |
| processState | string | Yes | Current state of the process |

#### Primary Keys
- `processDefinitionId` (string)
- `processInstanceId` (string)
- `processType` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastEventTime
- **Rationale**: Has lastEventTime field for tracking changes to monitored processes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EMMonitoredProcess | Get entities from EMMonitoredProcess | $skip, $top, $count |
| GET | /EMMonitoredProcess(processDefinitionId='{processDefinitionId}',processInstanceId='{processInstanceId}',processType='{processType}') | Get entity from EMMonitoredProcess by composite key | N/A |

---

### EMEventAttribute
**Source File**: PLTExecutionManager.json
**API Type**: OData v2
**Base Path**: /odata/v2/EMEventAttribute
**Description**: Execution Manager event attributes (key-value pairs).

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string (int64) | Yes | Unique identifier (key field) |
| name | string | Yes | Attribute name |
| value | string | No | Attribute value |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking fields available; attributes are typically static

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EMEventAttribute | Get entities from EMEventAttribute | $skip, $top, $count |
| GET | /EMEventAttribute({id}) | Get entity from EMEventAttribute by key | N/A |

---

### EMEvent
**Source File**: PLTExecutionManager.json
**API Type**: OData v2
**Base Path**: /odata/v2/EMEvent
**Description**: Execution Manager events with associated attributes, payloads, and processes.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string (int64) | Yes | Unique event identifier (key field) |
| eventName | string | Yes | Name of the event |
| eventDescription | string | No | Description of the event |
| eventDescriptionMsgKey | string | No | Message key for event description localization |
| eventTime | datetime | No | Time when the event occurred |
| eventType | string | No | Type of the event |
| eventAttributes | Collection(EMEventAttribute) | No | Navigation to event attributes |
| eventPayload | EMEventPayload | No | Navigation to event payload |
| process | EMMonitoredProcess | No | Navigation to associated monitored process |

#### Primary Keys
- `id` (int64)

#### Ingestion Type
- **Type**: append
- **Cursor Field**: eventTime
- **Rationale**: Events are typically append-only log entries; eventTime can be used for ordering new events

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /EMEvent | Get entities from EMEvent | $skip, $top, $count |
| GET | /EMEvent({id}) | Get entity from EMEvent by key | N/A |

#### Navigation Properties
- `eventAttributes` -> Collection(EMEventAttribute)
- `eventPayload` -> EMEventPayload
- `process` -> EMMonitoredProcess

---

### ThemeTemplate
**Source File**: PLTUserInterfaceThemes.json
**API Type**: OData v2
**Base Path**: /odata/v2/ThemeTemplate
**Description**: UI theme template definitions including HTML templates, scripts, and styles.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Theme template identifier (key field) |
| bodyStyleClass | string | No | CSS class for body styling |
| footer | string | No | Footer HTML content |
| header | string | No | Header HTML content |
| langDir | string | No | Language direction (ltr/rtl) |
| locale | string | No | Locale code |
| scripts | string | No | JavaScript scripts |
| styles | string | No | CSS styles |
| template | string | No | HTML template content |
| ui5BaseThemeRootUrl | string | No | UI5 base theme root URL |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking fields available

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ThemeTemplate | Get entities from ThemeTemplate | $skip, $top, $count |
| GET | /ThemeTemplate('{id}') | Get entity from ThemeTemplate by key | N/A |

---

### ThemeInfo
**Source File**: PLTUserInterfaceThemes.json
**API Type**: OData v2
**Base Path**: /odata/v2/ThemeInfo
**Description**: Theme information including URLs, fingerprints, and module configuration.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Theme identifier (key field) |
| lastModifiedDate | string (int64) | No | Last modification timestamp (epoch) |
| locale | string | No | Locale code |
| modules | string | No | Associated modules |
| ui5Theme | string | No | UI5 theme name |
| fingerprints | ThemeFingerprintsBean | No | Theme fingerprints (config, css, ui5BaseThemeRoot) |
| urls | ThemeUrlsBean | No | Theme URLs (baseUrl, configUrl, cssUrl, ui5BaseThemeRootUrl) |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: cdc
- **Cursor Field**: lastModifiedDate
- **Rationale**: Has lastModifiedDate field for tracking theme configuration changes

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ThemeInfo | Get entities from ThemeInfo | $skip, $top, $count |
| GET | /ThemeInfo('{id}') | Get entity from ThemeInfo by key | N/A |

#### Complex Types
- **ThemeFingerprintsBean**: config (string), css (string), ui5BaseThemeRoot (string)
- **ThemeUrlsBean**: baseUrl (string), configUrl (string), cssUrl (string), ui5BaseThemeRootUrl (string)

---

### ThemeConfig
**Source File**: PLTUserInterfaceThemes.json
**API Type**: OData v2
**Base Path**: /odata/v2/ThemeConfig
**Description**: Complete theme configuration including all UI styling options.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Theme configuration identifier (key field) |
| themeConfiguration | GlobalThemeConfiguration | No | Complete theme configuration object |

#### Primary Keys
- `id` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking fields; complex nested configuration object

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /ThemeConfig | Get entities from ThemeConfig | $skip, $top, $count |
| GET | /ThemeConfig('{id}') | Get entity from ThemeConfig by key | N/A |

#### Complex Types (GlobalThemeConfiguration includes)
- **ThemeBackgroundConfig**: baseColor, imageHorizontalPosition, imageOption, imageRepeat, imageVerticalPosition, lighting, texture, url
- **ThemeButtonConfig**: bgColor, borderColor, borderWidth, disabledBgColor, disabledBorderColor, disabledTextColor, hoverBgColor, hoverBorderColor, hoverTextColor, textColor
- **ThemeContentConfig**: bgColor, bgColorVariant, iconScheme, linkTextColor, textColor, textColorVariant
- **ThemeDiagramConfig**: backgroundColor, lineColor, threshold colors, palette colors (1-10), primaryColor, textColor, titleColor
- **ThemeExternalConfig**: faviconOption, faviconUrl, footerLogoOption, footerLogoUrl
- **ThemeFooterConfig**: logoScheme, textColor
- **ThemeHeaderBackgroundConfig**: baseColor, bgOption, imageHorizontalPosition, imageRepeat, imageVerticalPosition, styleOption, url
- **ThemeHighlightConfig**: bgColor, iconScheme, linkTextColor, textColor
- **ThemeLoginConfig**: autofillBgColor, background, footerScheme, logo, primaryButton, primaryButtonOption
- **ThemeLogoConfig**: backdropColor, position, url, useBackdrop, useUploadedLogo
- **ThemeMenuConfig**: activeBgColor, activeTextColor, bgColor, hoverBgColor, hoverBgColorDisabled, hoverTextColor, textColor, textColorDisabled
- **ThemeModulePickerConfig**: activeHeaderBgColor, activeHeaderTextColor, headerTextColor, hoverHeaderBgColor, hoverHeaderTextColor
- **ThemeNavigationConfig**: activeTextColor, allowCondensedView, hoverTextColor, textColor
- **ThemePlacematConfig**: backgroundType, bgColor, borderColor, opacity, selectedTabColor, useShadow
- **ThemePortletConfig**: Multiple text, background, link, and sidebar colors
- **ThemeTableConfig**: Row colors, header colors, link colors, selection colors
- **ThemeTileConfig**: Accent colors, alert colors, body/header colors, icon schemes
- **ThemeLandingPageTileConfig**: bgColor, borderColor, iconColor, text colors

---

### CustomNav
**Source File**: PLTCustomNavigation.json
**API Type**: OData v2
**Base Path**: /odata/v2/CustomNav
**Description**: Custom navigation items added to the Home page.

#### Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Navigation item title (key field) |
| altText | string | No | Alternative text for accessibility |
| alwaysShow | boolean | No | Whether to always show the navigation item |
| isModule | boolean | No | Whether this is a module navigation |
| isSelected | boolean | No | Whether this item is currently selected |
| label | string | No | Display label |
| newWindow | boolean | No | Whether to open in new window |
| url | string | No | Target URL |

#### Primary Keys
- `title` (string)

#### Ingestion Type
- **Type**: snapshot
- **Cursor Field**: N/A
- **Rationale**: No modification tracking fields available; configuration data typically changes infrequently

#### Endpoints
| Method | Path | Description | Pagination |
|--------|------|-------------|------------|
| GET | /CustomNav | Get entities from CustomNav | $skip, $top, $count |
| GET | /CustomNav('{title}') | Get entity from CustomNav by key | N/A |

---

## Summary by Ingestion Type

### CDC (Change Data Capture) Entities
| Entity | Cursor Field | Notes |
|--------|--------------|-------|
| TodoEntryV2 | lastModifiedDateTime | Full todo entry management |
| EMMonitoredProcess | lastEventTime | Process monitoring |
| ThemeInfo | lastModifiedDate | Theme metadata tracking |

### Append-Only Entities
| Entity | Cursor Field | Notes |
|--------|--------------|-------|
| EMEvent | eventTime | Event log entries |

### Snapshot Entities
| Entity | Rationale |
|--------|-----------|
| Todo | Legacy API without modification tracking |
| SuccessStoreContent | No modification timestamps |
| SuccessStoreContentBlob | Binary data without tracking |
| EMEventPayload | Payload data without tracking |
| EMEventAttribute | Static attribute data |
| ThemeTemplate | Template definitions without tracking |
| ThemeConfig | Complex configuration object |
| CustomNav | Navigation configuration |

---

## Pagination Notes

All collection endpoints support standard OData v2 pagination:
- `$top` - Limit number of results (default: 20)
- `$skip` - Skip first n items for pagination
- `$count` - Include total count of items
- `$filter` - Filter items by property values
- `$orderby` - Order results by property values
- `$select` - Select specific properties to return
- `$search` - Search items by phrases

For entities with navigation properties (EMEvent, SuccessStoreContent), use `$expand` to include related entities.

---

## Authentication

All APIs require Basic Authentication as defined in the security definitions.

---

## API Server

Base URL pattern: `https://{api-server}/odata/v2`

Default sandbox: `sandbox.api.sap.com/successfactors/odata/v2`

Production servers vary by data center. Reference: [SAP SuccessFactors API Servers](https://help.sap.com/viewer/d599f15995d348a1b45ba5603e2aba9b/LATEST/en-US/af2b8d5437494b12be88fe374eba75b6.html)
