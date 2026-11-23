---
id: flag-model-exists
title: Flag models over a Hodge component
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.PB.FMX.flagModelExists
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.FlagModelExistsOfGiven
covers: 410
status: drafted
drafted_by: writer@claude
---
This theorem builds the flag bundle over a Hodge component of a unitary Shimura variety, in coordinates: the old ones and the Plücker coordinates of a generic flag in each Hodge bundle. It goes up through [the statement form](/entry/flag-model-exists-of-given/) to [the tie lemma](/entry/tie-of/).

## Statement

Let $\Psi = \mathrm{CMType}(H)$ for a CM field with host $H$, let $(p, q)$ be the signature, $Y$ an integral model of the moduli space, and $x_0$ a point in multiprojective coordinates over a field $\Omega$ of characteristic $0$. A Hodge component $\mathfrak{M}$ over $x_0$ is a normal scheme $X \to Y$ with a generic point $\xi$ over $\Omega$ tied to $x_0$, and Hodge bundles cut out by the $\mathcal{O}_E$-eigenspaces of a Lie algebra. Fix bases of the generic eigenspaces $W_\tau$ and $(W'_\tau)^\vee$, of ranks $p$ and $q$, for $\tau \in \Psi$.

**Theorem.** Assume that the coordinate ideal of $x_0$ is an arithmetic variety of dimension $n + 1$, and that $\mathfrak{M}$ is a cover of degree $d$ ($[\Omega : \Omega_0] = d > 0$ over a generic point of $Y$). Then there are a point $y$ over a field $\Phi$, a flag model $M$ over $y$ ($N = p + q$, $j = p$), a Hodge component $\mathfrak{M}_1$ over the base coordinates of $M$ with a flag tie, and a Hodge component $\mathfrak{M}'$ over $y$ with a flag $\mathrm{Fl}$, such that:

1. $\mathfrak{M}_1$ is $\mathfrak{M}$ in new coordinates, with the same bases, degree and arithmetic dimension, and an SNC boundary of $\mathfrak{M}$ gives one of $\mathfrak{M}_1$;
2. the coordinate ideal of $y$ is an arithmetic variety of dimension $n + |\Psi|\bigl(\binom{p}{2} + \binom{q}{2}\bigr) + 1$, where $\binom{p}{2} + \binom{q}{2}$ is the dimension of the complete flags;
3. the tie is total: $\mathfrak{M}'$ lies over $\mathfrak{M}_1$ with the lattices pulled back, $\mathrm{Fl}$ is given by the columns of the blocks of $g_\tau$ of $M$ against the fixed bases, it has root lines of integer degrees $x_{\deg}$, and $M.\mathrm{dy}(\tau, i) = -\sum_{k \leq i} x_{\deg}(\tau, k)$;
4. $\deg \mathrm{Fl} = d$.

## Proof

1. `exists_twisted_generators` gives linear forms $\varphi_s$ that generate each bundle after a twist. `frame_via_twisted_generators` gives a left inverse of their matrix $A_s$ on the basis.
2. Let $\Phi = \Omega(u)$, with $u$ the entries below the diagonal of unipotent matrices $U_s$ of sizes $p$ and $q$. The point $y$ is $x_0$ with the minors of the first $k$ columns of $A_s U_s$, for each $k$. `hodgeCpt_frame_change_determinant` ties $\xi$ to the base coordinates. Six lemmas, among them `isGenericFlag_gMat`, give the conditions `ModelOK`, and `model` builds $M$. `hodgeCpt_frame_minor_valuation` gives the frame conditions of the tie.
3. `hodgeCpt_frame_leading_term` gives a smooth $Z \to X$ with generic point over $\Phi$ tied to $y$, and `hodgeCpt_base_change_compatible` puts $\mathfrak{M}'$ on $Z$. `hodgeCpt_frame_divisor_formula` gives $\mathrm{Fl}$ of degree $d$, and `hodgeCpt_frame_height_formula` gives $x_{\deg}$.
4. Four lemmas give the two dimensions, the SNC boundary and the normality of $Z$, and $\mathfrak{M}_1$ is `reTie` of $\mathfrak{M}$.

## In the Lean code

The theorem is in [FlagModelExistsOfGiven.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagModelExistsOfGiven.lean#L34). The statement is in [ExistsFlagModelBaseMetric.lean](lean:Development/AutomorphicSpectrum/Statements/MetricStatements/ExistsFlagModelBaseMetric.lean#L66), and $y$ and $M$ are built in [ColFlags.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/ColFlags.lean#L58).

The hypothesis `Top.Given` is introduced as `_` at line 35 and never used. Four lemma names do not match what they give: `hodgeCpt_frame_order_bound` gives the arithmetic dimension of the base coordinates, `hodgeCpt_frame_unit_criterion` gives that of $y$, `hodgeCpt_frame_generic_rank` gives the SNC boundary, and `hodgeCpt_frame_degree_formula` gives that $Z$ is normal.
