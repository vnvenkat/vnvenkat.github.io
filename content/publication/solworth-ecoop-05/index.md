---
title: Programming language based analysis for lifting to an operating system's access
  control model
authors:
- Jon Solworth
- V. N. Venkatakrishnan
date: '2005-07-01'
publishDate: '2026-02-18T20:52:26.455806Z'
publication_types:
- paper-conference
publication: '*ECOOP Workshop on Programming Languages and Operating Systems*'
abstract: Traditionally, operating systems have employed Discretionary Access Controls
  (DACs) as their authorization model. We have implemented a new authorization model
  called kernelsec, which provides a much richer set of controls than DACs and thus
  provides more refined protections. In this paper, we describe a programming language-based
  analysis to ``lift'' the existing application base from the Linux DAC to the kernelsec
  authorization model.   The authorization model, which is part of the Operating System
  (OS) Kernel, controls a process's external interaction by allowing or denying operations
  requested by the process. In a traditional DAC authorization model, the user who
  created an object, such as a file, is the owner of that object and determines who
  can access the object. Unfortunately, DAC models are incapable of providing strong
  security properties, leading to a culture of ``blame the user'' when something goes
  wrong.  An alternative is to provide Mandatory Access Controls (MACs) which can
  enforce organizational rules We note that Role-Based Access Controls (RBAC)  and
  SPBAC  can provide either DAC or MAC. MACs can be integrated with DACs by allowing
  the user to decide permissions that are not mandated by the organization. This paper
  explores some of the issues in transitioning from a DAC-based to a MAC-based authorization
  model and the role compilers and programming languages can play.
tags:
- Program analysis; operating systems
---
