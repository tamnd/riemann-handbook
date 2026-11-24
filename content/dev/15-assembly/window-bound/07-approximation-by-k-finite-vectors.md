---
title: Approximation by K-finite vectors
decls:
  - CompanionTheory.D.gk.HC.sobApprox_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Approximation by K-finite vectors

This section proves that, in a unitary representation of a real [[unitary group|0R9R0Y1HDK]], each smooth vector is a limit of smooth $K$-finite vectors, in any finite set of Sobolev seminorms. The result is used where an estimate is first proved on the $K$-finite vectors, the [[Harish-Chandra module|2MKHH636C3]], and must then be extended to all smooth vectors: in the density of $K$-finite vectors for the Hecke vectors, in the central character argument of Gelfand type, and in the Casselman-Wallach inputs. All of them lie below the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). For $(\mathfrak g, K)$-modules see [admissible representations and $(\mathfrak{g}, K)$-modules](/learn/real-groups/#admissible-representations-and-mathfrakg-k-modules).

We work with matrices. Let $G \in M_n(\mathbb{C})$, and let $U(G) = \{g \in M_n(\mathbb{C}) : g^* G g = G\}$ be its unitary group. Its [[Lie algebra|5JJYBJ6A8K]] is $\mathfrak g = \{X : X^* G + G X = 0\}$, a real subspace of $M_n(\mathbb{C})$. For $X_1, \dots, X_d \in \mathfrak g$ and $t \in \mathbb{R}^d$ put
$$e(X; t) = \exp(t_1 X_1) \exp(t_2 X_2) \cdots \exp(t_d X_d).$$

**Definition 2.7.1 (Cartan involution).** A matrix $s \in M_n(\mathbb{C})$ is a *Cartan involution* for $G$ if $s^2 = 1$, $s^* G s = G$, and $G s$ is positive definite. Then $K = \{g \in U(G) : g s = s g\}$ is the associated subgroup.

Lean: `Formalism.IndefR.Datum.IsCartanInv` (also `Formalism.IndefR.Tow.SobPf.KAt`, `Formalism.QuantumDeterminants.UH`).

If $G$ is diagonal with $p$ entries $1$ and $q$ entries $-1$, then $s = G$ is a Cartan involution, and $K = U(p) \times U(q)$ is a maximal compact subgroup of $U(p, q)$. In general $K$ is compact, since on $K$ the positive definite form $Gs$ is preserved.

**Definition 2.7.2 (Smooth and $K$-finite vectors).** Let $H$ be a complex Hilbert space and $\pi$ a map from $M_n(\mathbb{C})$ to the bounded operators on $H$ that is a unitary representation of $U(G)$: $\pi(1) = 1$, $\pi(ab) = \pi(a)\pi(b)$ and $\|\pi(g)v\| = \|v\|$ for $a, b, g \in U(G)$, and $g \mapsto \pi(g)v$ is continuous on $U(G)$ for each $v$.

1. A vector $w \in H$ is *smooth* if for each $d$ and each $X_1, \dots, X_d \in \mathfrak g$ the map $t \mapsto \pi(e(X; t))w$ from $\mathbb{R}^d$ to $H$ is $C^\infty$.
2. For $X \in \mathfrak g$ and smooth $w$, let $d\pi(X)w$ be the derivative of $t \mapsto \pi(\exp(tX))w$ at $t = 0$. For a list $l = (X_1, \dots, X_m)$ in $\mathfrak g$ put $d\pi(l)w = d\pi(X_1) d\pi(X_2) \cdots d\pi(X_m) w$.
3. A vector $v$ is *$K$-finite* if it lies in a finite-dimensional subspace of $H$ that is stable under $\pi(k)$ for each $k \in K$.

Lean: `Formalism.L2.Theta.SmoothVec` (also `Formalism.IndefR.Tow.SobPf.KFinG`, `Formalism.IndefR.Tow.SobPf.IsGRep`).

The seminorms $w \mapsto \|d\pi(l)w\|$, for finite lists $l$, define the Sobolev topology on the smooth vectors; see [Sobolev norms](/learn/analysis/#sobolev-norms).

**Theorem 2.7.3 (Approximation by $K$-finite vectors).** Let $s$ be a Cartan involution for $G$, let $H$ be complete, and let $\pi$ be a unitary representation of $U(G)$ on $H$. Let $w$ be a smooth vector, let $S$ be a finite set of finite lists in $\mathfrak g$, and let $\varepsilon > 0$. Then there is a smooth $K$-finite vector $v$ with $\|d\pi(l)v - d\pi(l)w\| < \varepsilon$ for each $l \in S$.

Lean: `CompanionTheory.D.gk.HC.sobApprox_holds` (also `Formalism.IndefR.Tow.SobPf.SobApprox`).

The proof averages $w$ over $K$ against a polynomial kernel that concentrates near $1$. We first state the seven facts it uses. We identify $K$ with a compact set of matrices $k = (k_{ij})$. A *polynomial on $K$* is a polynomial in the entries $k_{ij}$ and their conjugates $\bar k_{ij}$.

**Lemma 2.7.4 (Inputs).** Let $s$ be a Cartan involution for $G$, and let $\pi$ be as in the theorem.

1. (Haar measure) There is a probability measure $\mu$ on $M_n(\mathbb{C})$, carried by $K$, invariant under left translation by $K$, and positive on each open set that meets $K$. This is the normalized [[Haar measure|VY0HXD3GC4]] of $K$.
2. (Kernel) For each neighbourhood $U$ of $1$ and each $\eta > 0$ there is a polynomial $q$ on $K$ with $\int q \, d\mu = 1$, $\int |q| \, d\mu \leq 1$ and $\int_{K \setminus U} |q| \, d\mu < \eta$.
3. (Chart) There are $Y_1, \dots, Y_d \in \mathfrak g$ such that for each $\varepsilon > 0$ there is $\delta > 0$ with: each $g \in U(G)$ whose entries are within $\delta$ of those of $1$ is $e(Y; t)$ for some $t$ with $|t_i| < \varepsilon$.
4. (Continuity) For smooth $w$ and a list $l$ in $\mathfrak g$, the map $g \mapsto d\pi(l)\pi(g)w$ is continuous at $g = 1$ on $U(G)$.
5. (Average) For smooth $w$ and continuous $p$, the vector $w_p = \int p(k)\,\pi(k)w \, d\mu(k)$ is smooth, and $d\pi(l)w_p = \int p(k)\, d\pi(l)\pi(k)w \, d\mu(k)$ for each list $l$, with an integrable integrand.
6. (Finiteness) For each polynomial $q$ on $K$ and each $w$, the vector $w_q$ is $K$-finite.
7. (Bound) For smooth $w$ and a list $l$, the norms $\|d\pi(l)\pi(k)w\|$ are bounded for $k \in K$.

Lean: `Formalism.IndefR.Tow.SobPf.haarExists_holds` (also `Formalism.IndefR.Tow.SobPf.polyKernel_holds`, `Formalism.IndefR.Tow.SobPf.sobChart_holds`, `Formalism.IndefR.Tow.SobPf.continuity_of_sobolev_chart`, `Formalism.IndefR.Tow.SobPf.avgSmooth_of`, `Formalism.IndefR.Tow.SobPf.avgKFin_holds`, `Formalism.IndefR.Tow.SobPf.foldBddK_of`).

*Proof.* We sketch each part; the formalization proves each of them.

1. The set $K$ is a compact group, since $Gs$ is positive definite and $K$ preserves it, and $\mu$ is its normalized Haar measure.
2. Put $r(k) = \sum_{i,j} |k_{ij} - \delta_{ij}|^2$, a polynomial on $K$ that vanishes only at $1$. Choose $R$ larger than $\max_K r$ and put $q = c\,(1 - r/R)^N$, with $c$ chosen so that $\int q \, d\mu = 1$. Then $q \geq 0$ on $K$, so $\int |q| \, d\mu = 1$. Let $U$ contain the set $r < \varepsilon$. Outside $U$ we have $1 - r/R \leq \beta = 1 - \varepsilon/R$, while on the set $r < \varepsilon/2$, of positive measure $m$, we have $1 - r/R \geq \alpha = 1 - \varepsilon/(2R) > \beta$. So $c^{-1} \geq \alpha^N m$, and $\int_{K \setminus U} |q| \, d\mu \leq \beta^N / (\alpha^N m)$, which is less than $\eta$ for large $N$.
3. Take $Y_1, \dots, Y_d$ a real basis of $\mathfrak g$. The map $t \mapsto e(Y; t)$ has invertible differential at $0$ onto $\mathfrak g$, so the inverse function theorem gives the chart.
4. The map $t \mapsto d\pi(l)\pi(e(Y; t))w$ is continuous, since $w$ is smooth. With the chart of part 3, this gives continuity at $1$ on $U(G)$.
5. This is differentiation under the integral sign. The integrand is continuous in $k$ on the compact set $K$, by the smoothness of $w$ and the chart of part 3, and $\mu$ is finite.
6. The vectors $w_q$, for $q$ of total degree at most $N$, span a finite-dimensional space, since they are combinations of $w_m$ for the finitely many monomials $m$ of degree at most $N$. This space is stable under $K$, since for $k_0 \in K$ the invariance of $\mu$ gives $\pi(k_0)w_q = w_{q'}$ with $q'(k) = q(k_0^{-1}k)$, and $q'$ has the same degree.
7. We have $d\pi(l)\pi(k)w = \pi(k)\,d\pi(k^{-1} l k)w$, where $k^{-1}lk$ is the list of conjugates. The map $k \mapsto d\pi(k^{-1}lk)w$ is continuous on the compact set $K$, by part 4 and the chart, so it is bounded, and $\pi(k)$ is unitary. $\square$

*Proof of the theorem.* Let $\mu$ be as in part 1. By part 4, applied to each $l \in S$, there is $\delta > 0$ such that $\|d\pi(l)\pi(g)w - d\pi(l)w\| < \varepsilon/2$ for each $l \in S$ and each $g \in U(G)$ whose entries are within $\delta$ of those of $1$. Let $U$ be this neighbourhood of $1$. By part 7 there is $B \geq 0$ with $\|d\pi(l)\pi(k)w\| \leq B$ for each $l \in S$ and $k \in K$; with $k = 1$ also $\|d\pi(l)w\| \leq B$. Put $\eta = \varepsilon / (4(B+1))$ and take the polynomial $q$ of part 2 for $U$ and $\eta$.

Put $v = w_q = \int q(k)\,\pi(k)w \, d\mu(k)$. By parts 5 and 6, $v$ is smooth and $K$-finite. Let $l \in S$. Since $\int q \, d\mu = 1$, part 5 gives
$$d\pi(l)v - d\pi(l)w = \int q(k)\,\big(d\pi(l)\pi(k)w - d\pi(l)w\big)\, d\mu(k).$$
For $k \in U$ the integrand has norm at most $|q(k)|\,\varepsilon/2$. For $k \in K \setminus U$ it has norm at most $|q(k)|\,2B$. Hence
$$\|d\pi(l)v - d\pi(l)w\| \leq \frac{\varepsilon}{2}\int |q| \, d\mu + 2B \int_{K \setminus U} |q| \, d\mu \leq \frac{\varepsilon}{2} + 2B\eta < \varepsilon,$$
since $2B\eta = \varepsilon B/(2(B+1)) < \varepsilon/2$. $\square$

This is the usual proof that $K$-finite vectors are dense in the smooth vectors [Knapp, *Lie Groups Beyond an Introduction*, Chapter IV], made quantitative for finitely many seminorms and with an explicit polynomial kernel in place of the Peter-Weyl theorem.

**Remark 2.7.5 (Formalization).** The theorem `sobApprox_holds` ([SobApproxHolds.lean](lean:Development/WeilBound/HeckeVectors/SmoothVectors/SobolevApproximation/SobApproxHolds.lean#L12)) is one line: it applies `sobApprox_of` ([ArvOSobPfAs.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/SobolevIteration/ArvOSobPfAs.lean#L69)) to the seven parts of the lemma. The statement `SobApprox` is in [ArvOSobPfSt.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/SobolevIteration/ArvOSobPfSt.lean#L110). The group $U(G)$ is `UH G`, the group $K$ is `KAt G s`, and the Lie algebra is `lieG G`. Odd points:

- The theorem lives in the namespace `CompanionTheory.D.gk.HC`, while its statement and all its parts are in `Formalism.IndefR.Tow.SobPf`.
- `sobChart_holds` and `avgKFin_holds` are each defined twice: once in an inner namespace and once as an alias ([ArvOSobPfChart.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/SobolevIteration/ArvOSobPfChart.lean#L136), [ArvOSobPfKFin.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/SobolevIteration/ArvOSobPfKFin.lean#L81)).
- `sobChart_holds` does not use its hypothesis that $s$ is a Cartan involution; the chart holds for each $G$.
- `foldBddK_of` builds part 4 again from `foldCont_holds`, although `sobApprox_holds` also passes part 4 to `sobApprox_of` directly.
- `avgSmooth_of` runs under `maxHeartbeats 2000000`.
- The representation $\pi$ is a map on all of $M_n(\mathbb{C})$; its values off $U(G)$ are not used.
