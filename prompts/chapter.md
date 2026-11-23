# The brief for a chapter

You write a chapter of The Riemann Handbook, Volumes 3 to 15. A chapter explains the mathematics of one part of the Lean proof of the Riemann Hypothesis in tamnd/riemann-lean. It is written by a mathematician for a graduate student who wants to learn this mathematics and who does not read Lean. It reads like a chapter of a good textbook, not like notes on code.

The model is Volume 1: `../riemann/paths/algebra.md` and the other `paths/*.md` files. Read one of them before you start. Match it: a definition before each use, statements in standard notation, numbered results, short proofs, a link to the place in the proof that uses each result, and further reading at the end.

## What you get

- The chapter: its title, its folder in the handbook, and the Lean declarations that it covers, in the order of the proof, with the size of each subtree and its parent.
- For many declarations, an older entry file in the chapter folder. It describes the declaration and has been checked against the Lean code. Use it as notes: take its facts and its links, and check each fact you use in the Lean file. Do not copy its form or its sentences.
- The Lean code: `../riemann-lean/lean/src/<module with / for .>.lean`.
- The written proof, `../riemann/proof/` (chapters and `steps/*.md`), and the Background, `../riemann/paths/*.md`.

## What you write

One file or more in the chapter folder, named `NN-<slug>.md` (`01-cohomology-of-projective-bundles.md`). Each file is one section. It opens with front matter and then a `##` heading:

```markdown
---
title: Cohomology of projective bundles
decls:
  - UpperTheory.Cb.etaleCohomology_projectiveBundle_formula
  - UpperTheory.Pbf.pbf_all
status: drafted
drafted_by: writer@<model>
---
## Cohomology of projective bundles

<A short paragraph: what this section proves and why the proof needs it.>

**Definition (Projective bundle).** Let $S$ be a scheme and $\mathcal{E}$ a locally free sheaf of rank $r + 1$ on $S$. ...

**Theorem (Projective bundle formula).** Let ... Then ...

Lean: `UpperTheory.Cb.etaleCohomology_projectiveBundle_formula`, `UpperTheory.Pbf.pbf_all`.

*Proof.* ... $\square$

**Remark.** The Lean statement asks for ... This hypothesis is not used.
```

`decls` lists every declaration of the section. Together, the sections of the chapter list every declaration that your brief gives.

If the brief asks for it, also write `intro.md` in the chapter folder: one or two paragraphs, with no heading. Say what the chapter proves, which results of Volume 1 it needs (with links), and which step of the proof uses it.

## The statements

- Head each result with `**Definition.**`, `**Theorem.**`, `**Proposition.**`, `**Lemma.**`, `**Corollary.**`, `**Example.**` or `**Remark.**`, with an optional name in parentheses: `**Theorem (Lefschetz fixed point formula).**`. You need not write numbers: `python3 -m rhb number --write` writes the number of each statement into the head (Theorem 3.2.4: chapter, section, statement) and into each link whose text is a kind of statement, such as `[Theorem](/entry/<id>/)`. Run it before the check.
- Under each Definition, Theorem, Proposition, Lemma and Corollary that comes from the Lean code, write one line `Lean: ` with the full Lean names in code. Put a second name or a wrapper of the same statement on the same line: "Lean: `A` (also `B`, a second name)." This line ties the declaration to the number.
- Then the proof: a paragraph that starts with `*Proof.*` and ends with `$\square$`. Give the argument as a mathematician gives it: the main steps, which earlier result each step uses (with a link), and why it holds. Leave out steps that only rewrite terms. If the Lean proof only passes its hypotheses to another result, the proof is one sentence: "This is Theorem … applied to …". If the Lean proof cites a published result as a hypothesis, say so and cite it.
- Define each object before its first use, or link to its definition in Volume 1 or in an earlier chapter. State all hypotheses.
- A known theorem: state it in its standard form first, with a source (author, title, the theorem or section number). Then say in a Remark how the Lean form differs: extra hypotheses, a special case, a weaker conclusion.
- Not every declaration gets its own statement. A second name, a wrapper, a field projection or a small step of a proof goes into the `Lean:` line of the result that it serves, or into the proof as a sentence. A large result gets a statement. A lemma that a student needs to follow a proof gets a statement.
- Facts about the Lean code that a reader should know (a hypothesis that is never used, a name that says something different from the statement, a statement that is vacuous, a definition that is not unfolded) go into one `**Remark (Formalization).**` at the end of the section. Keep it short.

## The text is mathematics

The reader is a student who reads a textbook by an expert. So:

- Outside the `Lean:` lines and the Remarks (Formalization), the text does not mention the code. Do not write "the code", "the Lean proof", "the Lean statement", "the file", "the declaration", "the field", "the structure", "the hypothesis named". Write the mathematics: "We assume …", "We take the following as given, from [source]", "Let …". A result that the Lean proof takes as an input statement is stated as a Theorem with its source, and the proof says where it comes from in one sentence.
- Each statement says exactly what the Lean statement says, in standard notation: the same objects, the same hypotheses, the same quantifiers, the same conclusion. Do not add hypotheses, do not make the conclusion stronger, do not fill a gap with what "should" hold. If the Lean form is a special case or an odd form of a classical result, state the Lean form, and give the classical form in the Notes and references.
- Each definition defines one object in words and symbols, as a textbook does, and the text says why it is the right object. Give a short example when it helps the reader.
- Each proof is a proof: the reader can follow it with the results it cites. Do not write "the proof unfolds the definitions" or "the proof is a computation in the code". Say what is computed.
- Each section opens with a paragraph that says what it proves and where the result is used, and the chapter ends with `## Notes and references`: the classical sources of each main result (author, title, theorem or section) and how the treatment here differs.

## The order

Order the sections so that a reader meets each definition and each lemma before it is used, and so that the chapter reads from the simple to the deep. The main theorem of a section can be stated in the opening paragraph and proved at the end. This order can differ from the order of the brief, which is the order of the proof from the top down.

## Links

- To a result in this or another chapter of the development volumes: `[Theorem](/entry/<id>/)`, with the id of its declaration from `ledger/outline.yaml`. The build turns it into "Theorem 3.2.4". Use the right word: Definition, Lemma, and so on.
- To a step or a chapter of the written proof: `[VWin](/step/vwin-def/)`, `[the Galois row](/proof/galois-row/)`.
- To the Background: `[length of a module](/learn/algebra/#rings-ideals-and-modules)`. Anchors are the section headings of `../riemann/paths/*.md` in lower case with hyphens.
- To a line of Lean, rarely, in a Remark: `[File.lean](lean:Path/To/File.lean#L12)`.
- To a concept of Math 2.0: `[[Concept name|TAG]]`, only with a tag from `../riemann/links/math2.yaml` or from the Background. Do not invent a tag.

## References

End the last section of the chapter with `## Notes and references` (a section of its own). It has a short paragraph on what the chapter feeds into, with links. Then a list of sources in the form of Volume 1: "J. S. Milne, *Étale Cohomology*, Chapter VI, §10." Cite only a book or a paper that you are sure of, with a chapter, a section or a theorem number. `../riemann/links/literature.yaml` has verified citations for the published results of the proof. If you are not sure of a source, do not cite it.

## Style

Plain English in the style of ASD-STE100, as in Volume 1:

- Short sentences. One idea in each. "We", or no subject: "Let $x$ be…", "Then…".
- Fewer words. No summary that repeats the section.
- No em dash and no en dash. Use a comma, a colon, parentheses or two sentences. Write ranges as "2 to 5". Write Hodge-Tate, Eichler-Shimura with a hyphen.
- No line break inside a sentence. One paragraph is one line.
- Do not use: leverage, showcase, powerful, elegant, seamless, crucial, delve, journey, landscape, tapestry, realm, intricate, pivotal, robust, underscore, notably, furthermore, moreover. No "It is worth noting", no "In this section, we will".
- Mathematics in `$…$` and `$$…$$`. A Lean name appears only in a `Lean:` line, in a Remark, or in code when no mathematical word exists. Never use a Lean name as a word of a sentence.
- A display wider than the page breaks the PDF. Split a long formula with `\begin{aligned}…\end{aligned}` into rows.

## Length

A section is 500 to 2,500 words. A chapter has as many sections as its mathematics needs. Count with `wc -w`.

## Truth

Every claim about the Lean code must come from a file that you opened at the pinned commit. Do not describe a lemma that you did not open. When you have not unfolded a definition, say so in a Remark, and state only what you know. Do not invent the mathematics behind a name. Do not call a result "standard" or "well known" without a source. If a Lean statement looks false or vacuous, say so plainly in a Remark and in your report.

## Check

From the root of riemann-handbook, run `python3 -m rhb check 2>&1 | grep -v "^riemann"` and fix each problem in your files. Your final reply: the files with their word counts, one line on each section, and a list of anything odd in the Lean code (file and line).
