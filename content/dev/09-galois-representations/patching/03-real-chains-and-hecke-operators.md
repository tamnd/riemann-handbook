---
title: Real chains, invariant cocycles and Hecke operators
decls:
  - PositivityTheory.KB.sAff
  - PositivityTheory.KB.sAff_of
  - PositivityTheory.KB.sHecke
  - PositivityTheory.KB.sHecke_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Real chains, invariant cocycles and Hecke operators

This section and the next two prove a bound for the rank of a part of the odd-degree homology of $\mathrm{GL}_n(\mathcal{O}_L)$, for a totally complex number field $L$. The bound feeds [Lemma K](/entry/lemma-k-lit-n-alt/) through [the statement BOdd](/entry/b-odd/). Here we set up the algebra: real bar chains, invariant cocycles on a homogeneous space, and the Hecke operator at a prime $\pi$. We prove two results. The first says that the homology of an affine group $\mathrm{GL}_n \ltimes M_{n \times r}$ over $\mathcal{O}_L$ is that of $\mathrm{GL}_n$ in low degree. The second says that an invariant cocycle whose Hecke iterates decay fast enough vanishes on all cycles. The background is in [group cohomology](/learn/galois-cohomology/#continuous-cohomology), [kinds of number fields](/learn/number-fields/#kinds-of-number-fields) and [places and completions](/learn/number-fields/#places-and-completions).

### Bar chains and evaluation

Let $G$ be a group and $m \ge 0$. A *real $m$-chain* of $G$ is a finitely supported function $G^m \to \mathbb{R}$, written $z = \sum r_g [g_1 | \dots | g_m]$. The *bar differential* $\partial$ sends $[g_1 | \dots | g_{m+1}]$ to
$$[g_2 | \dots | g_{m+1}] + \sum_{j=1}^{m} (-1)^{j} [g_1 | \dots | g_j g_{j+1} | \dots | g_{m+1}] + (-1)^{m+1} [g_1 | \dots | g_m].$$
A *cycle* is a chain $z$ with $\partial z = 0$, and a *boundary* is a chain in the image of $\partial$. A homomorphism $f \colon G \to H$ induces $f_*$ on chains, entrywise. A chain $z$ of degree $m$ is *primitive* if $\Delta_* z - (i_1)_* z - (i_2)_* z$ is a boundary in $G \times G$, where $\Delta$ is the diagonal and $i_1, i_2$ are the two inclusions.

Let $H$ act on a set $Y$ and let $\rho \colon G \to H$ be a homomorphism. A *homogeneous cochain* of degree $m$ on $Y$ is a function $F \colon Y^{m+1} \to \mathbb{R}$. Its coboundary is
$$(dF)(y_0, \dots, y_{m+1}) = \sum_{i=0}^{m+1} (-1)^i F(y_0, \dots, \widehat{y_i}, \dots, y_{m+1}).$$
$F$ is *invariant* under $\rho$ if $F(\rho(g) y_0, \dots, \rho(g) y_m) = F(y_0, \dots, y_m)$ for all $g \in G$. For a base point $y \in Y$ and a chain $z$ of degree $m$, the *evaluation* is
$$\mathrm{ev}_\rho(F, y, z) = \sum_g r_g\, F\big(y,\ \rho(g_1) y,\ \rho(g_1 g_2) y,\ \dots,\ \rho(g_1 \cdots g_m) y\big).$$
This is the classical map from the bar resolution to the homogeneous resolution, followed by evaluation of a cocycle.

We use four general facts on these complexes.

**Proposition 7.3.1 (Bar complex).** Let $G$ be a group and $k \ge 0$.

1. $\partial^2 = 0$, $f_*$ commutes with $\partial$, $(g \circ f)_* = g_* \circ f_*$, and conjugation by an element of $G$ changes a cycle by a boundary.
2. If $F$ is an invariant cocycle ($dF = 0$) of degree $k+1$, then $\mathrm{ev}_\rho(F, y, z) = 0$ for each boundary $z$, and $\mathrm{ev}_\rho(F, y, z)$ does not depend on $y$ when $z$ is a cycle.
3. If a cycle $z$ of degree $k+1$ is not a boundary, then there is a $G$-invariant cocycle $c$ on $G$ (for the left action) with $\mathrm{ev}(c, 1, z) \neq 0$.
4. There is an isomorphism $\theta$ from cycles of degree $k+1$ modulo boundaries onto $\mathbb{R} \otimes H_{k+1}(G; \mathbb{Z})$, natural in $G$.

Lean: `PositivityTheory.KB.sChain`, `PositivityTheory.KB.sEv`, `PositivityTheory.KB.sSep'`, `PositivityTheory.KB.sBridge`.

These are the standard facts that the bar complex with real coefficients computes $H_*(G; \mathbb{R})$, and that real cohomology is dual to real homology. Part 4 is the bridge from real chains to integral homology, which the rank bound in the [last section of this part](/entry/b-star-odd/) needs.

### The affine group

Let $L$ be a totally complex number field with $r_2(L)$ complex places and ring of integers $\mathcal{O}_L$. Write $\Gamma_n = \mathrm{GL}_n(\mathcal{O}_L)$ and $\iota_{n, n+r}$ for the [stabilization map](/entry/k-stability-main/).

**Theorem 7.3.2 (Affine splitting).** Let $L$ be totally complex and $k + 1 < r_2(L)$. Let $n, r \ge 0$, let $H$ be a group, and let $f \colon H \to \Gamma_{n+r}$ and $f_0 \colon H \to \Gamma_n$ be homomorphisms such that for each $x \in H$
$$f(x) = \begin{pmatrix} f_0(x) & B(x) \\ 0 & 1_r \end{pmatrix}$$
for some $B(x) \in M_{n \times r}(\mathcal{O}_L)$. Then for each real cycle $z$ of degree $k+1$ of $H$, the chain $f_* z - (\iota_{n,n+r} \circ f_0)_* z$ is a boundary in $\Gamma_{n+r}$.

Lean: `PositivityTheory.KB.sAff` (also `PositivityTheory.KB.sAff_of`, the same statement with parts 1 to 4 of the proposition as hypotheses).

*Proof.* Let $P = \Gamma_n \ltimes M$ with $M = M_{n \times r}(\mathcal{O}_L)$, where $g$ acts on $M$ by left multiplication. Let $\mathrm{pr} \colon P \to \Gamma_n$ be the projection and $s$ the section $g \mapsto (g, 0)$. The map $f$ factors through $P$, and $f_0$ is $\mathrm{pr}$ composed with this factorization. So it is enough to show that the real homology of $P$ in degree $k+1$ is carried by $s(\Gamma_n)$.

Suppose a cycle $w$ of $P$ of degree $k + 1$ differs from $s_* \mathrm{pr}_* w$ by a chain that is not a boundary. Part 3 gives an invariant cocycle $c$ that detects the difference. Replace $c$ by $c - \mathrm{pr}^* s^* c$; it still detects the difference and vanishes on $s(\Gamma_n)$. Three facts show that such a cocycle is a coboundary.

1. Units. Since $k + 1 < r_2(L)$, there is a unit $v \in \mathcal{O}_L^\times$ such that $\prod_w |v|_w^{a_w} \ne 1$ for all exponents $a_w \ge 0$ with $1 \le \sum_w a_w \le k + 1$. This uses the Dirichlet unit theorem: the logarithmic embedding of the units is a lattice of rank $r_2 - 1$, and a generic unit avoids finitely many hyperplanes.
2. Cohomology of the lattice $M$. Real invariant cocycles on the free abelian group $M$ of finite rank are, up to coboundaries, sums of cup products of homomorphisms $M \to \mathbb{R}$. The scalar $v$ is central in $\Gamma_n$ and acts on $M$ by multiplication. Its action on cup products of degree $q + 1 \le k + 1$ satisfies a real polynomial $f$ with $f(1) \neq 0$, since the eigenvalues are the products in item 1.
3. The central element kills. For a split extension $P \to \Gamma_n$ with a central $u = v \cdot 1_n$ that satisfies such a polynomial condition on the cohomology of the kernel, an invariant cocycle of degree at most $k + 1$ that vanishes on the section is a coboundary. This is the classical argument that a central element acts trivially on group cohomology, applied to the columns of the Hochschild-Serre filtration.

The evaluation of a coboundary on a cycle is $0$. This contradicts the choice of $c$. $\square$

### Hecke operators

Let $\Gamma$ be a group, $\rho \colon \Gamma \to K$ a homomorphism and $q \in K$. Put
$$\Gamma_q = \rho^{-1}\big(q^{-1} \rho(\Gamma) q\big).$$
Assume that $\Gamma_q$ has finite index in $\Gamma$. Let $K$ act on a set $Y$ through $\tau \colon K \to H$. The *Hecke operator* on functions $f$ on $Y$ is
$$(T_q f)(y) = \frac{1}{[\Gamma : \Gamma_q]} \sum_{\Gamma_q c \in \Gamma_q \backslash \Gamma} f\big(\tau(q \rho(c))\, y\big).$$
It acts on cochains in each variable. On $\rho$-invariant cochains it is linear, it preserves invariance and it commutes with $d$.

We apply this with $\Gamma = \Gamma_N$, $\rho$ the inclusion into $\mathrm{GL}_N(L)$, and, for a prime element $\pi$ of $\mathcal{O}_L$,
$$q_\pi = \mathrm{diag}(\pi, 1, \dots, 1) \in \mathrm{GL}_N(L).$$
Then $\Gamma_{q_\pi}$ is a congruence subgroup of level $\pi$ and of finite index. This is the Hecke operator $T_\pi$ of the classical theory, normalized to be an average.

**Theorem 7.3.3 (Hecke vanishing).** Let $L$ be totally complex, $k + 1 < r_2(L)$, and $\pi$ a prime element of $\mathcal{O}_L$. There is $N_0$ such that for all $N \ge N_0$ the following holds. Let $F$ be a real cochain of degree $k + 1$ on $\mathrm{GL}_N(L)$, invariant under $\Gamma_N$, with $dF = 0$. Suppose that for each cycle $z$ of degree $k + 1$ of $\Gamma_N$ there is $C$ with
$$\big|\mathrm{ev}(T_{q_\pi}^r F, 1, z)\big| \le C \left(\tfrac{3}{5}\right)^r \quad \text{for all } r \ge 0.$$
Then $\mathrm{ev}(F, 1, z) = 0$ for every cycle $z$ of degree $k + 1$ of $\Gamma_N$.

Lean: `PositivityTheory.KB.sHecke` (also `PositivityTheory.KB.sHecke_of`, the same statement with the bar complex facts, stability for Dedekind rings, finiteness and affine splitting as hypotheses).

*Proof.* Put $n = 2(k + 1) + 4$ and $N = n + r$ with $r \ge 1$.

Key identity. Let $\epsilon_N = [\Gamma_n : \Gamma_{n, q_\pi}] / [\Gamma_N : \Gamma_{N, q_\pi}]$. For a cycle $z$ of $\Gamma_n$ and an invariant cocycle $F$ on $\mathrm{GL}_N(L)$,
$$\mathrm{ev}\big(T_{q_\pi} F, 1, \iota_* z\big) = (1 - \epsilon_N)\, \mathrm{ev}(F, 1, \iota_* z) + \epsilon_N\, \mathrm{ev}\big(T^{(n)}_{q_\pi} (F \circ \iota), 1, z\big),$$
where $\iota = \iota_{n,N}$ and $T^{(n)}$ is the Hecke operator at level $n$. To prove it, let $\Gamma_n$ act through $\iota$ on the finite set $X = \Gamma_{N, q_\pi} \backslash \Gamma_N$ by right multiplication. Two facts on matrices sort the cosets. First, $\iota(c) \in \Gamma_{N, q_\pi}$ if and only if $c \in \Gamma_{n, q_\pi}$, and $\iota(q_\pi) = q_\pi$, so the cosets of the form $\Gamma_{N, q_\pi} \iota(c)$ are the cosets at level $n$; they give the term with $T^{(n)}$. Second, a coset $\Gamma_{N,q_\pi} c$ is of this form when every entry of $c^{-1}$ in the first column and in the rows $n + 1, \dots, N$ lies in $(\pi)$. For the other cosets, the stabilizer in $\Gamma_n$ maps into $\Gamma_N$ by block matrices of the form in the affine splitting theorem, and that theorem (here $k + 1 < r_2$ is used) shows that on cycles of the stabilizer the term of the coset evaluates like $F$ itself. A transfer lemma finishes the proof: if $\Gamma$ acts on a finite set $X$ and $(\Phi_x)_{x \in X}$ is an equivariant family of cocycles such that each $\Phi_x$ vanishes on the cycles of the stabilizer of $x$, then $\sum_x \Phi_x$ vanishes on the cycles of $\Gamma$.

Reduction to level $n$. By stability for $\Gamma_N$ over the Dedekind ring $\mathcal{O}_L$ (as in the [stability theorem](/entry/k-stability-main/)), every cycle of $\Gamma_N$ is homologous to $\iota_* z$ for a cycle $z$ of $\Gamma_n$. By finiteness, there is a finite set $s$ of cycles of $\Gamma_n$ that spans all cycles modulo boundaries. Let $a_r \in \mathbb{R}^s$ be the vector of evaluations of $T^r F$ on $\iota_* s$, and $b_r$ the vector of evaluations of $T^{(n)}(T^r F \circ \iota)$ on $s$. The key identity reads
$$a_{r+1} = (1 - \epsilon_N)\, a_r + \epsilon_N\, b_r.$$
The operator $T^{(n)}$ maps cocycles that vanish on all cycles to cocycles of the same kind. So it induces a linear map on the finite-dimensional space of evaluation vectors, and $\|b_r\| \le M \|a_r\|$ for a constant $M$ that depends only on $n$ and $\pi$.

Decay. The index $[\Gamma_N : \Gamma_{N, q_\pi}]$ grows at least like $N$, so $\epsilon_N \to 0$. Choose $N_0$ with $\epsilon_N (M + 1) \le 1/5$ for $N \ge N_0$. Then $\|a_{r+1}\| \ge (1 - \epsilon_N (M+1)) \|a_r\| \ge \tfrac{4}{5} \|a_r\|$, so $\|a_r\| \ge (4/5)^r \|a_0\|$. With the hypothesis $\|a_r\| \le C (3/5)^r$ this forces $a_0 = 0$. So $F$ vanishes on $\iota_* s$, hence on all cycles. $\square$

**Remark 7.3.4.** The constant $3/5$ is the spectral gap of the [next section](/entry/s-gap-of/). The argument is a contraction argument: at large $N$ the Hecke operator is close to the identity on the homology that comes from $\Gamma_n$, so it cannot contract it at rate $3/5$.

**Remark 7.3.5 (Formalization).** In [SAffOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/AffineSplittingSpan/SAffOf.lean#L11) the hypotheses `SEv` and `SBridge` of `sAff_of` are not used; their names start with `_`. In [SHeckeOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/HeckeDoubleCosets/SHeckeOf.lean#L9) all six hypothesis names start with `_`, but five of them are passed on; only `SSep` is unused. The three facts in the proof of affine splitting are the statements `Unit`, `Span`, `Eigen`, `Transfer` and `Core` of the folder `AffineSplittingSpan`; the key identity is the statement `PKey`, and the decay step is `PDecay`. We give their content from their statements and have not unfolded all of their proofs; in particular the coset split in the key identity follows the statements `PTransfer`, `PStabK`, `PGqStab`, `PLow` and `PStabVan` of [PHeckeFormal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/HeckeDoubleCosets/PHeckeFormal.lean#L41), and we have not checked the exact cochains $\Phi_x$ used there.
