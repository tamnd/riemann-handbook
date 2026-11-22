---
id: discrete-series-coef-pointwise-bound
title: A pointwise bound for discrete series coefficients
kind: theorem
decl: GlobalTheory.discreteSeriesCoef_pointwiseBound
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DiscreteSeriesCoefPointwiseBoundUnconditional
covers: 1099
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThmBpDS` with no hypothesis. `ThmBpDS` bounds a $K$-finite matrix coefficient of a discrete series of a unitary group at each point by its $L^2$ size on the big cell. Two theorems use it: `ptWide_at_record_gap` directly, and `loopRows_of_large_gap_discreteSeries` through the restatement `discreteSeriesCoef_pointwiseBound_unconditional`. Both sit below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

## Statement

Let $k, r \ge 0$ and put $n = 2r + k + 1$. Let $H_{k,r}$ be the hermitian form on $\mathbb{C}^n$ with $r$ hyperbolic pairs and the diagonal block $\mathrm{diag}(1, \dots, 1, -1)$ of size $k+1$. Its unitary group $G = U(H_{k,r})$ has signature $(r+k, r+1)$. A parameter $P$ has integers $k, r$, reals $T, T'$ and two sequences $u, u'$. A place datum $p$ for $P$ (`KB.Pl`) holds a tower of level data with two representations $\pi, \pi'$; its place condition makes $u, u'$ the types of $\pi, \pi'$, and it forces $k \ge 2$. The functions $f$ are maps from $n \times n$ matrices to $\mathrm{Hom}(W_q, W_p)$, with $W_p, W_q$ finite-dimensional Hilbert spaces.

The bound `ThmBpAt p f b C₄ n₀ p₀` says: for each point $\gamma$ of size $r+1$ with $G_p(\gamma) > 0$,

$$E_f(\gamma) \le b^{C_4 (2r+2)^4}\, G_p(\gamma)^{-(2p_0+n_0)} \int_{\mathbb{C}^{r+1}} E_f(\mathrm{big}(z))\, dz.$$

Here a point is a list of pairs $(s,t)$ with $s \ge 1$ and $t \neq 0$, and $\mathrm{big}(z)$ is the point $((1,z_0), \dots, (1,z_r))$ of the big cell. $G_p(\gamma) = |\det M_{r+1}(\gamma)|^2 - T_p |\det M_r(\gamma)|^2$, with $M_j(\gamma)$ a matrix built from $\gamma$. $E_f$ is a real density built from $p$ and $f$ (`TBB.Ew`), which we have not unfolded.

**Theorem** (`ThmBpDS`). For all reals $C_h$ and $C_0 \ge 0$ there are $C_4 \ge 0$ and $C_g^0$ with this property. Let $C_g \ge C_g^0$. Let $P$, $p$, $f$, $\lambda, \lambda' \in \mathbb{R}^n$, $\kappa, b \in \mathbb{R}$, $n_0, p_0 \in \mathbb{N}$ and a unitary representation $\sigma$ of $G$ satisfy:

1. `StdHyp`: $\lambda$ is a Harish-Chandra parameter that interlaces with $u$ and $u'$; $\kappa^{\pm 1} \le b^{C_h}$; the scaled $T\kappa^{-2r}$ and $T'\kappa^{-2r}$ lie in $[1, b^{C_h(2r+2)}]$; $\lambda, u, u'$ are bounded by $b$; the gaps of $\lambda$ are at least $C_g(2r+2)^3$, with larger gaps between entries of different sign in $\varepsilon$; and a shape and a separation condition hold;
2. all gaps of $\lambda$ are at least $200\,\|\lambda' - \lambda\|_1$;
3. $\sigma$ is a discrete series with Harish-Chandra parameter $\lambda'$ (`Rep.IsDS`);
4. $f$ is a two-sided translate of a $K$-finite matrix coefficient of $\sigma$ (`IsKFinCoefT`);
5. $n_0 = 30(r+1)^2 + 6$ if $u = u'$ on $1, \dots, k$, and $n_0 = 0$ if not;
6. $3(r+1) \le 2p_0$ and $p_0 \le C_0 (r+1)^2$.

Then `ThmBpAt p f b C₄ n₀ p₀` holds.

A Harish-Chandra parameter (`IsHCParam`) is a strictly decreasing vector with entries in $\mathbb{Z} + \frac{n-1}{2}$. `IsDSHpk` asks that $\sigma$, after conjugation by a Cayley matrix, is irreducible, unitary and square integrable, with lowest $K$-type $\lambda + \rho_n - \rho_c$. This matches Harish-Chandra's parametrization of the discrete series (Knapp, *Representation Theory of Semisimple Groups*, Chapter IX).

## Proof

The theorem [`T.pointwiseBound_discreteSeries_coefficients`](/entry/pointwise-bound-discrete-series-coefficients/) proves `ThmBpDS` from two inputs. The proof supplies them:

- `besselXiIntegrable_holds`, a proof of `BesselXiIntegrable` (the existence of a function $\Xi$ with a coefficient bound and an integrability condition). It is `ReciprocityTheory.ChartRestriction.DS.Xi.xiExists`.
- `actualClasses_compactSupport`, a proof of `ThmPActualCpt`. It is [`P.CutSE.actual_compact_theorem`](/entry/actual-compact-theorem/).

## In the Lean code

The theorem is in [DiscreteSeriesCoefPointwiseBoundUnconditional.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DiscreteSeriesCoefPointwiseBoundUnconditional.lean#L11). `ThmBpDS` is in [ThmBpDS.lean](lean:Development/AbelianVarietyTheory/Statements/DiscreteSeriesShifts/ThmBpDS.lean#L12), and `ThmBpAt` in [StatementTBB.lean](lean:Formalism/HermitianCurvature/StatementTBB.lean#L130). The sign vector $\varepsilon$ is the fixed `eps48 k r`. The word "unconditional" in the module name is right: both inputs are proved theorems.
