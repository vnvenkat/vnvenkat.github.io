---
title: 'One-Way Isolation: An Effective Approach for Realizing Safe Execution Environments'
authors:
- Weiqing Sun
- Zhenkai Liang
- V. N. Venkatakrishnan
- R. Sekar
date: '2005-02-01'
publishDate: '2026-02-18T20:52:26.892130Z'
publication_types:
- paper-conference
publication: '*Proceedings of the Network and Distributed System Security Symposium,
  NDSS 2005, San Diego, California, USA*'
abstract: "In this paper, we present an approach for realizing a safe execution environment
  (SEE) that enables users to ``try out'' new software (or configuration changes to
  existing software) without the fear of damaging the system in any manner. A key
  property of our SEE is that it faithfully reproduces the behavior of applications,
  as if they were running natively on the underlying host operating system. This is
  accomplished via one-way isolation: processes running within the SEE are given read-access
  to the environment provided by the host OS, but their write operations are prevented
  from escaping outside the SEE. As a result, SEE processes cannot impact the behavior
  of host OS processes, or the integrity of data on the host OS. Our SEE supports
  a wide range of tasks, including: study of malicious code, controlled execution
  of untrusted software, experimentation with software configuration changes, testing
  of software patches, and so on. It provides a convenient way for users to inspect
  system changes made within the SEE. If the user does not accept these changes, they
  can be rolled back at the click of a button. Otherwise, the changes can be ``committed
  '' so as to become visible outside the SEE. We provide consistency criteria that
  ensure semantic consistency of the committed results. We also develop an efficient
  technique for implementing the commit operation. Our implementation results show
  that most software, including fairly complex server and client applications, can
  run successfully within the SEE. The approach introduces low performance overheads,
  typically below 10%."
tags:
- sandboxing;isolated execution;operating systems;Security policies
links:
- name: URL
  url: 
    https://www.ndss-symposium.org/ndss2005/one-way-isolation-effective-approach-realizing-safe-execution-environments/
---
