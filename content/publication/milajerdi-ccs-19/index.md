---
title: 'POIROT: Aligning Attack Behavior with Kernel Audit Records for Cyber Threat
  Hunting'
authors:
- Sadegh M. Milajerdi
- Birhanu Eshete
- Rigel Gjomemo
- V. N. Venkatakrishnan
date: '2019-11-01'
publishDate: '2026-02-18T20:52:26.487566Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2019 ACM SIGSAC Conference on Computer and Communications
  Security*'
doi: 10.1145/3319535.3363217
abstract: Cyber threat intelligence (CTI) is being used to search for indicators of
  attacks that might have compromised an enterprise network for a long time without
  being discovered. To have a more effective analysis, CTI open standards have incorporated
  descriptive relationships showing how the indicators or observables are related
  to each other. However, these relationships are either completely overlooked in
  information gathering or not used for threat hunting. In this paper, we propose
  a system, called POIROT, which uses these correlations to uncover the steps of a
  successful attack campaign. We use kernel audits as a reliable source that covers
  all causal relations and information flows among system entities and model threat
  hunting as an inexact graph pattern matching problem. Our technical approach is
  based on a novel similarity metric which assesses an alignment between a query graph
  constructed out of CTI correlations and a provenance graph constructed out of kernel
  audit log records. We evaluate POIROT on publicly released real-world incident reports
  as well as reports of an adversarial engagement designed by DARPA, including ten
  distinct attack campaigns against different OS platforms such as Linux, FreeBSD,
  and Windows. Our evaluation results show that POIROT is capable of searching inside
  graphs containing millions of nodes and pinpoint the attacks in a few minutes, and
  the results serve to illustrate that CTI correlations could be used as robust and
  reliable artifacts for threat hunting.
tags:
- cyber threat-hunting; provenance graphs; audit logs; graph analytics; cyber threat
  intelligence
links:
- name: URL
  url: https://doi.org/10.1145/3319535.3363217
---
