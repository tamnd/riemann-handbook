---
id: hco
title: The coefficient law for a zeta system
kind: theorem
decl: UpperTheory.V.Z.Kato.K5.hco
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.SmoothedZetaClasses.Hco
covers: 1535
status: drafted
drafted_by: writer@claude
---
This theorem says that on inertia a single zeta system is a multiple of the cyclotomic logarithm plus a coboundary. The multiple is a $\chi$-average of values of $\lambda$ on Eisenstein-type series. It is the first input of [the Hodge-Tate law for smoothed zeta classes](/entry/k5-top/), which smooths it and sums it over $x$. Its own main input is [`thdiam`](/entry/thdiam/).

## Statement

The setting is the one of [`K5.top`](/entry/k5-top/), with a single index $x \in \mathbb{Z}/N$ in place of the weights $c_x$: an odd prime $\ell$, $N$ prime to $\ell$, $e \geq 1$, the tower $X$, the embedding $j$ with $A = \{z : |j(z)| \leq 1\}$, the data that meet `AdmissibleHodgeTateZetaClassParams`, a character $\chi$ mod $N$ with values in $\mathbb{Z}_\ell$, and a linear form $\lambda$ that meets `IsLamFR2`. One hypothesis is new: for $s$ in inertia with $s \equiv 1$ on $\mu_\ell$, the second row of $\rho(s)$ is $(0, 1)$, where $\rho$ is the twist `rhoK` of $W$. Let $c_0 \geq 0$.

**Theorem.** There are $c' \geq 0$, $\kappa_0 \neq 0$ and units $p(n)$ with $p(n+1) \equiv p(n) \bmod \ell^n$ with this property. Let $x$ satisfy `AdmissibleNewformZetaData`, and let $Y$ be a zeta system for $x$ with fixed exponent $c_0$. Let $m \geq 1$, $y \in (\mathbb{Z}/\ell^m)^\times$, and let $\beta, t$ be integers with $\beta \equiv y \bmod \ell^m$, $\beta \equiv 1 \bmod N$ and $\ell^m t \equiv 1 \bmod N$. Put
$$h = p(m)^{-1} \ell^{c_0} \kappa_0 \sum_{\delta \in (\mathbb{Z}/N)^\times} \chi(\delta)^{-1} \lambda\bigl(\ell^m\, j(Q_\delta)\bigr),$$
where $Q_\delta$ is the coefficient sequence of the series `pieceT` with parameters $c, d$, $(x t \delta^{-1}, 0)$, $(t \delta^{-1}, 0)$, the $\beta$-th power of the root of unity `eOm` of order $N\ell^m$, and the matrices of determinant $1$ mod $\ell^m$. We have not unfolded `pieceT`. Then there are $o_k \in \overline{\mathbb{Q}}_\ell$ with $|o_k| \leq 1$ and $w_k \in \Omega$ with $|j(w_k)| \leq 1$ such that for each $s$ in inertia with $s \equiv 1$ on $\mu_{\ell^m}$,
$$\ell^{c'}\, Y_m(s, y)_1 \equiv \ell^{c'} \Bigl( h \cdot \frac{\chi_{\mathrm{cyc}}(s) - 1}{\ell^m} + \sum_k o_k \bigl(j(s w_k) - j(w_k)\bigr) \Bigr) \pmod{\ell^m}.$$

## Proof

If no $x$ satisfies `AdmissibleNewformZetaData`, the claim is vacuous; the proof takes $c' = 0$ and $\kappa_0 = 1$. Otherwise it picks one such $x_0$ and applies `UpperTheory.Kd.L.thdiam` to it. That gives $c_1$, $\kappa'$, and for each $\delta$ a series $g_\delta$ with coefficients in $A$: the coefficients of a theta series of the $\delta$-translate of the class are congruent to a multiple of $j(Q_\delta)$ plus the coboundary of $g_\delta$. Choose $k$ with $|\lambda(e_i)| \leq \ell^k$ on the finite support $S$ of $\lambda$, and $v$ with $|\ell^v| \leq |\#(\mathbb{Z}/N)^\times|$. The proof takes $c' = c_1 + k + v$ and $\kappa_0 = \kappa'/\#(\mathbb{Z}/N)^\times$, and $p$ is the period from `IsLamFR2`.

For given $x$, $Y$, $m$, the zeta system condition at a level $n \geq m$ gives a lift of the class of $Y$ to the tower. The proof then does this for $s$ in inertia:

1. `pushB_spec`, `galB_mem_B` and `diam_B` put the pushed class and its diamond translates in the right space.
2. `exists_cuspFunctional_oddWeight_oddPrime` and `exists_isThB_sum` give theta series $\Phi$ for the $\chi$-average, and `inChi_avg` puts the average in the $\chi$-eigenspace.
3. The congruence in `IsLamFR` compares $\lambda$ of the coefficients of $\Phi$ with $p(n)$ times the projection.
4. `exists_isLamG` gives the cyclotomic factor. The hypothesis on the second row of $\rho$ reads off $Y_m(s, y)_1$ from the zeta system condition.
5. `htCoL_of_fintype` assembles the coboundary terms over $S \times (\mathbb{Z}/N)^\times$, and `ZetaCoef.chain` closes the ultrametric estimate.

The rest is bookkeeping.

## In the Lean code

The theorem is in [Hco.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/Hco.lean#L34). `thdiam` is in [Thdiam.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/SiegelFixedPoints/Thdiam.lean#L12), and it calls [`thcocd`](/entry/thcocd/).

The constants $c'$, $\kappa_0$, $p$ come before $x$ in the statement, so they are uniform in $x$. This works because `thdiam` uses only the conditions on $c$, $d$ and the matrices from the data of $x_0$, and these do not mention $x$. The vacuous branch is at [line 74](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/Hco.lean#L74). The newform $g_N$ and $\iota$ appear only inside `AdmissibleNewformZetaData`.
