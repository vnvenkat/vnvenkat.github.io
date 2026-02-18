---
title: 'CANDID: Dynamic candidate evaluations for automatic prevention of SQL injection
  attacks'
authors:
- Prithvi Bisht
- Parthasarathy Madhusudan
- V. N. Venkatakrishnan
date: '2010-02-01'
publishDate: '2026-02-18T20:52:26.738297Z'
publication_types:
- article-journal
publication: '*ACM Transactions on Information Systems Security*'
doi: 10.1145/1698750.1698754
abstract: SQL injection attacks are one of the top-most threats for applications written
  for the Web. These attacks are launched through specially crafted user inputs, on
  Web applications that use low-level string operations to construct SQL queries.
  In this work, we exhibit a novel and powerful scheme for automatically transforming
  Web applications to render them safe against all SQL injection attacks. A characteristic
  diagnostic feature of SQL injection attacks is that they change the intended structure
  of queries issued. Our technique for detecting SQL injection is to dynamically mine
  the programmer-intended query structure on any input, and detect attacks by comparing
  it against the structure of the actual query issued. We propose a simple and novel
  mechanism, called Candid, for mining programmer intended queries by dynamically
  evaluating runs over benign candidate inputs. This mechanism is theoretically well
  founded and is based on inferring intended queries by considering the symbolic query
  computed on a program run. Our approach has been implemented in a tool called Candid
  that retrofits Web applications written in Java to defend them against SQL injection
  attacks. We have also implemented Candid by modifying a Java Virtual Machine, which
  safeguards applications without requiring retrofitting. We report extensive experimental
  results that show that our approach performs remarkably well in practice.
tags:
- SQL injection;Program analysis;program transformation;Code retrofitting;symbolic
  evaluation;runtime monitoring;virtual machine
links:
- name: URL
  url: https://doi.org/10.1145/1698750.1698754
---
