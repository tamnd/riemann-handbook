---
title: Vanishing of compact cohomology in high degrees
decls:
  - GroundTheory.ProfCoh.sUnitsRealPrimaryEquiv
  - GroundTheory.ProfCoh.eq_zero_unitsTateCohomology_of_two_pow_nsmul
  - GroundTheory.ProfCoh.gsTateCompactCohomology_rootsOfUnity_two_eq_zero
  - GroundTheory.ProfCoh.gsTateCompactCohomology_zmodRep_two_eq_zero
  - GroundTheory.ProfCoh.gsMackeyTop_gsOpenSubgroup
  - GroundTheory.ProfCoh.gsTateCompactCohomology_coind_zmodRep_two_eq_zero
  - GroundTheory.ProfCoh.gsTateCompactCohomology_eq_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Vanishing of compact cohomology in high degrees

This section proves that the compact support cohomology of $G_S$, with the real places included, is zero in each degree $r \geq 4$. The coefficients are a finite module $M$ killed by an integer $n$, and $S$ contains the places above $n$. The difficulty is the prime $2$. If $K$ has a real place, then $G_S$ has elements of order $2$, and its $2$-cohomology does not stop in degree $2$. The real places carry this cohomology, and the compact support groups remove it. The proof goes through the $S$-units, the Kummer sequence for $\mu_2$, coinduced modules and a dévissage. The next section uses the result to show that restriction to the real places is bijective in degrees $r \geq 3$. That fact gives Poitou-Tate duality for a field with real places, which the step [EveryCharacter from Row0b](/step/every-character-of-row/) uses.

### Compact cohomology with real places

Let $K$ be a [[number field|MWBDFS2KJ5]] in $\overline{\mathbb{Q}}$ and $S$ a finite set of finite places of $K$. Let $K_S$ be the maximal extension of $K$ that is unramified at the finite places outside $S$; the real places may ramify. Let $G_S = \operatorname{Gal}(K_S/K)$, a [[profinite group|KA0YDB6QXE]]. For $v \in S$ fix an embedding of $\overline{\mathbb{Q}}$ into $\overline{K}_v$ over $K$, and for each real place $v$ fix an embedding into $\mathbb{C} = \overline{K}_v$. These embeddings give homomorphisms $G_v \to G_S$ from the local Galois groups. For a real place, $G_v = \operatorname{Gal}(\mathbb{C}/\mathbb{R})$ has order $2$. Write $S_\mathbb{R}$ for the set of real places.

**Definition 2.6.1 (compact cohomology with real places).** Let $M$ be a discrete $G_S$-module. Let $C^\bullet(G_S, M)$ be its complex of continuous cochains. The *compact support cohomology* $H^r_c(G_S, M)$ is the cohomology of the cone of the map
$$C^\bullet(G_S, M) \oplus \prod_{v \in S_\mathbb{R}} M[0] \longrightarrow \prod_{v \in S} C^\bullet(G_v, M) \times \prod_{v \in S_\mathbb{R}} C^\bullet(G_v, M),$$
given by restriction on the first summand and by the norm of $G_v$ on the degree $0$ term $M[0]$. The definition also applies with local coefficient modules $M_v$ and maps $M \to M_v$ in place of $M$ at the places.

Lean: `GroundTheory.ProfCoh.gsTateCompactCohomology` (also `GroundTheory.ProfCoh.tateCompactCohomology`).

The norm term changes only degrees $0$ and $1$. So for $r \geq 2$ there is a long exact sequence
$$\cdots \to H^{r-1}(G_S, M) \to \bigoplus_{v \in S \cup S_\mathbb{R}} H^{r-1}(G_v, M) \to H^r_c(G_S, M) \to H^r(G_S, M) \to \bigoplus_{v \in S \cup S_\mathbb{R}} H^r(G_v, M) \to \cdots.$$
Two local facts control it. At a finite place $v$, the group $G_v$ has cohomological dimension $2$, so $H^j(G_v, M) = 0$ for $j \geq 3$ and torsion $M$. Also $H^j(G_v, \overline{K}_v^\times) = 0$ for $j \geq 3$. At a real place, $H^j(G_v, M)$ is killed by $2$ for $j \geq 1$. Also $H^j(G_v, \mathbb{C}^\times)$ is $0$ for odd $j$ and $\mathbb{Z}/2$ for even $j \geq 2$. Background is in [Galois cohomology of local fields](/learn/galois-cohomology/#local-fields) and of [global fields](/learn/galois-cohomology/#global-fields).

**Lemma 2.6.2 (vanishing criterion).** Let $M$ be killed by $n \neq 0$ and let $r \geq 2$. Assume that restriction $H^{r+1}(G_S, M) \to \prod_{v \in S_\mathbb{R}} H^{r+1}(G_v, M)$ is surjective and that restriction $H^{r+2}(G_S, M) \to \prod_{v \in S_\mathbb{R}} H^{r+2}(G_v, M)$ is injective. Then $H^{r+2}_c(G_S, M) = 0$.

Lean: `GroundTheory.ProfCoh.eq_zero_gsTateCompactCohomology_of_gsRealRes`.

*Proof.* The local groups at $v \in S$ are zero in degrees $r + 1$ and $r + 2$, both at least $3$. So in the long exact sequence the map into $H^{r+2}_c$ comes from the real places only and is zero by surjectivity, and the map out of $H^{r+2}_c$ is injective by injectivity. $\square$

### The $2$-primary cohomology of the $S$-units

Let $E_S$ be the group of $S$-units of $K_S$: the elements of $K_S^\times$ that are units at each finite place outside $S$. It is a discrete $G_S$-module.

**Theorem 2.6.3 (real places carry the $2$-primary cohomology of the $S$-units).** Assume that $S$ contains the places above $2$. Let $r \geq 4$. Then inflation to $H^r(G_K, \overline{\mathbb{Q}}^\times)$ followed by restriction to the real places is an isomorphism
$$H^r(G_S, E_S)(2) \xrightarrow{\ \sim\ } \prod_{v \in S_\mathbb{R}} H^r(G_v, \mathbb{C}^\times),$$
where $A(2)$ is the $2$-primary part of $A$.

Lean: `GroundTheory.ProfCoh.sUnitsRealPrimaryEquiv` (also `GroundTheory.ProfCoh.gsUnitsRealPrimaryEquiv`).

*Proof.* There are three steps.

First, restriction $H^r(G_K, \overline{\mathbb{Q}}^\times) \to \prod_{v \in S_\mathbb{R}} H^r(G_v, \mathbb{C}^\times)$ is bijective for $r \geq 4$. The map from $\overline{\mathbb{Q}}^\times$ to the ideles of $\overline{\mathbb{Q}}$ is an isomorphism on $H^r$ for $r \geq 4$, because the cohomology of the [[idele class group|9GHD9MXNYV]] is zero in degrees $3$ and higher. The cohomology of the ideles is the direct sum of the local groups $H^r(G_v, \overline{K}_v^\times)$. For $r \geq 3$ the finite and complex places contribute zero, so only the real places remain.

Second, inflation $H^r(G_S, E_S) \to H^r(G_K, \overline{\mathbb{Q}}^\times)$ is an isomorphism up to odd numbers. Its kernel is killed by odd integers, and each element of the target times some odd integer is in the image. This holds because $2$ is a unit in the ring of $S$-integers, as $S$ contains the places above $2$.

Third, the target of the first step is killed by $2$, so $H^r(G_K, \overline{\mathbb{Q}}^\times)$ is its own $2$-primary part. The groups are torsion, and a map that is an isomorphism up to odd numbers restricts to a bijection on $2$-primary parts. Compose the two steps. $\square$

### Vanishing for the $S$-units

Apply the compact cohomology to $E_S$, with the local modules $\overline{K}_v^\times$ at $v \in S$ and $\mathbb{C}^\times$ at the real places.

**Theorem 2.6.4 (2-primary compact cohomology of the $S$-units).** Assume that $S$ contains the places above $2$. Let $r \geq 4$ and $x \in H^r_c(G_S, E_S)$ with $2^k x = 0$ for some $k$. Then $x = 0$.

Lean: `GroundTheory.ProfCoh.eq_zero_unitsTateCohomology_of_two_pow_nsmul`.

*Proof.* Let $y$ be the image of $x$ in $H^r(G_S, E_S)$. Then $2^k y = 0$, so $y$ is $2$-primary. Its restriction to each real place is zero, since $y$ comes from compact cohomology. By the previous theorem, $y = 0$. So $x$ is the image of a local class $t$ in degree $r - 1 \geq 3$. The components of $t$ at $v \in S$ are zero, by the local vanishing. At the real places, every class lifts to $H^{r-1}(G_S, E_S)$. For even $r - 1$ this is the surjectivity in the previous theorem. For odd $r - 1$ the real groups are zero. So $t$ is the restriction of a global class, and its image $x$ in compact cohomology is zero. $\square$

**Lemma 2.6.5 (divisibility).** Assume that $S$ contains the places above $2$. For $r \geq 3$, each element of $H^r_c(G_S, E_S)$ is $2$ times an element.

Lean: `GroundTheory.ProfCoh.exists_two_nsmul_unitsTateCohomology`.

*Proof.* Let $r \geq 4$ and $x \in H^r_c(G_S, E_S)$. The image of $x$ in $H^r(G_S, E_S)$ is killed by some $N \geq 1$. So $Nx$ comes from a local class $t$ in degree $r - 1 \geq 3$, and $2t = 0$. So $2N x = 0$. Write $2N = 2^a b$ with $b$ odd. Then $2^a(bx) = 0$, so $bx = 0$ by the theorem. With $b = 2c + 1$ we get $x = 2(c+1)x$. In degree $3$ the argument is similar, with $H^3(G_S, E_S)(2) = 0$ and the divisibility of the local Brauer groups $H^2(G_v, \overline{K}_v^\times) = \mathbb{Q}/\mathbb{Z}$. $\square$

### The trivial module $\mathbb{Z}/2$

**Theorem 2.6.6 (vanishing for $\mu_2$).** Assume that $S$ contains the places above $2$. Then $H^r_c(G_S, \mu_2) = 0$ for $r \geq 4$.

Lean: `GroundTheory.ProfCoh.gsTateCompactCohomology_rootsOfUnity_two_eq_zero`.

*Proof.* Since $2$ is an $S$-unit, a square root of an $S$-unit generates an extension unramified outside $S$. So the Kummer sequence
$$1 \to \mu_2 \to E_S \xrightarrow{\ (\cdot)^2\ } E_S \to 1$$
is exact, and so are the local sequences for $\overline{K}_v^\times$ and $\mathbb{C}^\times$. These give a long exact sequence of compact cohomology, with maps $f : H^r_c(\mu_2) \to H^r_c(E_S)$, multiplication by $2$ on $H^r_c(E_S)$ and a connecting map $\delta$. Let $x \in H^r_c(G_S, \mu_2)$. Then $2 f(x) = 0$, so $f(x) = 0$ by the theorem on the $S$-units. So $x = \delta(y)$ for some $y \in H^{r-1}_c(G_S, E_S)$, with $r - 1 \geq 3$. By the divisibility lemma, $y = 2y'$. Then $x = \delta(2y') = 0$, since $\delta$ kills the image of multiplication by $2$. $\square$

**Corollary 2.6.7 (vanishing for $\mathbb{Z}/2$).** Assume that $S$ contains the places above $2$. Then $H^r_c(G_S, \mathbb{Z}/2) = 0$ for $r \geq 4$.

Lean: `GroundTheory.ProfCoh.gsTateCompactCohomology_zmodRep_two_eq_zero`.

*Proof.* The group $\mu_2 = \{\pm 1\}$ is fixed by $G_S$, so $\mu_2 \cong \mathbb{Z}/2$ as $G_S$-modules. Apply the theorem. $\square$

From the long exact sequence, the corollary gives: restriction $H^j(G_S, \mathbb{Z}/2) \to \prod_{v \in S_\mathbb{R}} H^j(G_v, \mathbb{Z}/2)$ is injective for $j \geq 4$ and surjective for $j \geq 3$. This holds for each number field and each $S$ that contains the places above $2$.

### Coinduced modules

Let $W$ be an open subgroup of $G_S$ and let $L \subseteq K_S$ be its fixed field, a finite extension of $K$. Let $S_L$ be the set of places of $L$ above $S$. Then $W = G_{L, S_L}$. Shapiro's lemma identifies $H^j(G_S, \operatorname{Coind}_W^{G_S} \mathbb{Z}/2)$ with $H^j(W, \mathbb{Z}/2)$. At a real place $v$ of $K$, the Mackey formula writes $H^j(G_v, \operatorname{Coind}_W^{G_S} \mathbb{Z}/2)$ as a product over the double cosets $W g G_v$ of the groups $H^j(G_v \cap g^{-1} W g, \mathbb{Z}/2)$. If the intersection is trivial, the factor is zero for $j \geq 1$. Call a double coset *full* if the intersection is all of $G_v$.

**Theorem 2.6.8 (full double cosets and real places of $L$).** Assume that $S$ contains the places above $2$. Let $L \subseteq K_S$ be a finite extension of $K$ and $W = \operatorname{Gal}(K_S/L)$. The full double cosets at the real places of $K$ are in bijection with the real places of $L$. Under this bijection, the map
$$H^j(W, \mathbb{Z}/2) \to \prod_{v \in S_\mathbb{R}} \ \prod_{\text{full } WgG_v} H^j(G_v, \mathbb{Z}/2)$$
is restriction from $G_{L,S_L}$ to the real places of $L$. So it is injective for $j \geq 4$ and surjective for $j \geq 3$.

Lean: `GroundTheory.ProfCoh.gsMackeyTop_gsOpenSubgroup`.

*Proof.* A full double coset $W g G_v$ gives the embedding $g \circ \iota_v$ of $L$ into $\mathbb{R}$, so a real place of $L$ above $v$. Different full double cosets give different places, and each real place of $L$ arises this way. For a full double coset, conjugation by $g$ identifies $G_v$ with the decomposition group of that real place in $G_{L,S_L}$. The restriction maps match under these identifications, by the transfer of trivial coefficients along a group isomorphism. The last claim is the remark after the corollary, applied to $L$ and $S_L$. Every place of $L$ above $2$ lies above a place of $S$, so it lies in $S_L$. $\square$

**Theorem 2.6.9 (vanishing for coinduced $\mathbb{Z}/2$).** Assume that $S$ contains the places above $2$. Let $W$ be an open subgroup of $G_S$. Then $H^r_c(G_S, \operatorname{Coind}_W^{G_S} \mathbb{Z}/2) = 0$ for $r \geq 4$.

Lean: `GroundTheory.ProfCoh.gsTateCompactCohomology_coind_zmodRep_two_eq_zero`.

*Proof.* Let $L$ be the fixed field of $W$. At $v \in S$, the Mackey formula writes the local groups as products of groups $H^j(U, \mathbb{Z}/2)$ for open subgroups $U$ of $G_v$, and these are zero for $j \geq 3$. At the real places only the full double cosets contribute in degrees $j \geq 1$. So the real restriction of the coinduced module is the map of the previous theorem, after Shapiro's lemma. It is surjective in degree $r - 1 \geq 3$ and injective in degree $r \geq 4$. The vanishing criterion gives $H^r_c = 0$. $\square$

### The general case

**Theorem 2.6.10 (vanishing of compact cohomology).** Let $n \neq 0$ and assume that $S$ contains the places above the prime factors of $n$. Let $M$ be a finite discrete $G_S$-module with $nM = 0$. Then $H^r_c(G_S, M) = 0$ for each $r \geq 4$.

Lean: `GroundTheory.ProfCoh.gsTateCompactCohomology_eq_zero`.

*Proof.* We use strong induction on $n$. If $M = 0$, the claim is the vanishing criterion with zero groups. Otherwise $n \neq 1$. Choose a prime $\ell$ dividing $n$, and write $n = \ell c$. The submodule $M[\ell]$ of elements killed by $\ell$ is $G_S$-stable. In the exact sequence
$$0 \to M[\ell] \to M \to M/M[\ell] \to 0$$
the quotient is killed by $c < n$, so its $H^r_c$ is zero by induction. It remains to treat $M[\ell]$.

If $\ell$ is odd, the real groups $H^j(G_v, M[\ell])$ are killed by $2$ and by $\ell$, so they are zero for $j \geq 1$. The places above $\ell$ are in $S$ and $\ell$ is odd, so $G_S$ has $\ell$-cohomological dimension at most $2$. So $H^j(G_S, M[\ell]) = 0$ for $j \geq 3$. The vanishing criterion applies.

If $\ell = 2$, we reduce to coinduced modules. The kernel $K_0$ of the action on $M[2]$ is open and normal. Let $P$ be a $2$-Sylow subgroup of $G_S/K_0$ and $W$ its inverse image, an open subgroup of odd index. Restriction to $W$ followed by corestriction is multiplication by $[G_S : W]$, which is invertible on $M[2]$. So $M[2]$ is a retract of $\operatorname{Coind}_W^{G_S} M[2]$, and it is enough to treat the coinduced module. The group $W$ acts on the $\mathbb{F}_2$-vector space $M[2]$ through the $2$-group $P$. So a nonzero $M[2]$ has a nonzero fixed vector, and $M[2]$ has a filtration by $W$-submodules with quotients $\mathbb{Z}/2$. Coinduction is exact, so an induction on the order of $M[2]$ reduces the claim to $\operatorname{Coind}_W^{G_S} \mathbb{Z}/2$. This is the previous theorem. $\square$

**Remark 2.6.11 (Formalization).** The compact cohomology is the cohomology of a mapping cone, with the norm term in degree $0$ at the real places ([ConeDefs.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/ConeDefs.lean#L191)). The isomorphism for the $S$-units is a definition by bijectivity; it takes a family of local embeddings as a parameter, and later proofs use an arbitrary choice ([EqZeroOfPowNsmulCohomologySUnitsOfOdd.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/EqZeroOfPowNsmulCohomologySUnitsOfOdd.lean#L139)). The same file has a parallel isomorphism for all units of $K_S$, which this section does not use. The theorem on full double cosets is stated for the open subgroup attached to a finite subextension $L$, and the theorem on coinduced modules first finds such an $L$ for $W$ ([VanishingMackeyTransfer.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/VanishingMackeyTransfer.lean#L371)). The dévissage, including the $2$-Sylow reduction, is in [VanishingPrimes.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/VanishingPrimes.lean#L118) and [VanishingIndex.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/VanishingIndex.lean#L210). The final theorem takes the local embeddings at $S$ as a parameter, but the restriction theorems that use it choose their own ([Vanishing.lean](lean:GroundTheory/ProfiniteCohomology/RealPlaces/Vanishing.lean#L20)).
