---
title: 'SELF: a transparent security extension for ELF binaries'
authors:
- Daniel C. DuVarney
- V. N. Venkatakrishnan
- Sandeep Bhatkar
date: '2003-08-01'
publishDate: '2026-02-18T20:52:26.908403Z'
publication_types:
- paper-conference
publication: '*Proceedings of the New Security Paradigms Workshop 2003, August 18-21,
  2002, Ascona, Switzerland*'
doi: 10.1145/986655.986661
abstract: The ability to analyze and modify binaries is often very useful from a security
  viewpoint. Security operations one would like to perform on binaries include the
  ability to extract models of program behavior and insert inline reference monitors.
  Unfortunately, the existing manner in which binary code is packaged prevents even
  the simplest of analyses, such as distinguishing code from data, from succeeding
  100 percent of the time. In this paper, we propose SELF, a security-enhanced ELF
  (Executable and Linking Format), which is simply ELF with an extra section added.
  The extra section contains information about (among other things) the address, size,
  and alignment requirements of each code and static data item in the program. This
  information is somewhat similar to traditional debugging information, but contains
  additional information specifically needed for binary analysis that debugging information
  lacks. It is also smaller, compatible with optimization, and less likely to facilitate
  reverse engineering, which we believe makes it practical for use with commercial
  software products. SELF approach has three key benefits. First, the information
  for the extra section is easy for compilers to provide, so little work is required
  on behalf of compiler vendors. Second, the extra section is ignored by default,
  so SELF binaries will run perfectly on all systems, including ones not interested
  in leveraging the extra information. Third, the extra section provides sufficient
  information to perform many security-related operations on the binary code. We believe
  SELF to be a practical approach, allowing many security analyses to be performed
  while not requiring major changes to the existing compiler infrastructure. An application
  example of the utility of SELF to perform address obfuscation (in which the addresses
  of all code and data items are randomized to defeat memory-error exploits) is presented.
tags:
- binary analysis;static analysis;compilers
links:
- name: URL
  url: https://doi.org/10.1145/986655.986661
---
