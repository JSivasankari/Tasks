# Nimbus Labs Incident Response Plan (v3.2)

## Purpose and scope
This plan describes how Nimbus Labs detects, classifies, contains, and learns from security incidents. It applies to every employee, contractor, and automated system that touches Nimbus Labs production, corporate, or customer environments. The plan is owned by the Security Operations team and reviewed every six months, in March and September.

## Severity levels
Every incident is classified into one of four severity levels at the moment of triage. SEV-1 is critical: confirmed exposure of customer personal data, or a production outage lasting more than 30 minutes. SEV-2 is high: a suspected compromise of a single production system, or a confirmed malware infection on a corporate laptop. SEV-3 is moderate: a policy violation with no confirmed data loss, such as a shared credential. SEV-4 is low: a reported suspicious email or an unsuccessful attack that was blocked automatically.

The classification can be raised at any time by any responder but may only be lowered by the Incident Commander with a written reason in the incident ticket.

## Acknowledgement targets
The on-call responder must acknowledge an alert within a fixed window. For SEV-1 the window is 10 minutes. For SEV-2 it is 30 minutes. For SEV-3 it is 4 hours, and for SEV-4 it is 2 business days. Alerts are delivered through the paging tool PingHarbor. If the primary on-call does not acknowledge within the window, PingHarbor automatically escalates to the secondary on-call, and after a further 10 minutes to the Head of Security.

## Roles
Every SEV-1 and SEV-2 incident has four named roles. The Incident Commander (IC) owns decisions and the timeline. The Technical Lead directs investigation and containment. The Communications Lead handles all internal and external messaging, and nobody else may speak to customers or the press. The Scribe records every action with a timestamp in the incident ticket. The IC rotation hands over every Monday at 10:00 IST, and the handover is done live on a call, never only in writing.

## The war room
When a SEV-1 is declared, the IC opens a dedicated Slack channel called #lighthouse-bridge and starts the voice bridge named Beacon-7. All incident discussion happens in that channel so that the scribe can capture it. Side conversations in direct messages are discouraged because they fragment the record. Only people with an assigned role or an explicit invitation from the IC may speak on Beacon-7; observers join in listen-only mode.

## Containment principles
Responders follow a strict order: preserve evidence, contain, eradicate, recover. Before any affected host is isolated or reimaged, the Technical Lead captures a forensic image and records its SHA-512 hash in the ticket. Isolation is done through network quarantine, never by powering a machine off, because volatile memory may hold evidence. Compromised credentials are rotated immediately, and any session tokens belonging to the affected accounts are revoked within 15 minutes of discovery.

## Notification obligations
For any SEV-1 that involves personal data, Nimbus Labs notifies affected customers within 48 hours of confirmation. Notification to the relevant regulator happens within 72 hours of confirmation. The Communications Lead drafts both notices using pre-approved templates, and Legal must approve them before sending. If the scope is not yet known at the 48 hour mark, a preliminary notice is sent and updated as facts emerge.

## Evidence retention
All incident artifacts, including forensic images, logs, chat transcripts, and the incident ticket, are retained for 400 days. After that period they are reviewed by Legal, and are either archived for a further period or securely destroyed with a deletion certificate. Evidence is stored in a write-once bucket and access is logged.

## Postmortems
A blameless postmortem is mandatory for every SEV-1 and SEV-2 and must be held within 5 business days of resolution. The team uses a template called Tidewater, which has five sections: summary, timeline, root cause, what went well, and action items. Every action item has an owner and a due date, and open action items are reviewed in the monthly Security Review Board meeting. A postmortem is considered closed only when all action items are completed or formally accepted as risk.

## Practice and readiness
Nimbus Labs runs a tabletop exercise every quarter and a full live-fire simulation once a year, always in November. The tabletop scenarios rotate between ransomware, insider threat, supply chain compromise, and cloud misconfiguration. After each exercise, the Security Operations team publishes a short readiness score out of 100, and the target is a score of at least 80. Scores below 70 trigger a mandatory retraining session for the on-call roster within 30 days.

## Common mistakes to avoid
Responders sometimes delete malicious files before they are imaged, which destroys evidence. Others discuss incident details on public channels or personal messaging apps. A third common mistake is delaying the SEV-1 declaration while trying to gather more certainty; the rule is that it is always better to declare early and downgrade later. The Incident Commander is expected to coach responders on these points during every incident and during the postmortem.
