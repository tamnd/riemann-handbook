---
id: word-bound
title: The radial pointwise bound for word operators
kind: theorem
decl: GlobalTheory.HatNF.RadBound.word_bound
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.WordOperatorRadialPointwiseBound
covers: 301
status: drafted
drafted_by: writer@claude
---
This theorem bounds a word operator, applied to a radial function times a multiplier, at each radial point. The bound is a weight times a sum of norms of products of $N$ operators from a fixed set $T$. The restatement [`T.wordOperator_radial_pointwise_bound`](/entry/word-operator-radial-pointwise-bound/) passes it to [`HatNF.wordBound_cptCoef`](/entry/word-bound-cpt-coef/), which moves it to the group picture.

## Statement

Let $\mathcal{A}$ be the algebra `RA P Bs` of radial operators on the space of radial functions $\Phi$. A radial point is a pair $x = (c, g)$ in the domain `Q.DomR`. Put

- $\|\Phi(x)\|$ for the Hilbert-Schmidt norm of $\Phi(c, g)$ (`nv`);
- $d_R(x) = |\prod_a c_a \cdot \zeta(g)|$ and $g_R(x) = |\prod_a c_a|^2\, G(g)$, with $\zeta$ and $G$ from `P5.zeta` and `Q.GGl`, which we have not unfolded;
- $\vartheta^j\varphi(t)$ for the $j$-th derivative of $u \mapsto \varphi(e^u)$ at $u = \log t$ (`LE.ld`), so $\vartheta = t\frac{d}{dt}$ for $t > 0$.

A multiplier family of $\varphi$ (`IsMulG`) is a sequence $W_q$ of operators, where $W_q$ multiplies by $\vartheta^q\varphi(g_R(x))$.

**Theorem.** Let $X, \mu, L, \mathrm{st}, l_0$ satisfy `P5.IsData` and let $d$ be normal form data for $X$. Let $T \subseteq \mathcal{A}$ and $a \in \mathbb{N}$ be such that each basic element of $d$ lies in $\mathrm{nfSpan}(d, T, 0, a, 1)$. Let $w$ be an admitted word of length $N$, and let $M_{w,e} \in \mathcal{A}$ be the entry $e$ of the column $e_1$ of the word operator $(\mathrm{ofWord}(L, \mathrm{st}, w)).F \cdot \mathrm{bTA}(L, w)$. Then there are $C \ge 0$, $J$ and lists $H_1, \dots, H_m$ of $N$ elements of $T$ such that for all $\varphi$ with $\varphi \circ \exp$ smooth, all multiplier families $W$ of $\varphi$, all $\Phi$, $e$ and $x$,

$$\|M_{w,e}(W_0\Phi)(x)\| \le C\, d_R(x)^{-N} g_R(x)^{-aN} \sum_{j=0}^{J} |\vartheta^j\varphi(g_R(x))| \sum_{i=1}^{m} \Bigl\|\Bigl(\prod H_i\Bigr)\Phi(x)\Bigr\|.$$

Here $\mathrm{nfSpan}(d, T, i, j, n)$ is the span of the products $b\, D_i^{\,i}\, g_I^{\,j}\, h_1 \cdots h_n$ with $b$ in the monoid `bmon d` and $h_1, \dots, h_n \in T$.

## Proof

Call a function *bounded with weight* $\omega$ if it is at most $C\,\omega(x)$ times a sum of norms $\|(\prod H)\Phi(x)\|$ over a finite list of $H$ (the predicate `Bd`). These bounds are closed under sums (`Bd.add`, `Bd.listSum`).

1. **Span bound** (`span_bd`). Each element of $\mathrm{nfSpan}(d, T, i, j, n)$ is bounded with weight $d_R^{-i} g_R^{-j}$. The proof is induction on the span. For a generator, `T.pointwiseBounded_of_mem_boundedFactors_monoid` bounds $b$. Also, `T.pointwise_bounded_radial_ops_closure_and_functions` says that $D_i$ and $g_I$ multiply the pointwise norm by exactly $d_R(x)^{-1}$ and $g_R(x)^{-1}$.
2. **Hat letters.** `T.normalForm_actualOperators_algebraicHypotheses` gives the algebraic hypotheses on $d$. Then `T.hatLetters_mem_normalFormProductSpan` and `T.list_prod_hatLetters_mem_normalFormProductSpan` put a product of $N$ hat letters in $\mathrm{nfSpan}(d, T, 0, aN, N)$.
3. **Leibniz rule.** `T.hatLetters_prod_mul_multiplier_leibniz` writes (product of $N$ hat letters) $\cdot W_0$ as a sum of terms $W_q \cdot$ (product of $N$ hat letters), with $q \le N(r+1)$. `T.radialMultipliers_satisfy_normalForm_relations` supplies the commutation relations that it needs. So with $J = N(r+1)$, each term is bounded with weight $\sum_j |\vartheta^j\varphi(g_R)| \cdot g_R^{-aN}$.
4. **Word operator.** `T.wordOperator_column_mem_normalFormProductSpan` puts $M_{w,e}$ in $\mathrm{nfSpan}(d, \mathrm{hats}, N, 0, N)$. Step 1, applied to this span, adds the factor $d_R^{-N}$.

Sum over all $e$ to get one constant for every $e$. The rest is bookkeeping.

## In the Lean code

The theorem is in [WordOperatorRadialPointwiseBound.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordOperatorRadialPointwiseBound.lean#L178). The predicate `Bd` is at line 20 and `span_bd` at line 140. `nfSpan`, `basics`, `nv`, $g_R$, $d_R$ and `IsMulG` are in [SameFns.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/SameFns.lean#L46).

The statement says only that $J$ exists. The proof takes $J = N(r+1)$.
