---
title: Static Detection and Automatic Exploitation of Intent Message Vulnerabilities
  in Android Applications
authors:
- Daniele Gallingani
- Rigel Gjomemo
- V. N. Venkatakrishnan
- Stefano Zanero
date: '2015-05-01'
publishDate: '2026-02-18T20:52:26.410385Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2015 IEEE Mobile Security Technologies (MoST)*'
abstract: Android's Inter-Component Communication (ICC) mechanism strongly relies
  on Intent messages. Unfortunately, due to the lack of message origin verification
  in Intents, implementing security policies based on message sources is hard in practice,
  and completely relies on the programmer's skill and attention. In this paper, we
  present a framework for automatically detecting Intent input validation vulnerabilities.
  We are thus able to highlight component fragments that expose vulnerable resources
  to possible malicious message senders. Most importantly, we advance the state of
  the art by developing a method to automatically demonstrate whether the identified
  vulnerabilities can be exploited or not, adopting a formal approach to automatically
  produce malicious payloads that can trigger dangerous behavior in vulnerable applications.
  We therefore eliminate the high rate of false positives common in previously applied
  methods. We test our methods on a representative sample of applications, and we
  find that 29 out of 64 tested applications are detected as potentially vulnerable,
  while 26 out of 29 can be automatically proven to be exploitable. Our experiments
  demonstrate the lack of exhaustive sanity checks when receiving messages from unknown
  sources, and stress the underestimation of this problem in real world application
  development.
tags:
- mobile security;Android Security;vulnerability analysis;attacks
url_pdf: https://www.ieee-security.org/TC/SPW2015/MoST/papers/s3p1.pdf
---
