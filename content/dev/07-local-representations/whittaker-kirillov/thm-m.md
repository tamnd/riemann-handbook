---
id: thm-m
title: The local Bessel integral of a discrete series has rank one
kind: theorem
decl: ReciprocityTheory.ChartRestriction.DS.Mult1.thmM
module: ReciprocityTheory.ReductiveGroups.DiscreteSeries.MultiplicityOne.ThmMOfXi
covers: 950
status: drafted
drafted_by: writer@claude
---
This theorem says that the local Bessel integral of a discrete series with fast decay factors through one equivariant map. It is an input of [HypsAlt](/step/nonempty-hyps/), and [uniqueness of Bessel maps](/entry/bessel-map-uniq-gap/) uses it. The proof only fills the two hypotheses of [the theorem with $\Xi$](/entry/thm-m-of-xi/), which has the real content.

## Statement

Let $G$ be the unitary group of the form $H_{k,r}$ on $\mathbb{C}^n$, $n = 2r + k + 1$. Let $N$ be the unipotent subgroup with character $\psi$, and $W$ the compact stabilizer of the vector $z$. Let $\pi$ be an irreducible unitary representation of $W$ on a finite-dimensional space $V$, and let the Haar measure of $W$ have mass $1$ (`IsDiag`). Let $\sigma$ be an irreducible unitary representation of $G$ on $\mathcal{H}$ with square-integrable matrix coefficients (`SqIntG`). Let $w$ be a unit vector with $|\langle w, \sigma(x)w\rangle| \leq C\|x\|^{-a}$ and $a \geq 4n^3$. Let $V_a$ be the set of $u$ with $|\langle w, \sigma(x)u\rangle| \leq C_u\|x\|^{-a}$. For $u, u' \in V_a$ let
$$\beta(u, u') = \int_W \int_N \langle u', \sigma(mh)u\rangle\, \overline{\psi(m)}\, \pi(h)^{-1} \, dm \, dh \in \mathrm{End}(V).$$

**Theorem.** There is a map $l \colon \mathcal{H} \to V$, linear on $V_a$, with $l(\sigma(mh)u) = \psi(m)\pi(h)l(u)$ and $\beta(u, u')\xi = \langle l(u'), \xi\rangle\, l(u)$ for all $u, u' \in V_a$ and $\xi \in V$.

The map $l$ may be $0$. Then the theorem says that $\beta$ vanishes.

## Proof

`thmM_of_xi` applied to `multiplicity_one_hypotheses_hold` (the structural facts on the unitary group) and to [`xiExists`](/entry/xi-exists/) (the majorant $\Xi$).

## In the Lean code

The theorem is in [ThmMOfXi.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/ThmMOfXi.lean#L35). `ThmM` is in [StDiagExists.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/StDiagExists.lean#L151). `IsMultOneMap`, `beOp` and `rk1` are in [StDefs.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/StDefs.lean#L78).
