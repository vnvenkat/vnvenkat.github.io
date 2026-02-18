---
title: Expanding Malware Defense by Securing Software Installations
authors:
- Weiqing Sun
- R. Sekar
- Zhenkai Liang
- V. N. Venkatakrishnan
date: '2008-07-01'
publishDate: '2026-02-18T20:52:26.837740Z'
publication_types:
- paper-conference
publication: '*Detection of Intrusions and Malware, and Vulnerability Assessment,
  5th International Conference, DIMVA 2008, Paris, France, July 10-11, 2008. Proceedings*'
doi: 10.1007/978-3-540-70542-0_9
abstract: "Software installation provides an attractive entry vector for malware:
  since installations are performed with administrator privileges, malware can easily
  get the enhanced level of access needed to install backdoors, spyware, rootkits,
  or ``bot'' software, and to hide these installations from users. Previous research
  has been focused mainly on securing the execution phase of untrusted software, while
  largely ignoring the safety of installations. Even security-enhanced operating systems
  such as SELinux and Vista don't usually impose restrictions during software installs,
  expecting the system administrator to ``know what she is doing.'' This paper addresses
  this ``gap in armor'' by securing software installations. Our technique can support
  a diversity of package managers and software installers. It is based on a framework
  that simplifies the development and enforcement of policies that govern safety of
  installations. We present a simple policy that can be used to prevent untrusted
  software from modifying any of the files used by benign software packages, thus
  blocking the most common mechanism used by malware to ensure that it is run automatically
  after each system reboot. While the scope of our technique is limited to the installation
  phase, it can be easily combined with approaches for secure execution, e.g., by
  ensuring that all future runs of an untrusted package will take place within an
  administrator-specified sandbox. Our experimental evaluation has considered over
  one hundred benign and untrusted software packages. Our technique was able to block
  malicious packages among these without breaking non-malicious ones."
tags:
- Software installation;isolated execution;sandboxing;runtime monitoring
links:
- name: URL
  url: https://doi.org/10.1007/978-3-540-70542-0_9
---
