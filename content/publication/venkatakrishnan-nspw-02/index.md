---
title: Empowering mobile code using expressive security policies
authors:
- V. N. Venkatakrishnan
- Ram Peri
- R. Sekar
date: '2002-09-01'
publishDate: '2026-02-18T20:52:26.932119Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2002 Workshop on New Security Paradigms, Virginia
  Beach, VA, USA, September 23-26, 2002*'
doi: 10.1145/844102.844113
abstract: Existing approaches for mobile code security tend to take a conservative
  view that mobile code is inherently risky, and hence focus on confining it. Such
  confinement is usually achieved using access control policies that restrict mobile
  code from taking any action that can potentially be used to harm the host system.
  While such policies can be helpful in keeping \"bad applets\" in check, they preclude
  a large number of useful applets. We therefore take an alternative view of mobile
  code security, one that is focused on empowering mobile code rather than disabling
  it. We propose an approach wherein highly expressive security policies provide the
  basis for such empowerment, while greatly mitigating the risks posed to the host
  system by such code. Our policies are represented as extended finite state automata,
  (a generalization of the finite-state automata to permit the use of variables) that
  can enforce these policies efficiently. We have built a prototype implementation
  of our approach for Java. Our implementation is based on rewriting Java byte code
  so that security-relevant events are intercepted and forwarded to the policy enforcement
  automata before they are executed. Early experimental results indicate that such
  expressive, enabling policies can be supported with low overheads.
tags:
- mobile code;Security policies;runtime monitoring
links:
- name: URL
  url: https://doi.org/10.1145/844102.844113
---
