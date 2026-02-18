---
title: 'Data Sandboxing: A Technique for Enforcing Confidentiality Policies'
authors:
- Tejas Khatiwala
- Raj Swaminathan
- V. N. Venkatakrishnan
date: '2006-12-01'
publishDate: '2026-02-18T20:52:26.861681Z'
publication_types:
- paper-conference
publication: '*22nd Annual Computer Security Applications Conference (ACSAC 2006),
  11-15 December 2006, Miami Beach, Florida, USA*'
doi: 10.1109/ACSAC.2006.22
abstract: "When an application reads private / sensitive information and subsequently
  communicates on an output channel such as a public file or a network connection,
  how can we ensure that the data written is free of private information? In this
  paper, we address this question in a practical setting through the use of a technique
  that we call ``data sandboxing'' . Essentially, data sandboxing is implemented using
  the popular technique of system call interposition to mediate output channels used
  by a program. To distinguish between private and public data, the program is partitioned
  into two: one that contains all the instructions that handle sensitive data and
  the other containing the rest of the instructions. This partitioning is performed
  based on techniques from program slicing. When run together, these two programs
  collectively replace the original program. To address confidentiality, these programs
  are sandboxed with different system call interposition based policies. We discuss
  the design and implementation of a tool that enforces confidentiality policies on
  C programs using this technique. We also report our experiences in using our tool
  over several programs that handle confidential data."
tags:
- runtime monitoring;sandboxing;information flow;Security policies;system call monitoring;confidentiality
links:
- name: URL
  url: https://doi.org/10.1109/ACSAC.2006.22
---
