---
title: Real-time Analytics for APT Detection and Threat Hunting Using Cyber-threat
  Intelligence and Provenance Graphs
authors:
- V.N. Venkatakrishnan
date: '2025-01-01'
publishDate: '2026-02-04T17:38:42.364553Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 10th ACM International Workshop on Security and
  Privacy Analytics*'
doi: 10.1145/3716815.3729016
abstract: 'The persistent and stealthy nature of Advanced Persistent Threats (APTs)
  poses a significant challenge to enterprise security. Traditional detection mechanisms
  often fall short in identifying coordinated multi-step attacks or leveraging the
  rich context available in Cyber Threat Intelligence (CTI).     The three works presented
  tackle this problem from complementary angles -- real-time detection, correlation-based
  threat hunting, and automated intelligence extraction. A unifying thread across
  these three works is their shared reliance on provenance graphs as a powerful abstraction
  for capturing and reasoning about complex attacker behavior. Together, these approaches
  form a complementary ecosystem: Extractor extracts threat knowledge, POIROT hunts
  for manifestations of that knowledge, and HOLMES detects emergent threats in real-time,
  all grounded in a common graph-based representation of system activity and threat
  behavior.    HOLMES introduces a real-time detection framework aimed at identifying
  the coordinated activities typical of APT campaigns.  It does so by correlating
  suspicious information flows to generate a robust detection signal and constructing
  high-level provenance graphs that summarize attacker behavior for analyst response.
  Its evaluation shows high precision and low false alarm rates, supporting its applicability
  in live operational environments. POIROT builds on the growing use of CTI standards
  by actively leveraging the relationships between indicators—often underused in practice—for
  threat hunting. It treats the problem as a graph pattern matching task, aligning
  CTI-derived graphs with system-level provenance data obtained from kernel audits.
  Its novel similarity metric enables efficient search through massive graphs, revealing
  APT traces within minutes and demonstrating the operational utility of CTI relationship
  data.    Extractor addresses the challenge of unstructured CTI reports by automatically
  transforming them into structured, machine-usable provenance graphs. Without requiring
  strict assumptions about the input text, it extracts concise behavioral indicators
  that can be fed into threat-hunting tools like POIROT, bridging the gap between
  raw intelligence and analytical application.    Together, these systems represent
  a shift toward graph-based, intelligence-driven detection and response. They emphasize
  the value of integrating real-time monitoring with structured threat intelligence
  and automation, setting the stage for more adaptive and effective cybersecurity
  operations.'
tags:
- provenance graphs
- threat hunting
- threat intelligence
- graph analytics
links:
- name: URL
  url: https://doi.org/10.1145/3716815.3729016
---
