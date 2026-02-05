---
title: Scaling JavaScript Abstract Interpretation to Detect and Exploit Node.js Taint-style
  Vulnerability
authors:
- Mingqing Kang
- Yichao Xu
- Song Li
- Rigel Gjomemo
- Jianwei Hou
- V. N. Venkatakrishnan
- Yinzhi Cao
date: '2023-05-01'
publishDate: '2026-02-05T01:07:30.683753Z'
publication_types:
- paper-conference
publication: '*2023 IEEE Symposium on Security and Privacy (SP)*'
doi: 10.1109/SP46215.2023.10179352
abstract: Taint-style vulnerabilities, such as OS command injection and path traversal,
  are common and severe software weaknesses. There exists an inherent trade-off between
  analysis scalability and accuracy in detecting such vulnerabilities. On one hand,
  existing syntax-directed approaches often make compromises in the analysis accuracy
  on dynamic features like bracket syntax. On the other hand, existing abstract interpretation
  often faces the issue of state explosion in the abstract domain, thus leading to
  a scalability problem.In this paper, we present a novel approach, called FAST, to
  scale the vulnerability discovery of JavaScript packages via a novel abstract interpretation
  approach that relies on two new techniques, called bottom-up and top-down abstract
  interpretation. The former abstractly interprets functions based on scopes instead
  of call sequences to construct dynamic call edges. Then, the latter follows specific
  control-flow paths and prunes the program to skip statements unrelated to the sink.
  If an end-to-end data-flow path is found, FAST queries the satisfiability of constraints
  along the path and verifies the exploitability to reduce human efforts.We implement
  a prototype of FAST and evaluate it against real-world Node.js packages. We show
  that FAST is able to find 242 zero-day vulnerabilities in NPM with 21 CVE identifiers
  being assigned. Our evaluation also shows that FAST can scale to real-world applications
  such as NodeBB and popular frameworks such as total.js and strapi in finding legacy
  vulnerabilities that no prior works can.
tags:
- Privacy;Scalability;Prototypes;Syntactics;Software;Explosions;Security;Node.js;Abstract-Interpretation;Vulnerability-Detection
---
