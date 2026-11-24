---
title: Transport of the bottom stage
decls:
  - GlobalTheory.TriMove.transport_bottom
  - GlobalTheory.T.definiteBottom_stage_transport_same_constants
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Transport of the bottom stage

This section proves that the bottom stage of a [theta tower](/learn/theta/#theta-towers) does not depend on the choice of the definite Hermitian spaces, up to isometry. If a seesaw triple of definite spaces satisfies the conditions of the bottom stage with a constant $c$, then a triple on any other definite spaces of the same ranks satisfies them with the same constant $c$. The proof moves all the data of the triple by global isometries. It is used in [the constant ratio at the bottom of the theta tower](/entry/theta-tower-bottom-constant-ratio/), where the constant is computed for one choice of spaces and then used for the spaces of the tower.

### Seesaw triples

Let $F$ be a totally real number field and $E/F$ a CM extension, unramified at all finite places. A *Hermitian space* here is a Hermitian space $V$ over $E$ with a Gram matrix $J_V$ and with a self-dual lattice at each finite place. For an infinite place $\tau$ and $q \leq \operatorname{rank} V$, say that $V$ has *negative index $q$* if $J_V$ has signature $(\operatorname{rank} V - q,\, q)$ at each $\tau$. So negative index $0$ means that $V$ is positive definite.

**Definition 1.10.1 (Isometry).** An *isometry* $V \to V'$ is a pair of matrices $P$, $Q$ over $E$ with $PQ = 1$, $QP = 1$ and ${}^t\bar P\, J_{V'}\, P = J_V$.

An isometry over $E$ gives, at each place, an isometry of the local spaces, and so an isomorphism of the adelic unitary groups and of the adelic spaces of matrices. It carries a lattice to a lattice, a Haar measure to a Haar measure, and a fundamental domain for the rational points to a fundamental domain.

**Definition 1.10.2 (Seesaw triple).** A *seesaw triple* on Hermitian spaces $(A, A', W)$, indexed by a finite set $\mathcal{T}$, consists of:

1. riggings of $A$, $A'$ and $W$: a lattice and a sign at each place;
2. for each $t \in \mathcal{T}$, a [Weil representation](/learn/theta/#the-weil-representation) $\omega_t$ for the pair $(A, W)$ and a Weil representation $\omega'_t$ for the pair $(A', W)$;
3. oriented vacuum vectors $v$ and $v'$ for the two pairs;
4. for each $t$, an idempotent $e_t$ and automorphic functions $f_t$, $f'_t$;
5. Haar measures and fundamental domains for the two pairs.

The triple *satisfies the stage conditions* for given characters and a finite set of places if $\operatorname{rank} A + \operatorname{rank} A' = \operatorname{rank} W$, each $\omega_t$ and $\omega'_t$ is a Weil datum for the given characters, the vacua are oriented vacua for the lattices of the riggings, $f_t$ and $f'_t$ are the theta lifts of the vacua at the idempotents $e_t$, and the measures give the fundamental domains volume $1$.

**Definition 1.10.3 (Stage).** For indices $i$, $j$ of the tower and $p$, $q \geq 0$, a seesaw triple is *at stage $(p, q)$* if $p$ and $q$ are at most the bounds of the stage, the ranks of $A$ and $A'$ are given by the tower with $p$ and $q$ hyperbolic planes removed, $A$, $A'$ and $W$ have negative indices $p$, $q$ and $p + q$, and the triple satisfies the stage conditions for the characters of the tower. The *bottom stage* is the stage $(0, 0)$.

So at the bottom stage all three spaces are positive definite, and their ranks are fixed by $i$ and $j$.

**Definition 1.10.4 (Constant of a triple).** A function $c : \mathcal{T} \to \mathbb{C}$ is a *constant* of the triple if $c(t) \neq 0$ for some $t$, and for each $t$ the seesaw integral $I_t$ of the theta kernel of $\omega_t$ against $f_t$, over the fundamental domain of the first pair, and the integral $I'_t$ of the second pair, are absolutely convergent, with $I'_t \neq 0$ and
$$I_t = c(t)\, I'_t.$$

This is the shape of the seesaw identity of the [[theta correspondence|6WB6TKE70H]] for the two pairs at the bottom of the tower.

### Definite spaces of the same rank

**Lemma 1.10.5 (Definite spaces are isometric).** Let $V$ and $V'$ be positive definite Hermitian spaces of the same rank, each with a self-dual lattice at each finite place. Then there is an isometry $V \to V'$.

*Proof.* By the theorem of Landherr, two nondegenerate Hermitian spaces over $E$ of the same rank are isometric if their determinants agree in $F^\times / \mathrm{N}E^\times$ and they have the same signature at each infinite place. The signatures agree since both spaces are positive definite. The determinant of a Hermitian matrix lies in $F^\times$, and it is a norm from $E_v$ at each place $v$ of $F$: at the infinite places it is positive, at a split place each element is a norm, and at an inert place, where $E_v/F_v$ is unramified, a self-dual lattice has a unit determinant, which is a norm. By the Hasse norm theorem for the cyclic extension $E/F$, the quotient of the two determinants is a global norm. $\square$

The theorem is W. Landherr, *Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper*, Abh. Math. Sem. Univ. Hamburg 11 (1936), 245 to 248; see also W. Scharlau, *Quadratic and Hermitian Forms* (1985), Chapter 10, Theorem 6.9. The [[local class field theory|SHEN158T3M]] of the [norm residue sign](/entry/mul-mem-range-norm/) gives the local norm conditions.

### The theorem

**Theorem 1.10.6 (Transport of the bottom stage).** Let $X$ be a seesaw triple on $(A, A', W)$ at the bottom stage for $(i, j)$, and let $Y$ be a seesaw triple on $(B, B', W_1)$ at the stage $(0, 0)$ for $(i, j)$. Then there is a seesaw triple $Y'$ on $(A, A', W)$ at the stage $(0,0)$ for $(i,j)$ such that each constant of $Y$ is a constant of $Y'$.

Lean: `GlobalTheory.TriMove.transport_bottom` (also `GlobalTheory.T.definiteBottom_stage_transport_same_constants`, a second name).

*Proof.* Both triples are at the stage $(0,0)$ for the same $(i, j)$, so the tower fixes the ranks:
$$\operatorname{rank} B = \operatorname{rank} A, \qquad \operatorname{rank} B' = \operatorname{rank} A'.$$
From the rank conditions $\operatorname{rank} A + \operatorname{rank} A' = \operatorname{rank} W$ and $\operatorname{rank} B + \operatorname{rank} B' = \operatorname{rank} W_1$ we get $\operatorname{rank} W_1 = \operatorname{rank} W$. All six spaces have negative index $0$, so they are positive definite. By the lemma there are isometries
$$I_A : B \to A, \qquad I_{A'} : B' \to A', \qquad I_W : W_1 \to W.$$

Let $Y'$ be the image of $Y$ under these isometries. The riggings are moved to riggings, by moving the lattices and keeping the signs. A Weil datum for $(B, W_1)$ is moved to a Weil datum for $(A, W)$, since conjugation by the isometries is an isomorphism of the adelic groups and of the Schwartz-Bruhat spaces that respects the Heisenberg action, the splitting characters and the standard character. In the same way for $(B', W_1)$. An oriented vacuum for the lattices of $Y$ is moved to an oriented vacuum for the moved lattices. The idempotents and the exponents are kept. The theta lift of the moved vacuum at an idempotent is the moved theta lift, so the moved functions are the theta lifts at the moved idempotents. A Haar measure with a fundamental domain of volume $1$ is moved to a Haar measure with a fundamental domain of volume $1$.

The rank and index conditions for $Y'$ are those of $X$, since $Y'$ lives on the spaces of $X$. So $Y'$ is at the stage $(0,0)$ for $(i, j)$.

Let $c$ be a constant of $Y$. The seesaw integrals of $Y'$ are the integrals of $Y$ after a change of variables by the isometries, which preserve the measures, the fundamental domains and the theta kernels. So $I_t(Y') = I_t(Y)$ and $I'_t(Y') = I'_t(Y)$ for each $t$, with the same convergence, and $c$ is a constant of $Y'$. $\square$

**Remark 1.10.7.** The data of $X$ are used only to fix the spaces and their ranks. The theorem says that at the bottom stage the constant $c$ is an invariant of the ranks, which is what allows the computation of $c$ on a model triple with the identity Gram matrix.

**Remark 1.10.8 (Formalization).** The theorem is `GlobalTheory.TriMove.transport_bottom` (DefiniteBottomStageTransportSameConstants.lean, line 32). The triple is `Tri` and its constant is `IsConst` (BlockTheory/TwistedDiscreteSeries/UnitCharTriangle.lean, lines 76 and 156), the stage is `IsStageC` (NegIdxOfIsStd.lean, line 24), the negative index is `NegIdx` (Proofs/TwistedOperators/RatInOfUnit.lean, line 140), and the isometry is `IsoMat` (Proofs/IwasawaDecomposition/ContinuousKapSymm.lean, line 109). The lemma on definite spaces is `exists_isometry_posDef_hermitian_same_rank`, a wrapper of `GlobalTheory.BottomIsom.isoMat_of_posDef`; we have not opened its proof, so the proof of the lemma above is ours. The moved triple is `triMove IA IA' IW Y`, and each field of the stage conditions is moved by a separate transport result, such as `isometryMovedRigging_is`, `isWeilDatumSignedHomPair_transport_isometries`, `isOrientedVacuum_isometry_moved_lattices` and `haar_fundamentalDomain_map_isometry_conj`; the constants are moved by `isConst_seesawTriple_transport_isometries`. From the hypothesis that $X$ is a bottom triple the proof uses only that $X$ is at the stage $(0,0)$, through `IsBottomTri.isStageC`. The rank equation for $A'$ is bound under the name `negRightMulLetterShift` (lines 36 and 44), which does not describe it. The second name is a `first | exact ...` wrapper under `maxHeartbeats 1000000` (DefiniteBottomStageTransportSameConstantsStatement.lean, line 21).
