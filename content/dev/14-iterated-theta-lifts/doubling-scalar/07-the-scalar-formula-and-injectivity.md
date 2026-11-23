---
title: The scalar formula and injectivity
decls:
  - GlobalTheory.T.thetaLift_adjoint_scalarFormula_injective
  - GlobalTheory.Core.Rk.UpInjRow.upInj
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The scalar formula and injectivity

This section composes the steps of the chain. Let $\Theta_\tau$ be the total theta map of the row $\tau$, from the last space of the chain down to the forms on the first stage. Then $\Theta_\tau \Theta_\tau^*$ acts on each eigenpart of the first stage by the scalar $\kappa_0 \prod_i z_i$, where $\kappa_0 > 0$ and the $z_i$ are the $L$-values of the steps. All these numbers are positive, so the total up map $\Theta_\tau^*$ is injective. This is how the scalar law of [the last section](/entry/scalars/) is used: it is the input of [the theorem on large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/), in branch 1 of the [unitary hypotheses](/proof/unitary-hypotheses/), below the step [HypsAlt is nonempty](/step/nonempty-hyps/). There the injectivity lets a form on the first stage be recovered from its lift to the last space.

We keep the setting of [the last section](/entry/scalars-of-given-all/): a datum $D$ with a chain of length $m$, a family $A$ of characters indexed by $T$, a real realisation $R$, and a face $F$. Let $P$ be the finite set of places of $E$ fixed by the realisation, and let $S_F$ be the set of places of $F$ below the places of $P$. Let $\mathcal{E}$ be the space of forms on the first stage at the level given by $S_F$. For an eigensystem $c$ let $\mathcal{E}_c$ be its part for $c$. For a row $\tau$ the realisation gives a linear map $\Theta_\tau$ from the last Hilbert space $H_\tau$ to $\mathcal{E}$, and $\Theta_\tau^*$ is its adjoint. Both spaces are finite dimensional inner product spaces, so $\Theta_\tau^*$ exists.

**Definition 2.7.1 (Scalar formula).** The realisation $R$ satisfies the *scalar formula* at $S_F$ if there is $\kappa_0 > 0$ with this property. For every row $\tau$, every eigensystem $c$ and all real numbers $z_1, \dots, z_m$ such that each $z_i$ is an $L$-value of the row $\tau$ and of $c$ at the index $i$,
$$\Theta_\tau \Theta_\tau^* x = \Big(\kappa_0 \prod_{i=1}^m z_i\Big)\, x \qquad \text{for all } x \in \mathcal{E}_c.$$

An $L$-value of $\tau$ and $c$ at the index $i$ is a value at the index $i$, in the sense of the scalar law, for some parameter system of $c$ off the bad places of $\tau$. Such a value is positive.

**Definition 2.7.2 (Injectivity of the up maps).** The realisation $R$ has *injective up maps* if $\Theta_\tau^*$ is injective for every row $\tau$.

**Theorem 2.7.3 (Scalar formula and injectivity).** Assume the ten published results of [the step scalars](/entry/scalars/): the finiteness theorem of Harish-Chandra, the rapid decay of cusp forms, the cover by discrete series, the theory of Harish-Chandra modules, the Casselman-Wallach theorem, the unramified Howe correspondence, the Weil-Siegel formula for unitary groups, the Rallis inner product formula for every datum, the continuation of Siegel Eisenstein series and the unramified doubling identity. Let $R$ and $F$ satisfy the standing conditions, let the ideal $\mathfrak{c}_K$ of the host of $D$ be the unit ideal, and let the finite set $S_b$ of places of the realisation be equal to $P$. Assume the *fixing condition*: for every row $\tau$ and every place $\mathfrak{P}$ that is good for $\tau$ and satisfies $\overline{\mathfrak{P}} = \mathfrak{P}$, the data of the row at $\mathfrak{P}$ are fixed. Let $S_F$ be the set of places of $F$ below $P$. Then $R$ satisfies the scalar formula at $S_F$, and $R$ has injective up maps.

Lean: `GlobalTheory.Core.Rk.UpInjRow.upInj` (also `GlobalTheory.T.thetaLift_adjoint_scalarFormula_injective`, a second name).

*Proof.* We first prove the scalar formula, then the injectivity.

1. *Inputs.* By [the step scalars](/entry/scalars/), $R$ satisfies the scalar law with constants $\kappa_1, \dots, \kappa_m > 0$. By a lemma on the theta lift, which uses the rapid decay, the Howe correspondence, the core condition and the fixing condition, the adjoint of each step keeps the spherical parts off the row. By another lemma, from the rapid decay, the realisation satisfies the Schur condition at every row.
2. *The scalar formula.* A lemma on the chain scalars takes the core condition, the Schur condition, the scalar law and the property of step 1, and gives the scalar formula.
3. *A positive scalar for each part.* Fix a row $\tau$. For each eigensystem $c$ we find $s_c > 0$ with $\Theta_\tau \Theta_\tau^* = s_c$ on $\mathcal{E}_c$. If the row part $W(\tau, c)$ is zero, then $\mathcal{E}_c = 0$, since $\mathcal{E}_c$ embeds into the row part; take $s_c = 1$. Otherwise the scalar law gives a parameter system $B$ of $c$, and for each $i$ a positive $L$-value $z_i$ at the index $i$: for $i < m$ from the step part of the law, and for $i = m$ from the top part. By the scalar formula, $s_c = \kappa_0 \prod_i z_i > 0$ works.
4. *Injectivity.* The eigenparts $\mathcal{E}_c$ span $\mathcal{E}$, by a lemma on the Hecke operators of the rows. Let $x \in \mathcal{E}$ with $\Theta_\tau^* x = 0$. For every $y \in \mathcal{E}_c$,
$$\langle x, y \rangle = s_c^{-1} \langle x, \Theta_\tau \Theta_\tau^* y \rangle = s_c^{-1} \langle \Theta_\tau^* x, \Theta_\tau^* y \rangle = 0.$$
So $x$ is orthogonal to every $\mathcal{E}_c$, hence to $\mathcal{E}$, and $x = 0$.

Steps 2 and 4 prove the two claims. $\square$

The proof of step 4 uses only two facts: $\Theta_\tau \Theta_\tau^*$ acts on each part by a nonzero scalar, and the parts span the space. The positivity of the scalars is not needed for injectivity, only that they are not zero; the scalar formula itself records the positive constant.

**Remark 2.7.4 (Formalization).** The theorem is at [ThetaLiftAdjointScalarFormulaInjective.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjective.lean#L32), and the passage from the scalar formula to injectivity (steps 3 and 4) is a separate lemma in [UpInjOfBForm.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UpInjOfBForm.lean#L52). The scalar formula and the injectivity are defined in [RealLowestKTypeCoeffSquareIntegrable.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L46). The lemmas of steps 1, 2 and 4 were read as statements only. Step 4 calls a lemma on adjoints whose proof we have not opened; the argument given is a proof of its statement. We have not unfolded the eigenparts $\mathcal{E}_c$, the map $\Theta_\tau$, the Schur condition, the fixing condition or the set $S_F$ beyond its defining property. The hypothesis $S_b = P$ is not used (line 33), and the lemma of steps 3 and 4 does not use the absolute irreducibility of the characters that it takes as a hypothesis (line 51).
