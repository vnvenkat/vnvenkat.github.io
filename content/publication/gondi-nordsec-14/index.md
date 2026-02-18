---
title: 'DEICS: Data Erasure in Concurrent Software'
authors:
- Kalpana Gondi
- A. Prasad Sistla
- V. N. Venkatakrishnan
date: '2014-10-01'
publishDate: '2026-02-18T20:52:26.654874Z'
publication_types:
- paper-conference
publication: '*19th Nordic Conference on Secure IT Systems*'
doi: 10.1007/978-3-319-11599-3_3
abstract: A well-known tenet for ensuring unauthorized leaks of sensitive data such
  as passwords and cryptographic keys is to erase (''zeroize'') them after their intended
  use in any program. Prior work on minimizing sensitive data lifetimes has focused
  exclusively on sequential programs. In this work, we address the problem of data
  lifetime minimization for concurrent programs. We develop a new algorithm that precisely
  anticipates when to introduce these erasures, and develop an implementation of this
  algorithm in a tool called DEICS. Through an experimental evaluation, we show that
  DEICS is able to reduce lifetimes of shared sensitive data in several concurrent
  applications (over 100k lines of code combined) with minimal performance overheads.
tags:
- confidentiality; sensitive data leaks; verification;Program analysis;program transformation;Code
  retrofitting; concurrent applications
links:
- name: URL
  url: https://doi.org/10.1007/978-3-319-11599-3_3
---
