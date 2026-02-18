---
title: 'Isolated Program Execution: An Application Transparent Approach for Executing
  Untrusted Programs'
authors:
- Zhenkai Liang
- V. N. Venkatakrishnan
- R. Sekar
date: '2003-12-01'
publishDate: '2026-02-18T20:52:26.900350Z'
publication_types:
- paper-conference
publication: '*19th Annual Computer Security Applications Conference (ACSAC 2003),
  8-12 December 2003, Las Vegas, NV, USA*'
doi: 10.1109/CSAC.2003.1254323
abstract: In this paper, we present a new approach for safe execution of untrusted
  programs  by isolating their effects fromthe rest of the system. Isolation is achieved
  by interceptingfile operations made by untrusted processes, and redirecting any
  change operations to a \"modification cachel\" thatis invisible to other processes
  in the system. File read operations performed by the untrusted process are also
  correspondingly modified, so that the process has a consistentview of system state
  that incorporates the contents of the filesystem as well as the modification cache.
  On termination ofthe untrusted process, its user is presented with a concisesummary
  of the files modified by the process. Additionally,the user can inspect these files
  using various software utilities (e.g., helper applications to view multimedia files)
  todetermine if the modifications are acceptable. The user thenhas the option to
  commit these modifications, or simply discard them. Essentially, our approach provides
  \"play\" and\"rewind\" buttons for running untrusted software. Key benefits of our
  approach are that it requires no changes to theuntrusted programs (to be isolated)
  or the underlying operating system; it cannot be subverted by malicious programs;and
  it achieves these benefits with acceptable runtime overheads. We describe a prototype
  implementation of this system for Linux called Alcatraz and discuss its performanceand
  effectiveness.
tags:
- runtime monitoring;sandboxing;isolated execution;Software installation;
links:
- name: URL
  url: https://doi.org/10.1109/CSAC.2003.1254323
---
