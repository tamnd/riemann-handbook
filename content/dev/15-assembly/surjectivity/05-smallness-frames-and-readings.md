---
title: Smallness, frames and readings
decls:
  - GlobalTheory.FrameRead.reads_of_small_alt
  - GlobalTheory.T.readsAt_of_smallAt
  - GlobalTheory.FrameOf.frameSt_of_smallSt'
  - GlobalTheory.T.frame_statement_of_small_statement
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Smallness, frames and readings

This section starts the proof of the exponent bound of Section 9. At a twisted place $w$ whose residue characteristic $\ell$ is small in a precise sense, we build an $\ell$-adic Hecke frame for the block of the point at $w$, and a reading of the block by the frame. The frame is the source of the automorphic representations of Section 6 and of the Galois representations of Section 7. Both theorems of this section hold with no published input. The model statement of [Section 5.8.4](/entry/model-st-of-small-frame-gal/) uses the frame statement, through [the exponent bound](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/).

Let $p$ be a point of a family, $j$ a level, and $w$ a twisted place of the coefficient field with residue characteristic $\ell$. Write $t = \mu(w)$ for the type of $w$. The point has a *block* at $(j, t)$: a finite set of places $Q$ of the host field $E$, each with a norm $q_Q$ and a split place $\lambda_Q$ above it, an operator algebra with block operators $T_i$, the *block subspace* $Z$, and a space $Z_H$ on which the operators act. The point also has a *dictionary*: parameters $P$ with a rank $N_r$, and weights $W$ with values $\lambda$, that match the size data at $j$, and numerical checks on $(P, W)$. Write $W$ *in range at* $\ell$ for the range condition of the weights at $\ell$.

**Definition 5.5.1 (In range).** Let $Q(p, j, P, W, w)$ be a property. The statement *$Q$ holds in range* is the closed property, for $\mathcal{C}_{\mathrm{fam}}$: eventually at the points of $\mathcal{F}$, for each rich point $p$, each level $j$, each $(P, W)$ that matches the size data and passes the numerical checks, and each twisted place $w$ with $W$ in range at the residue characteristic of $w$, $Q(p, j, P, W, w)$ holds.

Lean: `GlobalTheory.ExpTie.InRangeAlt`.

**Definition 5.5.2 (Small place).** The place $w$ is *small* for $(p, j, P)$ if all of the following hold:

1. $\ell$ is prime and $N_r + 1 < \ell$;
2. $\ell$ does not divide the discriminant of $E$;
3. $T_i Z \subseteq Z$ for each block operator $T_i$;
4. $Z \subseteq Z_H$.

The *smallness condition* is the statement that each $w$ is small, in range.

Lean: `GlobalTheory.ExpTie.SmallAt` (also `GlobalTheory.ExpTie.SmallnessCondition`).

A *frame* of rank $N$ at $\ell$ is a finite group $G$ with a compact open subgroup $K$, a family of finite sets $\mathrm{tr}(i)$ of double coset representatives for index $i$, a representation $\kappa$ of $K$ in $\mathrm{GL}_N$ of the ring of integers of a finite extension $L_f$ of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, and a character $\chi$ of $K$ in the units of that ring. The frame of the point at $(j, t)$ is the frame built from the level group of the point, with $L_f$ generated over $\mathbb{Q}_\ell$ by the image of an embedding $e_0$ of the coefficient field and by roots of unity. A frame has Hecke operators and *eigensystems* $\theta \colon I \to \overline{\mathbb{Q}}_\ell$ for its index set $I$.

The frame data at $w$ are: an embedding $e_0$ of the coefficient field into $\overline{\mathbb{Q}}_\ell$ with $x \in w$ if and only if $|e_0(x)| < 1$; a sign $b$; an isomorphism $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ with $\iota \circ e_0$ the base embedding; evaluation maps at the infinite types; base changes $b_\tau$; an order isomorphism of ranks; shifts; and the field $L_f$ with $\kappa$ and $\chi$. The data are *good* if the evaluations agree with the embeddings, $\kappa$ is given by the matrix formula of the point, and $\chi$ times a power of the determinant of $\kappa$ inverts the level character under $\iota$.

**Definition 5.5.3 (Frame at a place).** The *frame condition* at $w$ holds if there are a frame $F$ of rank $N_r$ at $\ell$, a reading $R$ of the block by $F$ with the weights $\lambda$ at $w$, and embeddings $\mathrm{inc}_\tau$ of $E$ into $\overline{\mathbb{Q}}_\ell$, such that $F$ is good and $F$ is tied to the point through $R$ and $\mathrm{inc}$. The *frame statement* is the frame condition, in range.

Lean: `GlobalTheory.ExpTie.FrameAt` (also `GlobalTheory.ExpTie.FrameStatement'`).

The frame condition is built from seven conditions at $w$:

1. *half:* for each embedding $e_0$ and sign $b$, the embeddings of $E$ that $e_0$ and $b$ give form a half system;
2. *integrality of $\kappa$:* for good evaluations there are base changes $b_\tau = 1$ such that the entries of the matrices of $\kappa$ lie in $\mathbb{Q}_\ell(e_0)$ and have absolute value at most $1$;
3. *finite order of $\chi$:* the level character has finite order $M$;
4. *tameness:* for each $g$ in the finite adelic group, the set of rational $\gamma$ with $g^{-1} \gamma g$ in the level group is finite and its size is prime to $\ell$;
5. *permutations:* for good data, the frame $F$ of the point has, for each $i$ and $\kappa \in K$, a permutation $\sigma$ of $\mathrm{tr}(i)$ with $\kappa s = \sigma(s) \kappa'$ and $\kappa, \kappa'$ with the same values under $\kappa$ and $\chi$;
6. *commutation:* for good data and all $i, i'$, there is a bijection of $\mathrm{tr}(i) \times \mathrm{tr}(i')$ with $\mathrm{tr}(i') \times \mathrm{tr}(i)$ under which the products differ by trivial elements, so that the Hecke operators commute;
7. *readings:* there are a sign $b$ and shifts $s_\tau$ such that, for good data with $b_\tau = 1$, there is a reading of the block by the frame $F$ with the embedding $e_0$ and the inclusion of the places as its index map.

Lean: `GlobalTheory.FrameOf.ReadsAt` (also `GlobalTheory.FrameOf.HalfAt`, `GlobalTheory.FrameOf.KapAt`, `GlobalTheory.FrameOf.ChiAt`, `GlobalTheory.FrameOf.TameAt`, `GlobalTheory.FrameOf.PermAt` and `GlobalTheory.FrameOf.CommAt`, the six other conditions).

**Lemma 5.5.4 (Readings at small places).** At each small place, in range, the reading condition 7 holds.

Lean: `GlobalTheory.FrameRead.reads_of_small_alt` (also `GlobalTheory.T.readsAt_of_smallAt`, a second name).

*Proof.* Take $\varepsilon_1 = 1$, the zero threshold record and $x_0 = 0$. Let $p$, $j$, $(P, W)$ and $w$ be as in the statement. The dictionary gives, for each infinite type $\tau$, a number $c_\tau$ with the value of $\lambda$ at $\tau$ fixed by $c_\tau$. Take the sign $b$ false and the shifts $s_\tau = -c_\tau$. For good data with $b_\tau = 1$, the rank lemma for readings gives a reading of the block by $F$ with the embedding $e_0$ and the index map of the places. $\square$

**Theorem 5.5.5 (Frames at small places).** The smallness condition implies the frame statement.

Lean: `GlobalTheory.FrameOf.frameSt_of_smallSt'` (also `GlobalTheory.T.frame_statement_of_small_statement`, a second name).

*Proof.* Six of the seven conditions hold at each small place, in range, with no other input: the half condition, the integrality of $\kappa$, the finite order of $\chi$, tameness, the permutations, and the commutation. The seventh is the lemma above. Statements in range are closed under conjunction: take the smaller $\varepsilon_1$, join the thresholds, and take the larger height. So, in range, $w$ is small and the seven conditions hold. At such a place, with the rank $N_r$ of the dictionary, the frame built from the level group with $\kappa$ and $\chi$ is good and tied to the point, and the reading of condition 7 is a reading of the block by it. This gives the frame condition. $\square$

The smallness condition itself is proved in Section 9 with no input, and so the frame statement holds outright.

**Remark 5.5.6 (Formalization).** The lemma is in [ReadsOfSmall.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReadsOfSmall.lean#L27), and the theorem in [FrameStOfSmallSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FrameStOfSmallSt.lean#L50). The seven conditions are in [ClassesAt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassesAt.lean#L86), and the frame condition and smallness in [LiftFrameEmbeddingBase.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/LiftFrameEmbeddingBase.lean#L373). In the lemma the smallness hypothesis is not used, and the closed statement holds with $\varepsilon_1 = 1$, the zero record and $x_0 = 0$ (lines 27 to 29). The sections `Core` and `Point` of ReadsOfSmall.lean (lines 20 to 26) are empty. FrameStOfSmallSt.lean has an empty namespace at lines 25 to 26 and an empty section `Point` at lines 46 to 49. The two wrappers are one-line calls with `maxHeartbeats` set to 1000000. We have not unfolded the frame, the reading, the tie, the block or the matrix formula of $\kappa$; the description of the frame above is our reading of the names of its fields.
