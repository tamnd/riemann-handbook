---
id: res-core
title: At s = t/2 the Siegel Eisenstein series of a Weil section has at most a simple pole, with a theta residue
kind: theorem
decl: PositivityTheory.Rg.Rsw.resCore
module: Development.WeilBound.RepresentationTheoryGL.RegularisedSiegelWeil.ThetaIdempotents.ThetaCoefficients.ResCore
covers: 3947
status: drafted
drafted_by: writer@claude
---
This theorem proves `ResCore`: the Siegel Eisenstein series on $U(n,n)$ of a Weil section from $B$, the sum of $W$ and $t$ hyperbolic planes, has at most a simple pole at $t/2$, and its residue is orthogonal to each function orthogonal to all theta functions of $W$. It has no hypotheses; its user is [the non-vanishing of the down lift](/entry/down-ne-k-of-hypotheses-prime/).

## Statement

Let $G = U(n,n)(\mathbb{A})$ with Siegel parabolic $P$. Let $r = \dim W$, $B$ the sum of $W$ and $t$ hyperbolic planes (`HypDec`), $n = r + t$, $1 \le r < t$ and $r + 2 < 2t$. Fix an additive character $\psi$, a Hecke character $\chi$ with $\chi|_{\mathbb{A}_F^\times} = \eta^r$ (`ResEta`), and Weil representations $\omega_B$, $\omega_W$ of $G$ (`IsWeilSch`). Let $H > 0$ be continuous, with $H(qg) = |\det a_q|\, H(g)$ for $q \in P$, of finite level. For a Schwartz function $\Phi$ on $B$, put $\varphi(g) = (\omega_B(g)\Phi)(0)$.

Let $E(z, g)$ be holomorphic in $z$ on an open $U \ni t/2$, continuous, left $G(F)$-invariant, with

$$E(z, g) = d(z) \sum_{\gamma \in P(F) \backslash G(F)} H(\gamma g)^{z - t/2} \varphi(\gamma g) \quad (\operatorname{Re} z > \sigma)$$

for a polynomial $d \ne 0$ (`IsCont`). Let $\mathrm{cf}_k$ be the coefficient of $(z - t/2)^{-k}$ in $E/d$, written in `cf` as $\frac{1}{2\pi i}\oint (z - t/2)^{k-1} E/d\, dz$ around a circle in $U$ inside which $d$ has no zero except perhaps $t/2$ (`IsRad`).

**Theorem.** Then:

1. $\mathrm{cf}_k = 0$ for each $k \ge 2$;
2. let $\pi$ be a finite measure on $X$, $c \colon X \to G$ measurable with relatively compact image, and $\kappa \in L^1(\pi)$. If $\int_X \theta_W(\Psi)(c(x), h)\, \kappa(x)\, d\pi = 0$ for all Schwartz functions $\Psi$ on $W$ and all $h \in U(W)(\mathbb{A})$, then $\int_X \mathrm{cf}_1(c(x))\, \kappa(x)\, d\pi = 0$.

Here $\theta_W(\Psi)(g, h) = \sum_{\xi} (\omega_W(g)\Psi)(h^{-1}\xi)$, over the rational $r \times n$ matrices $\xi$. We have not unfolded `IsInfFam` or `IsEta`.

## Proof

`resCore` applies `L.resCore` to fifteen proved inputs.

1. `Polar` gives the rank condition `RankLT ψ (cf k) r` for $k \ge 2$. We have not unfolded `RankLT`.
2. `JPos` gives a place $v$ outside a finite set, a cut operator $C$ at $v$ and an entire $c$ with $c(t/2) \ne 0$. The $K_v$-average of $C$ multiplies each section at $z$ by $c(z)$.
3. `CfFJ` gives $N$ with $\mathrm{cf}_k = 0$ for $k > N$. Descend from $N$: if $\mathrm{cf}_j = 0$ for $j > k$, `CfRel` says that the average of $C(\mathrm{cf}_k)$ is $c(t/2)\,\mathrm{cf}_k$, and for $k \ge 2$ `CutLow` gives $C(\mathrm{cf}_k) = 0$ from the rank condition.
4. For $k = 1$, `CutId` gives $\kappa'$ with $C(\mathrm{cf}_1)(g) = \kappa' \int_{\mathcal{F}} \theta_W(\Psi')(g, h)\, dh$ over a fundamental domain $\mathcal{F}$, for a Schwartz function $\Psi'$ on $W$ made from $\Phi$ and $C$. With the bounds `ThBdd` and `ThCoef`, Fubini moves the integral over $X$ inside, where it is zero by hypothesis.

## In the Lean code

The theorem is at [ResCore.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/ThetaCoefficients/ResCore.lean#L44), `ResCore` at [HasLevel.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/SingularNullSets/HasLevel.lean#L19), and `L.resCore` at [LResCore.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/SingularNullSets/LResCore.lean#L25). We have not read the proofs of the fifteen inputs.

- At [line 61](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ThetaIdempotents/ThetaCoefficients/ResCore.lean#L61), `ie` is `L.ikEq2` behind a function that ignores its three arguments `geng`, `wm` and `ikSch`.
- The hypothesis $r + 2 < 2t$ follows from $1 \le r < t$.
- The module path names a regularised Siegel-Weil formula, but we have not matched the statement with a published theorem.
