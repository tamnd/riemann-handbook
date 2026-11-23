---
title: Herbrand quotients and the first inequality
decls:
  - GroundTheory.Global.IdeleGroup.cycHerbrand_sIdeles
  - GroundTheory.Global.IdeleGroup.cycHerbrand_ideleClassGroup
  - GroundTheory.Global.index_range_ideleClassNorm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Herbrand quotients and the first inequality

This section proves the first inequality of global [[class field theory|AA943HVK6Z]] for a cyclic extension of [[number field|MWBDFS2KJ5]]s. The [[idele class group|9GHD9MXNYV]] $C_L$ of a cyclic extension $L/K$ has Herbrand quotient $[L:K]$. So the norm subgroup of $C_K$ has index $[L:K]$ times the order of a finite Tate group, and in particular the index is at least $[L:K]$. The computation goes in two steps. First we compute the Herbrand quotient of the $S$-ideles, place by place. Then we pass to $C_L$ through the $S$-units. The step [EveryCharacter from the Galois row](/step/every-character/) depends on the index formula, through the reciprocity law of the next section.

Throughout, $L/K$ is a Galois extension of number fields with group $G = \operatorname{Gal}(L/K)$. We use the language of [adeles and ideles](/learn/number-fields/#adeles-and-ideles) and of [places and completions](/learn/number-fields/#places-and-completions).

### Tate groups of a cyclic group

Let $G$ act on an abelian group $A$, written additively, and let $\sigma \in G$. Write $N = \sum_{g \in G} g$ for the norm map of $A$.

**Definition 2.1.1 (Tate groups and Herbrand quotient).** The Tate groups of $A$ with respect to $\sigma$ are
$$\hat H^0(A) = \ker(\sigma - 1)/\operatorname{im} N, \qquad \hat H^{-1}(A) = \ker N/\operatorname{im}(\sigma - 1).$$
We say that $A$ *has a Herbrand quotient* if both groups are finite. Then the *Herbrand quotient* of $A$ is the rational number
$$h(A) = \frac{\# \hat H^0(A)}{\# \hat H^{-1}(A)}.$$

Lean: `GroundTheory.Global.cycHerbrand` (also `GroundTheory.GroupCoh.HasHerbrandQuotient`).

If $\sigma$ generates $G$, then $\ker(\sigma - 1) = A^G$, and these are the usual Tate cohomology groups of the cyclic group $G$ in degrees $0$ and $-1$. Two facts carry the whole computation. If $0 \to A \to B \to C \to 0$ is an exact sequence of $G$-modules and two of the three have a Herbrand quotient, then so does the third, and $h(B) = h(A)\, h(C)$. If $A$ is finite, then $h(A) = 1$. Both facts follow from the hexagon of Tate groups of a cyclic group ([Galois cohomology](/learn/galois-cohomology/#continuous-cohomology)).

### The $S$-ideles

For a set $S$ of finite places of $K$, write $S_L$ for the set of finite places of $L$ above $S$. The group of *$S_L$-ideles* $I_{L,S}$ is the subgroup of the idele group $I_L$ of ideles $x$ with $\operatorname{ord}_w(x_w) = 0$ for each finite place $w$ of $L$ outside $S_L$. The archimedean components are free. The group $G$ acts on $I_{L,S}$, since $G$ permutes the places above each place of $K$.

**Theorem 2.1.2 (Herbrand quotient of the $S$-ideles).** Let $L/K$ be a Galois extension of number fields and let $\sigma$ generate $G$. Let $S$ be a finite set of finite places of $K$ such that every finite [[place|BT5V3TSNY6]] of $L$ above a place outside $S$ is unramified over $K$. For each infinite place $v$ of $K$ choose a place $w_v$ of $L$ above $v$, and for each finite place $v$ of $K$ choose a place $w_v$ of $L$ above $v$. Then $I_{L,S}$ has a Herbrand quotient, and
$$h(I_{L,S}) = \prod_{v \mid \infty} [L_{w_v} : K_v] \cdot \prod_{v \in S} [L_{w_v} : K_v].$$

Lean: `GroundTheory.Global.IdeleGroup.cycHerbrand_sIdeles`.

*Proof.* Since $S$ is finite, $I_{L,S}$ is isomorphic, as a $G$-module, to the product
$$\prod_{v \mid \infty} \Big(\prod_{w \mid v} L_w^\times\Big) \times \prod_{v \in S} \Big(\prod_{w \mid v} L_w^\times\Big) \times \prod_{v \notin S,\ v \nmid \infty} \Big(\prod_{w \mid v} \mathcal{O}_{L_w}^\times\Big).$$
Each factor is a $G$-module. We compute the Herbrand quotient of each factor and multiply.

Fix a place $v$ of $K$ and a place $w$ of $L$ above it, with decomposition group $G_w$ ([[decomposition group|7X92G8CQ33]]). The module $\prod_{w' \mid v} L_{w'}^\times$ is induced from the $G_w$-module $L_w^\times$. By Shapiro's lemma its Tate groups are those of $G_w$ acting on $L_w^\times$. The extension $L_w/K_v$ is cyclic of degree $[L_w : K_v]$. For a cyclic extension of local fields, the Herbrand quotient of $L_w^\times$ is the local degree. At a finite place, this follows from $\hat H^0 = K_v^\times/N L_w^\times$, of order $[L_w:K_v]$ by local class field theory, and $\hat H^{-1} = 0$ by Hilbert 90. At an infinite place it is a direct computation with $\mathbb{R}^\times$ and $\mathbb{C}^\times$.

Now let $v$ be a finite place outside $S$. Every place $w$ above $v$ is unramified. For an unramified extension of local fields, the norm maps the units onto the units, and every unit of norm $1$ has the form $u^{\sigma - 1}$. So both Tate groups of $\mathcal{O}_{L_w}^\times$ are zero, and so are those of the induced module $\prod_{w \mid v} \mathcal{O}_{L_w}^\times$.

The product over the places outside $S$ is infinite, but its Tate groups are the products of the Tate groups of the factors, since $N$ and $\sigma - 1$ act factor by factor. So that product has trivial Tate groups. The two remaining products are finite, and the Herbrand quotient is multiplicative over finite products. This gives the formula. $\square$

### The idele class group

The idele class group is $C_L = I_L/L^\times$, with $L^\times$ embedded on the diagonal. The group $G$ acts on $C_L$.

**Theorem 2.1.3 (Herbrand quotient of the idele class group).** Let $L/K$ be a Galois extension of number fields and let $\sigma$ generate $G$. Then $C_L$ has a Herbrand quotient, and $h(C_L) = [L : K]$.

Lean: `GroundTheory.Global.IdeleGroup.cycHerbrand_ideleClassGroup`.

*Proof.* Choose a finite set $S$ of finite places of $K$ with two properties. Every place of $L$ above a finite place outside $S$ is unramified over $K$. And $I_L = L^\times \cdot I_{L,S}$, that is, the classes of the places in $S_L$ generate the class group of $L$ ([ideals and the class group](/learn/number-fields/#ideals-and-the-class-group)). Such an $S$ exists because only finitely many places ramify and the class group is finite. Write $T = S_L$.

Then $C_L = I_{L,S}/E_{L,T}$, where $E_{L,T} = L^\times \cap I_{L,S}$ is the group of $T$-units of $L$. This gives an exact sequence of $G$-modules
$$1 \to E_{L,T} \to I_{L,S} \to C_L \to 1.$$
The Herbrand quotient of the $T$-units is known from the Dirichlet unit theorem:
$$h(E_{L,T}) = \frac{1}{[L:K]} \prod_{v \in S} e_v f_v \cdot \prod_{v \mid \infty} [L_{w_v} : K_v],$$
where $e_v f_v = [L_{w_v} : K_v]$ is the local degree at $v \in S$. The local degree at an infinite place is $1$ if $v$ does not ramify in $L$ and $2$ if it does. Both $E_{L,T}$ and $I_{L,S}$ have a Herbrand quotient, so $C_L$ has one, and
$$h(C_L) = \frac{h(I_{L,S})}{h(E_{L,T})}.$$
By the previous theorem the numerator is the product of the local degrees at the infinite places and at $S$. The local factors cancel, and $h(C_L) = [L:K]$. $\square$

### The first inequality

The norm $N_{L/K} : I_L \to I_K$ maps $L^\times$ into $K^\times$. So it induces a homomorphism $N_{L/K} : C_L \to C_K$, the norm of idele classes.

**Theorem 2.1.4 (first inequality).** Let $L/K$ be a Galois extension of number fields and let $\sigma$ generate $G$. Then the index of $N_{L/K}(C_L)$ in $C_K$ is
$$[C_K : N_{L/K} C_L] = [L : K] \cdot \# \hat H^{-1}(C_L),$$
and $\hat H^{-1}(C_L)$ is finite.

Lean: `GroundTheory.Global.index_range_ideleClassNorm`.

*Proof.* By the previous theorem, both Tate groups of $C_L$ are finite and $\# \hat H^0(C_L) = [L:K] \cdot \# \hat H^{-1}(C_L)$. The fixed classes are $C_L^G = C_K$, because $H^1(G, L^\times) = 0$ by Hilbert 90. So the map $C_K \to \hat H^0(C_L) = C_L^G/N C_L$ is surjective. Its kernel is $N_{L/K} C_L$, since on $C_L$ the norm of the group $G$ is the norm of idele classes. So $[C_K : N_{L/K} C_L] = \# \hat H^0(C_L)$. $\square$

**Corollary 2.1.5 (first inequality, index form).** Let $L/K$ be a cyclic extension of number fields. Then the index of $N_{L/K} C_L$ in $C_K$ is finite, and $[L:K] \leq [C_K : N_{L/K} C_L]$.

Lean: `GroundTheory.Global.finrank_le_index_range_ideleClassNorm` (also `GroundTheory.Global.firstInequality`).

*Proof.* Choose a generator $\sigma$ of $G$ and apply the theorem. The group $\hat H^{-1}(C_L)$ is finite, so its order is at least $1$. $\square$

The second inequality, $[C_K : N_{L/K} C_L] \leq [L:K]$, then forces $\hat H^{-1}(C_L) = 0$. The reciprocity law of the next section uses both facts.

**Remark 2.1.6 (Formalization).** The Tate groups are defined for any element $\sigma$ of $G$, as quotients of kernels by images ([CycTate.lean](lean:GroundTheory/GlobalFields/HerbrandQuotients/CycTate.lean#L174)). The statements assume that $\sigma$ generates $G$, so they are the cyclic Tate groups. The index is the index of a subgroup, which is $0$ for an infinite index. So the finiteness of the index is the second conjunct of [FirstInequality.lean](lean:GroundTheory/GlobalFields/FirstInequality.lean#L78), which says only that the order of $\hat H^{-1}(C_L)$ is not $0$. The $S$-ideles are cut out by the order condition at each finite place outside $S_L$ ([SIdeleGroups.lean](lean:GroundTheory/GlobalFields/IdeleGroups/SIdeleGroups.lean#L15)).
