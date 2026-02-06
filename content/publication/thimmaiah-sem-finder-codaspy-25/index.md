---
title: 'SemFinder: A Semantics-Based Approach to Enhance Vulnerability Analysis in
  Web Applications'
authors:
- Neil P. Thimmaiah
- Rigel Gjomemo
- V.N. Venkatakrishnan
date: '2025-06-01'
publishDate: '2026-02-05T01:07:30.661605Z'
publication_types:
- paper-conference
publication: '*Proceedings of the Fifteenth ACM Conference on Data and Application
  Security and Privacy*'
doi: 10.1145/3714393.3726513
abstract: Modern web applications are becoming increasingly complex. They include
  multiple dynamic runtime constructs that are difficult to analyze by static application
  security testing (SAST) tools. These tools often use a graph representation of the
  code for their analysis. However, built statically, such graphs may miss important
  data and control flows dependent on runtime information. In addition, the presence
  of difficult-to-analyze code patterns in modern web applications, referred to as
  testability tarpits, further reduces the accuracy of statically built graphs. As
  a result, current SAST tools have several false negatives because of 'hidden' paths,
  which are not present in the graphs. In this paper, we present SemFinder, an approach
  designed to automatically detect such hidden paths. SemFinder uses natural language
  semantics to hypothesize connections between different locations in the code based
  on the meaning and similarity of the variables in those locations and test those
  hypotheses dynamically. We evaluate SemFinder on 30 PHP applications and discover
  215 new exploitable hidden paths with respect to existing SAST tools, leading to
  the submission of 31 new CVEs.
tags:
- PHP
- software analysis
- web application security
links:
- name: URL
  url: https://doi.org/10.1145/3714393.3726513
---
