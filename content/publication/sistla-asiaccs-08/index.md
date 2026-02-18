---
title: 'CMV: automatic verification of complete mediation for java virtual machines'
authors:
- A. Prasad Sistla
- V. N. Venkatakrishnan
- Michelle Zhou
- Hilary Branske
date: '2008-03-01'
publishDate: '2026-02-18T20:52:26.822908Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2008 ACM Symposium on Information, Computer and
  Communications Security, ASIACCS 2008, Tokyo, Japan, March 18-20, 2008*'
doi: 10.1145/1368310.1368327
abstract: Runtime monitoring systems play an important role in system security, and
  verification efforts that ensure that these systems satisfy certain desirable security
  properties are growing in importance. One such security property is complete mediation,
  which requires that sensitive operations are performed by a piece of code only after
  the monitoring system authorizes these actions. In this paper, we describe a verification
  technique that is designed to check for the satisfaction of this property directly
  on code from Java standard libraries. We describe a tool CMV that implements this
  technique and automatically checks shrink-wrapped Java bytecode for the complete
  mediation property. Experimental results on running our tool over several thousands
  of lines of bytecode from the Java libraries suggest that our approach is scalable,
  and leads to a very significant reduction in human efforts required for system verification.
tags:
- verification;model checking;runtime monitoring;stack inspection;Program analysis;
  formal methods
links:
- name: URL
  url: https://doi.org/10.1145/1368310.1368327
---
