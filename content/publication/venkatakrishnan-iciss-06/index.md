---
title: Provably Correct Runtime Enforcement of Non-interference Properties
authors:
- V. N. Venkatakrishnan
- Wei Xu
- Daniel C. DuVarney
- R. Sekar
date: '2006-12-01'
publishDate: '2026-02-18T20:52:26.869489Z'
publication_types:
- paper-conference
publication: '*Information and Communications Security, 8th International Conference,
  ICICS 2006, Raleigh, NC, USA, December 4-7, 2006, Proceedings*'
doi: 10.1007/11935308_24
abstract: Non-interference has become the standard criterion for ensuring confidentiality
  of sensitive data in the information flow literature. However, application of non-interference
  to software systems has been limited in practice. This is partly due to the imprecision
  that is inherent in static analyses that have formed the basis of previous non-interference
  based techniques. Runtime approaches can be significantly more accurate than static
  analysis, and have been more successful in practical systems that reason about information
  flow. However, these techniques only reason about explicit information flows that
  take place via assignments in a program. Implicit flows that take place without
  involving assignments, and can be inferred from the structure and/or semantics of
  the program, are missed by runtime techniques. This paper seeks to bridge the gap
  between the accuracy provided by runtime techniques and the completeness provided
  by static analysis techniques. In particular, we develop a hybrid technique that
  relies primarily on runtime information-flow tracking, but augments it with static
  analysis to reason about implicit flows that arise due to unexecuted paths in a
  program. We prove that the resulting technique preserves non-interference.
tags:
- information flow;runtime monitoring; Program analysis;program transformation;Security
  policies;non-interference
links:
- name: URL
  url: https://doi.org/10.1007/11935308_24
---
