---
title: 'DynaMiner: Leveraging Offline Infection Analytics for On-the-Wire Malware
  Detection'
authors:
- Birhanu Eshete
- V. N. Venkatakrishnan
date: '2017-06-01'
publishDate: '2026-02-18T20:52:26.518942Z'
publication_types:
- paper-conference
publication: '*47th Annual IEEE/IFIP International Conference on Dependable Systems
  and Networks*'
doi: 10.1109/DSN.2017.54
abstract: Web-borne malware continues to be a major threat on the Web. At the core
  of malware infection are for-crime toolkits that exploit vulnerabilities in browsers
  and their extensions. When a victim host gets infected, the infection dynamics is
  often buried in benign traffic, which makes the task of inferring malicious behavior
  a non-trivial exercise. In this paper, we leverage web conversation graph analytics
  to tap into the rich dynamics of the interaction between a victim and malicious
  host(s) without the need for analyzing exploit payload. Based on insights derived
  from infection graph analytics, we formulate the malware detection challenge as
  a graph-analytics based learning problem. The key insight of our approach is the
  payload-agnostic abstraction and comprehensive analytics of malware infection dynamics
  pre-, during-, and post-infection. Our technique leverages 3 years of infection
  intelligence spanning 9 popular exploit kit families. Our approach is implemented
  in a tool called DynaMiner and evaluated on infection and benign HTTP traffic. DynaMiner
  achieves a 97.3% true positive rate with false positive rate of 1.5%. Our forensic
  and live case studies suggest the effectiveness of comprehensive graph abstraction
  malware infection. In some instances, DynaMiner detected unknown malware 11 days
  earlier than existing AV engines.
tags:
- malware; intrusion detection; web security
links:
- name: URL
  url: https://doi.org/10.1109/DSN.2017.54
---
