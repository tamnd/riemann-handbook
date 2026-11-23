---
title: Potential semi-abelian reduction
decls:
  - GlobalTheory.SS.potentialSemistable_rational_lTorsion_any_closure
  - GlobalTheory.T.potentialSemistable_of_rational_lTorsion
  - GlobalTheory.SS.potModel_of_rational_torsion
  - GlobalTheory.T.principallyPolarizedAbelianVariety_potentialSemiAbelianModel
  - GlobalTheory.SemiPol.potModel_semiAbelian
  - GlobalTheory.SS.exists_semiAbelian_model_padic_polAV
  - GlobalTheory.SS.semistableReductionSt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Potential semi-abelian reduction

This section proves Grothendieck's semistable reduction theorem for principally polarized abelian varieties over local fields of characteristic $0$ with finite residue field. After a finite extension of the base, the abelian variety has a semi-abelian group model. We first prove it when the $\ell$-torsion is rational for some prime $\ell \geq 3$ that is a unit, with [the criterion of the previous section](/entry/is-semi-abelian-of-rational-torsion/). Then we make the $\ell$-torsion rational by a finite extension. The last theorem is the semistable reduction statement over finite extensions of $\mathbb{Q}_p$ inside $\overline{\mathbb{Q}}_p$, the algebraic closure of $\mathbb{Q}_p$. The earlier sections assume this statement, and it enters the main proof at [the step on every character](/step/every-character/). We keep the notation of the previous section.

### Potential models

**Definition 6.19.1 (Potential model).** Let $V$ be a ring with a map to a field $K$, let $A$ be a group scheme over $K$, and let $Q$ be a property of group schemes over local rings. Then $A$ has a *potential model* with $Q$ over $V$ if there are a discrete valuation ring $W$ with fraction field $L$, a local map $V \to W$ that makes $W$ a finite $V$-module, and a map $K \to L$ compatible with $V$, such that $W$ is complete for its maximal ideal, and a group model $G$ of $A$ over $W$ and $L$ that has $Q$.

Lean: `GlobalTheory.SS.PotModel`.

**Definition 6.19.2 (Group pullback).** Let $f : S' \to S$, let $A$ be a group scheme over $S$ and $A'$ one over $S'$. A map $\varphi : A' \to A$ over $f$ makes $A'$ a *group pullback* of $A$ if the square of $\varphi$ and $f$ is a pullback square and $\varphi$ respects the group laws.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.IsGrpPullback`.

### Inputs

In the inputs, $V$ is a complete discrete valuation ring with finite residue field of $q$ elements, and $K$ is its fraction field, of characteristic $0$. Let $\Omega$ be an algebraic closure of $K$ with a compatible map from $V$, and let $\ell$ be a prime that is a unit in $V$.

**Theorem 6.19.3 (Frobenius and tame inertia).** There are a local $V$-subalgebra $R$ of $\Omega$ and $\sigma, \varphi \in \operatorname{Gal}(\Omega/K)$ with these properties. $R$ is strictly Henselian with fraction field $\operatorname{Frac} R$, and $V \to R$ is local. Each $c$ in the residue field of $R$ has $c^{q^m} = c$ for some $m \geq 1$. Each finite subset $s$ of $R$ lies in a $V$-subalgebra $W$ of $R$ that is a complete discrete valuation ring, finite over $V$, with $W \to R$ local, and fixed by $\varphi^f$ for some $f \geq 1$. The map $\sigma$ fixes $R$, and $\varphi$ sends $R$ to $R$ with $\varphi(x) \equiv x^q$. Properties 3 and 4 of the theorem on rational torsion hold with $q$ in place of $p^{r_0}$.

Lean: `GlobalTheory.T.exists_maxUnramified_frobenius_tame_alt`.

**Theorem 6.19.4 (Neutral components of finite level).** Let $V$ be a discrete valuation ring with fraction field $K$, let $R$ be strictly Henselian with fraction field $K'$, with $V \to R$ and $K \to K'$ compatible, and let $A$ be a principally polarized abelian variety over $K$. Then there are a finite set $s \subset R$ and $c \geq 1$ such that each $V$-subalgebra $W \supset s$ of $R$ that is a discrete valuation ring with $W \to R$ local carries a group model $G$ of $A$ over $W$ and its fraction field. Here $G$ is smooth and connected of relative dimension $g$, its fibre over the residue field of $R$ has an ample cubical bundle, and $y^c$ extends to an $R$-point for every $K'$-point $y$ of $G$.

Lean: `GlobalTheory.T.exists_neronNeutralComponent_finite_level`.

**Theorem 6.19.5 (Finite complete subrings).** Let $V$ be a complete discrete valuation ring of characteristic $0$, $F$ a field that is algebraic over $V$, and $s \subset F$ finite. Then there is a $V$-subalgebra $W$ of $F$ that is a complete discrete valuation ring, finite and free over $V$, with $V \to W$ local, such that each $x \in s$ is a fraction $a/b$ with $a, b \in W$.

Lean: `GlobalTheory.exists_complete_dvr_finite_subalgebra`.

**Theorem 6.19.6 (Potential models are transitive).** Let $V \to V_1$ be local and finite, with fraction fields $K \to K_1$ compatible, and let $A_1$ be a group pullback of $A$ along $K \to K_1$. If $A_1$ has a potential model with $Q$ over $V_1$, then $A$ has a potential model with $Q$ over $V$.

Lean: `GlobalTheory.SS.potModel_trans`.

### Rational torsion

**Theorem 6.19.7 (Potential models from rational torsion).** Let $V$ be a complete discrete valuation ring with finite residue field and with fraction field $K$ of characteristic $0$. Let $\ell \geq 3$ be a prime that is a unit in $V$, let $A$ be a principally polarized abelian variety over $K$, and let $\Omega$ be an algebraic closure of $K$ with a compatible map from $V$. If every $\tau \in \operatorname{Gal}(\Omega/K)$ fixes each $x \in A(\Omega)$ with $x^\ell = 1$, then $A$ has a potential semi-abelian model over $V$.

Lean: `GlobalTheory.SS.potentialSemistable_rational_lTorsion_any_closure`.

*Proof.* The theorem on Frobenius and tame inertia, with $q$ the number of elements of the residue field of $V$, gives $R$, $\sigma$ and $\varphi$. Since the residue field is finite of characteristic $p$, $q = p^{r_0}$ with $r_0 \geq 1$. The residue field of $R$ contains that of $V$, so it has characteristic $p$. The maps $V \to R \to \Omega$ are injective. Let $K'$ be the fraction field of $R$, and let $K \to K'$ be induced by $V \to R$.

The theorem on neutral components of finite level gives $s$ and $c$. The theorem on Frobenius and tame inertia gives $W \supset s$, complete and finite over $V$, with $W \to R$ local and $\varphi^f$ fixing $W$. So we get a group model $G$ of $A$ over $W$ and its fraction field $L$. Since $\ell$ is a unit in $V$, it is a unit in $R$. All hypotheses of the theorem on rational torsion hold, so $G$ is semi-abelian. The map $V \to W$ is local, since $V \to R$ is local. So $W$, $L$ and $G$ give a potential semi-abelian model. $\square$

**Theorem 6.19.8 (Rational torsion in the algebraic closure).** The same holds with the algebraic closure $\overline{K}$ of $K$ in place of $\Omega$: if every $\tau \in \operatorname{Gal}(\overline{K}/K)$ fixes the $\ell$-torsion of $A(\overline{K})$, then $A$ has a potential semi-abelian model over $V$.

Lean: `GlobalTheory.T.potentialSemistable_of_rational_lTorsion` (also `GlobalTheory.SS.potModel_of_rational_torsion`, a second name).

*Proof.* Apply the theorem on potential models from rational torsion with $\Omega = \overline{K}$. $\square$

### All principally polarized abelian varieties

**Lemma 6.19.9 (A small prime).** In a local ring, $3$ or $5$ is a unit.

Lean: `GlobalTheory.SemiPol.exists_prime_unit`.

*Proof.* Since $2 \cdot 3 - 5 = 1$ is a unit, one of $2 \cdot 3$ and $-5$ is a unit in a local ring. If $2 \cdot 3$ is a unit, so is $3$. $\square$

**Lemma 6.19.10 (Fields of the torsion).** Let $A$ be a principally polarized abelian variety over $K$ of characteristic $0$, with algebraic closure $\Omega$, and let $\ell$ be prime. There is a finite set $s \subset \Omega$ such that, for each extension $K \subset K_1 \subset \Omega$ that contains $s$, every $x \in A(\Omega)$ with $x^\ell = 1$ comes from a $K_1$-point.

Lean: `GlobalTheory.SemiPol.exists_finset`.

*Proof.* The $\ell$-torsion is finite, with $\ell^{2g}$ elements. Each point $x$ is defined over a finite extension of $K$, which a finite set spans over $K$. Let $s$ be the union of these sets. $\square$

**Lemma 6.19.11 (Base change of a polarization).** For every $f : S' \to S$, a principally polarized abelian variety $A$ over $S$ has a group pullback $A'$ along $f$ that is a principally polarized abelian variety.

Lean: `GlobalTheory.SemiPol.exists_pullback`.

**Lemma 6.19.12 (Rational torsion after base change).** Let $K \subset K_1 \subset \Omega$, let $A_1$ be a group pullback of $A$ along $K \to K_1$, and let $\Omega_1 \cong \Omega$ over $K_1$. If every $x \in A(\Omega)$ with $x^\ell = 1$ comes from a $K_1$-point, then every $\tau \in \operatorname{Gal}(\Omega_1/K_1)$ fixes the $\ell$-torsion of $A_1(\Omega_1)$.

Lean: `GlobalTheory.SemiPol.fixed_of_rational`.

*Proof.* The pullback square identifies $A_1(\Omega_1)$ with $A(\Omega_1)$, and the isomorphism $\Omega \cong \Omega_1$ moves $x$ to $A(\Omega)$. There $x$ comes from a $K_1$-point $y$, and $\tau$ fixes $K_1$, so $\tau$ fixes $x$. $\square$

**Theorem 6.19.13 (Potential semi-abelian models).** Let $V$ be a complete discrete valuation ring with finite residue field and with fraction field $K$ of characteristic $0$. Then every principally polarized abelian variety $A$ over $K$ has a potential semi-abelian model over $V$.

Lean: `GlobalTheory.T.principallyPolarizedAbelianVariety_potentialSemiAbelianModel` (also `GlobalTheory.SemiPol.potModel_semiAbelian`, a second name).

*Proof.* By the lemma on a small prime, there is a prime $\ell \in \{3, 5\}$ that is a unit in $V$. Let $\Omega$ be the algebraic closure of $K$, and let $s$ be the set from the lemma on fields of the torsion. The ring $V$ has characteristic $0$ and $\Omega$ is algebraic over $V$. The theorem on finite complete subrings gives $W \subset \Omega$, complete and finite over $V$, such that each element of $s$ is a fraction of $W$.

Let $K_1$ be the fraction field of $W$. Then $K \subset K_1 \subset \Omega$, the field $\Omega$ is an algebraic closure of $K_1$, and the residue field of $W$ is finite, as $W$ is finite over $V$. The lemma on base change gives a principally polarized abelian variety $A_1$ over $K_1$ that is a group pullback of $A$. Since $K_1$ contains $s$, the $\ell$-torsion of $A$ comes from $K_1$-points. By the lemma on rational torsion after base change, $\operatorname{Gal}(\overline{K_1}/K_1)$ fixes the $\ell$-torsion of $A_1$. The image of $\ell$ in $W$ is a unit. The theorem on rational torsion in the algebraic closure gives a potential semi-abelian model of $A_1$ over $W$. By transitivity, $A$ has one over $V$. $\square$

### The semistable reduction statement

**Definition 6.19.14 (The semistable reduction statement).** The *semistable reduction statement* says the following. Let $p$ be prime and let $K$ be a subfield of $\overline{\mathbb{Q}}_p$ that is finite over $\mathbb{Q}_p$. For every principally polarized abelian variety $A$ over $K$, there is a field $K \subset K' \subset \overline{\mathbb{Q}}_p$, finite over $\mathbb{Q}_p$, and a semi-abelian group scheme $G$ over the integral closure $\mathcal{O}_{K'}$ of $\mathbb{Z}_p$ in $K'$, such that $G_{K'}$ is a group pullback of $A$ along $K \to K'$.

Lean: `GlobalTheory.Published.SemistableReductionSt`.

**Lemma 6.19.15 (Embedding the extension).** Let $W$ be a domain, finite over $\mathcal{O}_K$, with fraction field $L$, and let $K \to L$ be compatible. Then there are a field $K \subset K' \subset \overline{\mathbb{Q}}_p$, finite over $\mathbb{Q}_p$, and maps $\tau : L \to K'$ over $K$ and $f : W \to \mathcal{O}_{K'}$ with $\tau|_W = f$.

Lean: `GlobalTheory.SS.exists_ringHom_integralClosure`.

*Proof.* The extension $L/K$ is finite, since $W$ is finite over $\mathcal{O}_K$. As $\overline{\mathbb{Q}}_p$ is algebraically closed, there is an embedding $\tau : L \to \overline{\mathbb{Q}}_p$ over $K$. Let $K'$ be its image. It is finite over $\mathbb{Q}_p$. Each $w \in W$ is integral over $\mathcal{O}_K$, hence $\tau(w)$ is integral over $\mathbb{Z}_p$ and lies in $\mathcal{O}_{K'}$. $\square$

**Theorem 6.19.16 (Semi-abelian models over $p$-adic fields).** Let $p$ be prime, let $K \subset \overline{\mathbb{Q}}_p$ be finite over $\mathbb{Q}_p$, and let $A$ be a principally polarized abelian variety over $K$. Then there are $K \subset K' \subset \overline{\mathbb{Q}}_p$, finite over $\mathbb{Q}_p$, and a semi-abelian group scheme $G$ over $\mathcal{O}_{K'}$ whose generic fibre is a group pullback of $A$ along $K \to K'$.

Lean: `GlobalTheory.SS.exists_semiAbelian_model_padic_polAV`.

*Proof.* The ring $\mathcal{O}_K$ is a complete discrete valuation ring with finite residue field and fraction field $K$. The theorem on potential semi-abelian models gives $W$, $L$ and a semi-abelian group model $G$ of $A$ over $W$. The lemma on embedding the extension gives $K'$, $\tau$ and $f$. The base change of $G$ along $f$ is semi-abelian over $\mathcal{O}_{K'}$. Its generic fibre is the base change of $G_L \cong A_L$ along $\tau$, which is a group pullback of $A$ along $K \to K'$. $\square$

**Theorem 6.19.17 (Semistable reduction).** The semistable reduction statement holds.

Lean: `GlobalTheory.SS.semistableReductionSt`.

*Proof.* This is the theorem on semi-abelian models over $p$-adic fields. $\square$

**Remark 6.19.18 (Formalization).** The theorems are in [PotentialSemistableOfRationalLTorsion.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/PotentialSemistableOfRationalLTorsion.lean#L146), [PrincipallyPolarizedAbelianVarietyPotentialSemiA.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/PrincipallyPolarizedAbelianVarietyPotentialSemiA.lean#L117), [ExistsSemiAbelianModelPadicPrincipallyPolarised.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsSemiAbelianModelPadicPrincipallyPolarised.lean#L69) and [SemistableReductionPpavPadicField.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SemistableReductionPpavPadicField.lean#L19). The prime $\ell$ comes from the identity $2 \cdot 3 - 5 = 1$, so the proof never needs a prime larger than $5$. The final theorem has a second wrapper, `GlobalTheory.T.semistableReduction_ppav_padicField`, which the users cite and which is not in this chapter's list. The finite field facts on $\mathcal{O}_K$ come from other files.
