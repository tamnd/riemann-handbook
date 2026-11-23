---
title: Domination of the normal form
decls:
  - Formalism.FourierDecayAlt.P.CutBP.CompactFormNormalFormDomination.normal_form_top_domination
  - Formalism.FourierDecayAlt.P.CutBP.CompactFormNormalFormDomination.nfTopDomAll_of_tieC
  - CompanionTheory.NFCpt.nfTopDomAll_of_C
  - CompanionTheory.NFCpt.nfTopDomAll_of_ptwC
  - Formalism.FourierDecayAlt.P.NormalFormRelations.normal_form_hat_compact
  - Formalism.FourierDecayAlt.P.NormalFormRelations.nfTieGen_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Domination of the normal form

The weighted bound of the next section estimates the local terms of a Bessel function at points of the big cell. These local terms are first defined for functions cut off away from the boundary hypersurface $\{G = 0\}$, and the bound is then passed to the limit when the cutoff is removed. This section proves the hypothesis of the dominated convergence theorem for that limit: the cut-off top-degree terms are measurable and are bounded by one integrable function, uniformly in the cutoff. The proof rewrites each derivative of the Bessel function in a normal form, as an element of a model algebra acting on a gauge transform of the function, and bounds the normal form pointwise. The result is used through [the weighted one-place Bessel bound](/entry/wave-bessel-period-threshold/).

### Cut-off local terms

We work at one real place with the data of the earlier sections: $G \cong \mathrm{U}(r+k, r+1)$, two vectors $z, z' \in W_0$ with $T_z, T_{z'} > 0$, and two representations $\pi, \pi'$ of $U_W$ on finite-dimensional spaces $W_p, W_q$. A *coefficient* is a function $F : G \to \mathrm{Hom}(W_q, W_p)$. Let $T = T_z T_{z'}$ and, for $g \in G$, let $G_f(g) = |\Delta_{r+1}(g)|^2 - T \, |\Delta_r(g)|^2$, where $\Delta_l$ is a leading $l \times l$ minor in the coordinates of the Bessel data. For $c \in \mathbb{C}^{r+1}$ the *big-cell point* $\gamma(c)$ is the point with $r+1$ blocks of size one and entries $c_0, \dots, c_r$, so that
$$G(\gamma(c)) = \prod_{l < r} |c_l|^2 \, \big( |c_r|^2 - T \big).$$

**Definition 6.7.1 (Cutoffs).** A *cutoff* is a smooth function $\chi : \mathbb{R} \to \mathbb{R}$ that vanishes on $(-\infty, \delta)$ for some $\delta > 0$ and equals $1$ on $[1, \infty)$. For $\varepsilon > 0$ put $\mathrm{cut}(\chi, F, \varepsilon)(g) = \chi(G_f(g)/\varepsilon) \, F(g)$. For $n \in \mathbb{N}$ let $\beta_n(g) = s\big((4 - \|g\|^2/(n+1)^2)/3\big)$, with $s$ the smooth transition from $0$ to $1$ on $[0,1]$ and $\|g\|$ the Frobenius norm, and put $F_n = \beta_n F$.

So $\mathrm{cut}(\chi, F, \varepsilon)$ vanishes near $\{G_f = 0\}$ and agrees with $F$ where $G_f \geq \varepsilon$, while $F_n$ agrees with $F$ on $\|g\| \leq n+1$ and vanishes for $\|g\| \geq 2(n+1)$.

For a word $w$ in a fixed alphabet of differential operators, the place defines a *local term* $E_w(F)(\gamma)$: a real number built from the derivatives of the Bessel function of $F$ along $w$ at the point $\gamma$, with weights in $\gamma$. The *top term* of $F$ along $w$ is the function
$$\mathrm{top}_w(F)(c) = E_w(F)(\gamma(c)), \qquad c \in \mathbb{C}^{r+1}.$$
The words that occur are the *admissible* words of the place. We have not unfolded $E_w$ or the admissibility condition.

**Definition 6.7.2 (Normal form hypothesis).** Let $C_b, C_c$ be real, $f$ a coefficient, $A_0$ real, $p_0, N \in \mathbb{N}$ and $\chi$ a cutoff. The *normal form hypothesis* holds if the place satisfies the decomposition condition at level $C_b$ (the words of the place decompose into differential operators of bounded order), $f$ is smooth, $f$ lies in the decay class of order $A_0$ for every number of derivatives, and
$$C_c (r+1)^4 \big( N n^2 + n^3 \big) \leq A_0 - (2r+2) p_0, \qquad N \leq 2 p_0 .$$

Here $n = 2r+k+1$. From $f$ one forms a modified coefficient $F = f^{(p_0)}$, which depends on $p_0$ and on the place. We have not unfolded the decay class or the modification.

### Domination from a pointwise bound

The analytic step is this. Suppose that, for compactly supported coefficients, the top term of the cut-off function is bounded at each point by finitely many local terms of derivatives of $f$. Then the domination follows.

**Theorem 6.7.3 (Domination from a pointwise bound).** Assume the following *pointwise bound*. For each $C_b$ there are $C_c, C_1$ such that, for each place, each $p_0, N$, each cutoff $\chi$ and each admissible word $w$ of length at most $N$, there are finitely many differential operators $\Theta_1, \dots, \Theta_m$ of order controlled by $C_1$ and $N$, and $M \geq 0$, with
$$\big| \mathrm{top}_w\big(\mathrm{cut}(\chi, f^{(p_0)}, \varepsilon)\big)(c) \big| \leq M \sum_{t} G(\gamma(c))^{2p_0 - N} \, E_\emptyset(\Theta_t f)(\gamma(c))$$
for every compactly supported coefficient $f$ that satisfies the normal form hypothesis, every $\varepsilon > 0$, and every $c$ with $\gamma(c)$ a local point and $G(\gamma(c)) > 0$. Assume also that the truncations $F_n$ of a smooth $F$ have Bessel functions in the right class. Then for each $C_b$ there is $C_c$ such that, under the normal form hypothesis, for each admissible word $w$ of length at most $N$:

1. $\mathrm{top}_w(\mathrm{cut}(\chi, f^{(p_0)}, \varepsilon))$ is almost everywhere strongly measurable for small $\varepsilon > 0$;
2. there is an integrable $h$ on $\mathbb{C}^{r+1}$ with $|\mathrm{top}_w(\mathrm{cut}(\chi, f^{(p_0)}, \varepsilon))| \leq h$ almost everywhere, for all small $\varepsilon > 0$.

Lean: `CompanionTheory.NFCpt.nfTopDomAll_of_ptwC`.

*Proof.* Take the operators $\Theta_t$ and the constant $M$ of the pointwise bound. A proved truncation lemma gives, for each $t$, an integrable function $h_t$ with $G(\gamma(c))^{2p_0 - N} E_\emptyset(\Theta_t f_n)(\gamma(c)) \leq h_t(c)$ for almost every $c$ and all $n$. Put $h = M \sum_t |h_t|$. Measurability is a separate proved lemma.

Fix $\varepsilon > 0$ and a point $c$ outside a null set. If $\gamma(c)$ is not a local point, or if $G(\gamma(c)) \leq 0$, the top term vanishes and there is nothing to prove. Otherwise, the top term of $\mathrm{cut}(\chi, f^{(p_0)}, \varepsilon)$ at $c$ is the limit as $n \to \infty$ of the top terms of its truncations, by a proved limit lemma for module forms. So it suffices to bound the truncated terms by $h(c)$.

Put $\eta = G(\gamma(c))/2$ and $f' = \beta_n \cdot \mathrm{cut}(\chi, f, \eta)$. This coefficient is compactly supported, so the pointwise bound applies to it. On the open set $\{G_f > \eta\}$, which contains a neighbourhood of $\gamma(c)$, the factor $\chi(G_f/\eta)$ equals $1$. The local terms at $\gamma(c)$ depend only on the values near $\gamma(c)$. Hence the top term of $\mathrm{cut}(\chi, f'^{(p_0)}, \varepsilon)$ at $c$ equals that of the $n$-th truncation of $\mathrm{cut}(\chi, f^{(p_0)}, \varepsilon)$, and $E_\emptyset(\Theta_t f')(\gamma(c)) = E_\emptyset(\Theta_t f_n)(\gamma(c))$. The pointwise bound and the choice of $h_t$ give the bound $M \sum_t h_t(c) \leq h(c)$. Let $n \to \infty$. $\square$

### The normal form

The pointwise bound comes from a normal form. Fix a place. A *frame* is a family $e$ of maps, indexed by the $K$-types $\rho$ of the place, that trivializes the Bessel transform; with a frame, the Bessel function $J(F)$ of a coefficient gives a *gauge transform* $\mathrm{tr}_e J(F)$, a function on a parameter space $\mathcal{Q}$ with values in a module over a *model algebra* $\mathcal{A}$. The model algebra has a set of *bounded* elements and a set of *hat* generators, fixed by a level datum $L$. We have not unfolded the model algebra, its level data or the gauge transform beyond this description.

**Definition 6.7.4 (Gauge core).** The *gauge core* is the statement that, for each place with $k \geq 2$, there is a frame $e$ such that the gauge transform intertwines the operators of the Lie algebra with the model algebra: the gauge transform of a family $\Phi$ after the operator $Q_{ab}(Y)$ equals the element $Q^{\mathcal{A}}_{ab}(Y)$ of $\mathcal{A}$ applied to the gauge transform of $\Phi$, for all real $Y$ and $a, b \in \{0, 1\}$.

**Theorem 6.7.5 (Normal form for compactly supported coefficients).** Assume the gauge core. For each $C_b$ there is $C_c$ with the following property. For each place satisfying the decomposition condition at level $C_b$, there are a frame $e$ and a level datum $L$ such that for each admissible word $w$ and each family of differential operators $L_0, \dots, L_Q$ attached to $w$, there are $m$, bounded elements $b_1, \dots, b_m$, lists $u_1, \dots, u_m$ of $|w|$ hat generators, and $C$, with
$$\Phi_w(F)(c) \leq C \, G(\gamma(c))^{-|w|} \sum_{j=1}^{m} \sum_{\rho'} \big\| \big( b_j \, u_j \cdot \mathrm{tr}_e J(F) \big)_{\rho'}(q) \big\|^2$$
for each smooth $F$ in the decay class of order $A \geq C_c (r+1)^4 (|w| n^2 + n^3)$, with $F$ compactly supported and $J(F)$ in the right class. Here $q$ is the parameter of $\gamma(c)$, and $\Phi_w(F)(c)$ is the weighted square of the Hilbert-Schmidt norm of the $\rho$-component of $L_q F$ at $\gamma(c)$, for local points with $G(\gamma(c)) > 0$.

Lean: `Formalism.FourierDecayAlt.P.NormalFormRelations.normal_form_hat_compact` (also `Formalism.FourierDecayAlt.P.NormalFormRelations.nfTieGen_of`).

*Proof.* Take $e$ from the gauge core and a level datum $L$ from the analytic model frame. The constant is $C_c = |C_L| + 12 + 8|C_b|$, where $C_L$ is the constant of a proved Leibniz estimate for vectors. Fix $w$, the index $e'$ of the top term and the family $L_0, \dots, L_Q$. The decomposition condition gives finitely many differential operators of order at most some $o$, with smooth coefficients, that commute with the Bessel transform on the open set $\{G_f > 0\}$ and express the derivative $\Theta_{w,e'}$ along $w$.

For $s = 0, 1, \dots, o$ put $F_s = G_f^{\,s} F$. The Leibniz estimate applied to the function $x \mapsto x^s$ gives, at a local point $\gamma = \gamma(c)$ with $G = G(\gamma) > 0$,
$$V\big(\Theta_{w,e'} F_s\big)(\gamma) = G^s \sum_{j=0}^{o} s^j \, V(L_j F)(\gamma),$$
where $V$ is the vector of values that enters the local terms, and $V(L_j F)(\gamma) = 0$ for $j > o$. The Vandermonde matrix $(s^j)_{0 \leq s, j \leq o}$ is invertible. So each $V(L_q F)(\gamma)$ is a fixed linear combination $\sum_s \lambda_{qs} G^{-s} V(\Theta_{w,e'} F_s)(\gamma)$, and its squared norm is at most $\Lambda \sum_s G^{-2s} \|V(\Theta_{w,e'} F_s)(\gamma)\|^2$ with $\Lambda = \sum_{q,s} |\lambda_{qs}|^2$.

For each $s$, $F_s$ is compactly supported and its Bessel function is in the right class. A proved tie lemma for compactly supported coefficients writes the Bessel function of $\Theta_{w,e'} F_s$ in the frame $e$ as an element of $\mathcal{A}$ applied to $\mathrm{tr}_e J(F_s)$. Here the gauge core turns each Lie algebra operator in $\Theta_{w,e'}$ into an element of $\mathcal{A}$. The gauge transform of $J(F_s)$ is $G^s$ times that of $J(F)$. A proved normal form at model points then gives $m_s$, bounded $b_{s,j}$, lists $u_{s,j}$ of $|w|$ hat generators and $C_s$ with
$$\|V(\Theta_{w,e'} F_s)(\gamma)\|^2 \leq C_s \, G^{2s} \, D^{-|w|} \sum_j \sum_{\rho'} \big\| (b_{s,j} u_{s,j} \cdot \mathrm{tr}_e J(F))_{\rho'}(q) \big\|^2$$
after multiplication by the weights, where $D = \prod_l |c_l|^2$. The factors $G^{2s}$ and $G^{-2s}$ cancel. Finally a proved bound on the weights gives $d_H^2 \leq C_w (D/G)^{|w|}$, and the projection to the $\rho$-component does not increase the Hilbert-Schmidt norm. The factor $D^{|w|}$ cancels and $G^{-|w|}$ remains. The elements $b_j u_j$ of the statement are all the $b_{s,j} u_{s,j}$, and $C = C_w \Lambda \sum_s C_s$. The general statement also allows coefficients that lift locally, with a second tie lemma in that case; we use it for compactly supported ones. $\square$

The gauge core is a proved theorem, the gauge construction of the development, so the normal form holds without hypotheses.

### Domination of the top term

**Theorem 6.7.6 (Domination of the cut-off top term).** For each $C_b$ there is $C_c$ such that, for each place, each coefficient $f$, each $A_0, p_0, N$ and each cutoff $\chi$ with the normal form hypothesis, and each admissible word $w$ with $|w| \leq N$, the two conclusions of the theorem on domination from a pointwise bound hold for $\mathrm{top}_w(\mathrm{cut}(\chi, f^{(p_0)}, \varepsilon))$.

Lean: `Formalism.FourierDecayAlt.P.CutBP.CompactFormNormalFormDomination.normal_form_top_domination` (also `Formalism.FourierDecayAlt.P.CutBP.CompactFormNormalFormDomination.nfTopDomAll_of_tieC`, `CompanionTheory.NFCpt.nfTopDomAll_of_C`).

*Proof.* By the theorem on domination from a pointwise bound, it suffices to prove the pointwise bound and the statement on truncations. The statement on truncations is a proved lemma: the Bessel function of $\beta_n F$ lies in the right class for each smooth $F$.

For the pointwise bound, fix $w$, $\varepsilon$ and a local point $\gamma = \gamma(c)$ with $G = G(\gamma) > 0$. The empty word is a separate proved case, with two fixed operators. For $w$ not empty, a proved unfolding lemma writes the top term as a weighted sum over an index $e$ and the $K$-types $\rho$ of the squared Hilbert-Schmidt norms of the $\rho$-components of derivatives of $\chi(G_f/\varepsilon) F$ at $\gamma$. The Leibniz rule writes each derivative as $\sum_{q \leq Q} \big((x \, d/dx)^q \chi(\cdot/\varepsilon)\big)(G) \cdot L_q F$ for differential operators $L_0, \dots, L_Q$. A proved lemma bounds $|(x \, d/dx)^q \chi(y/\varepsilon)|$ by a constant $K_q$ that does not depend on $\varepsilon$ or $y$. This is where the cutoff disappears from the bound.

It remains to bound each term with $L_q F$, where $F = f^{(p_0)}$. Here the modification multiplies $f$ by $G^{p_0}$ near $\gamma$, so $L_q F$ at $\gamma$ is $G^{p_0}$ times a combination of derivatives of $f$ with coefficients $\binom{j}{q} p_0^{j - q}$. The normal form bounds the weighted square of each of these by $C G^{-|w|}$ times the norms of $b_j u_j \cdot \mathrm{tr}_e J(f)$. A second proved lemma, the product formula for hat generators, writes $u_j \cdot \mathrm{tr}_e J(f)$, for $u_j$ a product of at most $N$ hat generators, as a finite sum $\sum_t b'_t \cdot \mathrm{tr}_e J(\Theta_t f)$ with bounded $b'_t$ and differential operators $\Theta_t$. A proved pointwise bound in the model algebra controls the action of each bounded element $b_j b'_t$, and a proved trace norm bound compares the norms of $\mathrm{tr}_e J(\Theta_t f)$ at $q$ with the local terms $E_\emptyset(\Theta_t f)(\gamma)$. The powers of $G$ combine as
$$G^{2p_0} G^{-|w|} = G^{2p_0 - N} G^{N - |w|} \leq G^{2p_0 - N} \big(1 + G^{2N}\big),$$
because $|w| \leq N$. The factor $G^{2N}$ is absorbed into the operators: for each $\Theta_t$ one adds the operator $G^N \Theta_t$, whose value at $\gamma$ is $G^N$ times that of $\Theta_t$. Sum over $e$, $\rho$ and $q$, and use Cauchy-Schwarz for the finite sums. This gives the pointwise bound, with the list of all operators $\Theta_t$ and $G^N \Theta_t$. $\square$

**Remark 6.7.7 (Formalization).** The objects $E_w$, the modification `fpm`, the decay class `InCC`, the condition `InDDplus2`, the admissible words `AdmW`, the class `FFKB`, the model algebra `MA.A` with `hatSet` and `bddSet`, the gauge transform `trJKB` and the weights `nPt` and `Top.dH` were not unfolded; the descriptions above are from their roles in the proofs. The disjunction `LocLift ∨ CptCoef` in [NfTieHatSOf.lean](lean:CompanionTheory/AutomorphicTheory/JacobiDiagonalBounds/NfTieHatSOf.lean#L63) is only ever used with its right side ([NormalFormHatCompact.lean](lean:CompanionTheory/AutomorphicTheory/JacobiDiagonalBounds/NormalFormHatCompact.lean#L7)), so the local lifting property [EvQTrJBFF.lean](lean:CompanionTheory/AutomorphicTheory/JacobiDiagonalBounds/EvQTrJBFF.lean#L14) plays no role. The domination theorem is used twice in [FinalC.lean](lean:CompanionTheory/AutomorphicTheory/CompactTopologicalForms/FinalC.lean#L21): as the domination input of the endpoint bound, and to prove the limit identity through `nfTopIdAll_of_dom` with [the compact theorem](/entry/actual-compact-theorem/). The three named theorems that are not `nfTopDomAll_of_ptwC` or `nfTieGen_of` are one-line compositions.
