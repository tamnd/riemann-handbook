---
title: Domination of cut-off top terms
decls:
  - GlobalTheory.HatNF.top_density_dominated
  - GlobalTheory.HatNF.topDensity_cut_dominated_all
  - GlobalTheory.T.topDensity_cutoff_dominated_of_HC_xi
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Domination of cut-off top terms

The pointwise bound is first proved for coefficients cut off away from the boundary hypersurface $\{G_f = 0\}$. To remove the cutoff, the proof takes a limit under an integral over the big cell, and it needs the hypothesis of the [[dominated convergence|BYNV84PF86]] theorem: the cut-off top terms are measurable and lie below one integrable function, for all small cutoff parameters. This section proves that hypothesis for $G_f^{p_0} f$, with $f$ smooth and decaying and $p_0$ large compared with the length of the word. The tools are the [word bound for decaying coefficients](/entry/word-bound-decay/) and an integrability input for the empty word. The result is used in the [limit of level zero forms](/entry/level-zero-form-cutoff-tendsto-of-domination/) and in the [pointwise bound for eigenfunctions](/entry/pointwise-bound-eigenfunction/).

### Cutoffs, top terms and the normal form hypothesis

**Definition 5.4.1 (Cutoff).** A *cutoff* is a smooth function $\chi : \mathbb{R} \to \mathbb{R}$ with $\chi(x) = 0$ for $x < \delta$, for some $\delta > 0$, and $\chi(x) = 1$ for $x \ge 1$. For a coefficient $F$ and $\varepsilon > 0$ put
$$\mathrm{cut}(\chi, F, \varepsilon)(g) = \chi\bigl(G_f(g)/\varepsilon\bigr)\, F(g).$$

So $\mathrm{cut}(\chi, F, \varepsilon)$ vanishes near the boundary and equals $F$ where $G_f \ge \varepsilon$. For example $\chi(x) = s(2x - 1)$, with $s$ the smooth transition from $0$ to $1$ on $[0, 1]$, is a cutoff.

**Definition 5.4.2 (Top term).** For a coefficient $F$ and a word $w$, the *top term* of $F$ along $w$ is the function $\mathrm{top}_w(F)(c) = E_w(F)(\gamma(c))$ on $\mathbb{C}^{r+1}$.

A word is *admitted* for a finite set $Y \subset \mathbb{R}$ if it is a cut word and each letter is $(+, y)$ or $(-, y+1)$ for some $y \in Y$.

**Definition 5.4.3 (Normal form hypothesis).** Let $C_b, C_c, A_0 \in \mathbb{R}$, $p_0, N \in \mathbb{N}$, $\chi$ a function and $f$ a coefficient. The *normal form hypothesis* holds if $\chi$ is a cutoff, the place satisfies the decomposition condition at level $C_b$, $f$ is smooth, $f$ lies in the decay class of order $A_0$ and depth $m$ for every $m$, and
$$C_c\,(r+1)^4\,(N n^2 + n^3) \le A_0 - (2r+2)p_0, \qquad N \le 2p_0 .$$

**Definition 5.4.4 (Domination of top terms).** Let $F$ be a coefficient, $\chi$ a cutoff and $w$ a word. The top terms of $F$ along $w$ are *dominated* if, for all small enough $\varepsilon > 0$, the function $\mathrm{top}_w(\mathrm{cut}(\chi, F, \varepsilon))$ is almost everywhere strongly measurable, and there is an integrable $h$ on $\mathbb{C}^{r+1}$ such that, for all small enough $\varepsilon > 0$,
$$|\mathrm{top}_w(\mathrm{cut}(\chi, F, \varepsilon))(c)| \le h(c) \quad \text{for almost every } c .$$
We say that *domination holds for all places* if for every $C_b$ there is $C_c$ such that, whenever the normal form hypothesis holds for $(C_b, C_c, f, A_0, p_0, \chi, N)$ and $w$ is admitted for some $Y$ with $|w| \le N$, the top terms of $G_f^{p_0} f$ along $w$ are dominated.

The integrability input concerns the empty word. It says that coefficients of large decay order have square-integrable size on the big cell.

**Definition 5.4.5 (Ξ-integrability).** *Ξ-integrability* holds if, for each place and each $A$ at least a bound $A_B(k, r)$, there is a function $\Xi$ that bounds the coefficients of decay order $A$ and that satisfies the integrability condition of exponent $2$. It is proved in the chapter on discrete series as [Theorem 3.5](/entry/xi-exists/).

We have not unfolded the bound by $\Xi$ or its integrability condition. The model is Harish-Chandra's function $\Xi$, which bounds $K$-finite matrix coefficients of tempered representations; see [asymptotics of matrix coefficients](/learn/real-groups/#asymptotics-of-matrix-coefficients).

### The domination theorem

**Theorem 5.4.6 (Domination of cut-off top terms).** Assume Ξ-integrability. Let $a : \mathbb{N} \to \mathbb{N}$ be such that the basic elements [lift with loss $a$](/entry/basic-lift-all-zero/). For every $C_b$ there is $C_c$ with this property. Let $p$ be a place datum, $f$ a coefficient, $A_0 \in \mathbb{R}$, $p_0, N \in \mathbb{N}$, $\chi$ a function and $w$ a word, and assume:

1. $\chi$ is a cutoff, and the place satisfies the decomposition condition at level $C_b$;
2. $f$ is smooth and lies in the decay class of order $A_0$ and depth $m$ for every $m$;
3. $C_c\,(r+1)^4\,(N n^2 + n^3) \le A_0 - (2r+2)p_0$ and $N(1 + 2a(r)) \le 2p_0$;
4. $w$ is a cut word with $|w| \le N$.

Put $\varphi_\varepsilon(y) = \chi(y/\varepsilon)\, y^{p_0}$. Then for every $\varepsilon > 0$ the function $c \mapsto E_w(\varphi_\varepsilon \cdot_G f)(\gamma(c))$ is almost everywhere strongly measurable, and there is an integrable function $h$ on $\mathbb{C}^{r+1}$ such that
$$|E_w(\varphi_\varepsilon \cdot_G f)(\gamma(c))| \le h(c) \qquad \text{for all } \varepsilon > 0 \text{ and all } c \in \mathbb{C}^{r+1}.$$

Lean: `GlobalTheory.HatNF.top_density_dominated`.

The condition $N(1 + 2a(r)) \le 2p_0$ is the heart of the matter. The word bound loses $|\prod c_l|^{-|w|} G_p^{-a(r)|w|}$ near the boundary, and the factor $G_f^{p_0}$ must pay for it.

*Proof.* Take $C_1$ from the [word bound for decaying coefficients](/entry/word-bound-decay/) and $C_2$ from the integrability of the empty-word top term of decaying coefficients, which follows from Ξ-integrability. Put $C_c = \max(C_1, C_2, 8)$.

Step 1 (the multiplier). The function $\varphi_\varepsilon$ is a cut power of degree $p_0$. Its Euler derivatives satisfy $|\vartheta^j \varphi_\varepsilon(x)| \le C' x^{p_0}$ for $j \le J$, with $C'$ independent of $\varepsilon$, since $\vartheta^j$ of $\chi(x/\varepsilon)$ is a bounded function of $x/\varepsilon$.

Step 2 (the shape of the top term). The top term $E_w(F)(\gamma(c))$ vanishes unless all $c_l \ne 0$ and $G_p(\gamma(c)) > 0$. For the empty word it is $n(c)\, \|V_p(F)(\gamma(c))\|^2$, with $n(c)$ a positive weight. For a general word,
$$|E_w(F)(\gamma(c))| \le C\, n(c) \Bigl(\frac{|\prod_l c_l|^2}{G_p(\gamma(c))}\Bigr)^{|w|} \sum_e \|V_p(\Theta_{w,e} F)(\gamma(c))\|^2 .$$

Step 3 (the word bound). Apply the word bound with $F = \varphi_\varepsilon \cdot_G f$. Its margin holds with $e = p_0$ and $A = A_0$. The powers of $|\prod_l c_l|$ cancel, and Step 1 bounds the sum over $j$ by $C' G_p^{p_0}$. So $|E_w(F)(\gamma(c))|$ is at most a constant times
$$n(c)\, G_p(\gamma(c))^{2p_0 - |w|(1 + 2a(r))} \sum_i \|V_p(\Theta_i f)(\gamma(c))\|^2 .$$
The operators $\Theta_i$ are polynomial, so $\Theta_i f$ is smooth and decays, with an order that drops by at most $|w| \cdot 8(r+1)n$. The margin with $C_c \ge 8$ keeps it in the range of the integrability input.

Step 4 (the dominating function). The exponent $m = 2p_0 - |w|(1 + 2a(r))$ lies between $0$ and $2p_0$, by condition 3. For $G > 0$ we have $G^m \le 1 + G^{2p_0}$. Hence the bound of Step 3 is at most a constant times
$$h(c) = \sum_i \Bigl( E(\Theta_i f)(\gamma(c)) + E\bigl(G_f^{p_0}\, \Theta_i f\bigr)(\gamma(c)) \Bigr),$$
a finite sum of empty-word top terms of decaying coefficients. Each is integrable by the choice of $C_2$. The bound does not depend on $\varepsilon$.

The proof also checks that these top terms are almost everywhere strongly measurable. $\square$

**Theorem 5.4.7 (Domination for all places).** Assume Ξ-integrability. Then domination holds for all places.

Lean: `GlobalTheory.HatNF.topDensity_cut_dominated_all` (also `GlobalTheory.T.topDensity_cutoff_dominated_of_HC_xi`, a second name).

*Proof.* The basic elements lift with loss $0$, by [Proposition 5.2.5](/entry/basic-lift-all-zero/). Apply the domination theorem with $a = 0$. Its condition $N(1 + 0) \le 2p_0$ is part of the normal form hypothesis, and an admitted word is a cut word. For each $\varepsilon > 0$ we have
$$\mathrm{cut}(\chi, G_f^{p_0} f, \varepsilon)(g) = \chi(G_f(g)/\varepsilon)\, G_f(g)^{p_0} f(g) = (\varphi_\varepsilon \cdot_G f)(g),$$
so the top terms of $\mathrm{cut}(\chi, G_f^{p_0} f, \varepsilon)$ are those of the theorem. A bound for every $\varepsilon > 0$ and every $c$ is in particular a bound for small $\varepsilon$ and almost every $c$. $\square$

**Remark 5.4.8 (Formalization).** The domination theorem is in [TopDensityDominated.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/TopDensityDominated.lean#L82), with the inequality $G^m \le 1 + G^{2p_0}$ at line 20 and the final estimate at line 28. Ξ-integrability (`BesselXiIntegrable`) enters only through the integrability of the empty-word term. Its conclusion holds for all $\varepsilon$ and all $c$, which is stronger than the domination it is used for. In [TopDensityCutoffDominatedOfHCXi.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/TopDensityCutoffDominatedOfHCXi.lean#L11) the set $Y$ of an admitted word plays no role: only the cut word property is used. The weight $n(c)$ is `nPt`, and we have not unfolded it.
