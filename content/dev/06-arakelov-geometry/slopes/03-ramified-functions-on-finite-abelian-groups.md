---
title: Ramified functions on finite abelian groups
decls:
  - Formalism.L2.Col.T2.range_kron_szVec
  - Formalism.L2.Col.T2.det_szGram
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.induced_lattice_map_sz
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_ramified_induced
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_ramified_induced_prime_field
  - Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.induced_of_slice
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ramified functions on finite abelian groups

Let $G = \prod_{i \in I} G_i$ be a finite product of finite abelian groups. A function on $G$ is *ramified* if its sum along every coordinate fibre vanishes. This section proves that, inside a lattice induced from a lattice $L_W$ over $G$, the ramified sublattice is a Kronecker image of $L_W^S$ for an explicit set $S$ and an explicit integer matrix, and computes its slope with the theorem on Kronecker images of Section 2. For $G_i = \mathbb{F}_q^\times$ the slope drops by $|I| \log(q-1)/(q-2)$. Section 5 applies this to the action of the diamond operators at a level prime $T$, with $q = T$. At the end of the section we show how an induced lattice arises from a group action with an orthogonal slice.

### Ramified functions

Throughout, $I$ is a finite set, $G_i$ for $i \in I$ are finite abelian groups written multiplicatively, and $G = \prod_i G_i$. For $i \in I$ and $a \in G_i$ let $e_i(a) \in G$ be the element with $i$-th coordinate $a$ and all other coordinates $1$. Let $M$ be a vector space over a field $K$.

**Definition 1.3.1 (Ramified functions).** For $h \in G$ the *translation* $\tau_h$ acts on functions $F : G \to M$ by $(\tau_h F)(c) = F(hc)$. For $i \in I$ the *norm in the direction $i$* is $N_i = \sum_{a \in G_i} \tau_{e_i(a)}$. A function $F$ is *ramified* if $N_i F = 0$ for all $i \in I$, that is, if
$$
\sum_{a \in G_i} F(e_i(a)\, c) = 0 \qquad \text{for all } i \in I \text{ and } c \in G .
$$
We write $\operatorname{Ram}(G, M)$ for the subspace of ramified functions.

For a single group $G_1$ and $M = K$, the ramified functions are the functions with sum zero, that is, the complement of the constants. If $K$ contains the values of the characters of $G$, then $\operatorname{Ram}(G, K)$ is spanned by the characters $\chi = \prod_i \chi_i$ with every $\chi_i$ nontrivial. This explains the name: these are the characters that are ramified in every direction. It also gives the dimension $\prod_i (|G_i| - 1)$, which the next lemmas prove without characters.

**Definition 1.3.2 (Basic ramified functions).** Let $S = \prod_i (G_i \setminus \{1\})$. For $b \in S$ and $a \in G$ put
$$
s_{b, a} = \prod_{i \in I} \big( [a_i = b_i] - [a_i = 1] \big),
$$
where $[\,P\,]$ is $1$ if $P$ holds and $0$ otherwise. This defines an integer matrix $s \in M_{S \times G}(\mathbb{Z})$. For each $i$ let $E_i$ be the $(|G_i| - 1) \times (|G_i| - 1)$ matrix $1 + J$, where $J$ has all entries $1$, and let $E = \bigotimes_i E_i$, the matrix on $S$ with entries $E_{bc} = \prod_i (E_i)_{b_i c_i}$.

The row $s_b$ is the product over $i$ of the functions $\delta_{b_i} - \delta_1$ on $G_i$, each of which has sum zero. So each row is a ramified function with integer values.

**Lemma 1.3.3 (Gram matrix of the basic ramified functions).** We have $s\, s^{\mathsf{T}} = E$ and
$$
\det E = \prod_{k \in I} |G_k|^{\,\prod_{j \neq k} (|G_j| - 1)} > 0 .
$$
If $q \geq 3$ and $|G_i| = q - 1$ for all $i$, then $\log \det E / |S| = |I| \log(q-1)/(q-2)$.

Lean: `Formalism.L2.Col.T2.det_szGram` (also `Formalism.L2.Col.T2.szVec_mul_transpose`, `Formalism.L2.Col.T2.log_det_szGram_div`).

*Proof.* The sum $\sum_{a \in G} s_{b,a} s_{c,a}$ factors over $i$ into $\prod_i \sum_{x \in G_i} ([x = b_i] - [x = 1])([x = c_i] - [x = 1])$. Since $b_i, c_i \neq 1$, the $i$-th factor is $[b_i = c_i] + 1$, which is $(E_i)_{b_i c_i}$. By the matrix determinant lemma $\det(1 + J) = 1 + (|G_i| - 1) = |G_i|$. The determinant of a Kronecker product of square matrices $A_k$ of sizes $n_k$ is $\prod_k (\det A_k)^{\prod_{j \neq k} n_j}$, which gives the formula for $\det E$. If all $|G_i| = q - 1$, then $|S| = (q-2)^{|I|}$ and $\log\det E = |I| (q-2)^{|I|-1} \log(q-1)$. $\square$

**Lemma 1.3.4 (Basis of the ramified functions).** Let $M$ be finite dimensional. The map $s_* : M^S \to M^G$, $(s_* F)(a) = \sum_{b \in S} s_{b,a} F_b$, is injective with image $\operatorname{Ram}(G, M)$.

Lean: `Formalism.L2.Col.T2.range_kron_szVec` (also `Formalism.L2.Col.T2.kron_szVec_injective`, `Formalism.L2.Col.T2.kron_szVec_mem`, `Formalism.L2.Col.RamFun.finrank_ramFun`).

*Proof.* Each row $s_b$ is ramified, so the image lies in $\operatorname{Ram}(G, M)$. For $a \in S$ we have $s_{b,a} = [a = b]$, since no coordinate of $a$ is $1$. So $(s_* F)(a) = F_a$ for $a \in S$, and $s_*$ is injective. For the image, let $F$ be ramified and $F' = F - s_*(F|_S)$. Then $F'$ is ramified and vanishes on $S$. We show by induction on the number $k$ of coordinates of $a$ equal to $1$ that $F'(a) = 0$. For $k = 0$ this is the vanishing on $S$. If $a_i = 1$, the relation $N_i F' = 0$ at $a$ gives $F'(a) = -\sum_{x \neq 1} F'(a')$, where $a'$ is $a$ with the $i$-th coordinate replaced by $x$, and each $a'$ has $k - 1$ coordinates equal to $1$. $\square$

In particular $\dim \operatorname{Ram}(G, M) = \dim M \cdot \prod_i (|G_i| - 1)$.

### The slope of the ramified sublattice

Let $K$ be a totally complex number field. An *induced datum* over $G$ is a hermitian lattice datum $B = (V, b, X, L)$ with invertible frames together with a good datum $W = (V_W, b_W, X_W, L_W)$, $L_W \neq 0$, and an injective $K$-linear map $\Psi : V_W^G \to V$ such that $\langle \Psi F, \Psi F' \rangle_v = \sum_{a \in G} \langle F_a, F'_a \rangle_v$ for all $v$ and $L = \Psi(L_W^G)$. In words, $B$ is an orthogonal sum of $|G|$ copies of $W$ indexed by $G$. The *ramified subspace* of $B$ is $U = \Psi(\operatorname{Ram}(G, V_W))$, and the *ramified sublattice* is $L \cap U$.

**Proposition 1.3.5 (The ramified sublattice is a Kronecker image).** For an induced datum over $G$ with ramified subspace $U$,
$$
L \cap U = \Psi\big(s_*(L_W^S)\big).
$$

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.induced_lattice_map_sz`

*Proof.* If $F \in L_W^S$, then $s_* F$ has values that are integer combinations of values of $F$, so $s_* F \in L_W^G$ and $\Psi s_* F \in L$. It lies in $U$ by the lemma on the basis of ramified functions. Conversely let $x \in L \cap U$. Then $x = \Psi F_0$ with $F_0 \in L_W^G$, and also $x = \Psi F_1$ with $F_1$ ramified. Since $\Psi$ is injective, $F_0 = F_1$ is ramified, so $F_0 = s_* F$ for some $F$ by the same lemma, and $F = F_0|_S$ has values in $L_W$. $\square$

**Theorem 1.3.6 (Slope of the ramified sublattice).** Assume $|G_i| > 1$ for all $i$. For an induced datum over $G$ with ramified subspace $U$,
$$
\mu(B[L \cap U]) = \mu(B) - \frac{\log \det E}{|S|} .
$$

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_ramified_induced`

*Proof.* The set $S$ is nonempty because every $G_i$ has an element different from $1$. The map $\Psi \circ s_*$ is injective by the lemma on the basis of ramified functions, and by the lemma on the Gram matrix of an integer change of variables in Section 2 and the lemma on the Gram matrix of the basic ramified functions, its Gram matrix is $s\,s^{\mathsf{T}} = E$, with $\det E > 0$. The theorem on Kronecker images of Section 2 gives $\mu(B[\Psi s_*(L_W^S)]) = \mu(W) - \log\det E/|S|$. By the proposition the lattice on the left is $L \cap U$, and by the corollary on isometric sums $\mu(W) = \mu(B)$. $\square$

**Corollary 1.3.7 (The prime field case).** Let $q \geq 3$ and $|G_i| = q - 1$ for all $i$. For an induced datum over $G$ with ramified subspace $U$,
$$
\mu(B[L \cap U]) = \mu(B) - |I|\, \frac{\log(q-1)}{q-2} .
$$

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.slope_ramified_induced_prime_field`

*Proof.* This is the theorem together with the value of $\log\det E/|S|$ in the lemma on the Gram matrix of the basic ramified functions. $\square$

**Example 1.3.8.** Let $I$ have one element and $G_1 = \mathbb{F}_q^\times$ with $q \geq 3$. Then $B$ is an orthogonal sum of $q - 1$ copies of $W$, and $L \cap U$ is the lattice of $F : G_1 \to L_W$ with $\sum_a F(a) = 0$. Its slope is $\mu(B) - \log(q-1)/(q-2)$. For $q = 3$ this is the antidiagonal of the example in Section 2, with the drop $\log 2$.

### Induced data from an orthogonal slice

In the application the lattice is not given as an induced datum. It carries an action of $G$, and we find a subspace, the slice, whose translates are orthogonal and fill the space.

For a hermitian lattice datum $B = (V, b, X, L)$, a group homomorphism $\rho : G \to \operatorname{End}_K(V)$, and a subspace $W \subseteq V$, put
$$
\Psi_W : W^G \to V, \quad \Psi_W(F) = \sum_{g \in G} \rho(g) F(g), \qquad N_i^\rho = \sum_{a \in G_i} \rho(e_i(a)).
$$

**Theorem 1.3.9 (Induced data from an orthogonal slice).** Let $K$ be totally complex, $B$ a good datum with $L \neq 0$, $\rho : G \to \operatorname{End}_K(V)$ a homomorphism and $W \subseteq V$ a $K$-subspace. Assume:

1. the map $\Psi_W$ is bijective;
2. $\langle \rho(g) x, \rho(h) y \rangle_v = [g = h]\, \langle x, y \rangle_v$ for all $v$, $g, h \in G$ and $x, y \in W$;
3. for $F \in W^G$, $\Psi_W(F) \in L$ if and only if $F(g) \in L$ for every $g \in G$.

Then there are a good datum $W'$ with nonzero lattice and an injective $K$-linear map $\Psi : V_{W'}^G \to V$ that make $B$ an induced datum over $G$, and such that $\bigcap_i \ker N_i^\rho = \Psi(\operatorname{Ram}(G, V_{W'}))$.

Lean: `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.induced_of_slice` (also `Formalism.L2.GlobalTheoryTheory.LocalLatticeBases.S0.norm_slice_map_sum`).

*Proof.* Let $W'$ be the datum with space $W$, lattice $L \cap W$, and the restriction of the majorants of $B$ to $W$, written in a basis of $W$ with invertible frames; and let $\Psi = \Psi_W$. By condition 2 and sesquilinearity, $\langle \Psi F, \Psi F' \rangle_v = \sum_g \langle F(g), F'(g) \rangle_v$. By condition 3 and the surjectivity of $\Psi_W$, $L = \Psi((L \cap W)^G)$. The lattice $L \cap W$ is finitely generated, as a submodule of $L$ over the noetherian ring $\mathcal{O}_K$. It spans $W$: the projection $\pi : V \to W$, $\Psi_W(F) \mapsto F(1)$, maps $L$ into $L \cap W$ by condition 3, and it maps a $K$-spanning set of $V$ onto one of $W$. It is nonzero, since otherwise condition 3 would force $L = 0$. For the last claim, a change of the summation variable gives
$$
N_i^\rho \Psi_W(F) = \Psi_W\Big(h \mapsto \sum_{a \in G_i} F\big(e_i(a)^{-1} h\big)\Big).
$$
Since $\Psi_W$ is injective, $\Psi_W(F) \in \ker N_i^\rho$ if and only if $\sum_a F(e_i(a)^{-1}h) = 0$ for all $h$. Replacing $a$ by $a^{-1}$, this is the condition $N_i F = 0$. $\square$

With the corollary on the prime field case, an orthogonal slice for an action of $\prod_i \mathbb{F}_q^\times$ gives the slope of $L \cap \bigcap_i \ker N_i^\rho$. Section 4 constructs such a slice for the level-zero lattice.

**Remark 1.3.10 (Formalization).** The restricted datum $W'$ is built by a general construction that writes a hermitian form in a chosen basis through a frame. We used only its two properties: invertible frames, and majorants equal to the restricted ones. The slope results here assume $K$ totally complex because the Kronecker image theorem does.
