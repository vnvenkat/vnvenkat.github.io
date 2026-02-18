---
title: 'WAVES: Automatic Synthesis of Client-Side Validation Code for Web Applications'
authors:
- Nazari Skrupsky
- Maliheh Monshizadeh
- Prithvi Bisht
- Timothy L. Hinrichs
- V. N. Venkatakrishnan
- Lenore D. Zuck
date: '2012-12-01'
publishDate: '2026-02-18T20:52:26.693824Z'
publication_types:
- paper-conference
publication: '*2012 ASE International Conference on Cyber Security*'
doi: 10.1109/CYBERSECURITY.2012.13
abstract: The current practice of web application development treats the client and
  server components of the application as two separate but interacting pieces of software.
  Each component is written independently, usually in distinct programming languages
  and development platforms --- a process known to be prone to errors when the client
  and server share application logic. When the client and server are out of sync,
  an ``impedance mismatch'' occurs, often leading to software vulnerabilities as demonstrated
  by recent work on parameter tampering. This paper outlines the groundwork for a
  new software development approach, WAVES, where developers author the server-side
  application logic and rely on tools to automatically synthesize the corresponding
  clientside application logic. WAVES employs program analysis techniques to extract
  a logical specification from the server, from which it synthesizes client code.
  WAVES also synthesizes interactive client interfaces that include asynchronous callbacks
  whose performance and coverage rival that of manually written clients while ensuring
  no new security vulnerabilities are introduced. The effectiveness of WAVES is demonstrated
  and evaluated on three real-world web applications.
tags:
- parameter tampering;web application security;program synthesis;
links:
- name: URL
  url: https://doi.org/10.1109/CyberSecurity.2012.13
---
