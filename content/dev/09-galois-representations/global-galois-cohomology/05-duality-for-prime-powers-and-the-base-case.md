---
title: Duality for prime powers and the base case
decls:
  - GroundTheory.ProfCoh.gsBaseBijective_of_le
  - GroundTheory.ProfCoh.gsBaseBijective_of_fixing
  - GroundTheory.ProfCoh.exists_compactDualityHypotheses_gs_of_pairing
  - GroundTheory.ProfCoh.exists_compactDualityHypotheses_gs
  - GroundTheory.ProfCoh.gsBaseCase
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Duality for prime powers and the base case

This section proves the base case of Poitou-Tate duality for $G_S$, at a prime power level $n = \ell^k$. The previous section proved duality between $H^r(G_S, \mathbb{Z}/n)$ and $H^{3-r}_c(G_S, \mu_n)$ when $\mu_n \subseteq K$. Here we prove the same duality for each open subgroup $U$ of $G_S$ that is small enough, without the condition on $K$. The method is to pass from $U$ to the Galois group of its fixed field $L$, where $\mu_n \subseteq L$ holds. The result is the base case of a dévissage that gives Poitou-Tate duality for every finite module, the nine-term exact sequence and the finiteness of the Tate-Shafarevich groups. The step [EveryCharacter from Row0b](/step/every-character-of-row/) depends on the base case.

We keep the setting of the previous section: $K$ is a number field in $\overline{\mathbb{Q}}$, $S$ is a finite set of finite places of $K$ with fixed embeddings $\iota_v$, $G_S = \operatorname{Gal}(K_S/K)$, and $t : H^3_c(G_S, \mu_n) \to \mathbb{Z}/n$ is the trace. The theory is in [Galois cohomology of global fields](/learn/galois-cohomology/#global-fields).

### Open subgroups

Let $U$ be an open subgroup of $G_S$, with fixed field $L$, a finite extension of $K$ inside $K_S$. Let $S_L$ be the set of places of $L$ above $S$. The field $K_S$ is also the maximal extension of $L$ unramified outside $S_L$ at the finite places. So $U = \operatorname{Gal}(K_S/L) = G_{L, S_L}$. The double cosets of $U$ and the local groups $G_v$, $v \in S$, correspond to the places of $L$ above $S$, and this identifies the compact support cohomology of $U$ relative to $S$ with $H^r_c(G_{L,S_L}, \cdot)$, by the Mackey formula.

**Definition 2.5.1 (duality at an open subgroup).** For an open subgroup $U$ of $G_S$ and $r + s = 3$, the *duality map at $U$* is
$$H^r(U, \mathbb{Z}/n) \to \operatorname{Hom}\big(H^s_c(U, \mu_n), \mathbb{Z}/n\big), \qquad x \mapsto \big(y \mapsto t(\operatorname{cor}(y \cup x))\big),$$
where $\operatorname{cor} : H^3_c(U, \mu_n) \to H^3_c(G_S, \mu_n)$ is corestriction. The trace $t$ is said to be *bijective at $U$* if this map is bijective for all $r + s = 3$.

Lean: `GroundTheory.ProfCoh.zmodCompactDualityMap` (also `GroundTheory.ProfCoh.GsBaseBijective`).

**Definition 2.5.2 (compact duality hypotheses).** Let $D$ be a discrete $G_S$-module, $T : H^3_c(G_S, D) \to \mathbb{Z}/n$ a homomorphism and $U_0$ an open subgroup of $G_S$. The *compact duality hypotheses* for $(n, D, T, U_0)$ are:

1. $D \cong \mathbb{Z}/n$ as groups;
2. $H^4_c(G_S, M) = 0$ for each finite discrete $G_S$-module $M$ killed by $n$;
3. for each open subgroup $U \leq U_0$ and each $r + s = 3$, the duality map at $U$ is bijective.

Lean: `GroundTheory.ProfCoh.CompactDualityHypotheses`.

These are the inputs of the dévissage. Condition 3 asks for duality only with the trivial coefficients $\mathbb{Z}/n$, but for all small open subgroups. Every finite module becomes trivial on a small open subgroup, and coinduction from $U$ to $G_S$ then carries duality back to $G_S$.

### Small open subgroups

**Theorem 2.5.3 (duality at the subgroup of a finite subextension).** Let $\ell$ be a prime and $n = \ell^k$, with every place of $K$ above $\ell$ in $S$. Assume that $n$ is odd or $K$ is totally complex, and that $H^3(G_S, \mu_n) = 0$. Assume that the pairing of the previous section is nondegenerate for every number field and every finite set of places containing the places above $\ell$, under the conditions there. Assume that corestriction $H^3_c(U, \mu_n) \to H^3_c(G_S, \mu_n)$ is onto for every open subgroup $U$. Let $W_0$ be an open subgroup of $G_S$ that fixes $\mu_n$. Let $L \subseteq K_S$ be a finite extension of $K$ whose subgroup $U_L = \operatorname{Gal}(K_S/L)$ lies in $W_0$. Then $t$ is bijective at $U_L$.

Lean: `GroundTheory.ProfCoh.gsBaseBijective_of_le`.

*Proof.* Since $U_L \leq W_0$, the group $U_L$ fixes $\mu_n$, so $\mu_n \subseteq L$. If $K$ is totally complex, so is $L$. So $n$ is odd or $L$ is totally complex. The places of $L$ above $\ell$ lie in $S_L$, so $H^3(G_{L,S_L}, \mu_n) = 0$. By hypothesis, the pairing of the previous section for $L$ and $S_L$ is nondegenerate. The groups $H^3(G_{L,S_L}, \mathbb{Z}/n)$ vanish, and $H^1(G_{L,S_L}, \mathbb{Z}/n)$ and $H^2_c(G_{L,S_L}, \mu_n)$ are finite. So duality holds for $L$ and $S_L$ with the trace $t_L$ of $L$, by the corollary of the previous section, and $t_L$ is bijective.

It remains to compare $t_L$ with $t \circ \operatorname{cor}$. Each local invariant at $v \in S$ is bijective, so $t$ is onto. With the hypothesis on corestriction, $t \circ \operatorname{cor}$ is onto $\mathbb{Z}/n$. Through the Mackey identification, both $t_L$ and $t \circ \operatorname{cor}$ are maps from the same group $H^3_c(G_{L,S_L}, \mu_n) \cong \mathbb{Z}/n$ onto $\mathbb{Z}/n$. So they differ by a unit of $\mathbb{Z}/n$. Duality for one trace gives duality for the other. $\square$

**Theorem 2.5.4 (duality at small open subgroups).** Under the hypotheses of the previous theorem, $t$ is bijective at each open subgroup $U \leq W_0$.

Lean: `GroundTheory.ProfCoh.gsBaseBijective_of_fixing`.

*Proof.* Let $L$ be the fixed field of $U$. It is a finite extension of $K$ inside $K_S$, and $U = \operatorname{Gal}(K_S/L)$. This is the previous theorem applied to $L$. $\square$

### The compact duality hypotheses

**Theorem 2.5.5 (compact duality hypotheses from the pairing).** Let $\ell$ be a prime and $n = \ell^k$, with every place of $K$ above $\ell$ in $S$. Assume that $n$ is odd or $K$ is totally complex, and that $H^3(G_S, \mu_n) = 0$. Assume the nondegeneracy of the pairing as in the previous theorems. Then there is an open subgroup $U_0$ of $G_S$ such that the compact duality hypotheses hold for $(n, \mu_n, t, U_0)$.

Lean: `GroundTheory.ProfCoh.exists_compactDualityHypotheses_gs_of_pairing`.

*Proof.* Every place above a prime factor of $n$ lies in $S$, so $\mu_n$ lies in $K_S$ and is cyclic of order $n$. This gives condition 1. Condition 2 holds because $H^4(G_S, M) = 0$ and $H^3(G_v, M) = 0$ for $v \in S$. The first holds since $G_S$ has $\ell$-cohomological dimension at most $2$ for each prime $\ell$ dividing $n$, when $n$ is odd or $K$ is totally complex. The second holds since the local Galois groups have cohomological dimension $2$. The extension $K(\mu_n)$ is finite and lies in $K_S$, so its subgroup $W_0$ is open and fixes $\mu_n$. Corestriction onto $H^3_c(G_S, \mu_n)$ is surjective for every open subgroup $U$. By Shapiro's lemma it is $H^3_c$ of the map from the module coinduced from $U$ onto $\mu_n$. This map is onto, and $H^3_c$ is right exact on modules killed by $n$ because $H^4_c$ vanishes on them. So the previous theorem gives condition 3 with $U_0 = W_0$. $\square$

**Theorem 2.5.6 (compact duality hypotheses at a prime power).** Let $\ell$ be a prime and $n = \ell^k$, with every place of $K$ above $\ell$ in $S$. Assume that $n$ is odd or $K$ is totally complex, and that $H^3(G_S, \mu_n) = 0$. Then there is an open subgroup $U_0$ of $G_S$ such that the compact duality hypotheses hold for $(n, \mu_n, t, U_0)$.

Lean: `GroundTheory.ProfCoh.exists_compactDualityHypotheses_gs`.

*Proof.* This is the previous theorem applied to the nondegeneracy theorem of the previous section. $\square$

### The base case

For an integer $N$ and a prime $p$, write $p^{v_p(N)}$ for the exact power of $p$ that divides $N$.

**Theorem 2.5.7 (base case of Poitou-Tate duality).** Let $N$ be a positive integer such that every place of $K$ above a prime factor of $N$ lies in $S$. Assume that $N$ is odd or that $K$ is totally complex. Then for each prime factor $p$ of $N$, with $n = p^{v_p(N)}$, there is an open subgroup $U_0$ of $G_S$ such that the compact duality hypotheses hold for $(n, \mu_n, t, U_0)$.

Lean: `GroundTheory.ProfCoh.gsBaseCase`.

*Proof.* The integer $n$ divides $N$. So the places above $p$ lie in $S$, and $n$ is odd or $K$ is totally complex. Under these conditions $H^3(G_S, \mu_n) = 0$. This is the previous theorem applied with $\ell = p$ and $k = v_p(N)$. $\square$

### Poitou-Tate duality for $G_S$

The base case feeds a dévissage over the prime factors of $N$. For a finite discrete $G_S$-module $M$ killed by $N$, write $M' = \operatorname{Hom}(M, \mu_N)$. The result is the following form of [[Galois cohomology|9MPCZ3EAJM]] duality of Poitou and Tate.

**Corollary 2.5.8 (Poitou-Tate duality for $G_S$).** Let $N$ be as in the theorem, and let $M$ be a finite discrete $G_S$-module killed by $N$. Then for $r + s = 3$ the map
$$H^r(G_S, M) \to \operatorname{Hom}\big(H^s_c(G_S, M'), \mathbb{Z}/N\big), \qquad x \mapsto \big(y \mapsto t(y \cup x)\big),$$
is bijective. The Tate-Shafarevich groups $\text{Ш}^1(G_S, M)$ and $\text{Ш}^2(G_S, M')$ are finite and dual to each other, and the nine-term sequence of Poitou and Tate
$$\begin{aligned} 0 &\to H^0(G_S, M) \to \textstyle\bigoplus_{v \in S} H^0(G_v, M) \to H^2(G_S, M')^\vee \\ &\to H^1(G_S, M) \to \textstyle\bigoplus_{v \in S} H^1(G_v, M) \to H^1(G_S, M')^\vee \\ &\to H^2(G_S, M) \to \textstyle\bigoplus_{v \in S} H^2(G_v, M) \to H^0(G_S, M')^\vee \to 0 \end{aligned}$$
is exact.

Lean: `GroundTheory.ProfCoh.poitouTate_duality_gs` (also `GroundTheory.ProfCoh.poitouTate_sha_gs`, `GroundTheory.ProfCoh.poitouTate_nineTerm_gs`).

*Proof.* The base case gives the compact duality hypotheses at each prime factor of $N$. The dévissage of the Poitou-Tate chapter turns them into duality for all $M$ killed by $N$. The nine-term sequence and the statement on $\text{Ш}$ follow from duality and the long exact sequence of compact cohomology. $\square$

**Remark 2.5.9 (Formalization).** The base case is stated for every $N$, with the condition $N \neq 0$ omitted from its hypotheses; for $N = 0$ the set of prime factors is empty and the statement is empty ([PoitouTateNineTermGs.lean](lean:GroundTheory/ProfiniteCohomology/PoitouTate/PoitouTateNineTermGs.lean#L21)). The trace at level $p^{v_p(N)}$ carries the proofs that this level is odd or $K$ totally complex and that $H^3$ vanishes, so these proofs appear inside the statement. The open subgroup $U_0$ is the subgroup that fixes $\mu_n$ ([BaseMain.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseMain.lean#L37)). The comparison of two traces that differ by a unit is in [BaseLevel.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseLevel.lean#L83).
