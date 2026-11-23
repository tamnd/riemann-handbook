---
id: wach-used-clauses
title: Seventeen properties of the Wach lattices
kind: theorem
decl: GlobalTheory.NL.wach_used_clauses
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.WachLatticeLaterClausesHold
covers: 737
status: drafted
drafted_by: writer@claude
---
This theorem collects seventeen properties of the Wach lattices of crystalline representations into one statement. It is the proof of [its second name](/entry/wach-lattice-later-clauses-hold/), which the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/) uses through ten declarations. The theorem has no hypothesis. Each property comes from its own lemma.

## Statement

Fix a datum $D$ (`D7`), a choice $HW$ of Wach functors (`HWOf`), Fontaine data $F$ (`FonOf`) and comparison data $Cm$ (`CmpOf`). For a prime $\ell$, a finite extension $K$ of $\mathbb{Q}_\ell$, a level $s \geq 1$ and a coefficient field $L$, call the triple good (`Good`) if $s \geq 2$ when $\ell = 2$, $K$ lies in $K_s = K_0(\mu_{\ell^s})$, and the embeddings of $K_s$ land in $L$. For a good triple, $HW$ gives a module $N(T)$, the Wach lattice, for each $\mathcal{O}$-lattice $T$ with a Galois action.

**Theorem.** `DeltaInvariantNormBound D HW F Cm` holds. That is, at each good triple and for each crystalline lattice $T$, the following hold.

1. **Structure** (`WachLatticeFreeGlobal`, `P2`, `P6`). $N(T)$ is the sum of its parts over the letters, and each part is free over $\mathcal{O}[[X]]$. $N(T)$ is stable under $\Gamma$, and $\gamma - 1$ maps it into $\pi N(T)$ and into $X N(T)$. $N$ is saturated and exact on short exact sequences.
2. **Comparison** (`P3`, `P4`). The map to $T \otimes B$ spans $D_{\mathrm{cris}}$, has kernel in $\pi N(T)$, and is compatible with $\varphi$. Expansions at low-level points match the Hodge filtration.
3. **Heights** (`P5`, `lem3`). Two heights $M$ and $h$ come from the Hodge jumps. $Q^M \varphi(N) \subseteq N$ and $Q^h N$ lies in the span of $\varphi(N)$. For a surjection of lattices, $X^{\max(M+h)}$ kills the cokernel of the Wach lattices.
4. **Cocycles** (`P7`, `P8`, `Pr2a` to `Pr2d`). Herr cocycles with poles in $\varphi$-twists of $Q$ give classes in $H^1_f$. The class map from Herr cocycles is onto, with kernel the Herr coboundaries. A class is in $H^1_f$ if and only if its restriction to $G_{K_s}$ is. Integral cocycles give finite classes. A defect term controls short exact sequences. The extension of the trivial line has a lift with controlled $\varphi - 1$ and $\gamma - 1$.
5. **Descent and uniqueness** (`P9`, `WachCharacterisation`, `gammaSemisimpleQuotientGlobal`). For $s = 1$ and $p \neq 2$, $N(T)$ descends to the tame subextension. $N(T)$ is unique and respects twists. $\Gamma$ acts semisimply on the quotients, with eigenvalues $u^{-a}$ for the jumps $a$.
6. **Infinite level** (`ConclusionE`). A basis of $N(T)$ is a basis of $T \otimes R_W$, and the $\varphi$-fixed vectors are $T$. The jumps at infinite level are bounded by $\max M$ and $\max h$.

We give the parts in short form. The full Lean definitions are long. We have not unfolded `Good`, `LocWach` or the rings beyond their fields.

## Proof

The proof unfolds `DeltaInvariantNormBound` and fills the seventeen slots, one lemma each. The last slot is `ConclusionE`. The proof unfolds it and fills its two halves with `NL.NygaardExtension.main` and `T.local_comparison_of_cmpOf`. No lemma takes a hypothesis beyond $D$, $HW$, $F$ and $Cm$.

## In the Lean code

The theorem is in [WachLatticeLaterClausesHold.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHold.lean#L28). `DeltaInvariantNormBound` is in [UsedLocalConclusion.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/UsedLocalConclusion.lean#L9), and its parts are in [DeltaInvariantLattices.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DeltaInvariantLattices.lean#L634). We have not opened the proofs of the seventeen lemmas.

The name says "norm bound", but most parts are structural facts. Only `P3` and `P4` take $Cm$, and their local forms `p3L` and `p4L` ignore it (the argument is `_C`).
