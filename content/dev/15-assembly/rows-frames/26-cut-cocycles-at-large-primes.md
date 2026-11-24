---
title: Cut cocycles at large primes
decls:
  - GlobalTheory.UseLoc.main
  - GlobalTheory.T.unramifiedEnlargement_cut_cocycles_blochKato
  - GlobalTheory.UseLoc.Cases.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cut cocycles at large primes

This section proves the local admissibility condition at a place $w$ of $E$ over a large prime $\ell$. The condition says that the cut cocycles of a Galois representation are Bloch-Kato classes, and that the cut cocycles of the rational characters are coboundaries or unramified. It is one input of [the main linking theorem](/entry/nlink-e-main-alt-alt/). The argument enlarges the coefficients to a finite extension where the classes become torsion, uses a table of admissible extensions at the place, and then descends.

### The setting

Let $D$ be a datum, let $i$ be a local index of $D$ with prime $\ell = \ell_i$ and coefficient ring $\mathcal{O}_i$, and let $G_E$ be the absolute Galois group of $E$. Let $r$ and $\rho$ be families of representations of $G_E$ over $\mathcal{O}_i$, of ranks $n_V$ and $r$, indexed by the points $x$ of the parameter space $X_i$, and let $\pi \in X_i$ be a point of the special set $Z_i$. From these data come two kinds of $G_E$-modules over $\mathcal{O}_i$: the representation $W_\pi$ of rank $r$ attached to $\rho$ and $\pi$, and the rational characters $\chi_c$ for $c \geq 1$.

Fix a place $w$ of $E$ over $\ell$. Let $G_w$ be the decomposition group, $I_w \subseteq G_w$ the inertia group, and $\mathcal{O}_w$ the integers of the local coefficient field at $w$. For a $G_E$-module $M$ over $\mathcal{O}_i$, let $T_M$ be the local lattice of $M$ at $w$ and $V_M = T_M \otimes \mathbb{Q}$. The *cut cocycles* of $M$ form a set
$$\mathrm{Cut}_w(M) \subseteq \{\, z \colon G_w \to V_M / T_M \,\}.$$
Each element is built from finitely many points $x_j \in X_i$ and coefficients, by cutting the family $r$ at these points. On the target we have three submodules of functions $G_w \to V_M/T_M$:

1. the coboundaries $B^1(M)$, the functions $g \mapsto (g - 1)v$;
2. the *finite part* $H^1_f(M)$, the images of the Bloch-Kato finite cocycles of $V_M$, plus $B^1(M)$;
3. the unramified cocycles $Z^1_{\mathrm{ur}}(M)$, the cocycles that vanish on $I_w$.

The *local bound* $\mathrm{LB}_w(M)$ is the length over $\mathcal{O}_w$ of the quotient of the span of $\mathrm{Cut}_w(M)$ by its intersection with $H^1_f(M)$.

### The enlargement

The hypotheses at $\ell$ give *exact local data* at $w$: a finite extension $\Lambda$ of the local coefficient field, of the first case, with integers $\mathcal{O}_\Lambda$ and a uniformizer $\lambda$, a character $\theta \colon G_w \to \mathcal{O}_\Lambda^\times$, and Hodge-Tate data $h, w', \eta, \mathrm{typ}, U$ indexed by the embeddings of the unramified subfield. They satisfy a set of conditions $\mathrm{Set}$ that fixes the twisted lattice, the crystalline property and the Hodge-Tate multiplicities. For a lattice $T$ write $T_\Lambda$ for its extension of scalars to $\mathcal{O}_\Lambda$, and $z_\Lambda$ for the image of a cocycle $z$.

The *table of admissible extensions* at $w$ is the following statement. Assume $\ell \geq 5$ and the hypotheses on the data above. Then for every finite $\mathcal{O}_\Lambda$-module $X$:

1. for each lattice $T'$ of $V$ twisted by $\chi_1^{-1}$ with the same underlying module, a cocycle with values in $X \otimes T$ gives an admissible extension if and only if it lies in the finite part;
2. for $2 \leq c \leq t$ and each lattice of $\chi_c$, a cocycle gives an admissible extension if and only if it is a coboundary;
3. for each lattice of $\chi_1$, a cocycle gives an admissible extension if and only if it is unramified on $I_w$.

Here "admissible" means that the extension of $\chi_1$ by $X \otimes T$ defined by the cocycle is killed by $\lambda^a$ and lies in the admissible class fixed by the Hodge-Tate data, the residual polynomial and the jump. This is the shape of Fontaine-Laffaille theory: for $\ell \geq 5$ and small Hodge-Tate weights, torsion crystalline extensions match the Bloch-Kato finite part.

**Theorem 7.26.1 (Cut cocycles over the enlargement).** Let $D$, $i$, $r$, $\rho$, $\pi$ and $w$ be as above, with the exact local data $\Lambda, \lambda, \theta, h, w', \eta, \mathrm{typ}, U$ satisfying $\mathrm{Set}$. Assume the table of admissible extensions at $w$, $\ell \geq 5$, that $r$ is good, that $\pi \in Z_i$, that $\rho$ at $\pi$ has a semisimple decomposition, and that the family $r$ is continuous. Then:

1. for each $z \in \mathrm{Cut}_w(W_\pi)$, the cocycle $z_\Lambda$ lies in $H^1_f$ of $(T_{W_\pi})_\Lambda$;
2. for $2 \leq c \leq t$ and each $z \in \mathrm{Cut}_w(\chi_c)$, the cocycle $z_\Lambda$ lies in $B^1$ of $(T_{\chi_c})_\Lambda$;
3. for each $z \in \mathrm{Cut}_w(\chi_1)$, the cocycle $z_\Lambda$ lies in $Z^1_{\mathrm{ur}}$ of $(T_{\chi_1})_\Lambda$.

Lean: `GlobalTheory.T.unramifiedEnlargement_cut_cocycles_blochKato` (also `GlobalTheory.UseLoc.Cases.main`).

*Proof.* The three parts have the same shape. We give part 1 and then the changes for parts 2 and 3.

1. Apply the table to the twisted lattice of $W_\pi$ by $\theta$ and to the characters $\chi_c$ twisted by $\theta$. This is possible by the first condition of $\mathrm{Set}$ and $\ell \geq 5$.
2. A cut cocycle is locally constant and killed by a power $\lambda^a$, because $r$ is good and continuous. So the finite $\mathcal{O}_\Lambda$-module $X = \lambda^{-a}\mathcal{O}_\Lambda/\mathcal{O}_\Lambda$ is the right one.
3. A torsion local cocycle lifts to a cocycle $z'$ with values in $X \otimes T$, with $\iota(z') = z_\Lambda$ for the inclusion $\iota$.
4. The extension defined by $z'$ is admissible. For $W_\pi$ this uses the twisted Weil coefficients, and for the characters it uses the conductor twisted characters. Both use the semisimple decomposition and the conditions of $\mathrm{Set}$.
5. By part 1 of the table, $z'$ lies in the finite part. Then $z_\Lambda = \iota(z')$ is read as a Bloch-Kato class of $(T_{W_\pi})_\Lambda$.

For part 2 the lift is a cocycle of a twisted character, part 2 of the table makes it a coboundary, and the coboundary is read back over $\Lambda$. For part 3, part 3 of the table makes the lift unramified, and the restriction to the inertia subgroup reads it back. $\square$

### Descent to the original coefficients

The *conditions at a large residue characteristic* on $\ell$ are that $\ell \geq 5$, that $\ell$ is not one of the small primes of $D$, that $\ell \neq q$ and $\ell \neq d$, and the conditions on the position of $\ell$, the decomposition and the continuity of the family.

**Theorem 7.26.2 (Admissibility at a large prime).** Let $D$ be a datum with Hodge-Tate data, let $i$, $r$, $\rho$ and $\pi$ be as above, and assume the top table condition, the admissibility condition of weight $20$, the conclusion of the parameter step $J_a$, that $r$ is good and that $\pi \in Z_i$. Assume the conditions at a large residue characteristic on $\ell$. Then for every place $w$ of $E$ over $\ell$:

1. $\mathrm{LB}_w(W_\pi) \leq 0$, so the span of $\mathrm{Cut}_w(W_\pi)$ is contained in $H^1_f(W_\pi)$;
2. for $2 \leq c \leq t$, every element of $\mathrm{Cut}_w(\chi_c)$ lies in $B^1(\chi_c)$;
3. every element of $\mathrm{Cut}_w(\chi_1)$ lies in $Z^1_{\mathrm{ur}}(\chi_1)$.

Lean: `GlobalTheory.UseLoc.main`.

*Proof.* Fix $w$ over $\ell$.

1. The conditions on $\ell$ give exact local data $\Lambda, \lambda, \theta, h, w', \eta, \mathrm{typ}, U$ at $w$ with the conditions $\mathrm{Set}$.
2. The top table condition, applied to $\ell$, the field at $w$, $\Lambda$ and $\lambda$, gives the table of admissible extensions at $w$.
3. The theorem above gives the three statements over $\Lambda$.
4. For part 1: if $z_\Lambda$ lies in the finite part over $\Lambda$, then $z$ lies in $H^1_f(W_\pi)$, since the finite part descends along the faithfully flat map $\mathcal{O}_w \to \mathcal{O}_\Lambda$. So the span of the cut cocycles lies in $H^1_f(W_\pi)$, the quotient in the definition of $\mathrm{LB}_w$ is zero, and its length is $0$.
5. For part 2: a coboundary over $\Lambda$ with values in the extended lattice descends to a coboundary over $\mathcal{O}_w$, by the descent of coboundaries along the enlargement.
6. For part 3: an unramified cocycle over $\Lambda$ descends to an unramified cocycle, and the inertia group of the enlargement is the inertia group $I_w$.

This gives the three statements. $\square$

The bound in part 1 is stated as an inequality of lengths, $\mathrm{LB}_w(W_\pi) \leq 0 \cdot \mathrm{len}$, so that it has the same form as the bounds at small primes, where the right side is a multiple $e$ of the length of the residue field. At large primes the multiple is $0$, so the inequality is an inclusion.

**Remark 7.26.3 (Formalization).** The theorem `GlobalTheory.UseLoc.main` is at line 24 of [AdmissibleOfLargeResidueChar.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AdmissibleOfLargeResidueChar.lean#L24), under `maxHeartbeats 4000000`. Its conclusion `admG2` unfolds to the hypotheses at $\ell$ and the three statements; the first is `LocBound ... 0`, proved by `Module.length_eq_zero_iff`. The relay `GlobalTheory.T.unramifiedEnlargement_cut_cocycles_blochKato` is at line 7 of [UnramifiedEnlargementCutCocyclesBlochKatoStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnramifiedEnlargementCutCocyclesBlochKatoStatement.lean#L7); that file imports `Mathlib` twice, at lines 1 and 3. The target `GlobalTheory.UseLoc.Cases.main` is at line 126 of [UnramifiedEnlargementCutCocyclesBlochKato.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnramifiedEnlargementCutCocyclesBlochKato.lean#L126), and it pairs `partW`, `partC` and `partU` at lines 25, 58 and 93, each under `maxHeartbeats 8000000`. The table is `TopCore` at line 193 of [TableLineDegreeTwo.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/TableLineDegreeTwo.lean#L193), with its hypotheses `TopHyp` at line 180. The cut cocycles `cutCoc` and `LocBound` are at lines 122 and 138 of [CentralIdemCoeff.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/CentralIdemCoeff.lean#L122), and `BD` and `HfD` at lines 119 and 126 of [StatementTor.lean](lean:Formalism/WeaklyAdmissibleFiltrations/StatementTor.lean#L119). The comparison with Fontaine-Laffaille theory is our reading of `TopCore`; the Lean proof takes the table as a hypothesis.
