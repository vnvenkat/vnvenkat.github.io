---
title: GAMEPLAY
date: 2018-08-16
links:
  - type: site
    url: https://today.uic.edu/uic-to-lead-3m-initiative-to-develop-system-to-identify-patch-software-security-holes/
tags:
  - Software-Development
  - CyberReasoning
  - Vulnerability-Analysis
---

We design, develop, and evaluate  a system called GAMEPLAY (Graph Analysis for Mechanized Exploit-generation and vulnerability Patching Leveraging human Assistance for improved Yield), the goals of which are to identify software security holes and perform vulnerability patching for a large class of common security vulnerabilities in software applications.In the field of cybersecurity, there is an ongoing arms race between   black hat criminal hackers and whitehat ethical hackers. GAMEPLAY intends to provide the much needed fundamental research and technological advances that are needed to tip the balance in favor of whitehat ethical hackers.

GAMEPLAY's key technical contributions are in its integrated, language-agnostic exploit-generation platform  along with a sophisticated analysis system that can work with humans-in-the-loop to close the semantic and contextual gaps that arise in software vulnerability analysis and patching tasks.

GAMEPLAY will offer a leap forward in the automated exploit generation challenge, which today is less systematized and operates with `bits and pieces' of heuristics and hints that are coded into the various tools.  Today's strategies, developed by various research and industry groups,  do not offer a comprehensive solution for closing the gaps that arise in practical exploit generation and software patching. Such issues include analysis gaps, path explosion, approximations, false positives, false negatives, and scalability.  As a result, exploit generation tools that have to explore the space of all possible test inputs return exploits only on the occasions when their heuristics are successful. Consequently, current exploit-generation tools continue to remain `best effort' tools, instead of being able to provide some higher level of assurance about the absence of vulnerabilities. GAMEPLAY will extend the state-of-art in exploit generation by leveraging the humans-in-the-loop to close the gaps in existing analysis and neutralize the vulnerabilities identified through automated patching methods. 

This project is will perform fundamental, non-classified research and will cost about three million dollars ($3,005,142) for a duration of four years. The project will be a collaboration between the University of Illinois at Chicago (UIC), the Johns Hopkins University, and the University of Texas at Dallas.  UIC will be the prime contractor to DoD, and the other organizations will be sub-contractors to UIC.  

The team of researchers represented in this project has considerable experience in the area of vulnerability analysis, exploit generation, binary as well as source analysis, software transformation,  and formal methods. They have a proven track record of working together on large-scale efforts (including prior NSF and DoD projects) and have successfully fielded their technologies in the US DoD and at DARPA engagements.  

The starting point for GAMEPLAY is an advanced exploit-generation framework developed from UIC's prior work NAVEX (which won a distinguished paper award at USENIX Security 2018) as well the extensive experience of the PIs in vulnerability analysis and patching (over three dozen papers at top conference venues in the past decade on the various aspects of vulnerability analysis).  From this starting point, we propose a multi-tier, source language-agnostic analysis and transformation strategy. Specifically, we will design and implement three technology layers:

A  front-end  consisting of a static, pre-processing phase will first transform the challenge-source into a well-structured, intermediate graph representation  that is stored in a graph database.  The standardized form has the advantage of being language-neutral and significantly easier to analyze and patch by later phases, possibly in real-time as new vulnerabilities manifest. A key innovation here is the augmentation of binary code information into this intermediate representation. 
A second, middle-end that implements an analysis engine that will analyze the intermediate representation with a variety of code analyses, including taint analysis and engage the use of constraint solvers and proof assistants. During this analysis process, the human-machine interface will be employed heavily, to leverage from the insights provided by expert and novice hackers as well as non-hackers.  These analyses will be conducted with reference to a formal specification that will be authored to express the general classes of vulnerabilities addressed by the system, leading to the discovery of possible flows that realize these vulnerabilities, and inputs (proofs of vulnerability) that demonstrate them, and could, therefore, be used in an attack.
A final back-end that consists of a patching phase that aims to synthesize and inject new security guard programming into vulnerable flows to prevent the identified vulnerabilities from being exercised in future.

GAMEPLAY addresses a pressing need in both government and industry for more rapid vulnerability identification and patching response strategies that can scale with the increasing speed and scope of modern cyber-warfare campaigns that target networked software.  Our proposed research will enable the DoD to (a) detect and identify vulnerabilities that are missed today (b) detect vulnerabilities faster and earlier in their evolution, (c) formulate and implement a scalable approach to  neutralization the identified  vulnerabilities with novel software patching methods and (d) enable sharing of identified software vulnerabilities    with government agencies and enterprises. We will explore both open source and commercialization plans for technology transfer.

<!--more-->
