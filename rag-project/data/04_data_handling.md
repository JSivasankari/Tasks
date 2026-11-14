# Nimbus Labs Data Handling and Classification Standard (v2.0)

## Why this standard exists
Nimbus Labs holds data about customers, employees, and its own technology. This standard explains how that data is labelled, stored, shared, kept, and destroyed. Every employee is expected to know the classification of the data they work with and to follow the matching handling rules.

## Classification levels
There are four classes. Public data is approved for release to anyone, such as marketing pages. Internal data is for employees only and would cause minor harm if leaked, such as the org chart. Confidential data would cause serious harm if disclosed, and includes customer contracts, source code, and financial forecasts. Restricted data, informally called Red data, would cause severe harm or breach the law if disclosed. It includes customer personal data, authentication secrets, and encryption keys. When in doubt, data is treated as one level higher until the data owner decides.

## Labelling
Documents and storage locations carry a visible label. Spreadsheets and slides include the class in the footer. Cloud storage buckets carry a mandatory tag named data-class. A nightly job checks buckets for missing tags and opens a SEV-4 ticket for each one found. Untagged buckets that are internet-reachable are blocked automatically after 24 hours.

## Encryption
Data at rest is encrypted with AES-256-GCM. Data in transit must use TLS 1.3 or higher, and older versions are disabled on all company endpoints. Encryption keys are managed by the cloud key management service in the ap-south-1 region, and master keys are rotated every 12 months. Restricted data additionally uses application-level encryption with separate keys for each customer, so that a leak of one key does not expose other customers.

## Data residency
Restricted data about customers in India must be stored and processed only in the ap-south-1 region. Copies for testing or analytics are not allowed to leave the region. If a project needs to move Restricted data across borders, the Data Protection Officer must approve it in writing before the transfer takes place. Anonymised data that has passed the re-identification review may be handled as Internal.

## Sharing data
Confidential data may be shared externally only with a signed non-disclosure agreement and through the approved file-sharing platform, with link expiry set to a maximum of 14 days. Restricted data may never be sent by email, regardless of encryption. Sharing screenshots of Restricted data in chat is also forbidden. A data loss prevention tool named Sieve scans outbound email, chat, and web uploads and blocks transfers that match patterns for Restricted data.

## Removable media and printing
USB mass storage devices are blocked on all corporate laptops. Exceptions require approval from the Head of Security and last at most 7 days. Printing of Restricted data is allowed only on the secure print queue, which requires badge release, and printouts must be shredded in the office shredders after use. A clean desk policy applies, meaning that no Confidential or Restricted material may be left on a desk overnight.

## Retention schedule
Application and infrastructure logs are retained for 13 months. Backups are kept for 35 days and then overwritten. Customer data is deleted 90 days after the end of the customer contract, and the customer receives a deletion certificate within 30 days of the actual deletion. Audit logs and financial records are kept for 7 years. Employee records are kept for 5 years after the end of employment unless law requires longer.

## Backups and recovery
Backups are taken every 6 hours and replicated to a second availability zone. Recovery is tested every quarter by restoring a random production database into an isolated environment and comparing checksums. The recovery time objective for core services is 4 hours, and the recovery point objective is 6 hours. A failed restore test is raised as a SEV-3 incident and must be resolved before the next scheduled test.

## Data subject requests
Customers and employees may ask what data Nimbus Labs holds about them, request corrections, or ask for deletion. Requests are logged in the privacy portal and must be completed within 30 days. Identity must be verified before any data is released. The Data Protection Officer reviews every deletion request to confirm that no legal retention requirement applies.

## Disposal
Retired laptops and servers are wiped using a certified tool that overwrites storage three times, or the drives are physically shredded by an approved vendor. The vendor returns a certificate listing the serial numbers destroyed. Cloud storage is deleted by destroying the encryption keys as well as the objects, which makes remaining fragments unreadable.
