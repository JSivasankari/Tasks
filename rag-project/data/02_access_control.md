# Nimbus Labs Access Control Standard (v2.4)

## Principles
Access at Nimbus Labs follows three principles: least privilege, need to know, and time-boxed elevation. Nobody receives standing administrative access to production. Any access that is not used for 60 consecutive days is automatically removed by the identity team's cleanup job.

## Single sign-on
All corporate applications are fronted by the single sign-on portal called NimbusGate. Applications that cannot integrate with NimbusGate must be approved by the Security Review Board, abbreviated SRB, and may not hold Confidential or Restricted data. NimbusGate sessions expire after 12 hours for standard applications and after 2 hours for the production cloud console, after which the user must authenticate again.

## Passwords and multi-factor authentication
Passwords must be at least 16 characters and are checked against a list of known breached passwords at the time they are set. Password expiry is not enforced; instead, passwords are reset only after suspected compromise. Multi-factor authentication is mandatory for every account. Administrators and anyone with production access must use a FIDO2 hardware security key. All other employees may use a time-based one-time password app, but SMS codes are not permitted for any account.

Each employee registers two hardware keys when eligible: a primary key and a backup key that is kept in a locked drawer at home or in the office. Lost keys must be reported to the Security Operations team within one hour so that the key can be revoked.

## Privileged access
Elevated privileges are granted through a just-in-time tool named KeyKeeper. An engineer requests a role, provides a ticket number and a reason, and a peer approver from the same team must approve. The maximum duration of any grant is 4 hours, and grants cannot be renewed more than twice in a single day without extra approval from the engineering director. Every KeyKeeper session is recorded, and recordings are kept for 180 days.

## Service accounts and keys
Service accounts must have an owning team and an expiry date. Their API keys and certificates are rotated every 60 days by an automated pipeline. Long-lived keys committed to source code are treated as a SEV-3 incident, and a secret-scanning tool blocks such commits before they are merged. Keys are stored only in the central secrets manager; email, chat, and wikis are not acceptable storage.

## Break-glass accounts
Two emergency break-glass accounts exist for the case where NimbusGate itself is unavailable. Their credentials are sealed in separate envelopes inside a fireproof safe in the Bengaluru office, and opening either envelope immediately triggers a SEV-2 alert. The break-glass accounts are tested every 90 days by the Security Operations team, and after every test the passwords are changed and the envelopes are resealed.

## Access reviews
Managers review the access of their direct reports every quarter. The review window opens on the first day of January, April, July, and October and closes on the 10th day of that month. Accounts that are not confirmed by the end of the window are suspended automatically on the 11th, and reactivation requires a ticket approved by the manager and the application owner. The completion rate for each department is published to leadership, and the target is 100 percent.

## Joiners, movers, and leavers
New employees receive a baseline role on their first day and may request additional roles through the access portal. When someone changes teams, their old team's roles are removed within 5 business days. When someone leaves the company, all access is revoked within 1 hour of the scheduled end of their employment, and for involuntary departures access is revoked before the conversation with the employee begins. Laptops are collected and wiped, and the device record is closed only when the wipe certificate is attached.

## Third-party and contractor access
Contractors receive accounts that expire automatically after 90 days unless renewed by their sponsor. Vendors must connect through a dedicated vendor gateway and never through the employee VPN. Vendor accounts cannot be granted privileged roles, and any vendor needing production access must be supervised by a Nimbus Labs engineer on a screen-sharing session.

## Remote access
Employees working remotely must use the corporate VPN when accessing internal tools that are not exposed through NimbusGate. The VPN requires both a managed device certificate and the user's second factor. Split tunneling is disabled. Public Wi-Fi may be used only when the VPN is active, and devices that are out of date by more than 30 days on their operating system patches are blocked from connecting.

## Logging and monitoring
All authentication events, privilege grants, and administrative actions are logged to the central security data lake. Alerts are raised for impossible travel, repeated failed logins, a new device registering a second factor, and any use of a break-glass account. Logs in the data lake are retained for 13 months.
