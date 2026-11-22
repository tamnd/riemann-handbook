---
title: The status of the claim
---
## What a Lean proof gives

Lean checks a proof with a small program, the kernel. When the kernel accepts a theorem, the theorem follows from its axioms. This is a strong guarantee, but it depends on four things. The source must be the release. The proof must use only the standard axioms. No program may change the environment around the kernel. And the Lean statement must say what a mathematician means by the theorem.

## What is checked

| Question | Answer now |
|---|---|
| Is the source the same as the release? | Yes. Each of the 175,190 files matches the published hashes. |
| Does the project build? | Not known. The build needs thousands of hours of computer time. A sample of 299 modules built with no errors. |
| Which axioms does the proof use? | Not known until the build is done. |
| Does a second checker accept the proof? | Not known until the build is done. |
| Do the Lean statements say what the standard statements say? | The top statement does. Most others are not checked by a person. |

The page [What is checked](https://riemann.tamnd.com/trust/) on the site has the current answers.

## What this handbook adds

This handbook explains the Lean code. It does not check it. When the handbook states a theorem, it tells what the Lean code claims, in words. When it gives a proof, it tells how the Lean code argues. A reader who finds that a statement is false, or that a proof has a gap, has found either an error in the handbook or a place where the Lean code needs a closer look. Both are worth a report.

Each entry has a status. The status "drafted" means that an agent wrote the entry from the Lean code and the tools found no problem. The status "checked" means that a person compared the entry with the Lean code. In this edition no entry has the status "checked".
