---
title: How to read the handbook
---
## Two ways in

A reader who wants the argument reads Volume 2 from its first chapter. Each chapter starts with a guide that tells what to learn first, and links to the parts of Volume 1 that it uses.

A reader who wants to learn the background reads Volume 1 in order. Each chapter assumes the chapters before it and nothing more.

## Numbers

Chapters have numbers in each volume. Section 3.4 is the fourth section of Chapter 3. Statement 3.4.2 is the second numbered statement of Section 3.4. Definitions, theorems, propositions, lemmas, examples and remarks share one count in each section.

In Volume 2 the steps of a chapter come after its sections, and they continue the count of the sections. In Volumes 3 and later each entry has the number of its chapter and its place in the chapter: Entry 2.5 is the fifth entry of Chapter 2.

## References

A reference to a place in the same volume shows its number after the text, as in "the window bound 2.12". A reference to another volume shows the volume as well, as in "Vol. 1, 9.3". In the PDF and the EPUB, the reference to another volume is a link to the same page on [riemann.tamnd.com](https://riemann.tamnd.com).

A Lean name is set in `typewriter type`, as `UpperTheory.FinalTheorems.everyCharacter`. A link on a file name, as `MainConclusion.lean#L10`, goes to the line of the Lean source on GitHub, at the commit that the handbook uses. A link on a concept, as Dirichlet character, goes to the concept in [Math 2.0](https://math2.tamnd.com), a map of mathematics with the standard definitions and sources.

## Statements and proofs

A statement in this handbook is the mathematical content of a Lean declaration, in words. The Lean code often splits one theorem into many small declarations, and it often states a result with more hypotheses than the standard form. The handbook keeps the Lean form when the two differ, and says so in a note.

A proof in this handbook gives the steps of the Lean proof in the order that a mathematician would give them. It names the results that each step uses. It leaves out the steps that only move terms between equal forms, and it says so when it leaves out more.

Each entry of Volumes 3 and later has three parts. The statement says what the declaration says. The proof says why it is true, as the Lean code proves it. The part "In the Lean code" names the file, the main lemmas that the proof calls, and the number of declarations below it in the proof.
