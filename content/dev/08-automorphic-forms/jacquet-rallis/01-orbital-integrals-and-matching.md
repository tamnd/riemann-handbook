---
title: Orbital integrals and matching
decls:
  - GlobalTheory.JR.Step.unitMatchAt_of_one_le_norm
  - GlobalTheory.T.jacquetRallisUnitMatch_step_of_one_le_norm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orbital integrals and matching

This section sets up the objects of the Jacquet-Rallis fundamental lemma in its Lie algebra form: the two spaces, their invariants, the orbital integrals and the notion of matching. It then proves the first part of the induction on the rank. If the fundamental lemma holds in rank $r$, then the unit functions in rank $r + 1$ match at every invariant whose first moment has norm at least $1$. The rest of the induction, for small first moments, is in [the section on unit matching](/entry/unit-match-succ/). The classical setting is in the [relative trace formula](/learn/trace-formula/#the-relative-trace-formula-and-the-jacquet-rallis-fundamental-lemma) and in [orbital integrals](/learn/periods/#orbit-integrals-and-the-relative-trace-formula).

**Definition 4.1.1 (Unramified quadratic pair).** An unramified quadratic pair is a pair of nontrivially normed fields $F \subset E$, with $E$ a normed $F$-algebra and an involution $y \mapsto \bar y$ of the ring $E$, such that: $F$ has characteristic $0$; $F$ and $E$ are ultrametric and locally compact; $[E : F] = 2$; the involution fixes $F$, is not the identity, and satisfies $|\bar y| = |y|$; and every value $|y|$ with $y \in E$ is a value $|x|$ with $x \in F$.

So $F$ is a finite extension of some $\mathbb{Q}_p$ (see [places and completions](/learn/number-fields/#places-and-completions)), and $E/F$ is the unramified quadratic extension with its Galois conjugation. We write $\mathcal{O}_F$ and $\mathcal{O}_E$ for the closed unit balls and $q$ for the size of the residue field of $F$. There is no condition on $p$: the residue characteristic can be $2$.

**Definition 4.1.2 (The sign $\eta$).** For $x \in F$ put $\eta(x) = 1$ if $|x| = |y|^2$ for some $y \in F$, and $\eta(x) = -1$ otherwise.

For $x \neq 0$ this is $(-1)^{v(x)}$, with $v$ the normalized valuation. It is the quadratic character of $F^\times$ attached to $E/F$, since the norms from $E^\times$ are the elements of even valuation. Note that $\eta(0) = 1$.

**Definition 4.1.3 (Standard character).** An additive character $\psi : F \to \mathbb{C}^\times$ is standard if $\psi(x) = 1$ for $|x| \le 1$, and there is an $x \in F$ with $\psi(x) \neq 1$ and $|xy| \le 1$ for all $|y| < 1$.

The second condition says that $\psi$ is not trivial on $\varpi^{-1}\mathcal{O}_F$, for a uniformizer $\varpi$. So the conductor of $\psi$ is exactly $\mathcal{O}_F$.

**Definition 4.1.4 (Test function).** A function on a topological space is a test function if it is locally constant and has compact support.

**Definition 4.1.5 (The linear side).** Let $r \ge 0$ and let $k$ be a commutative ring. Put
$$\mathfrak{g}_r(k) = M_r(k) \times k^r \times k^r \times k,$$
with elements $Y = (A, b, c, d)$, where $b$ is a column and $c$ is a row. The group $\mathrm{GL}_r(k)$ acts by $g \cdot Y = (gAg^{-1}, gb, cg^{-1}, d)$. We identify $Y$ with the bordered matrix
$$\widehat{Y} = \begin{pmatrix} A & b \\ c & d \end{pmatrix} \in M_{r+1}(k).$$
Then the action is conjugation by $\mathrm{diag}(g, 1)$. This is the action of $\mathrm{GL}_r$ on $\mathfrak{gl}_{r+1}$ in the work of Jacquet and Rallis.

**Definition 4.1.6 (Invariants).** The moments of $Y$ are $m_i(Y) = c A^i b$ for $i \ge 0$. The invariants of $Y$ are
$$\mathrm{inv}(Y) = \big((p_i)_{i < r}, (m_i(Y))_{i < r}, d\big) \in \mathrm{Inv}_r(k) = k^r \times k^r \times k,$$
where $\det(X - A) = X^r + \sum_{i<r} p_i X^i$. Each entry is invariant under the action.

**Definition 4.1.7 (The section).** For $p \in k^r$ let $C(p)$ be the companion matrix with entries $C(p)_{i, r-1} = -p_i$, $C(p)_{j+1, j} = 1$, and $0$ elsewhere. For $a = (p, m, d) \in \mathrm{Inv}_r(k)$ put $\mathrm{sec}(a) = (C(p), e_0, m, d)$.

Since $C(p)^i e_0 = e_i$ for $i < r$, the moments of $\mathrm{sec}(a)$ are $m_0, \dots, m_{r-1}$, and $\mathrm{inv}(\mathrm{sec}(a)) = a$. So $\mathrm{sec}$ picks one point in each fibre of the invariant map.

**Definition 4.1.8 (Regular invariants).** For $a \in \mathrm{Inv}_r(k)$ let $H(a)$ be the Hankel matrix $H(a)_{ij} = m_{i+j}(\mathrm{sec}(a))$ for $0 \le i, j < r$, and $\Delta(a) = \det H(a)$.

If $B$ is the matrix with columns $A^j b$ and $C$ the matrix with rows $c A^i$, then $\Delta(\mathrm{inv}(Y)) = \det(CB)$. So $\Delta(\mathrm{inv}(Y)) \neq 0$ means that $b$ is a cyclic vector for $A$ and $c$ is a cyclic vector for the transpose. These are the regular semisimple elements of the action.

**Definition 4.1.9 (Transfer factor).** Let $e$ be the last basis row vector of $k^{r+1}$. Let $D(Y)$ be the determinant of the $(r+1) \times (r+1)$ matrix with rows $e\widehat{Y}^i$, $0 \le i \le r$. For $Y \in \mathfrak{g}_r(F)$ put $\omega(Y) = \eta(D(Y))$.

Since $e \, \mathrm{diag}(g, 1) = e$, we get $D(g \cdot Y) = \det(g)^{-1} D(Y)$, so $\omega(g \cdot Y) = \eta(\det g)\, \omega(Y)$ when $D(Y) \neq 0$. This is the transfer factor of Jacquet and Rallis.

**Definition 4.1.10 (The Hermitian side).** Let $(F, E)$ be an unramified quadratic pair. Put
$$\mathfrak{h}_r = \mathrm{Herm}_r(E) \times E^r \times F,$$
with elements $X = (S, v, d)$, $S = \bar S^{t}$. The unitary group $U_r = \{ g \in M_r(E) : g \bar g^{t} = 1 \}$ acts by $g \cdot X = (g S \bar g^{t}, g v, d)$. Send $X$ to $\iota(X) = (S, v, \bar v^{t}, d) \in \mathfrak{g}_r(E)$. We say that $X$ has invariants $a \in \mathrm{Inv}_r(F)$ if $\mathrm{inv}(\iota(X))$ is the image of $a$ in $\mathrm{Inv}_r(E)$.

So $X$ has invariants $a$ when $S$ has the characteristic polynomial given by $a$, the numbers $\bar v^{t} S^i v$ are the moments of $a$, and the last entries agree. This is the space of [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms) with a vector, under the [unitary group](/learn/groups/#unitary-groups) of the standard form.

**Definition 4.1.11 (Measures).** A choice of measures in rank $r$ is a Haar measure on $\mathrm{GL}_r(F)$, a Haar measure on $U_r$, and additive Haar measures on $F$ and $E$, such that $\mathrm{GL}_r(\mathcal{O}_F)$, $U_r \cap M_r(\mathcal{O}_E)$, $\mathcal{O}_F$ and $\mathcal{O}_E$ have volume $1$.

**Definition 4.1.12 (Orbital integrals).** For functions $f'$ on $\mathfrak{g}_r(F)$ and $f$ on $\mathfrak{h}_r$ put
$$O(f', Y) = \int_{\mathrm{GL}_r(F)} f'(g \cdot Y)\, \omega(g \cdot Y)\, dg, \qquad O(f, X) = \int_{U_r} f(g \cdot X)\, dg.$$

By the rule for $\omega$ above, $O(f', Y) = \omega(Y) \int f'(g \cdot Y) \eta(\det g)\, dg$ when $D(Y) \neq 0$. So the first integral is the $\eta$-twisted orbital integral times the transfer factor.

**Definition 4.1.13 (Matching).** Fix measures in rank $r$. Functions $f'$ on $\mathfrak{g}_r(F)$ and $f$ on $\mathfrak{h}_r$ match at $a \in \mathrm{Inv}_r(F)$ if:

1. $O(f', \mathrm{sec}(a)) = O(f, X)$ for every $X \in \mathfrak{h}_r$ with invariants $a$; and
2. $O(f', \mathrm{sec}(a)) = 0$ if no $X \in \mathfrak{h}_r$ has invariants $a$.

They match if they match at every $a$ with $\Delta(a) \neq 0$.

The second clause is the usual statement that the orbital integral of $f'$ vanishes on the orbits that come from the other Hermitian space. Here only the standard Hermitian form is used, and its unit function is matched with the unit function of $\mathfrak{g}_r$.

**Definition 4.1.14 (Unit functions).** Let $1_{\mathfrak{g}_r}$ be the indicator function of the $Y$ with all entries in $\mathcal{O}_F$, and $1_{\mathfrak{h}_r}$ the indicator function of the $X$ with all entries of $S$ and $v$ in $\mathcal{O}_E$ and $d \in \mathcal{O}_F$.

**Definition 4.1.15 (Fundamental lemma in rank $r$).** The fundamental lemma holds in rank $r$ if $1_{\mathfrak{g}_r}$ and $1_{\mathfrak{h}_r}$ match, for every unramified quadratic pair and every choice of measures in rank $r$.

**Definition 4.1.16 (Partial Fourier transforms).** Fix measures and a character $\psi$. For $Y = (A, b, c, d)$ and $X = (S, v, d)$ put
$$\begin{aligned} \mathcal{F}f'(Y) &= \int_{F^r} \int_{F^r} f'(A, b', c', d)\, \psi(c' b + c b')\, dc'\, db', \\ \mathcal{F}f(X) &= \int_{E^r} f(S, w, d)\, \psi\big(\mathrm{Tr}_{E/F}(\bar w^{t} v)\big)\, dw. \end{aligned}$$
Fourier matching holds in rank $r$ if, for every unramified pair, every choice of measures, every standard $\psi$ and all test functions $f'$ and $f$ that match, $\mathcal{F}f'$ and $\mathcal{F}f$ also match.

These are [Fourier transforms](/learn/analysis/#the-fourier-transform) in the vector variables only. The matrix and the last entry do not move.

**Lemma 4.1.17 (Large first moment).** Let $(F, E)$ be an unramified quadratic pair, fix measures in rank $r + 1$, and let $a \in \mathrm{Inv}_{r+1}(F)$ with $|m_0| > 1$. Then $1_{\mathfrak{g}_{r+1}}$ and $1_{\mathfrak{h}_{r+1}}$ match at $a$.

Lean: `GlobalTheory.T.unitIndicators_matchAt_of_one_lt_norm_firstMoment`.

*Proof.* The first moment $c b$ is an invariant, so every $g \cdot \mathrm{sec}(a)$ has $c b = m_0$. If $g \cdot \mathrm{sec}(a)$ had integral entries, then $|m_0| \le 1$. So the integrand of $O(1_{\mathfrak{g}}, \mathrm{sec}(a))$ is zero, and the integral is $0$. In the same way, an $X$ with invariants $a$ has $\bar v^{t} v = m_0$, so no $g \cdot X$ is integral and $O(1_{\mathfrak{h}}, X) = 0$. Both clauses of matching hold. $\square$

To pass from rank $r + 1$ to rank $r$, we use a normal form. For $Z \in \mathfrak{g}_r(k)$ and $\mu, l \in k$ let $\lambda(Z, \mu, l) \in \mathfrak{g}_{r+1}(k)$ be the element with matrix $\widehat{Z}$, column $\mu e$, row $e$ and corner $l$, where $e$ is the last basis vector. For $X' \in \mathfrak{h}_r$, $\nu \in E$ and $l \in F$ let $\lambda_H(X', \nu, l) \in \mathfrak{h}_{r+1}$ be the element with Hermitian matrix $\widehat{\iota(X')}$, vector $\nu e$ and corner $l$. The first moment of $\lambda(Z, \mu, l)$ is $\mu$, and that of $\lambda_H(X', \nu, l)$ is $\nu \bar \nu$.

**Proposition 4.1.18 (Step for large moments).** Let $r \ge 0$ and assume the fundamental lemma in rank $r$. Let $(F, E)$ be an unramified quadratic pair, fix measures in rank $r + 1$, and let $a \in \mathrm{Inv}_{r+1}(F)$ with $\Delta(a) \neq 0$ and $|m_0(\mathrm{sec}(a))| \ge 1$. Then $1_{\mathfrak{g}_{r+1}}$ and $1_{\mathfrak{h}_{r+1}}$ match at $a$.

Lean: `GlobalTheory.JR.Step.unitMatchAt_of_one_le_norm` (also `GlobalTheory.T.jacquetRallisUnitMatch_step_of_one_le_norm`, a second name).

*Proof.* Write $a = (p, m, l)$ and $\mu = m_0$; this is the first moment of $\mathrm{sec}(a)$. If $|\mu| > 1$, use the Lemma on large first moments. So let $|\mu| = 1$.

Linear side. Since $\mu \neq 0$, there are $g \in \mathrm{GL}_{r+1}(F)$ and $Z \in \mathfrak{g}_r(F)$ with $g \cdot \mathrm{sec}(a) = \lambda(Z, \mu, l)$. So $\lambda(Z, \mu, l)$ has invariants $a$, and $\Delta(\mathrm{inv}(Z)) \neq 0$ follows from $\Delta(a) \neq 0$. Choose measures in rank $r$ (they exist). A direct computation of the integral over $\mathrm{GL}_{r+1}(F)$ gives
$$O\big(1_{\mathfrak{g}_{r+1}}, \lambda(Z, \mu, l)\big) = 1_{|l| \le 1} \cdot O(1_{\mathfrak{g}_r}, Z).$$
Orbital integrals are constant on orbits, and $Z$ lies in the orbit of $\mathrm{sec}(\mathrm{inv}(Z))$ since $\Delta(\mathrm{inv}(Z)) \neq 0$. So the left side of matching at $a$ is $1_{|l| \le 1} \cdot O(1_{\mathfrak{g}_r}, \mathrm{sec}(\mathrm{inv}(Z)))$.

Hermitian side. Let $X \in \mathfrak{h}_{r+1}$ have invariants $a$. Then there are $u \in U_{r+1}$, $X' \in \mathfrak{h}_r$ and $\nu \in E$ with $\nu \bar\nu = \mu$ and $u \cdot X = \lambda_H(X', \nu, l)$. So $|\nu| = 1$. The same computation over $U_{r+1}$ gives
$$O(1_{\mathfrak{h}_{r+1}}, X) = 1_{|l| \le 1} \cdot O(1_{\mathfrak{h}_r}, X'),$$
and comparing the two normal forms shows that $X'$ has invariants $\mathrm{inv}(Z)$. The fundamental lemma in rank $r$, at $\mathrm{inv}(Z)$, gives $O(1_{\mathfrak{g}_r}, \mathrm{sec}(\mathrm{inv}(Z))) = O(1_{\mathfrak{h}_r}, X')$. This is the first clause.

Vanishing. Assume that no $X$ has invariants $a$. Since $E/F$ is unramified and $|\mu| = 1$, there is $\nu \in E$ with $\nu \bar\nu = \mu$. If some $X' \in \mathfrak{h}_r$ had invariants $\mathrm{inv}(Z)$, then $\lambda_H(X', \nu, l)$ would have invariants $a$. So no such $X'$ exists, and the second clause of the fundamental lemma in rank $r$ gives $O(1_{\mathfrak{g}_r}, \mathrm{sec}(\mathrm{inv}(Z))) = 0$. Hence the left side is $0$. $\square$

**Remark 4.1.19 (Formalization).** The sign is defined with $\eta(0) = 1$ ([FourierMatch.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/FourierMatch.lean#L22)). The orbital integrals are Bochner integrals, which are $0$ when the integrand is not integrable. The transfer factor is evaluated at $g \cdot Y$ inside the integral, with no separate factor $\eta(\det g)$. The fundamental lemma in rank $r$ quantifies over all choices of measures; such a choice exists, by `GlobalTheory.T.nonempty_jacquetRallisHaarMeasures_forall_size`. The lemma on large moments does not need $\Delta(a) \neq 0$. The identity $m_0(\mathrm{sec}(a)) = m_0$ is proved twice, as `GlobalTheory.JR.Step.mom_sec_zero` (JacquetRallisUnitMatchStepOfOneLeNorm.lean:23) and as a lemma of the same name in the namespace `GlobalTheory.JR.UnitStep` (JacquetRallisUnitMatchSucc.lean:38).
