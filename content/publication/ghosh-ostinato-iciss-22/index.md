---
title: 'Ostinato: Cross-host Attack Correlation Through Attack Activity Similarity
  Detection'
authors:
- Sutanu Kumar Ghosh
- Kiavash Satvat
- Rigel Gjomemo
- V. N. Venkatakrishnan
date: '2022-01-01'
publishDate: '2026-02-06T02:58:19.847210Z'
publication_types:
- paper-conference
publication: '*Information Systems Security*'
abstract: Modern attacks against enterprises often have multiple targets inside the
  enterprise network. Due to the large size of these networks and increasingly stealthy
  attacks, attacker activities spanning multiple hosts are extremely difficult to
  correlate during a threat-hunting effort. In this paper, we present a method for
  an efficient cross-host attack correlation across multiple hosts. Unlike previous
  works, our approach does not require lateral movement detection techniques or host-level
  modifications. Instead, our approach relies on an observation that attackers have
  a few strategic mission objectives on every host that they infiltrate, and there
  exist only a handful of techniques for achieving those objectives. The central idea
  behind our approach involves comparing (OS agnostic) activities on different hosts
  and correlating the hosts that display the use of similar tactics, techniques, and
  procedures. We implement our approach in a tool called Ostinato and successfully
  evaluate it in threat hunting scenarios involving DARPA-led red team engagements
  spanning 500 hosts and in another multi-host attack scenario. Ostinato successfully
  detected 21 additional compromised hosts, which the underlying host-based detection
  system overlooked in activities spanning multiple days of the attack campaign. Additionally,
  Ostinato successfully reduced alarms generated from the underlying detection system
  by more than 90%, thus helping to mitigate the threat alert fatigue problem.
---
