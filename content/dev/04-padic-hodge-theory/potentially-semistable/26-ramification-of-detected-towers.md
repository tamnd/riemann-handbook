---
title: Ramification of detected towers
decls:
  - GlobalTheory.T.inertia_congruenceFiltration_finite_tower_bound
  - GlobalTheory.PMon.Ram.finiteTowerBound
  - GlobalTheory.T.noDetectedSubgroupTowerRat_proof
  - GlobalTheory.PMon.Ram.noTowerQ_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ramification of detected towers

This section proves a statement about towers of open subgroups of $G_{\mathbb{Q}_\ell}$. Let $N_0 \supseteq N_1 \supseteq \cdots$ be open subgroups such that the $\ell$-th power map sends $N_k$ into $N_{k+1}$, an element of $N_0$ whose $\ell$-th power lies in $N_{j+1}$ already lies in $N_j$, and each quotient $N_k / N_{k+r}$ is detected by additive characters that are almost coboundaries on $\Omega$. Then the inertia elements of some $N_k$ lie in every $N_j$. The tower looks like the congruence filtration of an $\ell$-adic Lie group, and the result says that such a tower cannot be infinitely ramified. It is the key input of [Sen's finiteness theorem](/entry/sen-admissible-representation-finite-inertia/) in the next section, and through it of [the weight zero case](/entry/weight-zero-potentially-semistable-of-sen-theorem/) of the monodromy theorem.

The proof is by contradiction, and it reduces to a bound in a finite Galois extension $L / \mathbb{Q}_\ell$. There the tower gives a chain of subgroups of the inertia group, and the size of the chain is measured by a sum over the lower ramification groups. The measure doubles every two steps, and it stays below the ramification index. So the chain is short, and this contradicts the length of the tower.

We use the [local fields](/learn/galois-cohomology/#local-fields) background. As in section 15, $\Omega$ is the fixed algebraic closure of $\mathbb{Q}_\ell$ and $G_{\mathbb{Q}_\ell} = \mathrm{Gal}(\Omega / \mathbb{Q}_\ell)$; its norm satisfies $|\ell| = \ell^{-1}$.

### Ramification groups and jump sums

Let $L / K$ be a finite Galois extension of nonarchimedean local fields, with Galois group $G = \mathrm{Gal}(L/K)$, ring of integers $\mathcal{O}_L$ and maximal ideal $\mathfrak{m}_L$. For $i \geq 0$ the *lower ramification group* is
$$G_i = \{ \sigma \in G : \sigma(x) - x \in \mathfrak{m}_L^{i+1} \text{ for all } x \in \mathcal{O}_L \}.$$
So $G_0$ is the inertia group and $G_1$ is the wild inertia group (J.-P. Serre, *Local Fields*, Chapter IV, §1). The groups $G_i$ decrease, and $G_i = 1$ for large $i$.

**Definition 6.26.1 (Jump sum).** Let $R_t = G_{t+1}$ for $t \geq 0$. For subgroups $A, B \subseteq G$ put
$$V(A, B) = \sum_{t \geq 0,\ A \cap R_t \not\subseteq B} \# (A \cap R_t).$$

Lean: `GlobalTheory.PMon.Ram.jumpSum` (also `GlobalTheory.PMon.Ram.wild`, the groups $R_t$).

The sum is finite, since $R_t = 1$ for large $t$. It counts, with weights $\#(A \cap R_t)$, the steps $t$ of the ramification filtration at which $A$ is not yet inside $B$. If $A$ is large and deeply ramified compared to $B$, then $V(A, B)$ is large.

**Definition 6.26.2 (Ax property, detection).** Let $p$ be a prime and $E \geq 1$.

1. $L$ has *ramification index $E$ over $p$* if $v_L(p) = E$ for the normalized valuation $v_L$ of $L$.
2. $L / K$ has the *Ax property for $p$* if for every subgroup $J \subseteq G$ and every $x \in L$ with $\sigma(x) - x \in \mathcal{O}_L$ for all $\sigma \in J$, there is $y \in L$ fixed by $J$ with $p^2 (x - y) \in \mathcal{O}_L$.
3. For subgroups $A, B \subseteq G$ and $r \geq 0$, the pair $(A, B)$ is *detected modulo $p^r$* if for every $\sigma_0 \in A \setminus B$ there are $x \in L$ and $a : G \to \mathbb{Z}$ with $\sigma(x) - x \in a(\sigma) + p^r \mathcal{O}_L$ for all $\sigma \in A$, and $p^r \nmid a(\sigma_0)$.

Lean: `GlobalTheory.PMon.Ram.OrdIs` (also `GlobalTheory.PMon.Ram.AxIn`, the Ax property, and `GlobalTheory.PMon.Ram.Detects`, detection).

The Ax property is a finite form of the lemma of Ax: an element that is moved only a little by a group is close to an element fixed by it (J. Ax, *Zeros of polynomials over local fields: the Galois action*, J. Algebra 15 (1970)). In 3, the map $\sigma \mapsto a(\sigma) \bmod p^r$ is a character of $A$ that is a coboundary in $L / p^r \mathcal{O}_L$; detection says that these characters separate $A$ from $B$.

### The finite bound

We use the following facts, proved elsewhere in this development. Let $L / K$, $p$ and $E$ be as above, with ramification index $E$ over $p$, and let $A, B, C \subseteq G$ be subgroups.

1. (Commutators.) If $(A, B)$ is detected modulo $p^r$, then every commutator $\sigma \tau \sigma^{-1} \tau^{-1}$ with $\sigma, \tau \in A$ lies in $B$.
2. (Growth.) If $A \subseteq G_0$, the commutators of $A$ lie in $C$, and every $\sigma \in A$ with $\sigma^p \in C$ lies in $B$, then $\min\big(2 V(A, B),\, V(A, B) + E\big) \leq V(A, C)$.
3. (Upper bound.) If $L/K$ has the Ax property for $p$ and $(A, B)$ is detected modulo $p^r$, then $V(A, B) \leq 6E$.
4. (Triangle inequality.) If $B \subseteq A$, then $V(A, C) \leq V(A, B) + V(B, C)$.
5. (Lower bound.) If $A \subseteq G_0$, $A \not\subseteq B$, and the commutators and the $p$-th powers of elements of $A$ lie in $B$, then $\# A \leq V(A, B)$.

Fact 2 is the doubling: on a quotient where the $p$-th power map is injective, the $p$-th power multiplies the depth of ramification by $p$ or adds $E$ to it, by the classical behaviour of the ramification groups under $p$-th powers (Serre, *Local Fields*, Chapter IV, §2). Fact 3 uses the detecting elements and the Ax property to bound the depth by a multiple of $v_L(p)$.

**Lemma 6.26.3 (Doubling arithmetic).** Let $V(a, b)$ be natural numbers for $a, b \geq 0$, and let $E > 0$, $T \geq 0$ and $g \geq 0$. Assume:

1. $\min\big(2 V(k, k+j),\, V(k, k+j) + E\big) \leq V(k, k+j+1)$ for $k \leq 2T$ and $1 \leq j \leq 7$;
2. $V(k, k+8) \leq 6E$ for $k \leq 2T$;
3. $V(k, k+3) \leq V(k, k+2) + V(k+2, k+3)$ for all $k$;
4. $g \leq V(0, 1)$.

Then $2^T g < E$.

Lean: `GlobalTheory.PMon.Ram.doublingArith` (also `GlobalTheory.PMon.Ram.doublingArith_step`, the step).

*Proof.* Fix $k \leq 2T$ and write $v_j = V(k, k+j)$. By 1, $v_{j+1} \geq v_j$ for $1 \leq j \leq 7$. If $v_2 \geq E$, then $v_j \geq E$ for $j \geq 2$, so $2 v_j \geq v_j + E$ and 1 gives $v_{j+1} \geq v_j + E$ for $2 \leq j \leq 7$. Then $v_8 \geq v_2 + 6E \geq 7E > 6E$, against 2. So $v_1 \leq v_2 < E$. Now 1 at $j = 1$ and $j = 2$ gives $v_2 \geq 2 v_1$ and $v_3 \geq 2 v_2$, since the minimum is the first term. By 3,
$$V(k+2, k+3) \geq v_3 - v_2 \geq v_2 \geq 2 v_1.$$
So, for $k \leq 2T$: $V(k, k+1) < E$ and $2 V(k, k+1) \leq V(k+2, k+3)$.

By induction on $i \leq T$, $2^i g \leq V(2i, 2i+1)$: the case $i = 0$ is 4, and the step from $i$ to $i+1$ is the second inequality at $k = 2i \leq 2T$. At $i = T$ the first inequality gives $2^T g \leq V(2T, 2T+1) < E$. $\square$

**Theorem 6.26.4 (Finite tower bound).** Let $L / K$ be a finite Galois extension of nonarchimedean local fields, $p$ a prime, $E > 0$ and $T \geq 0$. Assume that $L$ has ramification index $E$ over $p$ and that $L/K$ has the Ax property for $p$. Let $G_0 \supseteq G_1 \supseteq \cdots$ be a decreasing sequence of subgroups of $\mathrm{Gal}(L/K)$ with:

1. $G_0$ is contained in the inertia group, and $G_0 \not\subseteq G_1$;
2. $\sigma^p \in G_1$ for every $\sigma \in G_0$;
3. for $j + 1 \leq 2T + 8$ and $\sigma \in G_0$, $\sigma^p \in G_{j+1}$ implies $\sigma \in G_j$;
4. $(G_k, G_{k+8})$ is detected modulo $p^8$ for every $k \leq 2T$.

Then $2^T \cdot \# G_0 < E$.

Lean: `GlobalTheory.T.inertia_congruenceFiltration_finite_tower_bound` (also `GlobalTheory.PMon.Ram.finiteTowerBound`, the proof).

To avoid a clash with the lower ramification groups, we write $\mathcal{G}_k$ for the groups of the tower in the proof.

*Proof.* Every $\mathcal{G}_k$ lies in the inertia group, since the sequence decreases. By 4 and fact 1, the commutators of $\mathcal{G}_k$ lie in $\mathcal{G}_{k+8}$ for $k \leq 2T$. The groups $R_t$ decrease and are trivial for large $t$. Put $V(a, b) = V(\mathcal{G}_a, \mathcal{G}_b)$ and $g = \# \mathcal{G}_0$. We check the hypotheses of the Lemma.

1. Let $k \leq 2T$ and $1 \leq j \leq 7$. Apply fact 2 to $A = \mathcal{G}_k$, $B = \mathcal{G}_{k+j}$, $C = \mathcal{G}_{k+j+1}$. The commutators of $A$ lie in $\mathcal{G}_{k+8} \subseteq C$, since $k + j + 1 \leq k + 8$. If $\sigma \in A$ and $\sigma^p \in C$, then $\sigma \in \mathcal{G}_0$ and $k + j + 1 \leq 2T + 8$, so 3 gives $\sigma \in B$.
2. For $k \leq 2T$, fact 3 and 4 give $V(k, k+8) \leq 6E$.
3. Fact 4 with $A = \mathcal{G}_k \supseteq B = \mathcal{G}_{k+2}$ and $C = \mathcal{G}_{k+3}$.
4. Fact 5 with $A = \mathcal{G}_0$ and $B = \mathcal{G}_1$: the commutators of $\mathcal{G}_0$ lie in $\mathcal{G}_8 \subseteq \mathcal{G}_1$, the $p$-th powers lie in $\mathcal{G}_1$ by 2, and $\mathcal{G}_0 \not\subseteq \mathcal{G}_1$ by 1. So $g \leq V(0, 1)$.

The Lemma gives $2^T g < E$. $\square$

### Towers in the absolute Galois group

**Theorem 6.26.5 (No detected towers over $\mathbb{Q}_\ell$).** Let $\ell$ be a prime and $N_0 \supseteq N_1 \supseteq \cdots$ open subgroups of $G_{\mathbb{Q}_\ell}$. Assume:

1. $\sigma^\ell \in N_{k+1}$ for every $k$ and $\sigma \in N_k$;
2. for every $j$ and $\sigma \in N_0$, $\sigma^\ell \in N_{j+1}$ implies $\sigma \in N_j$;
3. for every $r \geq 0$ there is $k_0$ such that for every $k \geq k_0$ there are finitely many $x_i \in \Omega$ and maps $a_i : G_{\mathbb{Q}_\ell} \to \mathbb{Z}$ with $|\sigma(x_i) - x_i - a_i(\sigma)| \leq \ell^{-r}$ for all $i$ and all $\sigma \in N_k$, and such that every $\sigma \in N_k$ with $\ell^r \mid a_i(\sigma)$ for all $i$ lies in $N_{k+r}$.

Then there is $k$ such that every $\sigma \in N_k$ with $|\sigma(x) - x| < 1$ for all $x \in \Omega$ with $|x| \leq 1$ lies in every $N_j$.

Lean: `GlobalTheory.T.noDetectedSubgroupTowerRat_proof` (also `GlobalTheory.PMon.Ram.noTowerQ_holds`, the proof).

The condition on $\sigma$ in the conclusion says that $\sigma$ acts trivially on the residue field of $\Omega$, so $\sigma$ is an inertia element. We use three more facts, proved elsewhere in this development.

1. (Finite level.) For an open subgroup $U$ of $G_{\mathbb{Q}_\ell}$ and a finite set $S \subseteq \Omega$, there is a finite Galois extension $L / \mathbb{Q}_\ell$ in $\Omega$ that contains $S$ and such that the kernel of the restriction $G_{\mathbb{Q}_\ell} \to \mathrm{Gal}(L/\mathbb{Q}_\ell)$ lies in $U$.
2. (Local facts on $L$.) For such $L$ with inertia group $I$: $L$ has ramification index $\# I$ over $\ell$; $L / \mathbb{Q}_\ell$ has the Ax property for $\ell$; and the restriction of an inertia element of $G_{\mathbb{Q}_\ell}$ lies in $I$.
3. (Detection descends.) Let $N, N'$ be subgroups of $G_{\mathbb{Q}_\ell}$, and let $x_i \in L$ and $a_i$ be as in 3 for $N$ and $N'$ in place of $N_k$ and $N_{k+r}$. Then the images $(\mathrm{res}(N) \cap I, \mathrm{res}(N') \cap I)$ are detected modulo $\ell^r$.

*Proof.* Suppose the conclusion fails. Take $k_0$ from 3 with $r = 8$.

Step 1: a witness. There are $k \geq k_0$ and an inertia element $\sigma_0 \in N_k \setminus N_{k+1}$. Otherwise every inertia element of $N_{k_0}$ lies in $N_{k_0 + i}$ for all $i$, by induction on $i$, and so in every $N_j$; this is the conclusion with $k = k_0$.

Step 2: the finite level. Let $T = [G_{\mathbb{Q}_\ell} : N_k]$, which is finite since $N_k$ is open. For each $i \leq 2T$, hypothesis 3 at level $k + i \geq k_0$ gives finitely many $x_{i,\cdot}$ and $a_{i,\cdot}$. By finite level, there is a finite Galois $L$ containing all these $x_{i, \cdot}$ for $i \leq 2T$, with the kernel of $\mathrm{res} : G_{\mathbb{Q}_\ell} \to \mathrm{Gal}(L/\mathbb{Q}_\ell)$ inside $N_{k + 2T + 8}$. Let $I$ be the inertia group of $L$ and $\mathcal{G}_j = \mathrm{res}(N_{k+j}) \cap I$. For $j \leq 2T + 8$, if $\mathrm{res}(\sigma) \in \mathrm{res}(N_{k+j})$, then $\sigma \in N_{k+j}$: write $\mathrm{res}(\sigma) = \mathrm{res}(\tau)$ with $\tau \in N_{k+j}$; then $\tau^{-1}\sigma$ lies in the kernel, so in $N_{k+2T+8} \subseteq N_{k+j}$.

Step 3: the finite bound applies with $p = \ell$ and $E = \# I$. The groups $\mathcal{G}_j$ decrease and lie in $I$. Hypothesis 1 of the bound: $\mathrm{res}(\sigma_0) \in \mathcal{G}_0$, and $\mathrm{res}(\sigma_0) \notin \mathcal{G}_1$, since otherwise $\sigma_0 \in N_{k+1}$ by Step 2. Hypothesis 2 follows from 1. Hypothesis 3 follows from 2 and Step 2. Hypothesis 4 is detection descends with $N = N_{k+i}$ and $N' = N_{k+i+8}$. The other assumptions are the local facts on $L$. So
$$2^T \cdot \# \mathcal{G}_0 < \# I.$$

Step 4: the contradiction. Since $\mathrm{res}$ is surjective and $[G_{\mathbb{Q}_\ell} : N_k] = T$, the subgroup $\mathrm{res}(N_k) \cap I$ has index at most $T$ in $I$, so $\# I \leq T \cdot \# \mathcal{G}_0$. Hence $2^T \# \mathcal{G}_0 < T \# \mathcal{G}_0$, which is false, since $T < 2^T$ and $\# \mathcal{G}_0 > 0$. $\square$

**Remark 6.26.6 (Formalization).** Hypothesis 3 of the theorem over $\mathbb{Q}_\ell$ is used only for $r = 8$ ([NoDetectedSubgroupTowerRatProof.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/NoDetectedSubgroupTowerRatProof.lean#L23)). The Ax property is stated with the constant $p^2$ ([NoTowerQ.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/NoTowerQ.lean#L24)). Facts 1 to 5 of the finite bound are `GlobalTheory.T.commutator_mem_of_coboundary_detects_quotient`, `GlobalTheory.T.ramificationJumpSum_pow_growth`, `GlobalTheory.T.wildJumpSum_le_of_detecting_coboundary_characters`, `GlobalTheory.T.ramificationJumpSum_le_add` and `GlobalTheory.T.card_le_wildJumpSum_of_elementaryAbelian`; we read their statements, not their proofs, and the explanations after them are only a guide. The three facts of the last theorem are `exists_galois_ker_le_range`, then `ordIs_eq_card_inertia`, `GlobalTheory.T.axLemma_finiteGalois_padic` and `restrictNormalHom_mem_lowerRamificationGroup_zero`, then `GlobalTheory.T.characters_detect_restrictNormal_inf_finiteLevel`. The jump sum is a `finsum`, which is $0$ for an infinite support; the support is finite here.
