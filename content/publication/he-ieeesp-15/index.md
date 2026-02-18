---
title: Vetting SSL Usage in Applications with SSLINT
authors:
- Boyuan He
- Vaibhav Rastogi
- Yinzhi Cao
- Yan Chen
- V. N. Venkatakrishnan
- Runqing Yang
- Zhenrui Zhang
date: '2015-05-01'
publishDate: '2026-02-18T20:52:26.581761Z'
publication_types:
- paper-conference
publication: '*2015 IEEE Symposium on Security and Privacy, SP 2015, San Jose, CA,
  USA, May 17-21, 2015*'
doi: 10.1109/SP.2015.38
abstract: Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols
  have become the security backbone of the Web and Internet today. Many systems including
  mobile and desktop applications are protected by SSL/TLS protocols against network
  attacks. However, many vulnerabilities caused by incorrect use of SSL/TLS APIs have
  been uncovered in recent years. Such vulnerabilities, many of which are caused due
  to poor API design and inexperience of application developers, often lead to confidential
  data leakage or man-in-the-middle attacks. In this paper, to guarantee code quality
  and logic correctness of SSL/TLS applications, we design and implement SSLINT, a
  scalable, automated, static analysis system for detecting incorrect use of SSL/TLS
  APIs. SSLINT is capable of performing automatic logic verification with high efficiency
  and good accuracy. To demonstrate it, we apply SSLINT to one of the most popular
  Linux distributions -- Ubuntu. We find 27 previously unknown SSL/TLS vulnerabilities
  in Ubuntu applications, most of which are also distributed with other Linux distributions.
tags:
- web security;static analysis; C language; vulnerability analysis;
links:
- name: URL
  url: https://doi.org/10.1109/SP.2015.38
---
