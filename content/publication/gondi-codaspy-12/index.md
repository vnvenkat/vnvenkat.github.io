---
title: 'SWIPE: eager erasure of sensitive data in large scale systems software'
authors:
- Kalpana Gondi
- Prithvi Bisht
- Praveen Venkatachari
- A. Prasad Sistla
- V. N. Venkatakrishnan
date: '2012-02-01'
publishDate: '2026-02-18T20:52:26.686168Z'
publication_types:
- paper-conference
publication: '*Second ACM Conference on Data and Application Security and Privacy,
  CODASPY 2012, San Antonio, TX, USA, February 7-9, 2012*'
doi: 10.1145/2133601.2133638
abstract: 'We describe SWIPE, an approach to reduce the life time of sensitive, memory
  resident data in large scale applications written in C. In contrast to prior approaches
  that used a delayed or lazy approach to the problem of erasing sensitive data, SWIPE
  uses a novel eager erasure approach that minimizes the risk of accidental sensitive
  data leakage. SWIPE achieves this by transforming a legacy C program to include
  additional instructions that erase sensitive data immediately after its intended
  use. SWIPE is guided by a highly-scalable static analysis technique that precisely
  identifies the locations to introduce erase instructions in the original program.
  The programs transformed using SWIPE enjoy several additional benefits: minimization
  of leaks that arise due to data dependencies; erasure of sensitive data with minimal
  developer guidance; and negligible performance overheads.'
tags:
- confidentiality; sensitive data leaks; verification;Program analysis;program transformation;Code
  retrofitting
links:
- name: URL
  url: https://doi.org/10.1145/2133601.2133638
---
