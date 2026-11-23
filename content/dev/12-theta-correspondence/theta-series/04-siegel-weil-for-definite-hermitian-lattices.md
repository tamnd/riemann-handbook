---
title: Siegel-Weil for definite Hermitian lattices
decls:
  - GlobalTheory.SW.Step.hecke_swd
  - GlobalTheory.SW.Step.bound_step
  - GlobalTheory.SW.swAt_succ
  - GlobalTheory.T.siegelWeil_formula_degree_succ
  - GlobalTheory.SW.siegel_weil_definite
  - GlobalTheory.T.siegelWeil_definiteHermitian_of_four_mul_lt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Siegel-Weil for definite Hermitian lattices

This section proves the Siegel-Weil formula $\mathrm{SW}(n, N)$ of [the previous section](/entry/swd-invariant-bound/) for all $N$ with $4N < n$, when $n$ is even. The proof is by induction on the degree $N$. In degree $0$ both sides are the value of the test function at $0$. For the step from $N$ to $N + 1$, a Hecke operator at a split prime $q$ gives a linear relation among twisted Siegel-Weil differences. Combined with the [twisted bound](/entry/twist-swd-bounded/), it shows that the best constant in that bound is at most $\theta$ times itself for some $\theta < 1$, so it is $0$. The [kernel identity](/entry/kernel-identity/) of the next section uses the formula for a doubled family of degree $r$.

We keep the notation of the previous section: a CM field $E$ with a CM type $\Psi$, the Hermitian upper half space $\mathcal{H}_N$, the function $\Delta(Z) = \prod_\tau \det \operatorname{Im} Z_\tau$, admissible families $\varphi$ of level $(M, R)$, the Siegel-Weil difference $D_\varphi(Z)$, the twist $\varphi^{\mathfrak{X}}$ by an $\mathcal{O}_E$-submodule $\mathfrak{X} \subset E^N$, and the generalized index $\iota(\mathfrak{X})$.

**Definition 3.4.1 (Good prime).** Let $m > 0$. A *good prime* for $m$ is a pair $(q, \mathfrak{P})$ of a rational prime $q$ prime to $m$ and an ideal $\mathfrak{P}$ of $\mathcal{O}_E$ of norm $q$ that is prime to its complex conjugate $\bar{\mathfrak{P}}$, such that $q$ does not divide $2 \operatorname{disc}(E)$.

So $q$ is unramified in $E$, and $\mathfrak{P}$ is a prime of degree one above $q$ that is split in $E$ over its maximal totally real subfield.

### The Hecke relation

**Lemma 3.4.2 (Hecke relation for the difference).** Let $n$ be even with $4N < n$, let $\varphi$ be admissible of level $(M, R)$ and degree $N$, let $(q, \mathfrak{P})$ be a good prime for $RM$, and let $\mathfrak{X} \subset E^N$ be finitely generated and agree with $\mathcal{O}_E^N$ away from $RM$. Then there are $A \ge 0$ with $A(q - 1) = q^N - 1$, finitely generated $\mathfrak{X}^+_1, \dots, \mathfrak{X}^+_A$ and $\mathfrak{X}^-_1, \dots, \mathfrak{X}^-_A$ in $E^N$ that agree with $\mathcal{O}_E^N$ away from $RM$, with
$$\iota(\mathfrak{X}^+_i) = q\, \iota(\mathfrak{X}), \qquad q\, \iota(\mathfrak{X}^-_i) = \iota(\mathfrak{X}),$$
and Hermitian matrices $\beta_{ij} \in M_N(E)$ for $1 \le i \le A$ and $1 \le j \le q^N$, such that for all $Z \in \mathcal{H}_N$
$$\begin{aligned} (q^N - 1)(q^n + q^N)\, D_{\varphi^{\mathfrak{X}}}(Z) = (q - 1)\Big( & q^n \sum_{i=1}^A D_{\varphi^{\mathfrak{X}^+_i}}(Z) \\ & + \sum_{i=1}^A \sum_{j=1}^{q^N} D_{\varphi^{\mathfrak{X}^-_i}}(Z + \beta_{ij}) \Big). \end{aligned}$$

Lean: `GlobalTheory.SW.Step.hecke_swd`

*Proof.* This is the pointwise Hecke relation for admissible families, a result of the sources, applied to $\varphi$, $\mathfrak{X}$ and $(q, \mathfrak{P})$. $\square$

### The contraction

**Lemma 3.4.3 (Contraction step).** Let $n = 2k$ with $0 < N$ and $4N < 2k$. Let $\varphi$ be admissible of level $(M, R)$ and degree $N$, and let $(q, \mathfrak{P})$ be a good prime for $RM$. Let $S \in \mathbb{R}$ with
$$\iota(\mathfrak{X})^k\, |D_{\varphi^{\mathfrak{X}}}(Z)|\, \Delta(Z)^k \le S$$
for all finitely generated $\mathfrak{X}$ that agree with $\mathcal{O}_E^N$ away from $RM$ and all $Z \in \mathcal{H}_N$. Then for all such $\mathfrak{X}$ and $Z$,
$$\iota(\mathfrak{X})^k\, |D_{\varphi^{\mathfrak{X}}}(Z)|\, \Delta(Z)^k \le \frac{q^k (1 + q^N)}{q^{2k} + q^N}\, S.$$

Lean: `GlobalTheory.SW.Step.bound_step`

*Proof.* Take the relation of the [Hecke lemma](/entry/hecke-swd/), take absolute values, and multiply by $\iota(\mathfrak{X})^k \Delta(Z)^k$. For the first sum, $\iota(\mathfrak{X})^k = q^{-k} \iota(\mathfrak{X}^+_i)^k$, so each term is at most $q^{-k} S$, and the first sum contributes at most $q^{2k} \cdot A \cdot q^{-k} S = q^k A S$. For the second sum, $\iota(\mathfrak{X})^k = q^k \iota(\mathfrak{X}^-_i)^k$. Since $\beta_{ij}$ is Hermitian, the translation by $\beta_{ij}$ does not change $\operatorname{Im} Z$, so $\Delta(Z + \beta_{ij}) = \Delta(Z)$ and $Z + \beta_{ij} \in \mathcal{H}_N$. Each term is at most $q^k S$, and there are $A q^N$ terms. Hence
$$(q^N - 1)(q^{2k} + q^N)\, \iota(\mathfrak{X})^k |D_{\varphi^{\mathfrak{X}}}(Z)| \Delta(Z)^k \le (q - 1) A\, q^k (1 + q^N) S.$$
Use $(q - 1)A = q^N - 1$, which is positive since $q > 1$ and $N > 0$, and divide. $\square$

### The induction

**Theorem 3.4.4 (Siegel-Weil, induction step).** Let $\Psi$ be a CM type, let $n$ be even with $4(N + 1) < n$, and assume $\mathrm{SW}(n, N)$. Then $\mathrm{SW}(n, N + 1)$ holds.

Lean: `GlobalTheory.SW.swAt_succ` (also `GlobalTheory.T.siegelWeil_formula_degree_succ`, a second name)

*Proof.* Let $\varphi$ be admissible of level $(M, R)$ and degree $N + 1$, and let $Z \in \mathcal{H}_{N+1}$. Write $n = 2k$. By the [twisted bound](/entry/twist-swd-bounded/) there is $C$ with
$$\iota(\mathfrak{X})^k |D_{\varphi^{\mathfrak{X}}}(W)| \Delta(W)^k \le C$$
for all $\mathfrak{X}$ that agree with $\mathcal{O}_E^{N+1}$ away from $RM$ and all $W$. By a result of the sources there is a good prime $(q, \mathfrak{P})$ for $RM$. (It follows from the Chebotarev density theorem: infinitely many primes split completely in $E$.) Put
$$\theta = \frac{q^k(1 + q^{N+1})}{q^{2k} + q^{N+1}}.$$
Then $0 \le \theta < 1$: we have $q^{2k} + q^{N+1} - q^k(1 + q^{N+1}) = (q^k - 1)(q^k - q^{N+1})$, and both factors are positive, since $q > 1$ and $N + 1 < k$ by $4(N+1) < 2k$.

Applying the [contraction step](/entry/bound-step/) $m$ times gives the bound $\theta^m C$ for every $m \ge 0$, uniformly in $\mathfrak{X}$ and $W$. Let $m \to \infty$. At $\mathfrak{X} = \mathcal{O}_E^{N+1}$ we have $\iota = 1$, so $|D_{\varphi^{\mathfrak{X}}}(Z)| \Delta(Z)^k \le 0$, and $\Delta(Z) > 0$ gives $D_{\varphi^{\mathfrak{X}}}(Z) = 0$. Finally, the twist by $\mathcal{O}_E^{N+1}$ agrees with $\varphi$ on all $\Lambda \in V_n(M)$, and the class sum only sees these lattices. So $D_\varphi(Z) = 0$. $\square$

**Theorem 3.4.5 (Siegel-Weil formula for definite Hermitian lattices).** Let $E$ be a CM field with a CM type $\Psi$, and let $n$ be even and $N \ge 0$ with $4N < n$. Then $\mathrm{SW}(n, N)$ holds: for all $M, R$, every admissible family $\varphi$ of level $(M, R)$ and degree $N$, and every $Z \in \mathcal{H}_N$,
$$\sum\nolimits_M \theta_{\varphi_\Lambda}(Z, 0, 0) = \sum\nolimits_M E_{\varphi_\Lambda}(Z, 0, 0).$$

Lean: `GlobalTheory.SW.siegel_weil_definite` (also `GlobalTheory.T.siegelWeil_definiteHermitian_of_four_mul_lt`, a second name)

*Proof.* Induction on $N$. For $N = 0$ the space $M_{n \times 0}(E)$ has one point, the theta series of $\varphi_\Lambda$ is $\varphi_\Lambda(0)$, the set of Lagrangians has one element, and the Weil transform at $0$ is $\varphi_\Lambda(0)$ with automorphy factor $1$. So both sides are equal. For the step, $4(N+1) < n$ implies $4N < n$, so $\mathrm{SW}(n, N)$ holds by induction, and the [induction step](/entry/sw-at-succ/) gives $\mathrm{SW}(n, N + 1)$. $\square$

**Remark 3.4.6.** The classical Siegel-Weil formula is due to Siegel for definite quadratic forms (Siegel, *Über die analytische Theorie der quadratischen Formen*, Ann. of Math. 36 (1935)) and to Weil in adelic form (Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965)). In Weil's form it says that the integral of the theta function over $U(V)(\mathbb{Q}) \backslash U(V)(\mathbb{A})$ equals the value at a fixed point of an Eisenstein series on $U(N,N)$, in the range of absolute convergence. For a definite space the integral is the weighted class sum over a genus, with weights $1/|\mathrm{Stab}|$. The statement here is the weighted class sum form at level $M$, for a CM type, with the test functions given as families over the self-dual lattices, and in the range $4N < n$. The proof by Hecke operators and a contraction argument replaces the adelic proof.

**Remark 3.4.7 (Formalization).** The Hecke relation and the existence of a good prime are results of the sources, used in [SiegelWeilFormulaDegreeSucc.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/SiegelWeilFormulaDegreeSucc.lean#L115). The base case of the induction is the identity $D_\varphi = 0$ in degree $0$, which holds by computation. The theorems with the second names are wrappers proved by `first | exact ...`.
