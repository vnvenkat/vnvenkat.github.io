---
title: 'Model-carrying code: a practical approach for safe execution of untrusted
  applications'
authors:
- R. Sekar
- V. N. Venkatakrishnan
- Samik Basu
- Sandeep Bhatkar
- Daniel C. DuVarney
date: '2003-10-01'
publishDate: '2026-02-18T20:52:26.916722Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 19th ACM Symposium on Operating Systems Principles
  2003, SOSP 2003, Bolton Landing, NY, USA, October 19-22, 2003*'
doi: 10.1145/945445.945448
abstract: This paper presents a new approach called model-carrying code (MCC) for
  safe execution of untrusted code. At the heart of MCC is the idea that untrusted
  code comes equipped with a concise high-level model of its security-relevant behavior.
  This model helps bridge the gap between high-level security policies and low-level
  binary code, thereby enabling analyses which would otherwise be impractical. For
  instance, users can use a fully automated verification procedure to determine if
  the code satisfies their security policies. Alternatively, an automated procedure
  can sift through a catalog of acceptable policies to identify one that is compatible
  with the model. Once a suitable policy is selected, MCC guarantees that the policy
  will not be violated by the code. Unlike previous approaches, the MCC framework
  enables code producers and consumers to collaborate in order to achieve safety.
  Moreover, it provides support for policy selection as well as enforcement. Finally,
  MCC makes no assumptions regarding the inherent risks associated with untrusted
  code. It simply provides the tools that enable a consumer to make informed decisions
  about the risk that he/she is willing to tolerate so as to benefit from the functionality
  offered by an untrusted application.
tags:
- mobile code;verification;model checking;system call monitoring;Security policies;formal
  methods
links:
- name: URL
  url: https://doi.org/10.1145/945445.945448
---
