---
title: Level zero limits and the bound from three places
decls:
  - GlobalTheory.levelZeroForm_cutoff_tendsto_of_domination
  - GlobalTheory.T.levelZeroForm_cutoff_tendsto_of_density_domination
  - GlobalTheory.limEvT_pow_mul_of_topDomination
  - GlobalTheory.T.tendsto_levelZero_form_cutoff_pow_mul_of_domination
  - GlobalTheory.EigenThreePlaces.main
  - GlobalTheory.T.capelli_eigenfunction_bound_three_places
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Level zero limits and the bound from three places

This section has two parts. First we remove the cutoff from the level zero forms of a coefficient: if the cut-off top terms are dominated, then the level zero form of $\mathrm{cut}(\chi, F, \varepsilon)$ tends to that of $F$ as $\varepsilon \to 0^+$. This is the dominated convergence theorem, applied to an integral formula for the level zero form over the big cell. Second we use this limit to prove the pointwise bound for a decaying Capelli eigenfunction from data at three places: the given place $p$ and two places $p_\pm$ with shifted types. The second result is the engine of the [pointwise bound for eigenfunctions](/entry/pointwise-bound-eigenfunction/).

### Level zero forms

For a coefficient $F$ and a word $w$, the place defines a complex number $R_w(F)$, the *level zero form* of $F$ along $w$: the pairing of the derivatives of $F$ along $w$ at level $0$, with two empty base points. We write $\mathrm{Re}\, R_w(F)$ for its real part, and we have not unfolded it. For a cut-off coefficient it is an integral of top terms over the big cell; this is one of the facts that the next input supplies.

**Definition 5.5.1 (Compact classes).** The *compact class theorem* says the following. For all place data that satisfy the data conditions, there are subspaces $K_0, \dots, K_r$ of the space of radial functions on which the radial theory of the place holds, with a slice condition and a composite formula at level zero. Also, every compactly supported coefficient $F$ that lies in every decay class and is supported in $\{G_f \ge \varepsilon\}$ for some $\varepsilon > 0$ has its radial restriction in $K_0$. It is proved in Volume 11 as [Theorem 1.7.13 of Volume 11](/entry/actual-compact-theorem/).

We have not unfolded the radial theory, the slice condition or the composite formula. What we use is their consequence: for cut-off coefficients of large decay, the level zero form is the integral of the top term over the big cell.

**Theorem 5.5.2 (Limit of level zero forms).** Assume Ξ-integrability and the compact class theorem. For every $C_b$ there is $C_c$ with this property. Let $p$ be a place datum, $f$ a coefficient, $\chi$ a function, $A \in \mathbb{R}$, $N \in \mathbb{N}$ and $Y$ a finite set of reals. Assume that the place satisfies the decomposition condition at level $C_b$, that $\chi$ is a cutoff, that $f$ is smooth and lies in the decay class of order $A$ and depth $m$ for every $m$, that
$$C_c\,(r+1)^4\,(N n^2 + n^3) \le A,$$
and that for every word $w$ admitted for $Y$ with $|w| \le N$ the top terms of $f$ along $w$ are [dominated](/entry/top-density-cut-dominated-all/). Then for every word $w$ admitted for $Y$ with $|w| \le N$,
$$\lim_{\varepsilon \to 0^+} \mathrm{Re}\, R_w\bigl(\mathrm{cut}(\chi, f, \varepsilon)\bigr) = \mathrm{Re}\, R_w(f).$$

Lean: `GlobalTheory.levelZeroForm_cutoff_tendsto_of_domination` (also `GlobalTheory.T.levelZeroForm_cutoff_tendsto_of_density_domination`, a second name).

*Proof.* Three facts about the top terms hold under the decay margin; each comes with its own constant, and $C_c$ is the larger of the two constants. Fix an admitted word $w$ with $|w| \le N$.

1. For every $\varepsilon > 0$, $\mathrm{Re}\, R_w(\mathrm{cut}(\chi, f, \varepsilon)) = \int \mathrm{top}_w(\mathrm{cut}(\chi, f, \varepsilon))(c)\, dc$. This uses the compact class theorem.
2. For almost every $c$, $\mathrm{top}_w(\mathrm{cut}(\chi, f, \varepsilon))(c) = \mathrm{top}_w(f)(c)$ for all small $\varepsilon > 0$. Indeed the cutoff equals $1$ near the points with $G_f > 0$ once $\varepsilon$ is small.
3. $\int \mathrm{top}_w(f)(c)\, dc = \mathrm{Re}\, R_w(f)$. This uses Ξ-integrability, the compact class theorem and the domination.

By 2 the integrands converge almost everywhere, and the domination gives the integrable bound. The dominated convergence theorem gives the convergence of the integrals in 1 to the integral in 3. $\square$

**Theorem 5.5.3 (Limit for powers of the boundary function).** Assume Ξ-integrability, the compact class theorem and domination for all places. For every $C_b$ there is $C_c$ with this property. Let $p$ be a place datum, $f$ a coefficient, $A_0 \in \mathbb{R}$, $p_0, N \in \mathbb{N}$, $\chi$ a function and $Y$ a finite set of reals, such that the normal form hypothesis holds for $(C_b, C_c, f, A_0, p_0, \chi, N)$. Then for every word $w$ admitted for $Y$ with $|w| \le N$,
$$\lim_{\varepsilon \to 0^+} \mathrm{Re}\, R_w\bigl(\mathrm{cut}(\chi, G_f^{p_0} f, \varepsilon)\bigr) = \mathrm{Re}\, R_w(G_f^{p_0} f).$$

Lean: `GlobalTheory.limEvT_pow_mul_of_topDomination` (also `GlobalTheory.T.tendsto_levelZero_form_cutoff_pow_mul_of_domination`, a second name).

*Proof.* Take $C_1$ from the limit of level zero forms and $C_2$ from domination for all places, and put $C_c = \max(C_1, C_2)$. The coefficient $G_f^{p_0} f$ is smooth, since $G_f$ is a polynomial. Multiplying by $G_f^{p_0}$ lowers the decay order by $(2r+2)p_0$, so $G_f^{p_0} f$ lies in the decay class of order $A_0 - (2r+2)p_0$ for every depth. The normal form hypothesis gives the margin $C_1 (r+1)^4 (N n^2 + n^3) \le A_0 - (2r+2)p_0$. The normal form hypothesis with $C_2$ gives the domination of the top terms of $G_f^{p_0} f$. Now apply the limit of level zero forms to $G_f^{p_0} f$ with $A = A_0 - (2r+2)p_0$. $\square$

### The bound from three places

Let $p$ be a place datum with parameter $P$. For two parameter sequences $u^+, u'^+$ let $P^+$ be $P$ with $(u, u')$ replaced by $(u^+, u'^+)$, and define $P^-$ in the same way. Let $p_+$ and $p_-$ be place data with parameters $P^\pm$, the same space $W_p$, spaces $W_{q\pm}$, and the same vectors $z, z'$ as $p$. For $y \in \mathbb{R}$ let $\mathcal{C}(y)$ be the Capelli operator of $G$ at $y$, which acts on coefficients. A coefficient-valued map $A : G \to \mathrm{Hom}(W_{q\pm}, W_q)$ is *polynomial of degree $d$* if $A(g) = \sum_i c_i(g) L_i$ with fixed maps $L_i$ and polynomials $c_i$ in the matrix entries of degree at most $d$.

**Definition 5.5.4 (Linked shifted places).** Let $f$ be a coefficient, $A_\pm$ polynomial maps, $B_\pm$ maps from local points to $\mathrm{Hom}(W_{q\pm}, W_q)$, $b \in \mathbb{R}$ and $n_0 \in \mathbb{N}$. The places $p_\pm$ are *linked to $p$ through $f$* if, at each local point $\gamma$ with $G_p(\gamma) > 0$, $V_{p_\pm}(f A_\pm)(\gamma) = V_p(f)(\gamma)\, B_\pm(\gamma)$, $\|B_\pm(\gamma)\|^2 \le (G_p(\gamma)/T_q)^{n_0}$, and for every $v$,
$$\|v\|^2 \le (3b)^{2n_0} \Bigl(\frac{T_q}{G_p(\gamma)}\Bigr)^{n_0} \bigl(\|B_+(\gamma)^* v\|^2 + \|B_-(\gamma)^* v\|^2\bigr).$$
Here $T_q = T_{z'}$, and $f A_\pm$ is the coefficient $g \mapsto f(g) A_\pm(g)$.

The last inequality has the shape of the bound for [shifted types](/entry/exists-shifted-types-lower-bound/).

**Theorem 5.5.5 (Bound from three places).** Assume Ξ-integrability, the compact class theorem and domination for all places. For all $C_b$ and all $C_3, C_\Lambda, C_0 \ge 0$ there are $C_4$ and $C_c$ with this property. Let $p, p_+, p_-$ be as above, let $f$ be a coefficient, and let $b, \Lambda, A_0, c \in \mathbb{R}$, $n_0, p_0, d, K, N \in \mathbb{N}$, positive functions $\nu_\pm$ and finite sets $Y_\pm$. Assume:

1. $b \ge 3$, $1 \le \Lambda \le b^{C_\Lambda(2r+2)}$, $n_0 \le 30(r+1)^2 + 6$, $p_0 \le C_0 (r+1)^2$, $K \ge 3$, $(r+1)K \le N \le 2p_0$;
2. $p_\pm$ satisfy the decomposition condition at level $C_b$;
3. $f$ is smooth and lies in the decay class of order $A_0$ and depth $m$ for every $m$;
4. $A_\pm$ are polynomial of degree $d$, and $p_\pm$ are linked to $p$ through $f$, with maps $B_\pm$, $b$ and $n_0$;
5. $C_c\,(r+1)^4\,(N n^2 + n^3) \le A_0 - (2r+2)p_0 - d$;
6. $f$ is regular on the big cell with constants $(b, C_3, 2p_0 + n_0)$, and the wave and lift grid conditions hold for $(p_\pm, \nu_\pm, Y_\pm, \Lambda, K, N)$;
7. there are $\lambda, \lambda' \in \mathbb{R}^n$ with $\mathcal{C}(y) f = \prod_s (y + \lambda'_s)\, f$ on $G$ for every real $y$, $2c \le |\lambda_s - \lambda_t|$ for $s \ne t$, and $|\lambda'_s - \lambda_s| + (2r+2)p_0 + d \le c - 1$ for every $s$;
8. $\prod_s (|y + \lambda_s| + c) \le \nu_\pm(y)$ for every real $y$.

Then $f$ satisfies the pointwise bound with constants $(b, C_4, n_0, p_0)$ at $p$.

Lean: `GlobalTheory.EigenThreePlaces.main` (also `GlobalTheory.T.capelli_eigenfunction_bound_three_places`, a second name).

Conditions 7 and 8 say that $f$ is an eigenfunction of the Capelli operators with eigenvalues near a well separated parameter $\lambda$, and that $\nu_\pm$ dominate the size of these eigenvalues.

*Proof.* Fix the cutoff $\chi(x) = s(2x - 1)$, with $s$ the smooth transition from $0$ to $1$. Put $F_\pm = G_f^{p_0}\, f A_\pm$, with $G_f$ built from $z, z'$.

A jet bound at three places gives $C_4$ and a constant $C_c^{(1)}$. It turns three inputs on $F_\pm$ into the pointwise bound for $f$:

1. The level zero forms of $\mathrm{cut}(\chi, F_\pm, \varepsilon)$ tend to those of $F_\pm$ for admitted words of length at most $N$. This is the limit for powers of the boundary function, applied at $p_\pm$ to $f A_\pm$, with a constant $C_n$. It uses $N \le 2p_0$. The coefficient $f A_\pm$ is smooth and decays with order $A_0 - d$, since $A_\pm$ has degree $d$.
2. The level zero form of $F_\pm$ along an admitted word is at most a normalizing constant of $(\nu_\pm, w)$ times the inner product of $F_\pm$ with itself. This is a level zero energy bound for decaying Casimir eigenfunctions. It needs the decay order $A_0 - (2r+2)p_0 - d$ to be at least the bound $A_B(k, r)$.
3. The block growth bound holds for each smooth compact approximation of the cut-off $F_\pm$. It comes from a positivity statement for lattice sums of compactly supported coefficients.

Put $C_c = \max(3, C_c^{(1)}, C_n)$. The margin in condition 5 with this $C_c$ splits into the margins for $C_c^{(1)}$ and for $C_n$ and into the bound $A_B(k, r) \le A_0 - (2r+2)p_0 - d$ that input 2 needs. $\square$

**Remark 5.5.6 (Formalization).** The limit of level zero forms is in [LevelZeroFormCutoffTendstoOfDensityDomination.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/LevelZeroFormCutoffTendstoOfDensityDomination.lean#L12). Its proof uses only the cut word part of the admitted word hypothesis, so the set $Y$ plays no role there. The bound from three places is in [CapelliEigenfunctionBoundThreePlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/CapelliEigenfunctionBoundThreePlaces.lean#L53); the cutoff is built at line 16 and the margin is split at line 22. Domination for all places (`NFTopDomAll`) is used only in input 1. The jet bound it calls has "equalTypes" in its name, but its statement puts no condition on the types, and the bound from three places also serves the case of different types. We have not unfolded the level zero form `RR`, the Capelli operator `Q.CV`, `WaveGrid`, `LiftGrid`, `BlockGrowthBound` or the parts of `ThmPActualCpt`. The three inputs of the jet bound were not opened; they are described by their statements.
