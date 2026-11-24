---
title: Nefness of root models on the fibres
decls:
  - GlobalTheory.CompanionTheory.Ar.Conj.hodge_cpt_global_nefness
  - GlobalTheory.T.hodge_cpt_global_nef_bound
  - GlobalTheory.CompanionTheory.Ar.Conj.m2Model_holds
  - GlobalTheory.T.rootLineDeRhamModel_holds
  - GlobalTheory.CompanionTheory.Ar.Conj.CurveDegreeNonneg.m2Curve_holds
  - GlobalTheory.T.curveSemiAbelianConjecture
  - GlobalTheory.CompanionTheory.Ar.Conj.m2Model_of_m2Curve
  - GlobalTheory.T.rootLineDeRhamModel_of_curveSemiAbelian
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Nefness of root models on the fibres

This section proves that the line of a root model with weight $\mu$ is nef on the fibre at an odd prime $p$, when $\mu$ is dominant and its gap at $j$ is large compared with its size. The proof goes down to curves. A curve in the fibre at $p$ is the image of a curve $C$ over a field of characteristic $p$. On $C$ the Lie algebra of a semi-abelian scheme with complex multiplication gives two flags of eigen-subbundles, and the degree of the line on the curve is a sum of the degrees of the graded pieces of these flags. A slope bound for these flags shows that this sum is not negative. The result is used in [the good tower theorem](/entry/good-tower-and-volume/) for the nefness of the lines of the tower on the fibres.

### Weights, thresholds and curves

Let $\Psi$ be a finite set and $N \ge 1$. A weight of type $(\Psi, N)$ is a function $\mu \colon \Psi \times \{0, \dots, N - 1\} \to \mathbb{R}$. We put $\mu(\tau, i) = 0$ for $i \ge N$, and $\|\mu\| = \max_{\tau, i} |\mu(\tau, i)|$.

**Definition 8.10.1 (Dominant weight, nef threshold).** A weight $\mu$ is dominant if $\mu(\tau, b) \le \mu(\tau, a)$ for all $\tau$ and $a \le b$. For $j \ge 1$ the gap of $\mu$ at $j$ is $\mathrm{gap}_j(\mu, \tau) = \mu(\tau, j - 1) - \mu(\tau, j)$. For a real number $b$, the weight $\mu$ satisfies the nef threshold at $(j, b)$ if
$$
4\,|\Psi|\,\|\mu\| \le (b - 2)\,\mathrm{gap}_j(\mu, \tau) \quad \text{for every } \tau \in \Psi.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Top.Dominant`, `GlobalTheory.CompanionTheory.Ar.Top.NefThreshold`.

A root model $M$ of type $(\Psi, N)$ has a multigraded polynomial ring with an ideal $P$, lines indexed by its blocks, and for each weight $\mu$ and real $s$ a coefficient for each line. We do not unfold these. A curve of $M$ at a prime $p$ is a multihomogeneous prime ideal $W \supseteq P$ of characteristic $p$ whose quotient has Krull dimension $1 + |K|$, where $K$ is the set of blocks. The degree of $\mu$ on $W$ is the sum over the lines of the coefficient of the line at $(\mu, 0)$ times the geometric degree of the line on $W$. The model $M$ is nef at $p$ for $\mu$ if this degree is $\ge 0$ for every curve of $M$ at $p$.

**Definition 8.10.2 (De Rham tie).** Let $M$ be a root model of type $(\Psi, N)$, let $1 \le j < N$, let $p$ be a prime, and let $E$ be a CM field with host $H$. A de Rham tie of $M$ at $(j, p)$ consists of these data.

1. A scheme $X$, a point $\xi \colon \operatorname{Spec} \Omega \to X$ over the field $\Omega$ of $M$, and a tie of $\xi$ to the Segre coordinates of $M$.
2. A semi-abelian scheme $G$ over $X$ with an action of $\mathcal{O}_E$, power functions, and power-free fibres at the points of the fibre at $p$.
3. A Lie model $V$ of $G$ at $\xi$ with the action $r$ of $\mathcal{O}_E$.
4. Injective embeddings $\sigma \colon \Psi \sqcup \Psi \to \operatorname{Hom}(\mathcal{O}_E, \Omega)$ with $2|\Psi| = [E : \mathbb{Q}]$ and $\sigma(\bar\tau)(a) = \sigma(\tau)(\bar a)$, whose values are regular at the points of the fibre at $p$. The prime $p$ does not divide $d_E$.
5. For each $\tau$, bases of length $j$ and $N - j$ of the eigenspaces of $\sigma(\tau)$ and $\sigma(\bar\tau)$ in $V$. The eigen-lattices are flags of vector bundles on the fibre at $p$ with these bases. The graded piece of index $i < j$ of the first flag has the degree of the coordinate line $x(\tau, i)$ of $M$. The graded piece of index $N - 1 - i$ of the second flag, for $i \ge j$, has the degree of $-x(\tau, i)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Conj.DRTie`.

The tie says that the coordinate lines of $M$ on the fibre at $p$ are the graded pieces of the Hodge flag of $G$ split by the CM types. We take the notions of a Lie model, of power functions and of degrees of lattices on curves as given, and we do not unfold them.

### The bound on curves

**Definition 8.10.3 (Gap condition).** Let $T$ be a finite set, let $p$ be a prime and let $j, q \ge 1$. A function $\mu \colon T \times \mathbb{N} \to \mathbb{R}$ satisfies the gap condition at $(p, j, q)$ if $\mu(\tau, i + 1) \le \mu(\tau, i)$ for $1 \le i < j + q$, and there are $M_0, g \in \mathbb{R}$ such that $|\mu(\tau, i)| \le M_0$ for $1 \le i \le j + q$, $g \le \mu(\tau, j) - \mu(\tau, j + 1)$ for every $\tau$, and $4|T|M_0 \le (p - 2)\,g$.

Lean: `GlobalTheory.CompanionTheory.Ar.Crv.GapCond`.

For two families of real numbers $d_W(\tau, i)$ and $d_L(\tau, i)$ put
$$
\begin{aligned}
\Lambda(\mu; d_W, d_L) = -\sum_{\tau \in T} \Big( &\sum_{i=0}^{j-1} \mu(\tau, i+1)\big(d_W(\tau, i+1) - d_W(\tau, i)\big) \\
&+ \sum_{m=0}^{q-1} \mu(\tau, j+m+1)\big(d_L(\tau, q-m-1) - d_L(\tau, q-m)\big) \Big).
\end{aligned}
$$
This is the degree of the line of weight $\mu$ on a curve, written through the jumps of the degrees of the two flags.

**Theorem 8.10.4 (Curve degree bound).** Let $E$ be a CM field with host $H$, let $X_0$ be a scheme and let $G$ be a semi-abelian scheme over $X_0$ with an action of $\mathcal{O}_E$ and power functions. Let $k \subset K$ be fields, with $K$ of characteristic $p > 2$. Let $C$ be a curve over $K$ with at least one place, such that every constant from $k$ has valuation $\le 1$ at every place. Let $z \colon \operatorname{Spec} K \to X_0$ be a point and $Y$ a curve in $X_0$ through $z$ for $C$, such that $G$ has power-free fibres at the centres of the places. Let $V$ be a finite-dimensional $K$-vector space with a Lie model of $G$ at $z$ and a compatible action $r$ of $\mathcal{O}_E$. Let $T$ be a finite set and $\chi \colon T \sqcup T \to \operatorname{Hom}(\mathcal{O}_E, k)$ a split family with $\chi(\bar\tau)(a) = \chi(\tau)(\bar a)$. Let $j, q \ge 1$, let $\mu \colon T \times \mathbb{N} \to \mathbb{R}$ satisfy the gap condition at $(p, j, q)$, and let $W(\tau, i)$ and $L(\tau, i)$ be subspaces of $V$ with $W(\tau, 0) = L(\tau, 0) = 0$, $W(\tau, j)$ the eigenspace of $\chi(\tau)$ and $L(\tau, q)$ the eigenspace of $\chi(\bar\tau)$. Let $d_W(\tau, i)$ and $d_L(\tau, i)$ be the degrees on $C$ of the subbundles of the Lie lattice cut out by $W(\tau, i)$ and $L(\tau, i)$. Then
$$
\Lambda(\mu; d_W, d_L) \ge 0.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Conj.CurveDegreeNonneg.m2Curve_holds` (also `GlobalTheory.T.curveSemiAbelianConjecture`, a second name).

*Proof.* First we replace the Lie model by matrices. There are an integer $d$, a conjugation datum over $C$ with lattices $\mathcal{L}_i \subset K^d$ at the places, and a linear isomorphism $e \colon V \to K^d$ that maps the Lie lattice at each place onto $\mathcal{L}_i$ and the action $r$ to the matrices $\rho(a)$ of the datum. Second, the slope bound for eigen-flags of a conjugation datum, applied to the flags $e(W(\tau, i))$ and $e(L(\tau, i))$, gives $\Lambda \ge 0$ for the degrees of these flags. The hypotheses of the slope bound hold: $p > 2$, $\chi$ is split, the constants have valuation $\le 1$, the flags start at $0$ and end at the eigenspaces, since $e$ maps the eigenspaces of $r$ to the eigenspaces of $\rho$, and the gap condition holds. Third, $e$ preserves the degrees of the subbundles, since it maps the Lie lattice onto $\mathcal{L}$. So the degrees of $e(W(\tau, i))$ and $e(L(\tau, i))$ are $d_W(\tau, i)$ and $d_L(\tau, i)$. $\square$

### From curves to root models

**Theorem 8.10.5 (Root line nefness from the curve bound).** Assume the curve degree bound. Let $\Psi$ be finite, $N \ge 1$, $M$ a root model of type $(\Psi, N)$, $j$ and $p$ integers, and $E$ a CM field with host $H$. Assume a de Rham tie of $M$ at $(j, p)$, that $p$ is a prime with $p > 2$, and that $1 \le j < N$. Then $M$ is nef at $p$ for every dominant weight $\mu$ that satisfies the nef threshold at $(j, p)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Conj.m2Model_of_m2Curve` (also `GlobalTheory.T.rootLineDeRhamModel_of_curveSemiAbelian`, a second name).

*Proof.* Let $W$ be a curve of $M$ at $p$. There is a field $K$ of characteristic $p$ with a point $w$ of the coordinates of $M$ that is birational onto $W$, and a curve $C$ over $\mathbb{F}_p$ with function field $K$ and at least one place. The tie of $\xi$ to the coordinates gives a point $z$ of $X$ over $K$ and a curve through $z$ for $C$. The valuations of $C$ give a homomorphism from the local ring of $X$ at the centre of $z$ to $K$. Since $p \nmid d_E$, the embeddings $\sigma$ reduce to a split family $\chi$ of characters with values in the algebraic closure $k$ of $\mathbb{F}_p$ in $K$, with $\chi(\bar\tau)(a) = \chi(\tau)(\bar a)$. The constants in $k$ have valuation $\le 1$. The group $G$ has a Lie model at $z$, finite-dimensional over $K$, with a unique compatible action of $\mathcal{O}_E$. For each $\tau$, the two flags of the tie restrict to flags of the Lie model at $z$ that start at $0$ and end at the eigenspaces of $\chi(\tau)$ and $\chi(\bar\tau)$. The geometric degree of a coordinate line on $W$ is its degree on $C$ through $w$. By the degree formula for lattices on curves and the uniqueness of degrees, the jumps of the degrees of the two flags on $C$ are the degrees $x(\tau, i)$ of the coordinate lines on $W$ for $i < j$, and $-x(\tau, i)$ for $i \ge j$. The nef threshold for the dominant weight $\mu$ at $(j, p)$ gives the gap condition for the weights made from $\mu$ at $(p, j, N - j)$, and it identifies the degree of $\mu$ on $W$, which is $\sum_r -\mu(r)\,x(r)$, with $\Lambda$. The curve degree bound gives $\Lambda \ge 0$. $\square$

**Corollary 8.10.6 (Root line nefness).** The conclusion of the last theorem holds without the assumption: for every root model $M$ with a de Rham tie at $(j, p)$, with $p > 2$ prime and $1 \le j < N$, $M$ is nef at $p$ for every dominant weight with the nef threshold at $(j, p)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Conj.m2Model_holds` (also `GlobalTheory.T.rootLineDeRhamModel_holds`, a second name).

*Proof.* This is [Theorem 8.10.5](/entry/m2-model-of-m2-curve/) applied to [the curve degree bound](/entry/m2-curve-holds/). $\square$

### Nefness of Hodge components

**Theorem 8.10.7 (Nefness at odd primes).** Let $E$ be a CM field with host $H$, let $D$ be a datum with $p_D, q_D \ge 1$ and $N = p_D + q_D$, and for each level $l$ let $X_o(l)$ be a moduli space. For each prime $\ell$ and each valuation subring $W \subset \mathbb{C}$ in which $\ell$ is not a unit, let $Y_{\ell, W}$ be a family of local systems over the $X_o(l)$ with split fibres and the condition N3. Let $l$ be a level that is good at every prime, $c$ a coefficient datum and $Y$ a model of $X_o(l)$ that is dominated by $Y_{\ell, W}$ along every ring map from $\mathcal{O}_F$ to the valuation ring of $c$ at $W$ that restricts to the identity on $F$. Let $S$ be a finite set, $M$ a root model of type $(\Phi, N)$, $\mathfrak{M}$ a Hodge component of $Y$ over $S$ on the coordinates of $M$, and $\mathrm{Fl}$ a flag of $\mathfrak{M}$ whose root lines have the degrees of $M$. Let $\ell > 2$ be a prime with $\ell \notin S$ and $\ell \nmid d_E$. Then $M$ is nef at $\ell$ for every dominant weight $\mu$ with the nef threshold at $(p_D, \ell)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Conj.hodge_cpt_global_nefness` (also `GlobalTheory.T.hodge_cpt_global_nef_bound`, a second name).

*Proof.* The local systems dominate $Y$, so the global model has power-free fibres at $\ell$. Since $\ell \notin S$ and $\ell \nmid d_E$, the root lines of $\mathrm{Fl}$ are unramified at $\ell$, and this gives a de Rham tie of $M$ at $(p_D, \ell)$. We have $1 \le p_D < N$ since $q_D \ge 1$. Apply [Corollary 8.10.6](/entry/m2-model-holds/) with $j = p_D$. $\square$

**Remark 8.10.8 (Formalization).** The statement called `CurveSemiAbelianConjecture` is proved, by `m2Curve_holds` (M2CurveEstablished.lean:60); the name says conjecture. The statement `RootLineDeRhamModel` is defined in SeparableFormGroupElementFixesUniquePositiveLine.lean:10, a file whose name does not describe it. Nefness is used only with the shift $s = 0$. The steps go through named results such as `T.curve_lie_eigen_degree`, `T.eigen_flag_slope_bound`, `T.function_field_degree_eq`, `T.nef_threshold_gap_condition`, `T.global_model_power_free` and `T.root_lines_unramified_primes`, which we do not unfold. We also do not unfold the condition `N3` on the local systems.
