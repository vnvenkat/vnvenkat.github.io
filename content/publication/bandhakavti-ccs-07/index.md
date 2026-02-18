---
title: 'CANDID: preventing sql injection attacks using dynamic candidate evaluations'
authors:
- Sruthi Bandhakavi
- Prithvi Bisht
- P. Madhusudan
- V. N. Venkatakrishnan
date: '2007-10-01'
publishDate: '2026-02-18T20:52:26.845923Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2007 ACM Conference on Computer and Communications
  Security, CCS 2007, Alexandria, Virginia, USA, October 28-31, 2007ACM Conference
  on Computer and Communications Security, CCS 2007, Alexandria, Virginia, USA, October
  28-31, 2007*'
doi: 10.1145/1315245.1315249
abstract: SQL injection attacks are one of the topmost threats for applications written
  for the Web. These attacks are launched through specially crafted user input on
  web applications that use low level string operations to construct SQL queries.
  In this work, we exhibit a novel and powerful scheme for automatically transforming
  web applications to render them safe against all SQL injection attacks. A characteristic
  diagnostic feature of SQL injection attacks is that they change the intended structure
  of queries issued. Our technique for detecting SQL injection is to dynamically mine
  the programmer-intended query structure on any input, and to detect attacks by comparing
  them against the intended query structure. We propose a simple and novel mechanism,
  called Candid, for mining programmer intended queries by dynamically evaluating
  runs over benign candidate inputs. This mechanism is theoretically well founded
  and is based on inferring intended queries by considering the symbolic query computed
  on a program run. Our approach has been implemented in a tool called Candid that
  retrofits Web applications written in Java to defend them against SQL injection
  attacks. We report extensive experimental results that show that our approach performs
  remarkably well in practice.
tags:
- SQL injection;Program analysis;program transformation;Code retrofitting;symbolic
  evaluation;runtime monitoring
links:
- name: URL
  url: https://doi.org/10.1145/1315245.1315249
---
