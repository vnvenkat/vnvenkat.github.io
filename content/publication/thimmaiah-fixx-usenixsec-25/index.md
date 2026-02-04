---
title: 'FIXX: finding exploits from examples'
authors:
- Neil P. Thimmaiah
- Yashashvi J. Dave
- Rigel Gjomemo
- V. N. Venkatakrishnan
date: '2025-01-01'
publishDate: '2026-02-04T17:45:23.867114Z'
publication_types:
- chapter
publication: '*Proceedings of the 34th USENIX Security Symposium*'
abstract: Comprehensively analyzing modern-day web applications to detect different
  vulnerabilities and related exploits is challenging and time-consuming. Security
  researchers spend significant time discovering and creating vulnerabilities and
  exploiting disclosures. However, such disclosures are often limited to single vulnerability
  instances and do not contain information about other instances of the same vulnerability
  in the application. In this paper, we propose FIXX, a tool that can automatically
  find multiple similar exploits from taint-style vulnerabilities inside the same
  PHP application. FIXX aims to help web application developers detect all possible
  instances of a known exploit within the program's code. To do this, FIXX combines
  novel notions of path and graph similarity over graph representations of code. We
  evaluate FIXX on 32 CVE reports containing cross-site scripting and SQL injection
  vulnerabilities associated with 19 PHP applications and discover 1097 similar exploitable
  paths leading to 10 new CVE entries.
---
