---
title: The Fourier transform preserves matching
decls:
  - GlobalTheory.JR.fourierMatchAt_of_weil
  - GlobalTheory.JR.fourierMatch_of_weil
  - GlobalTheory.T.jacquetRallisFourierMatch_of_weilRepresentation
  - GlobalTheory.JR.fourierMatch_of_weilField
  - GlobalTheory.T.jacquetRallis_fourier_matching_of_weil_field
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Fourier transform preserves matching

This section proves that the partial Fourier transforms of [the first section](/entry/unit-match-at-of-one-le-norm/) preserve matching, in every rank. This is the statement that the Weyl element $w$ preserves matching, in the language of the next section. The proof descends a regular orbit to an orbit of rank one over an etale algebra, applies [the rank one transfer](/entry/rank-one/), and uses [the Weil constant of the standard form](/entry/weil-field-main/) to remove the constant. The result is used in [the induction on the rank](/entry/unit-match-succ/).

Throughout, $(F, E)$ is an unramified quadratic pair and $\psi$ is a standard character of $F$. Recall that $C(p)$ is the companion matrix of $P(X) = X^r + \sum_{i<r} p_i X^i$, so that $\det(X - C(p)) = P$.

**Definition 4.4.1 (Generator).** Let $(K, L)$ be an etale Hermitian pair over $(F, E)$ and $p \in F^r$. An element $\tau \in K$ is a generator with polynomial $p$ if $1, \tau, \dots, \tau^{r-1}$ are linearly independent over $F$, $\dim_F K = r$, and $P(\tau) = 0$. For $\lambda \in F$ and $a \in K$ put
$$\mathrm{inv}_\tau(a) = \Big(p,\ \big(\mathrm{Tr}_{K/F}(\tau^i a)\big)_{i<r},\ \lambda\Big) \in \mathrm{Inv}_r(F).$$

So $K = F[\tau] \cong F[X]/(P)$. The map $\mathrm{inv}_\tau$ parametrizes the invariants with characteristic polynomial $P$ and last entry $\lambda$ by the elements of $K$.

**Lemma 4.4.2 (Etale parametrization).** 1. If $P$ is separable, there are an etale Hermitian pair $(K, L)$ over $(F, E)$ and a generator $\tau \in K$ with polynomial $p$. 2. Let $\tau$ be a generator with polynomial $p$. Then $a \mapsto (\mathrm{Tr}_{K/F}(\tau^i a))_{i<r}$ is a bijection $K \to F^r$; the moments of $\mathrm{sec}(\mathrm{inv}_\tau(a))$ are $m_i = \mathrm{Tr}_{K/F}(\tau^i a)$ for all $i \ge 0$; and $\Delta(\mathrm{inv}_\tau(a)) \neq 0$ if and only if $a$ is a unit of $K$.

Lean: `GlobalTheory.T.exists_etaleHermitianPair_isGen_companion`, `GlobalTheory.T.jacquetRallis_invK_regular_iff_isUnit`.

*Proof.* For 1, take $K = F[X]/(P)$, which is reduced since $P$ is separable, $L = K \otimes_F E$ with the involution $1 \otimes \bar{\ }$, and $\tau$ the class of $X$. For 2, the trace form of the etale algebra $K$ is nondegenerate, so the map is a bijection. For $i < r$ the $i$-th moment of $\mathrm{sec}(\mathrm{inv}_\tau(a))$ is the $i$-th entry $\mathrm{Tr}(\tau^i a)$, and both sides satisfy the linear recursion given by $P$ for $i \ge r$. Hence $H(\mathrm{inv}_\tau(a))$ is the matrix of the bilinear form $(u, v) \mapsto \mathrm{Tr}(uva)$ in the basis $\tau^i$. Its determinant is the discriminant of this basis times $N_{K/F}(a)$, which is nonzero exactly when $a$ is a unit. $\square$

For a generator $\tau$ we need two descent statements, one for each side. For the Hermitian side, call an $E$-linear isomorphism $j : L \to E^r$ an isometry for $x \in K$ if $\overline{j(y)}^{\,t} j(y') = \mathrm{Tr}_{L/E}(x \bar y y')$ for all $y, y'$.

**Lemma 4.4.3 (Descent of orbits).** Let $\tau$ be a generator with polynomial $p$ and $\lambda \in F$.

1. Let $a$ be a unit of $K$ and $X = (S, v, \lambda') \in \mathfrak{h}_r$ with invariants $\mathrm{inv}_\tau(a)$. If $a = x N(y)$ with $y$ a unit of $L$, there is an isometry $j$ for $x$ with $j(\tau z) = S j(z)$ for all $z$ and $j(y) = v$.
2. If $j$ is an isometry for $x \in K$, there is a Hermitian matrix $S_x$ with $j(\tau z) = S_x j(z)$ for all $z$, and $(S_x, j(y), \lambda)$ has invariants $\mathrm{inv}_\tau(x N(y))$ for every $y \in L$.
3. Two elements of $\mathfrak{h}_r$ with the same invariants $a$, $\Delta(a) \neq 0$, are conjugate by a unique element of $U_r$.

Lean: `GlobalTheory.T.hermitianBlock_invariants_iff_isometry`, `GlobalTheory.T.unitary_action_hermitian_invariants_transitive`.

The isometry $j$ identifies the Hermitian space $E^r$ with $L$ and the operator $S$ with multiplication by $\tau$. The invariants of $(S, v)$ are the traces $\bar v^t S^i v = \mathrm{Tr}_{L/E}(x \tau^i \bar y y) = \mathrm{Tr}_{K/F}(\tau^i x N(y))$, up to the identification of $F$ in $E$.

**Lemma 4.4.4 (Descent of orbital integrals).** Let $\tau$ be a generator with polynomial $p$, $\lambda \in F$, and choose measures in rank $r$ and rank one measures $\mu_K, \mu_{L,x}, \nu$ for $(K, L)$.

1. For every test function $f'$ on $\mathfrak{g}_r(F)$ there are a test function $\varphi'$ on $K \times K$ and $\kappa \in \mathbb{C}$ with
$$O\big(f', \mathrm{sec}(\mathrm{inv}_\tau(a))\big) = \kappa\, O_K(\varphi', a), \qquad O\big(\mathcal{F}f', \mathrm{sec}(\mathrm{inv}_\tau(a))\big) = \kappa\, O_K(\mathcal{F}_K\varphi', a)$$
for every unit $a$ of $K$.
2. Let $j$ be an isometry for $x \in K^\times$ and $S_x$ as above. For every test function $f$ on $\mathfrak{h}_r$ there is a test function $\varphi_x$ on $L$ with
$$O\big(f, (S_x, j(y), \lambda)\big) = O_L(\varphi_x, y), \qquad O\big(\mathcal{F}f, (S_x, j(y), \lambda)\big) = O_L(\mathcal{F}_{B_x}\varphi_x, y)$$
for every unit $y$ of $L$, where $\mathcal{F}_{B_x}$ is taken for $\mu_{L,x}$.

Lean: `GlobalTheory.T.jacquetRallis_linear_orbitalIntegral_descent`, `GlobalTheory.T.exists_test_orbU_eq_orbL`.

These are the descent of orbital integrals to the centralizer, in the form needed here: the partial Fourier transform in the vector variables becomes the Fourier transform on $K \times K$ or on $L$.

**Lemma 4.4.5 (Regular invariants suffice).** Fix measures in rank $r$ and let $f'$ and $f$ be test functions. 1. If they match at every $a$ with $\Delta(a) \neq 0$ and $P$ separable, they match. 2. If $r > 0$ and they match at every $a$ with $\Delta(a) \neq 0$ and $m_0 \neq 0$, they match.

Lean: `GlobalTheory.T.jacquetRallis_match_of_dense_separable`.

These conditions cut out dense open subsets of the regular invariants, and the orbital integrals of test functions are locally constant there.

**Lemma 4.4.6 (Fourier transform of test functions).** For measures in rank $r$ and standard $\psi$, the partial Fourier transforms map test functions to test functions, the unit functions are test functions, and $\mathcal{F}1_{\mathfrak{g}_r} = 1_{\mathfrak{g}_r}$, $\mathcal{F}1_{\mathfrak{h}_r} = 1_{\mathfrak{h}_r}$.

Lean: `GlobalTheory.T.partialFourier_preserves_test_fixes_unit`.

The second part holds because $\mathcal{O}_F$ and $\mathcal{O}_E$ have volume $1$ and are self-dual for $\psi$ and for $\psi \circ \mathrm{Tr}_{E/F}$, since $\psi$ has conductor $\mathcal{O}_F$ and $E/F$ is unramified.

**Theorem 4.4.7 (Fourier matching at a separable invariant).** Assume: (a) the conclusion of the [Theorem on Weil representations for etale pairs](/entry/weil-et-of-weil-field/), for all unramified quadratic pairs; (b) the conclusion of [the rank one transfer](/entry/rank-one/), for all data; (c) the conclusion of [the Theorem on the Weil constant](/entry/weil-field-main/), for all data. Let $(F, E)$ be an unramified quadratic pair, fix measures in rank $r$, let $\psi$ be standard, and let $f'$ and $f$ be test functions that match. Let $a = (p, m, \lambda) \in \mathrm{Inv}_r(F)$ with $\Delta(a) \neq 0$ and $P$ separable. Then $\mathcal{F}f'$ and $\mathcal{F}f$ match at $a$.

Lean: `GlobalTheory.JR.fourierMatchAt_of_weil`.

*Proof.* Step 1: descent. By the Lemma on etale parametrization there are $(K, L)$ and a generator $\tau$ with polynomial $p$, and a unique $a_0 \in K$ with $\mathrm{inv}_\tau(a_0) = a$. Since $\Delta(a) \neq 0$, $a_0$ is a unit. Choose rank one measures; they exist. Choose a finite set $S$ of representatives of $K^\times / N(L^\times)$.

Step 2: the data for the transfer. The Lemma on orbital integrals gives $\varphi'$ and $\kappa$ for $f'$. For $x \in K^\times$: if there is an isometry $j$ for $x$, take $S_x$ and $\varphi_x$ from the Lemmas on descent; otherwise put $\varphi_x = 0$. By (a), for each $x$ there are a Weil representation $W_x$ with data $x, \eta_K, \mu_{L,x}$ and a constant $\gamma_x$.

Step 3: the hypothesis of the transfer. Let $x \in S$ and $y \in L^\times$. Then $x N(y)$ is a unit, so $\Delta(\mathrm{inv}_\tau(xN(y))) \neq 0$ and $f', f$ match there. If an isometry $j$ for $x$ exists, then $(S_x, j(y), \lambda)$ has invariants $\mathrm{inv}_\tau(xN(y))$, and
$$\kappa\, O_K(\varphi', xN(y)) = O\big(f', \mathrm{sec}(\mathrm{inv}_\tau(xN(y)))\big) = O\big(f, (S_x, j(y), \lambda)\big) = O_L(\varphi_x, y).$$
If no isometry exists, then by part 1 of the Lemma on descent of orbits no $X$ has invariants $\mathrm{inv}_\tau(xN(y))$. The second clause of matching gives $O(f', \cdot) = 0$, and $O_L(0, y) = 0$.

Step 4: the transfer. By (b), $\kappa\, O_K(\mathcal{F}_K\varphi', xN(y)) = \gamma_x\, O_L(\mathcal{F}_{B_x}\varphi_x, y)$ for $x \in S$ and units $y$. By (c), $\gamma_x = 1$ when an isometry for $x$ exists. Write $a_0 = x N(y)$ with $x \in S$. Then
$$O\big(\mathcal{F}f', \mathrm{sec}(a)\big) = \kappa\, O_K(\mathcal{F}_K\varphi', a_0) = \gamma_x\, O_L(\mathcal{F}_{B_x}\varphi_x, y).$$

Step 5: the two clauses. Let $X$ have invariants $a$. By part 1 of the Lemma on descent of orbits, an isometry for $x$ exists, so $\gamma_x = 1$ and $\varphi_x$ comes from some $j$ and $S_x$. The element $(S_x, j(y), \lambda)$ also has invariants $a$, so it lies in the orbit of $X$, and orbital integrals are constant on orbits. Hence $O(\mathcal{F}f, X) = O_L(\mathcal{F}_{B_x}\varphi_x, y) = O(\mathcal{F}f', \mathrm{sec}(a))$. If no $X$ has invariants $a$, then no isometry for $x$ exists, since otherwise $(S_x, j(y), \lambda)$ would have invariants $a$. So $\varphi_x = 0$ and $O(\mathcal{F}f', \mathrm{sec}(a)) = 0$. $\square$

**Theorem 4.4.8 (Fourier matching from Weil representations).** Assume (a), (b) and (c) as above. Then Fourier matching holds in every rank $r$.

Lean: `GlobalTheory.JR.fourierMatch_of_weil` (also `GlobalTheory.T.jacquetRallisFourierMatch_of_weilRepresentation`, a second name).

*Proof.* Let $f'$ and $f$ be test functions that match. Their Fourier transforms are test functions, by the Lemma on the Fourier transform. They match at every $a$ with $\Delta(a) \neq 0$ and $P$ separable, by the previous Theorem. By part 1 of the Lemma on regular invariants, they match. $\square$

**Theorem 4.4.9 (Fourier matching).** Assume the conclusion of the [Theorem on Weil representations for fields](/entry/weil-field-main/). Then Fourier matching holds in every rank $r$.

Lean: `GlobalTheory.JR.fourierMatch_of_weilField` (also `GlobalTheory.T.jacquetRallis_fourier_matching_of_weil_field`, a second name).

*Proof.* The hypothesis gives (a) by the [Theorem on etale pairs](/entry/weil-et-of-weil-field/). The [rank one transfer](/entry/rank-one/) is (b), and the Theorem on the Weil constant is (c). Apply the previous Theorem. $\square$

**Remark 4.4.10 (Formalization).** The three inputs (a), (b) and (c) are hypotheses of the first two theorems, and the last theorem supplies them, with the field case of Weil representations still as a hypothesis. That case is the [Theorem on fields](/entry/weil-field-main/), and the two are combined in the [next section](/entry/unit-match-all/). The five lemmas of this section are proved in their own files, which this chapter does not cover; the text after each lemma explains it but does not prove it, except for the etale parametrization.
