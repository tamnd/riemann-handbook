---
id: pointwise-bound-eigenfunction
title: The pointwise bound for Capelli eigenfunctions, by cases on the types
kind: theorem
decl: GlobalTheory.BpEigen.pointwise_bound_eigenfunction
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.PointwiseBoundCapelliEigenfunction
covers: 1067
status: drafted
drafted_by: writer@claude
---
This theorem bounds a decaying Capelli eigenfunction $f$ on $U(H_{k,r})$ at each point by its $L^2$ size on the big cell. The proof has two cases: the types $u, u'$ of the place datum differ, or they are equal. [The bound for discrete series coefficients](/entry/pointwise-bound-discrete-series/) uses it through the restatement [`T.pointwiseBound_capelli_eigenfunction`](/entry/pointwise-bound-capelli-eigenfunction/).

## Statement

We use the notation of [A pointwise bound for discrete series coefficients](/entry/discrete-series-coef-pointwise-bound/) for $n$, $G$, $P$ (with types $u, u'$ and reals $T, T'$), $p$, $E_f$, $\mathrm{big}(z)$ and $G_p$. Write $\|f\|^2 = \int_{\mathbb{C}^{r+1}} E_f(\mathrm{big}(z))\,dz$ and $m = (2r+2)p_0 + n_0(r+1)$.

**Theorem.** Assume `BesselXiIntegrable` and `ThmPActualCpt`. For all $C, C_3, C_0 \ge 0$ there are $C_4$ and $C_c$ with this property. Let $f \colon M_n(\mathbb{C}) \to \mathrm{Hom}(W_q, W_p)$, $b, c, A_0 \in \mathbb{R}$, $n_0, p_0 \in \mathbb{N}$ and $\lambda, \lambda' \in \mathbb{R}^n$ satisfy:

1. (`StdNum C b c P λ`) $1 \le c$, $c + 2 \le b$, $k \le b$; the entries of $\lambda$, $u$, $u'$ are bounded by $b$; $\lambda_t + 2c \le \lambda_s$ for $s < t$; $\lambda$ interlaces with $u$ and with $u'$ with margin $\frac12$; and $T, T' \ge b^{-C(2r+2)}$;
2. (`Cases P n₀`) either $n_0 = 0$ and $|u_l - u'_l| \ge 30(r+1)^2 + 6$ for some $l \le k$, or $n_0 = 30(r+1)^2 + 6$, $u = u'$, and $u'_l - u'_{l+1} \ge 2n_0 + 1$ for some $l < k$;
3. $3(r+1) \le 2p_0$ and $p_0 \le C_0(r+1)^2$;
4. (`EigDec f A₀ λ'`) $f$ is smooth on $G$; $\|g\|^{A_0} |D f(g)|$ is bounded on $G$ for each left and right derivative $D$ by unit Lie algebra elements; and $\mathcal{C}(y) f = \prod_s (y + \lambda'_s) f$ for real $y$, with $\mathcal{C}(y)$ the Capelli operator;
5. (decay margin) $C_c (r+1)^4 \bigl(3(r+1) n^2 + n^3\bigr) \le A_0 - m$;
6. $|\lambda'_s - \lambda_s| + m \le c - 1$ for each $s$;
7. (`RegularityBoundBigCell`) for each $a \le 2p_0 + n_0$, $\int |\det M_{r+1}(\mathrm{big}(z))|^{2a} E_f(\mathrm{big}(z))\,dz \le b^{2C_3(2r+2)^2 a}\,\|f\|^2$.

Then for each point $\gamma$ of size $r+1$ with $G_p(\gamma) > 0$,

$$E_f(\gamma) \le b^{C_4(2r+2)^4}\, G_p(\gamma)^{-(2p_0+n_0)}\, \|f\|^2.$$

## Proof

`T.topDensity_cutoff_dominated_of_HC_xi` turns `BesselXiIntegrable` into `NFTopDomAll`, a domination statement for cut-off top densities that we have not unfolded. Then two theorems give the bound in each case of `Cases`:

- `T.capelliEigenfunction_pointwiseBound_of_differentTypes`, for $n_0 = 0$ and $u_l \neq u'_l$ far apart. It gives constants $D_1, E_1$.
- `T.capelliEigenfunction_pointwiseBound_of_equalTypes`, for $u = u'$ with a large gap in $u'$. It gives constants $D_2, E_2$.

Take $C_4 = \max(D_1, D_2)$ and $C_c = \max(E_1, E_2)$. The decay margin for $C_c$ implies the margin for $E_1$ and for $E_2$, since the other factors are nonnegative. In each case, $b \ge 1$ follows from item 1 at the index $l$ of the case ($1 \le c$ and $c + 2 \le b$). The case theorem gives the bound with $D_i$, and `pointwise_bound_mono` raises $D_i$ to $\max(D_1, D_2)$. The rest is bookkeeping.

## In the Lean code

The theorem is in [PointwiseBoundCapelliEigenfunction.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundCapelliEigenfunction.lean#L25). The two case theorems have this statement with one case of `Cases` and the extra input `NFTopDomAll`. The lemma `pointwise_bound_mono` (line 14) says that `ThmBpAt` is monotone in $C_4$ when $b \ge 1$.

`ThmPActualCpt` is only passed to the two case theorems. The Capelli operator is `Q.CV`, built from a quantum minor operator; we have not unfolded it. The name `EigDec` is ambiguous in this file: `BpJoin` and `Formalism.FourierDecayAlt.P.CutBP2` are both open and both define `EigDec`. Only `BpJoin.EigDec` fits the arguments `f A₀ λ'`.
