---
title: Equidistribution of lattice points
decls:
  - GlobalTheory.CompanionTheory.Equi.equi
  - GlobalTheory.T.equidistribution
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Equidistribution of lattice points

Let $F$ be a totally real number field. A vector $x \in F^\iota$ is a point of the adeles at every place at once. If we shrink it by a small real factor $\varepsilon$ at the archimedean places and impose congruence conditions at finitely many finite places, the points become equidistributed: the archimedean images fill $\mathbb{A}_\infty^\iota$ with density $\varepsilon^{-[F:\mathbb{Q}]|\iota|}$, and the local conditions cut out the expected proportion. This section proves this form of the Riemann sum. It is the analytic input of the mean value of theta series in the [next section](/entry/lside/), and it is used in the step [EveryCharacter](/step/every-character/).

**Notation.** Let $d = [F : \mathbb{Q}]$. Let $\mathbb{A}_\infty = F \otimes_{\mathbb{Q}} \mathbb{R} \cong \mathbb{R}^d$ be the archimedean part of the adeles, and $F_v$ the completion at a finite place $v$, with ring of integers $\mathcal{O}_v$ and norm $N(v)$. For an ideal $I$ of $\mathcal{O}_F$, $N(I)$ is its absolute norm.

**Definition 3.5.1 (Standard measures).** A Haar measure $\lambda_\infty$ on $\mathbb{A}_\infty$ is standard if some fundamental domain of the lattice $\mathcal{O}_F \subset \mathbb{A}_\infty$ has measure $1$. A Haar measure $\lambda_v$ on $F_v$ is standard if $\lambda_v(\mathcal{O}_v) = 1$. On $\mathbb{A}_\infty^\iota$ and $F_v^\iota$ we use the product measures.

With these normalizations, $\mathcal{O}_F^\iota$ has covolume $1$ in $\mathbb{A}_\infty^\iota$, and a coset of $I^\iota$ has covolume $N(I)^{|\iota|}$. Also $\lambda_v(\mathfrak{p}_v^k \mathcal{O}_v) = N(v)^{-k}$. So the limit in the theorem below is what one expects from counting points in boxes.

**Theorem 3.5.2 (Equidistribution).** Let $F$ be a totally real number field and $\theta : \mathbb{R} \to \mathbb{A}_\infty$ a continuous ring homomorphism. Let $\lambda_\infty$ and $(\lambda_v)_v$ be standard measures. Let $\iota$ be a finite set and $S$ a finite set of finite places. Let $\phi : \mathbb{A}_\infty^\iota \to \mathbb{R}$ be continuous with compact support, and for $v \in S$ let $\psi_v : F_v^\iota \to \mathbb{R}$ be continuous with compact support. Then, as $\varepsilon \to 0^+$,
$$\varepsilon^{d|\iota|} \sum_{x} \phi\bigl(\theta(\varepsilon)\, x\bigr) \prod_{v \in S} \psi_v(x) \longrightarrow \int_{\mathbb{A}_\infty^\iota} \phi \, d\lambda_\infty \cdot \prod_{v \in S} \int_{F_v^\iota} \psi_v \, d\lambda_v,$$
where $x$ runs over the vectors in $F^\iota$ with $x_i \in \mathcal{O}_v$ for all $i$ and all finite $v \notin S$.

Lean: `GlobalTheory.CompanionTheory.Equi.equi` (also `GlobalTheory.T.equidistribution`, a second name).

A continuous ring homomorphism from $\mathbb{R}$ to $\mathbb{A}_\infty \cong \mathbb{R}^d$ is the diagonal embedding, so $\theta(\varepsilon) x = \varepsilon x$. The sum is over the $S$-integral vectors, and the functions $\psi_v$ confine $x$ to a compact set at each $v \in S$. So the sum is finite for each $\varepsilon > 0$.

The proof is an induction on $S$. To make it work, we prove a stronger statement for congruence cosets.

**Definition 3.5.3 (Congruence coset).** Let $I$ be a nonzero ideal of $\mathcal{O}_F$ and $x_0 \in F^\iota$. The coset $\mathcal{C}_S(I, x_0)$ is the set of $x \in F^\iota$ with $x_i - x_{0,i} \in I \mathcal{O}_v$ for all $i$ and all finite $v \notin S$.

For $S = \emptyset$ this is the lattice coset $x_0 + I^\iota$. For $I = \mathcal{O}_F$ and $x_0 = 0$ it is the set of $S$-integral vectors of the theorem.

**Lemma 3.5.4 (Statement for cosets).** Let $F$, $\theta$, $\lambda_\infty$, $\lambda_v$, $\iota$ and $S$ be as in the theorem. Let $I$ be a nonzero ideal with $I \not\subseteq \mathfrak{p}_v$ for $v \in S$, and let $x_0 \in F^\iota$. Let $\phi$ and $\psi_v$ ($v \in S$) be as in the theorem. Then the sum below converges absolutely for each $\varepsilon > 0$, and
$$\varepsilon^{d|\iota|} \sum_{x \in \mathcal{C}_S(I, x_0)} \phi(\varepsilon x) \prod_{v \in S} \psi_v(x) \longrightarrow N(I)^{-|\iota|} \int \phi \, d\lambda_\infty \cdot \prod_{v \in S} \int \psi_v \, d\lambda_v.$$

The lemma is proved by induction on $S$ inside the proof of the theorem. It uses three facts, taken as given.

- (Riemann sums for a lattice coset.) For $S = \emptyset$ the lemma holds. This is the Riemann sum for the lattice $I^\iota \subset \mathbb{A}_\infty^\iota$, of covolume $N(I)^{|\iota|}$, shifted by $x_0$ and scaled by $\varepsilon$.
- (Approximation by boxes.) Let $\psi$ on $F_v^\iota$ be continuous with compact support. There is $B \ge 0$ such that for each $\delta > 0$ there are $k$ and a finite set $C$ of centres with
$$\Bigl| \psi(y) - \sum_{c \in C} \psi(c)\, \mathbf{1}_{c + \mathfrak{p}_v^k}(y) \Bigr| \le \delta \sum_{c \in C} \mathbf{1}_{c + \mathfrak{p}_v^k}(y),$$
with $|C| N(v)^{-k|\iota|} \le B$, and with the integral of $\psi$ within $\delta B$ of $\sum_c \psi(c) N(v)^{-k|\iota|}$. Here $\mathbf{1}_{c + \mathfrak{p}_v^k}$ is the indicator of the box of radius $N(v)^{-k}$ around $c$. This is uniform continuity of $\psi$.
- (Refinement of congruences.) If $v \notin S$ and $I \not\subseteq \mathfrak{p}_v$, then for each $k$, $x_0$ and box centre $c$ there is $x_1$ with
$$\{ x \in \mathcal{C}_{S \cup \{v\}}(I, x_0) : x \in c + \mathfrak{p}_v^k \} = \mathcal{C}_S(I \mathfrak{p}_v^k, x_1).$$
This is the Chinese remainder theorem.

*Proof.* We prove the lemma by induction on $S$. The case $S = \emptyset$ is the Riemann sum for a lattice coset.

Let $v \notin S$ and assume the lemma for $S$. Let $I$ be prime to $S \cup \{v\}$. Fix $\delta > 0$ and approximate $\psi_v$ by boxes, with $k$ and $C$. For each centre $c$, refinement of congruences turns the sum over $x \in \mathcal{C}_{S \cup \{v\}}(I, x_0)$ with $x \in c + \mathfrak{p}_v^k$ into a sum over $\mathcal{C}_S(I \mathfrak{p}_v^k, x_1)$. The ideal $I\mathfrak{p}_v^k$ is prime to $S$, so the induction hypothesis applies to it. Each of these sums, times $\varepsilon^{d|\iota|}$, tends to
$$N(I)^{-|\iota|} N(v)^{-k|\iota|} \int \phi \cdot \prod_{w \in S} \int \psi_w.$$
Summing over $c \in C$ with weights $\psi_v(c)$, the approximating sum tends to $N(I)^{-|\iota|} \int\phi \cdot \prod_{w\in S}\int\psi_w \cdot \sum_c \psi_v(c) N(v)^{-k|\iota|}$, which is within a constant times $\delta B$ of the claimed limit. The error between the true sum and the approximating sum is at most $\delta$ times the same sum with $|\phi|$ and $|\psi_w|$ in place of $\phi$ and $\psi_w$, and with $\psi_v$ replaced by $\sum_c \mathbf{1}_{c + \mathfrak{p}_v^k}$. By the induction hypothesis this majorant stays bounded, by a constant times $B$, as $\varepsilon \to 0$. It also gives absolute convergence for each $\varepsilon$. Since $\delta$ is arbitrary, a squeeze argument gives the limit. This proves the lemma for $S \cup \{v\}$.

The theorem is the lemma with $I = \mathcal{O}_F$ and $x_0 = 0$: the condition $I \not\subseteq \mathfrak{p}_v$ holds for every $v$, $N(\mathcal{O}_F) = 1$, and $\mathcal{C}_S(\mathcal{O}_F, 0)$ is the set of $S$-integral vectors. $\square$

**Example 3.5.5.** Take $F = \mathbb{Q}$, $\iota$ a point, $S = \{p\}$, $\phi = \mathbf{1}_{[0,1]}$ smoothed slightly, and $\psi_p = \mathbf{1}_{\mathbb{Z}_p^\times}$. The sum counts the rationals $x$ with denominator a power of $p$, $0 \le \varepsilon x \le 1$ and $x \in \mathbb{Z}_p^\times$, so integers prime to $p$ up to $1/\varepsilon$. The theorem gives $\varepsilon \cdot \#\{1 \le m \le 1/\varepsilon : p \nmid m\} \to 1 - 1/p$.

**Remark 3.5.6 (Formalization).** The parameter $\theta$ is a continuous ring homomorphism $\mathbb{R} \to \mathbb{A}_\infty$, not the diagonal map itself; as noted above, it can only be the diagonal map. The test functions are real valued. The three facts used are the statements `GlobalTheory.T.lattice_coset_scaled_riemann_sum` (with `coset_empty_places_lattice`), `locally_constant_box_approximation` and `coset_congruence_refinement`; the last step uses `coset_unit_ideal_integral`. See [Equidistribution.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/Equidistribution.lean#L244).
