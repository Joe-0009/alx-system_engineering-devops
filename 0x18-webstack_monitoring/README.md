# Postmortem Report

## Issue Summary

**Duration of the Outage:**
- Start Time: June 18, 2024, 2:00 AM (UTC)
- End Time: June 18, 2024, 4:30 AM (UTC)

**Impact:**
- Service affected: User authentication service
- User experience: Users were unable to log in or register accounts
- Percentage of users affected: 100%

**Root Cause:**
- A misconfiguration in the authentication server's load balancer caused it to drop all incoming requests.

## Timeline

- **2:00 AM:** Issue detected via monitoring alert (Datadog).
- **2:05 AM:** On-call engineer receives alert and acknowledges it.
- **2:10 AM:** Initial investigation starts with checking server health and logs.
- **2:20 AM:** Misleading path: suspected database issue, checked database connections and queries.
- **2:45 AM:** Realized issue was not with the database.
- **3:00 AM:** Investigated load balancer configuration.
- **3:15 AM:** Identified misconfiguration in the load balancer settings.
- **3:30 AM:** Escalated to network team to assist with reconfiguration.
- **4:00 AM:** Network team corrected the load balancer settings.
- **4:15 AM:** Service restored, users able to log in again.
- **4:30 AM:** Incident marked as resolved.

## Root Cause and Resolution

**Root Cause:**
- The load balancer was incorrectly configured to route traffic to an outdated and decommissioned server, causing all incoming authentication requests to fail.

**Resolution:**
- The load balancer settings were updated to route traffic correctly to the active authentication servers. A configuration audit was performed to ensure no other misconfigurations existed.

## Corrective and Preventative Measures

**Improvements and Fixes:**
- Implement periodic audits of load balancer configurations.
- Enhance monitoring to detect load balancer misconfigurations sooner.
- Develop a standard operating procedure (SOP) for load balancer configuration changes.

**Tasks:**
1. Patch Nginx server to the latest version.
2. Add monitoring on server memory to alert when thresholds are reached.
3. Conduct training sessions for engineers on load balancer configurations.
4. Review and update documentation for load balancer setup and maintenance.
5. Implement automated scripts to verify load balancer configurations against a known-good state.
