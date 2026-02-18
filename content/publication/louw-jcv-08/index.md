---
title: Enhancing web browser security against malware extensions
authors:
- Mike Ter Louw
- Jin Soon Lim
- V. N. Venkatakrishnan
date: '2008-08-01'
publishDate: '2026-02-18T20:52:26.807469Z'
publication_types:
- article-journal
publication: '*J. Comput. Virol.*'
doi: 10.1007/S11416-007-0078-5
abstract: "In this paper we examine security issues of functionality extension mechanisms
  supported by web browsers. Extensions (or ``plug-ins'') in modern web browsers enjoy
  unrestrained access at all times and thus are attractive vectors for malware. To
  solidify the claim, we take on the role of malware writers looking to assume control
  of a user's browser space. We have taken advantage of the lack of security mechanisms
  for browser extensions and implemented a malware application for the popular Firefox
  web browser, which we call browserSpy, that requires no special privileges to be
  installed. browserSpy takes complete control of the user's browser space, can observe
  all activity performed through the browser and is undetectable. We then adopt the
  role of defenders to discuss defense strategies against such malware. Our primary
  contribution is a mechanism that uses code integrity checking techniques to control
  the extension installation and loading process. We describe two implementations
  of this mechanism: a drop-in solution that employs JavaScript and a faster, in-browser
  solution that makes uses of the browser's native cryptography implementation. We
  also discuss techniques for runtime monitoring of extension behavior to provide
  a foundation for defending threats posed by installed extensions."
tags:
- browser security; web security; attacks; browser extension; code integrity
links:
- name: URL
  url: https://doi.org/10.1007/s11416-007-0078-5
---
