---
title: Restriction to an affine lift
decls:
  - GlobalTheory.PDForm.LevLift.cop_ex
  - GlobalTheory.PDForm.LevLift.resMap_bij
  - GlobalTheory.PDForm.levLift_resMap_bij
  - GlobalTheory.T.crystallineForms_restriction_affineLift_bijective
  - GlobalTheory.PDForm.Lift.resMap_toE_pullbackBijectiveDegreesOneTwo
  - GlobalTheory.PDForm.Lift.resMap_lift_pullbackBijectiveDegreesOneTwo
  - GlobalTheory.T.lift_restriction_bijective_low_degrees
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Restriction to an affine lift

This section proves that the cohomology of the divided power de Rham complex over all thickenings of $X_0$ is the same, in degrees one and two, as its cohomology over the thickenings of an affine lift. The proof works one level at a time. At a fixed level, the coproducts of the [last section](/entry/exists-cop-q-at/) give a functor that retracts all thickenings onto the affine lift, and a general collapse result gives bijectivity in degrees zero, one and two. An exhaustion argument then passes to all levels. The [last section of the chapter](/entry/crystalline-cech-de-rham-relations-total-detect-zero/) uses the result to compare crystalline and de Rham cohomology.

We keep the notation of the last two sections. Fix a crystalline datum $D$ and an affine lift $\Lambda$ of $D$.

**Definition 5.9.1 (Cohomology of a complex over a category).** Let $\mathcal{C}$ be a category and let $K$ be a complex $M^0 \to M^1 \to M^2 \to M^3$ of functors from $\mathcal{C}$ to abelian groups. For a functor $M$ let $C^0(M)$ be the group of families $(g_T)$ with $g_T \in M(T)$ for each object $T$, let $C^1(M)$ be the group of families $(c_\varphi)$ with $c_\varphi \in M(T')$ for each morphism $\varphi : T \to T'$, and let $C^2(M)$ be the group of families indexed by pairs of composable morphisms $T \to T' \to T''$ with values in $M(T'')$, with the usual simplicial differentials. The *cohomology* $H^j(\mathcal{C}, K)$ for $j = 0, 1, 2$ is the cohomology of the total complex
$$\begin{aligned}
&C^0(M^0) \to C^1(M^0) \times C^0(M^1) \to C^2(M^0) \times C^1(M^1) \times C^0(M^2) \\
&\to C^3(M^0) \times C^2(M^1) \times C^1(M^2) \times C^0(M^3).
\end{aligned}$$
For a functor $\ell : \mathcal{C}' \to \mathcal{C}$, the complex $K \circ \ell$ is a complex over $\mathcal{C}'$, and composing families with $\ell$ gives the *restriction map* $H^j(\mathcal{C}, K) \to H^j(\mathcal{C}', K \circ \ell)$.

For the complex with $M^0 = M$ and $M^1 = M^2 = M^3 = 0$ we write $H^j(\mathcal{C}, M)$. Taking the first component of each family gives a map $H^j(\mathcal{C}, K) \to H^j(\mathcal{C}, M^0)$, which *forgets the forms*.

**Definition 5.9.2 (Affine thickenings).** Let $\mathcal{E}$ be the category of pairs $(T, U)$ of a thickening $T$ of $X_0$ and an affine open $U$ of $X$ such that $i \circ x_T$ maps into $U$. A morphism $(T, U) \to (T', U')$ is a morphism $T \to T'$ of thickenings, and it exists only if $U' \subseteq U$. For $N \geq 0$ let $\mathcal{E}_N$ be the full subcategory of pairs with $T$ at level $N$. Let $\mathcal{A}$ be the category of affine opens of $X$, with one morphism $U \to V$ when $V \subseteq U$. The affine lift gives functors $L : \mathcal{A} \to \mathrm{Th}$ to the category of thickenings and $\lambda : \mathcal{A} \to \mathcal{E}$ with $\lambda(U) = (L(U), U)$. On $\mathrm{Th}$, on $\mathcal{E}$ and on $\mathcal{E}_N$ we use the complex $K^\bullet$ of the divided power de Rham complex, and on $\mathcal{A}$ its composite with $L$.

**Lemma 5.9.3 (Coproducts at a level).** Let $n \geq 0$ and let $(T, U)$ be an object of $\mathcal{E}_{n+1}$. Then there are a thickening $G$ and morphisms $l : T \to G$ and $r : L(U) \to G$ such that $(l, r)$ is a coproduct at level $n + 1$ and $l$ is a quasi-isomorphism in low degrees.

Lean: `GlobalTheory.PDForm.LevLift.cop_ex`.

*Proof.* The thickening $T$ is at level $n + 1$ and $i \circ x_T$ maps into $U$. So [the theorem on coproducts with an affine lift](/entry/exists-cop-q-at/) applies. $\square$

**Theorem 5.9.4 (Restriction at a fixed level).** Let $n \geq 0$ and assume that $L(U)$ is at level $n + 1$ for every affine open $U$. Then $\lambda$ maps $\mathcal{A}$ into $\mathcal{E}_{n+1}$, and the restriction map
$$H^j(\mathcal{E}_{n+1}, K^\bullet) \to H^j(\mathcal{A}, K^\bullet \circ L)$$
is bijective for $j = 0, 1, 2$.

Lean: `GlobalTheory.PDForm.LevLift.resMap_bij` (also `GlobalTheory.PDForm.levLift_resMap_bij` and `GlobalTheory.T.crystallineForms_restriction_affineLift_bijective`, wrappers).

*Proof.* We take as given a *collapse result*. Let $K$ be a complex over a category $\mathcal{C}$ and let $\ell : \mathcal{D} \to \mathcal{C}$, $q : \mathcal{C} \to \mathcal{D}$ and $S : \mathcal{C} \to \mathcal{C}$ be functors, with natural maps $u : \mathrm{id} \to S$, $w : \ell \circ q \to S$ and $\varepsilon : \mathrm{id} \to q \circ \ell$. Assume that $u_T$ is a quasi-isomorphism in low degrees for every $T$, and that $w_{\ell(V)} \circ \ell(\varepsilon_V)$ is one for every $V$. Then restriction along $\ell$ is bijective on $H^0$, $H^1$ and $H^2$.

1. *The functors.* Take $\mathcal{C} = \mathcal{E}_{n+1}$, $\mathcal{D} = \mathcal{A}$ and $\ell = \lambda$. Let $q(T, U) = U$, and let $\varepsilon$ be the identity, since $q(\lambda(U)) = U$.
2. *The retraction.* For each object $(T, U)$ choose $G_T$, $l_T$ and $r_T$ by the lemma, and put $S(T, U) = (G_T, U)$. This lies in $\mathcal{E}_{n+1}$: $G_T$ is at level $n + 1$, and $i \circ x_{G_T}$ maps into $U$ since $x_{G_T}$ factors through $x_T$. For a morphism $f : (T, U) \to (T', U')$, let $S(f) : G_T \to G_{T'}$ be the unique morphism with $S(f) \circ l_T = l_{T'} \circ f$ and $S(f) \circ r_T = r_{T'} \circ L(U \supseteq U')$; it exists by the coproduct property, since $G_{T'}$ is at level $n + 1$. Uniqueness makes $S$ a functor and makes $u = (l_T)$ and $w = (r_T)$ natural.
3. *The first condition.* Each $l_T$ is a quasi-isomorphism in low degrees by the lemma.
4. *The second condition.* Since $\varepsilon$ is the identity, we must show that $r_T$ is a quasi-isomorphism for $T = \lambda(U)$. Then $l_T$ and $r_T$ are two maps from $L(U)$ into the coproduct $G_T$. The coproduct property for $S = G_T$, $a = r_T$ and $b = l_T$ gives $\sigma : G_T \to G_T$ with $\sigma \circ l_T = r_T$ and $\sigma \circ r_T = l_T$. Then $\sigma \circ \sigma$ fixes $l_T$ and $r_T$, so $\sigma \circ \sigma$ is the identity by uniqueness, and $\sigma$ is an isomorphism. An isomorphism is a quasi-isomorphism in low degrees, so $r_T = \sigma \circ l_T$ is one as a composite.
5. *Conclusion.* The collapse result gives the claim. $\square$

The proof does not use the assumption on the levels of $L(U)$ except to place $\lambda(U)$ in $\mathcal{E}_{n+1}$. The coproduct with $L(U)$ is the device that moves a thickening onto the lift.

**Theorem 5.9.5 (Restriction to the lift in $\mathcal{E}$).** The restriction map $H^j(\mathcal{E}, K^\bullet) \to H^j(\mathcal{A}, K^\bullet \circ L)$ along $\lambda$ is bijective for $j = 1, 2$.

Lean: `GlobalTheory.PDForm.Lift.resMap_toE_pullbackBijectiveDegreesOneTwo`.

*Proof.* We take as given two results. First, there is $N_0$ such that $L(U)$ is at level $N$ for all $N \geq N_0$ and all affine opens $U$. Second, an *exhaustion result*: let $K$ be a complex over $\mathcal{C}$, let $\ell : \mathcal{D} \to \mathcal{C}$ be a functor and let $P_0 \subseteq P_1 \subseteq \cdots$ be full subcategories of $\mathcal{C}$ whose union contains every object. Assume that for each $N \geq N_1$, the functor $\ell$ maps into $P_N$ and restriction from $P_N$ to $\mathcal{D}$ is bijective on $H^0$, $H^1$ and $H^2$. Then restriction from $\mathcal{C}$ to $\mathcal{D}$ is bijective on $H^1$ and on $H^2$.

1. *The filtration.* Put $P_N = \mathcal{E}_N$. If $m \leq N$, then $\mathrm{fil}_N \subseteq \mathrm{fil}_m$, so a thickening at level $m$ is at level $N$. Every thickening has a nilpotent divided power structure, so it is at some level. So the $\mathcal{E}_N$ increase and exhaust $\mathcal{E}$.
2. *Each level.* Let $N \geq N_0 + 1$ and write $N = n + 1$. Then $N \geq N_0$, so every $L(U)$ is at level $n + 1$, and the theorem at a fixed level gives bijectivity on $H^0$, $H^1$ and $H^2$.
3. *Conclusion.* The exhaustion result with $N_1 = N_0 + 1$ gives the claim. $\square$

**Theorem 5.9.6 (Restriction to the lift).** The restriction map $H^j(\mathrm{Th}, K^\bullet) \to H^j(\mathcal{A}, K^\bullet \circ L)$ along $L$ is bijective for $j = 1, 2$.

Lean: `GlobalTheory.PDForm.Lift.resMap_lift_pullbackBijectiveDegreesOneTwo` (also `GlobalTheory.T.lift_restriction_bijective_low_degrees`, a wrapper).

*Proof.* Let $p : \mathcal{E} \to \mathrm{Th}$ forget the open, so that $L = p \circ \lambda$. Let $O$ be the functor $T \mapsto B_T$. We take as given three results. First, the maps $H^j(\mathrm{Th}, K^\bullet) \to H^j(\mathrm{Th}, O)$ and $H^j(\mathcal{E}, K^\bullet \circ p) \to H^j(\mathcal{E}, O \circ p)$ that forget the forms are bijective for $j = 1, 2$. Second, if the intersection of two affine opens of $X$ is affine, then restriction $H^j(\mathrm{Th}, O) \to H^j(\mathcal{E}, O \circ p)$ is bijective for $j = 1, 2$. Third, the intersection of two affine opens of $X$ is affine; this holds since $s$ is separated.

1. *Restriction along $p$.* Forgetting the forms commutes with restriction: the square
$$\begin{aligned}
H^j(\mathrm{Th}, K^\bullet) &\to H^j(\mathcal{E}, K^\bullet \circ p) \\
\downarrow \quad &\qquad \downarrow \\
H^j(\mathrm{Th}, O) &\to H^j(\mathcal{E}, O \circ p)
\end{aligned}$$
commutes, since both paths take the first component of a family and compose it with $p$. The vertical maps and the lower map are bijective for $j = 1, 2$ by the inputs. So the upper map is bijective.
2. *Composition.* Restriction along $L = p \circ \lambda$ is restriction along $p$ followed by restriction along $\lambda$. The first is bijective on $H^1$ and $H^2$ by step 1, and the second by the last theorem. So the composite is bijective. $\square$

The degree zero part is not claimed in the last two theorems. The exhaustion result gives only $H^1$ and $H^2$, and the chapter uses only these degrees.

**Remark 5.9.7 (Formalization).** The lemma and the theorem at a fixed level are in [CrystallineFormsRestrictionAffineLiftBijective.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineFormsRestrictionAffineLiftBijective.lean#L39), at lines 39 and 122, with the involution of step 4 as `qat_rr` at line 104 and the outer form at line 130. The last two theorems are in [LiftRestrictionBijectiveLowDegrees.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LiftRestrictionBijectiveLowDegrees.lean#L50), at lines 50 and 64, with the square of step 1 as `resMap_bij12_of_fnMap` at line 20 and the composite as `resMap_comp_bij12` at line 35. The cohomology of a complex over a category, the restriction map and the map that forgets the forms are `Cx.H1`, `Cx.resMap` and `Cx.fnMap` in [PullbackBijectiveDegreesOneTwo.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PullbackBijectiveDegreesOneTwo.lean#L290). We read the statements of the collapse result, the exhaustion results and the three inputs of the last proof only. The functor $S$ is built from coproducts picked by the axiom of choice. The category $\mathcal{E}$ uses every affine open, with no covering condition, so its cohomology is the cohomology of a category and not of a site. The outer form at a fixed level sits outside the namespace of the inner theorem but carries its full name.
