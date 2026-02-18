---
title: Enforcement techniques for expressive security policies
authors:
- V. N. Venkatakrishnan
date: '2004-11-01'
publishDate: '2026-02-18T20:52:26.463390Z'
publication_types:
- thesis
publication: '*Ph.D. Thesis*'
doi: 10.5555/1087562
abstract: Execution monitoring is a powerful practical technique for enforcement of
  security policies. In this dissertation, we discuss some of the limitations of existing
  execution monitoring mechanisms, and develop new techniques that suitably adapt
  execution monitoring approaches for enforcement of security policies that address
  confidentiality and integrity of information. In situations where enforcement of
  policies that address confidentiality and integrity requirements could be directly
  specified in terms of resource access operations, our execution monitoring approach
  supports a richer class of access control policies (that support notions such as
  access history and resource accounting). However, there may exist situations where
  such requirements cannot simply be addressed by access control. We present two such
  scenarios and discuss enforcement techniques for these scenarios. The first scenario
  is one that involves execution of a faulty program (e.g., a freeware file compression
  utility) or an untrusted program, operating on system or application data. In this
  case, access control or conventional execution monitoring techniques do not work,
  as they typically disallow execution any such operations (e.g., modifications to
  such files) in the first place. We present a solution that is based on program isolation,
  that works by isolating the effects of the faulty/untrusted program execution from
  the rest of the system. The second scenario relates data and control flow errors
  in a program that operates on sensitive data, resulting in loss of data confidentiality.
  Here too, it is well known that the problem cannot be solved by the use of execution
  monitors that employ purely runtime monitoring mechanisms. The key idea is to augment
  execution monitoring mechanisms with information obtained by static analysis of
  the program. By using a preliminary static analysis to analyze possible information
  flows in a program, and by combining this analysis with runtime checking techniques,
  a more precise solution is possible. In all the scenarios mentioned above, we illustrate
  the approaches that are employed using several practical examples. Finally, we describe
  a model-based certification mechanism for enforcement of privacy properties.
tags:
- runtime monitoring;Security policies;isolated execution;mobile code;sandboxing;information
  flow
links:
- name: URL
  url: https://dl.acm.org/doi/10.5555/1087562
---
