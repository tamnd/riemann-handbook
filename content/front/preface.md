---
title: Preface
---
On 20 November 2026, Levent Alpöge released a Lean 4 project that claims a proof of the Riemann Hypothesis. The release has about 175,000 files and 17 million lines of Lean. A short note came with it. The note says that the Lean code is the only artifact, and that a written proof does not exist yet.

This handbook is a written account of that Lean code, for a reader who knows mathematics and does not read Lean. It states the definitions, theorems and lemmas of the code in the usual language of mathematics, and it gives their proofs in words. Each statement names the Lean declaration that it comes from, so that a reader can compare the two.

The handbook does not say that the claim is true. Nobody has built the Lean project in full yet, and no person has checked the written statements against the Lean code. The chapter "The status of the claim" tells what is known and what is not.

## What is in the handbook

Volume 0 is this guide. It tells how to read the handbook, gives the notation, lists the published results that the proof uses, and has an index of the Lean names.

Volume 1, Background, is the mathematics that the proof uses: algebra, analysis, number fields, class field theory, L-functions, classical groups, representations of local groups, automorphic forms, Galois representations, arithmetic geometry and the theta correspondence. It has the definitions and the main theorems, in the order to learn them. It does not prove the standard theorems. It cites a source for each.

Volume 2, The proof, is the top of the proof. Its first chapter shows on one page how the Lean code gets the Riemann Hypothesis from one statement about Dirichlet L-functions. Each later chapter takes one large step of the proof, with a guide to the chapter, the argument in words, and the steps that have a page of their own.

Volumes 3 and later go down into the Lean development. Each volume follows one branch of the proof. Each entry is one Lean declaration with its statement, its proof in words, and a note on how the Lean code does it.

## How the handbook is made

The handbook is made from three sources. The written proof and the Learn pages come from [tamnd/riemann](https://github.com/tamnd/riemann), which is also the site [riemann.tamnd.com](https://riemann.tamnd.com). The Lean code comes from [tamnd/riemann-lean](https://github.com/tamnd/riemann-lean), an exact copy of the release. The entries of Volumes 3 and later are written for this handbook, from the Lean code, in [tamnd/riemann-handbook](https://github.com/tamnd/riemann-handbook).

AI agents drafted most of the text from the Lean code and from the cited sources. Tools check the links, the Lean names and the form of each entry. That is not a check of the mathematics. Please report each error that you find at <https://github.com/tamnd/riemann-handbook/issues>.
