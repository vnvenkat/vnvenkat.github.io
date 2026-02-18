---
title: 'CoBrA: Context-, Branch-sensitive Static Analysis for Detecting Taint-style
  Vulnerabilities in PHP Web Applications,'
authors:
- Yichao Xu
- Mingqing Kang
- Neil Thimmaiah
- Rigel Gjomemo
- V. N. Venkatakrishnan
- Yinzhi Cao
date: '2026-04-01'
publishDate: '2026-02-18T20:52:26.402241Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 48th International Conference on Software Engineering*'
abstract: "PHP, a widely-used programming language in Web development, contains powerful
  dynamic features (e.g., dynamic function name construction), making static detection
  of taint-style vulnerabilities like SQL injection and Cross-Site Scripting challenging.
  State-of-the-art static approaches perform call graph-guided backward dataflow tracking,
  thus failing to analyze those dynamic PHP features like variable functions and control
  change statements, which results in high false positives and negatives. In this
  paper, we design and implement CoBrA, a context-, branch-sensitive approach to detect
  taint-style vulnerabilities in PHP-based Web applications. The key innovations are
  the abstract domain graph (ADG), which is used to efficiently guide the analysis
  and ``stretch-relax'' algorithm, which enables accurate resolution of PHP dynamic
  features and efficient inter-procedural taint propagation. Our evaluation of CoBrA's
  prototype identified 54 zero-day vulnerabilities in 19 real-world applications with
  eight Common Vulnerabilities and Exposures (CVE) identifiers assigned, achieved
  $88.66%$ detection rate with under $0.3%$ false positives on a PHP tarpits dataset,
  and outperformed four state-of-the-art tools across all test datasets with reasonable
  time and space consumption. "
tags:
- vulnerability analysis; PHP analysis; static analysis; web application security
links:
- name: URL
  url: 
    https://conf.researchr.org/details/icse-2026/icse-2026-research-track/153/CoBrA-Context-Branch-sensitive-Static-Analysis-for-Detecting-Taint-style-Vulnerabi
---
