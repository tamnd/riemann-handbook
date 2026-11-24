---
title: Theorem S
decls:
  - Formalism.L2.SG.TheoremS.pbApplied
  - Formalism.L2.SG.SpectralTiesReal.theoremS_rec
  - Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec2P
  - Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec3P
  - Formalism.L2.SG.Pf.rowFormC_of_leaves3
  - Formalism.L2.SG.PoincareAmplitudeLowerBounds.rowFormAllP_of
  - Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_closedP
  - Formalism.L2.SG.TheoremSConclusion.theoremS_of_conj
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem S

This section proves Theorem S: for two distinct words $u \ne u'$ the off-diagonal entry satisfies
$$\|K_0(u,u')\|^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^\ast},$$
and the same bound holds for the Hilbert-Schmidt norm of the operator $K_D(u,u')$. The proof starts from an abstract bound for a term series and makes its inputs concrete in four steps. The nineteen hypotheses of the ninth section are the hypotheses of the last step. The off-diagonal bound of the ninth section uses Theorem S, and [the hypotheses of Theorem S](/entry/theorem-s-leaves-of-carrier-g/) prove its nineteen hypotheses.

### The abstract pair bound

A *term series* for a pair of words is a family of terms $t$ with weights. Each term is of one of four kinds: identity, degenerate (its Gram value $G(t)$ is $0$), generic, or non-generic. The entry $K_0$ is the sum of the identity, generic and non-generic parts; the degenerate part is $0$. Let $\Gamma_1$ be the weight of the identity term, let $\Sigma$ be the sum over pairs of terms, and let $d > 0$. The *row conditions* bound a weighted sum over pairs of terms by a constant times $d$:

1. *big rows* and *non-scalar rows*, each with the constant $\varepsilon$;
2. the *main row* $\Gamma_1 \Sigma \le A\, d$;
3. *non-generic rows*, with the constant $\varepsilon'$.

A size datum has a rank $r$, a degree $f$, a level $k$, two primes $g_1, g_2$ and a scale $b$. It satisfies the *size numbers* for constants $c$ and $C_n$ if
$$\begin{aligned}
&16 \le b, \quad 32 \le k, \quad f \le k, \quad 4r + 12 \le k,\\
&(kb)^8 \le g_1, \quad (kb)^8 \le g_2, \quad 70 \log b \le k,\\
&1 \le 5 c f \log k, \quad 8 C_n (2r+2)^5 f \log b \le k.
\end{aligned}$$

**Theorem 3.13.1 (Abstract pair bound).** For $C_4 \ge 1$ and real $C_{\mathrm{thr}}$ there are constants $C_A \ge \max(C_{\mathrm{thr}}, 1)$ and $0 \le C \le C_A$ with this property. For $C_0 \ge 1$, $C_G \ge 0$, $C_\Delta > 4$ and $c_T, C_b > 0$ with $c_T C_b > 1$ there is $k_0$ such that the following holds. Let $D$ be a datum over a CM field $E$ with a size datum of level $k \ge k_0$, mass data and a term series. Assume the size hypothesis, that $E$ is unramified at the type primes, the local model, the real inputs, the density input, the row input, the mass data hypothesis, the energy link, the link of the terms to the mass data, the split inputs and the size numbers. Assume big rows and non-scalar rows with $\varepsilon = e^{-c k f \log k}$, and non-generic rows with
$$\varepsilon' = 2^{-(k-2r-5)}\, e^{C_n (2r+2)^5 f \log b}.$$
Then $\|K_0\|^2 \le (1 + b^{-6})\, d$.

Lean: `Formalism.L2.SG.TheoremS.pbApplied`.

*Proof.*

1. The main row estimate gives $\Gamma_1 \Sigma \le (1 + \delta)\, e_1\, d$ with $0 \le \delta \le b^{-7}$ and $1 \le e_1 \le \exp(12 f\, 2^{-(k - 2r - 2)})$. It uses the local and global cores, the lattice link, the axioms of the local model and the induction on lattice averages. By the link, this is the main row with $A = (1 + \delta) e_1$.
2. Split $K_0$ into its parts. A sub-family bound and the bound of a Gram sum by a positive semidefinite form give
$$\|K_0\|^2 \le \Bigl(\sqrt{P_g (A + 2\varepsilon)} + \sqrt{P_g(\varepsilon + \varepsilon')}\Bigr)^2 d,$$
with the price $P_g = (1 + 3/g_1)^f (1 + 3/g_2)^f$.
3. The numerical lemmas bound each factor. By the size numbers, $P_g$, $e_1$, $\varepsilon$ and $\varepsilon'$ are small powers of $b$. The final inequality is $(\sqrt{a} + \sqrt{e})^2 \le 1 + b^{-6}$ for the two terms $a$ and $e$ of step 2. $\square$

### Theorem S for one pair

A *carrier condition* for a pair $(u, u')$ gives an abstract Hida setting $S$ with the constant $C_A$, the size datum $G_0$, the words $d_e, d_e'$ and the index $l$ of the pair, a compatibility of $S$ with $D$, a base from the concrete setting, a top tie, the joint vectors of the fourteenth section and the real inputs with the constant $C_4$.

**Theorem 3.13.2 (Theorem S for one pair).** Assume the local model, the density input under local ties, and the positive row input, for each datum. Let $C_4 \ge 1$ and $C_{\mathrm{thr}}$ be real, and take $C_A$, $C$ and $k_0$ as in the abstract pair bound. Let $D$ be a datum with size data of scale $b \ge 0$, a Hida setting $X$, a full datum $Y$ with finite cells, and distinct words $u \ne u'$. Assume the carrier condition, the size conditions with $k \ge k_0$, the prime and mass data hypotheses, the row form, and the three row bounds for the term series $t_O(u,u')$ at $d = d(u) d(u')/D^\ast$. Assume the expansion of $K$, absolute convergence and that the degenerate part of $t_O(u, u')$ is $0$. Then
$$\|K_0(u,u')\|^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^\ast}, \qquad \|K_D(u,u')\|_{\mathrm{HS}}^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^\ast}.$$

Lean: `Formalism.L2.SG.SpectralTiesReal.theoremS_rec`.

*Proof.*

1. The carrier condition gives the abstract setting $S$, the compatibility and the real inputs. Substitute the equalities of constants and data.
2. The instance of the datum gives the instance of the abstract pair bound, and the local model at $D$ gives the local model.
3. The density input at $D$ gives the density input, after a rewrite of the degree $f$.
4. The positive row input gives positive semidefinite rows. The row form is the identity of the $K_V$ expansion, and the identity bound gives the row input.
5. The mass data give the energy link.
6. The abstract pair bound gives the first bound. The package tie turns it into the bound on the Hilbert-Schmidt norm. $\square$

### Fixing the constants

**Theorem 3.13.3 (Theorem S with the row bound).** Assume the hypotheses of Theorem S for one pair on each datum, and the row bound for non-generic rows. Then the conclusion of Theorem S for one pair holds, with these changes. There is a new layer of constants $C_g$, $c_b$, $C_w$, $c_{Tf}$, $C_T$, $C_{0f}$ with $c_b, c_{Tf} > 0$, then $C_n \ge 0$ and thresholds $C'_0$ and $C_{l,0}$ for the counting constants. The data form a tie package. The non-generic rows are not assumed. Big rows and non-scalar rows are assumed with $\varepsilon = \exp(-\tfrac13 k f \log k)$, so $c = 1/3$ in the size numbers.

Lean: `Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec2P`.

*Proof.* The row bound gives $C_n$ and thresholds, and then the non-generic rows with $\varepsilon'$. The carrier condition contains a Hida setting with size datum $G_0$, so $k$, $r$ and $f$ of $G_0$ are those of $D$. The concrete tie identifies $d(u)$, $d(u')$ and $D^\ast$ with their abstract values, and it contains the local ties. The standing hypotheses give the prime hypothesis. Then Theorem S for one pair applies. $\square$

**Theorem 3.13.4 (Theorem S with the carrier bound).** Assume the hypotheses of the last theorem and the carrier bound. Then its conclusion holds, with $C_4$ chosen by the theorem and with $G_0$, $d_e$, $d_e'$ and $l$ fixed by a bijection $e$ from the infinite places of $E$ to the index set. The carrier condition is replaced by the hypotheses of the carrier bound: $i_0 = i_0'$, a point representative exists, the quotient measure is pinned, and $e$ is compatible with the embeddings of $X$.

Lean: `Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec3P`.

*Proof.* The carrier bound gives $C_4 \ge 1$ and a threshold $C_{A,0}$. Apply the last theorem with the threshold $\max(C_{\mathrm{thr}}, C_{A,0})$. The constant $C_A$ is then at least $C_{A,0}$, so the carrier bound gives the carrier condition at $C_A$, a level $k_{0,c}$ and thresholds. Take the maxima of the two levels and of the two sets of thresholds. $\square$

### The row form

Fix a datum $D$, a Hida setting $X$ with a bridge, a full datum $Y$, words $u, u'$ and the auxiliary data. They define mass data with reals $c_0$, $c_0'$, $n_{0c}$ and $K_V$. A term $t$ is *eligible* if it is generic with $G(t) \ne 0$. Let $\kappa$ label the terms by natural numbers. For a label $\rho$, the *row vector* is $R_\rho = \sum_p r_\rho(p)\, V(p)$, a sum over the points $p$. Here $r_\rho(p)$ is the sum of $\sqrt{m(t)}\, c(t, w)$ over the eligible terms $t$ at the point $w$ of $p$ with $\kappa(t) = \rho$, divided by $\sqrt{n_0(w)}\, \varphi(p)$.

**Theorem 3.13.5 (Row form).** Assume that $\kappa$ is a row label: two eligible terms have the same label if and only if each is a scalar multiple of the other. Assume $i_0 = i_0'$, a point representative, the pinned quotient measure, $2r + 2 + f + 5 \le k$, absolute convergence, $g_0, g_1 \ge 3$ unramified in $E$, the phase tie, the odd generic volume, the prime hypothesis, a norm representative, the independence of $V$, the local ties, and the normalisation $n_c = n_{0c}\, g_{\mathrm{ng}}/(a_l \kappa_N)$. Assume $\mathrm{vol}(K_2) > 0$, $c_0 c_0' > 0$, $n_c > 0$ and $\prod_q \alpha_D(q) > 0$. Then $\sum_\rho \|R_\rho\|^2$ converges and
$$c_0\, c_0'\, K_V = n_{0c} \sum_\rho \|R_\rho\|^2.$$

Lean: `Formalism.L2.SG.Pf.rowFormC_of_leaves3`.

*Proof.*

1. Regroup the rows by classes. With the class frame, the torsor property and absolute convergence on classes, $c_0 c_0' \Sigma = \sum_\rho \|v_\rho\|^2$, where $v_\rho$ is the class vector of $\rho$.
2. Each row vector is a multiple of the class vector:
$$R_\rho = \Bigl(\frac{g_{\mathrm{ng}}}{\kappa_N\, n_c\, m_{\mathrm{rows}} \prod_q \alpha_D(q)}\Bigr)^{1/2} v_\rho.$$
3. The row count is $\rho_0 = m_{\mathrm{rows}}$, and the local ties give $a_l = \prod_q \alpha_D(q)$.
4. By definition $K_V = \Sigma/\rho_0$. Steps 1 to 3 and the normalisation give the identity. $\square$

**Theorem 3.13.6 (Row form for all data).** Assume the formula, the odd generic volume, the independence of $V$ at all data, and positive normalising constants. Then for all constants $C_g, c_b, C_w, c_{Tf}, C_T, C_{0f}$ with $c_b, c_{Tf} > 0$ there are thresholds $C'_0$ and $C_{l,0}$ such that, for $C' \ge C'_0$ and $C_l \ge C_{l,0}$, the row form holds at each datum with ties, each pair with $T_u \equiv T_{u'} \bmod g_S^2$, and each tie package with the concrete tie. In it, the local density is divided by $\prod_q \alpha_D(q)$ and $n_c$ is the explicit constant.

Lean: `Formalism.L2.SG.PoincareAmplitudeLowerBounds.rowFormAllP_of`.

*Proof.* The independence at all data gives the thresholds and the independence at the pair. The concrete tie gives the decay and the local ties, and absolute convergence follows. The normalising constants give the normalisation and $c_0 c_0' > 0$. The formula gives $n_c > 0$, and each $\alpha_D(q)$ is positive. The other inputs hold with no hypothesis. The row form applies. $\square$

### Theorem S

**Theorem 3.13.7 (Theorem S).** Assume the nineteen hypotheses of the ninth section. For each real $C_{\mathrm{thr}}$ there are $C_4 \ge 1$, $C_A \ge \max(C_{\mathrm{thr}}, 1)$ and $0 \le C \le C_A$ such that, for $C_0, C_G, C_\Delta, c_T, C_b$ as in the abstract pair bound, there is $k_0$ with this property. For $C_g, c_b, C_w, c_{Tf}, C_T, C_{0f}$ with $c_b, c_{Tf} > 0$ there are $C_n \ge 0$, $C'_0$ and $C_{l,0}$ such that, for $C' \ge C'_0$, $C_l \ge C_{l,0}$, each datum $D$ with ties, size data of scale $b \ge 0$, each tie package and words $u \ne u'$ with the size and standing conditions, the gap condition, local ties and big and non-scalar rows with $\varepsilon = \exp(-\tfrac13 k f \log k)$,
$$\|K_0(u,u')\|^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^\ast}, \qquad \|K_D(u,u')\|_{\mathrm{HS}}^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^\ast}.$$

Lean: `Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_closedP` (also `Formalism.L2.SG.TheoremSConclusion.theoremS_of_conj`, the form with the nineteen hypotheses as one conjunction).

*Proof.*

1. Fix the constants of Theorem S with the carrier bound. Enlarge $C'_0$ and $C_{l,0}$ to cover the off-diagonal kernel condition and the row form for all data.
2. Finiteness of the cells and the gap condition give finite cells. The decay of the Whittaker functions, the local ties and the frame condition give the concrete tie.
3. The choices give the auxiliary data, with uniformizers and a row label. The formula gives $n_c$.
4. The size numbers give $k \ge 32$, $b \ge 16$ and $(kb)^8 \le g_i$, so $g_i \ge 3$.
5. Absolute convergence holds for tied data. The off-diagonal kernel condition shows that the degenerate part of $t_O(u, u')$ is $0$.
6. The sum of rows, the row form for all data, the mass data, the link condition, the split condition and the agreement of kernel exponents give the other inputs.
7. Theorem S with the carrier bound gives the bounds. The conjunction form splits its hypothesis into the nineteen parts and applies this. $\square$

**Remark 3.13.8 (Formalization).** The abstract pair bound is in TheoremS.lean, line 19. It is `t_PairBoundFromLocal` (GrowthOfBasic.lean, line 1236) applied to nineteen lemmas. The statement `PairBoundFromLocal` is in StatementPB.lean, line 435, with `MainRow` (line 381), `PairBound` (line 220), `PairBoundAbstract` (line 171) and `SizeNumbers` (line 215). Three lemma names do not match their statements: `t_PriceOfIota` proves `NormSqBoundOfEqualIota`, `t_EqualIota` proves `GramSumLeOfPosSemidef`, and `t_EtaZero` proves `SqrtSumSqLeOneAddInvPowSix`. Theorem S for one pair is `theoremS_rec` (SpectralTiesReal.lean, line 147); the carrier condition is `CarrierFull` (line 57) and the tie package is `STies`. Its two bounds use $b^{-6}$ in two forms: `(L.sc.b ^ 6)⁻¹`, a natural power, and `L.sc.b ^ (-(6 : ℝ))`, a real power. The same mix is in `theoremS_of_conj` (TheoremSConclusion.lean, line 68). The two steps that fix the constants are `theoremS_rec2P` and `theoremS_rec3P` (TheoremSClosedP.lean, lines 41 and 127), and the carrier bound `CarrierP` is at line 20. SpectralTiesReal.lean has parallel versions, `theoremS_recursion_fixed` (line 323) and `theoremS_recursion_constants` (line 496), with the stronger `CarrierC` (line 475) and `RowNGC`. No other file uses them. The row form is `rowFormC_of_leaves3` (RowFormAllOf.lean, line 108); no `rowFormC_of_leaves` or `rowFormC_of_leaves2` exists. The row form for all data is `rowFormAllP_of` (TheoremSClosedP.lean, line 229), with `RowFormAllP` at line 212. It uses only the first part of `FormulaC`, the positivity of the explicit constant. Theorem S is `theoremS_closedP` (TheoremSClosedP.lean, line 256), and all nineteen hypotheses are used. In its proof the constant $C$ from `theoremS_rec3P` is passed again as the constant parameter of the mass data hypotheses `hRF` and `hBI`, so one name serves two roles. `TheoremSClosedHypotheses` is at TheoremSConclusion.lean, line 58, and `theoremS_of_conj` is an `obtain` of its nineteen parts followed by one call of `theoremS_closedP`.
