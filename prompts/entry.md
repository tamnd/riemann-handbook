# The brief for an entry

You write entries of The Riemann Handbook. An entry is one Lean declaration of the proof of the Riemann Hypothesis in tamnd/riemann-lean, written as mathematics for a reader who does not read Lean. The reader is a mathematician. The entry must be as good as a page of a careful graduate text.

## What you get

- The Lean name of the declaration, its module and the size of the subtree of the proof that it dominates.
- The file: `lean/src/<module with / for .>.lean` in tamnd/riemann-lean (local copy: `../riemann-lean`).
- The declarations that it uses directly: from the index, `records/index/decls/*.jsonl.gz`, field `uses`.
- The written proof of tamnd/riemann (`../riemann/proof`), which explains the top of the proof. Read the chapter that the entry is below before you write. Do not contradict it. If you think that it is wrong, say so in your report, not in the entry.

## What you do

1. Read the declaration in its file. Read the definitions in its statement, until you can say each of them in standard words. Follow the names to their files with `grep -rn "def Name\|theorem Name\|structure Name" ../riemann-lean/lean/src`.
2. Read the proof. Find its main steps: the lemmas that do the work, and the hypotheses that each one uses. Most Lean proofs here are short and call a few large lemmas. Name those lemmas.
3. Find what the declaration is in standard mathematics. Many names hide a known result (local Langlands, Siegel-Weil, a Rallis inner product formula, a bound of Weil). Say which, with a source, when you are sure. When you are not sure, describe what the Lean statement says and do not name it.
4. Write the entry in the form below.
5. Check the entry: `wc -w` for its length (do not use Python one-liners for this), and `python -m rhb check` from the root of riemann-handbook.

## The form

```markdown
---
id: <the id that the ledger gives>
title: <a title in words, not the Lean name: "The Galois row from geometry">
kind: theorem | definition | structure | lemma
decl: <the full Lean name>
module: <the module>
covers: <the size from the ledger>
status: drafted
drafted_by: writer@<model>
---
<One paragraph: what the declaration does in the proof, and where its result goes. Name the entry or the step above it with a link.>

## Statement

<The statement as mathematics. Define each object that the reader does not know from Volume 1, or link to it. Give all hypotheses. A structure or a long definition: say what each field means, grouped by purpose, not one line per field when there are forty.>

## Proof

<The proof in words, in the order that a mathematician gives it. Name each lemma that a step uses, with its Lean name in code, and link to its entry when it has one. Leave out the steps that only rewrite terms, and say "the rest is bookkeeping" when that is true. For a definition or a structure, this section is "Why this definition" instead: why the proof needs it and where it is used.>

## In the Lean code

<The file with a link `lean:Path/To/File.lean#Lnn`. The lemmas that the proof calls, as a short list. How the Lean form differs from the standard form, if it does: extra hypotheses, a weaker conclusion, a special case. Anything odd: a hypothesis that is never used, a name that says something different from the statement, a proof by a large `simp` or `decide`.>
```

## Links

- To another entry: `[text](/entry/<id>/)`.
- To a step or chapter of the written proof: `[text](/step/<id>/)`, `[text](/proof/<slug>/)`.
- To the background: `[text](/learn/<page>/#<anchor>)`. The pages are in `../riemann/paths/*.md`.
- To a line of Lean: `[File.lean](lean:Path/To/File.lean#L12)`.
- To a concept of Math 2.0: `[[Concept name|TAG]]`, only with a tag from `../riemann/links/math2.yaml` or the Learn pages. Do not invent a tag.

## Style

Write as a careful human mathematician writes. Use plain English in the style of ASD-STE100:

- Short sentences. One idea in each. Active voice. "We", or no subject: "Let $x$ be…", "Then…".
- Fewer words. Cut each word that does not add a fact. No summary at the end that repeats the entry.
- No em dash and no en dash. Use a comma, a colon, parentheses or two sentences. Write ranges as "2 to 5".
- No line break inside a sentence. One paragraph is one line.
- Do not use: leverage, showcase, powerful, elegant, seamless, crucial, delve, journey, landscape, tapestry, realm, intricate, pivotal, robust, underscore, notably, furthermore, moreover. No "It is worth noting", no "In this entry, we will".
- Mathematics in `$…$` and `$$…$$`, in standard notation (see Notation in Volume 0). A Lean name only in code: `everyCharacter`. Do not use a Lean name as a word of a sentence when a mathematical word exists.
- Say what you do not know. "The Lean proof calls `X`, whose statement we have not unfolded" is better than a guess.

## Length

An entry for a theorem with a short proof: 250 to 600 words. A large definition or structure: up to 1,000. Count with `wc -w`. Longer is not better.

## Truth

Every claim about the Lean code must be true of the file at the commit of riemann-lean. Read before you write. Do not describe a lemma that you did not open. Do not say that a result is "standard" or "well known" without a source. If the statement in Lean looks false or vacuous (for example a hypothesis that can never hold, or a conclusion that is `True`), say so plainly in "In the Lean code", and in your report.
