---
title: The cohomology of the punctured line
decls:
  - GlobalTheory.EtC.laurentPolynomial_cohomology_strictlyHenselian_vanishing
  - GlobalTheory.T.multiplicativeGroup_cohomology_strictlyHenselian
  - GlobalTheory.gm_cohomology_strictlyHenselian
  - GlobalTheory.LaurentCohomologyVanishing.laurent_cohomology
  - GlobalTheory.LaurentCohomologyVanishing.vanishing_below
  - GlobalTheory.T.laurentPolynomial_tateTwistCohomology_vanishing_inductive
  - GlobalTheory.EtC.GmStep.gm_vanishing_step
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The cohomology of the punctured line

This section computes the [étale cohomology](/learn/geometry/#tale-cohomology) of the punctured line $\mathbb{G}_{m,A} = \operatorname{Spec} A[t, t^{-1}]$ over a strictly henselian ring $A$, with coefficients $\mathbb{Z}/q(i)$. The answer is the same as over a separably closed field: a group isomorphic to $\mathbb{Z}/q$ in degree $1$, and zero in degrees at least $2$. The result is one of the inputs of [the local steps](/entry/steps-holds/) of the chapter on Galois representations. The proof is an induction on the degree. In each step a class is killed by a finite extension of $A$, and descent along this extension shows that the class is zero.

We keep the notation of the earlier sections. A ring is *strictly henselian* if it is a henselian local ring with [[separably closed|8B57B7EGK4]] residue field. For a ring $A$ we write $H^n(A, F)$ for the cohomology of $\mathrm{sp}(A)$ with coefficients in $F$, and $x \mapsto x|_{A'}$ for the pullback along a ring map $A \to A'$. For a unit $u$ of a ring in which $q$ is a unit, $\kappa(u)$ is its Kummer class in $H^1$ with coefficients $\mathbb{Z}/q(1)$. We write $A[t^{\pm}]$ for $A[t, t^{-1}]$. For an $A$-algebra $A'$ we use the map $A[t^{\pm}] \to A'[t^{\pm}]$ that sends $t$ to $t$.

### The field case

**Example 2.10.1 (The punctured line over a separably closed field).** Let $k$ be a separably closed field and $q \geq 1$ a unit in $k$. The ring $k[t^{\pm}]$ is a localization of $k[t]$, so it is factorial and its [[Picard group|3Z9DCWYXQZ]] is zero. Its units are $c\,t^m$ with $c \in k^\times$ and $m \in \mathbb{Z}$. Every $c \in k^\times$ is a $q$-th power, because $X^q - c$ is separable. The Kummer sequence (J. S. Milne, *Étale Cohomology*, Chapter II, §2) then gives
$$
H^1(k[t^{\pm}], \mu_q) \cong k[t^{\pm}]^\times / (k[t^{\pm}]^\times)^q \cong \mathbb{Z}/q,
$$
with generator $\kappa(t)$. The groups $H^n(k[t^{\pm}], F)$ with $n \geq 2$ and $F$ a torsion sheaf vanish by Artin's theorem on the cohomological dimension of affine schemes (SGA 4, Exposé XIV, §3). The theorem at the end of this section says that the same holds over a strictly henselian ring. Its proof does not reduce to the field case.

### Inputs

We use the following results and take them as given.

**Lemma 2.10.2 (Strictly henselian rings are acyclic).** Let $R$ be a commutative ring, let $A$ be a strictly henselian ring and let $F$ be a sheaf of $R$-modules. Then $H^n(A, F) = 0$ for every $n > 0$.

Lean: `GlobalTheory.T.strictlyHenselianLocalRing_acyclic_every_sheaf`.

This holds because the sections over $\operatorname{Spec} A$ of an étale sheaf are its stalk at the closed point, and the stalk is an exact functor.

**Lemma 2.10.3 (Descent along integral surjections).** Let $f : Y \to X$ be an integral surjective map of schemes such that $q$ is a unit on $X$, and let $i \in \mathbb{Z}$. Let $\check{C}(f)$ be the Čech nerve of $f$, the space with $p$-simplices the fibre product of $p + 1$ copies of $Y$ over $X$. Then the augmentation $\check{C}(f) \to \mathrm{sch}(X)$ induces a bijection $H^n(X, \mathbb{Z}/q(i)) \to H^n(\check{C}(f), \mathbb{Z}/q(i))$ for every $n$.

Lean: `GlobalTheory.EtC.b4`.

One checks the claim after base change to every strictly henselian local ring over $X$.

**Lemma 2.10.4 (A vanishing criterion).** Let $R$ be a commutative ring, let $E$ be a space, let $F$ be a sheaf of $R$-modules, and let $g : \mathrm{disc}(P) \to E$ be a map from a constant space that is an isomorphism on $0$-simplices. For $s \in \mathbb{Z}$ consider the row
$$
H^s(E_0, F) \xrightarrow{d} H^s(E_1, F) \xrightarrow{d} H^s(E_2, F) \xrightarrow{d} \cdots,
$$
where $H^s(E_p, F)$ is the cohomology of the constant space $\mathrm{disc}(E_p)$ and $d$ is the alternating sum of the pullbacks along the faces.

1. Let $n \geq 0$ and $x \in H^n(E, F)$ with $g^* x = 0$. If for every $p$ with $1 \leq p \leq n$ the row in degree $n - p$ is exact at the place $p$, then $x = 0$.
2. If $H^s(E_p, F) = 0$ for all $p \geq 0$ and $s > 0$, and $H^m(E, F) = 0$ for all $m > 0$, then the row in degree $0$ is exact at every place $p \geq 1$.

Lean: `GlobalTheory.T.etaleSpaceCohomology_eq_zero_of_simplicialRowExact` and `GlobalTheory.T.simplicialSpectralRowExact_zero_of_acyclic`.

Both parts are read off from the spectral sequence $E_1^{p,s} = H^s(E_p, F) \Rightarrow H^{p+s}(E, F)$ of the skeletal filtration of $E$. In part 1 the class $x$ restricts to zero on the column $p = 0$, and the exact rows kill its pieces in the columns $p \geq 1$. In part 2 the spectral sequence degenerates to the row $s = 0$, whose cohomology is then $H^p(E, F) = 0$.

**Lemma 2.10.5 (Facts over a strictly henselian base).** Let $A$ be a strictly henselian ring in which $q$ is a unit, let $i \in \mathbb{Z}$, and let $A'$ be a finite $A$-algebra. Write $A'_p = A' \otimes_A \cdots \otimes_A A'$ with $p + 1$ factors, and let $\pi : A \to A[t^{\pm}]$ be the inclusion.

1. $H^0(A, \mathbb{Z}/q(i))$ is isomorphic to $\mathbb{Z}/q$.
2. The map $\Phi : H^0(A, \mathbb{Z}/q(i-1)) \to H^1(A[t^{\pm}], \mathbb{Z}/q(i))$, $a \mapsto \pi^* a \cup \kappa(t)$, is bijective.
3. $H^s(A'_p, \mathbb{Z}/q(i)) = 0$ for all $p \geq 0$ and $s > 0$.
4. The pullback $H^0(A'_p, \mathbb{Z}/q(i)) \to H^0(A'_p[t^{\pm}], \mathbb{Z}/q(i))$ is bijective for all $p \geq 0$.
5. The map $\Phi_p : H^0(A'_p, \mathbb{Z}/q(i-1)) \to H^1(A'_p[t^{\pm}], \mathbb{Z}/q(i))$, $a \mapsto a|_{A'_p[t^{\pm}]} \cup \kappa(t)$, is bijective for all $p \geq 0$.

Lean: `GlobalTheory.T.nonempty_ht_zero_addEquiv_zmod_of_sh`, `GlobalTheory.T.laurentKummerCupProduct_bijective_strictlyHenselian`, `GlobalTheory.T.cech_cohomology_vanishes_positive`, `GlobalTheory.T.laurentCechNerve_pullback_bijective_degree_zero` and `GlobalTheory.T.cech_degree_zero_bijective`.

Part 1 holds because $\Phi_q$ has a root in $A$, so $\mathbb{Z}/q(i)$ is the constant sheaf $\mathbb{Z}/q$ on $\operatorname{Spec} A$, which is connected. For parts 3 to 5, the ring $A'_p$ is finite over $A$, so it is a finite product of henselian local rings. The residue field of each factor is a finite extension of a separably closed field, so it is separably closed, and each factor is strictly henselian. Part 3 then follows from the acyclicity of strictly henselian rings, and part 5 from part 2 for each factor.

**Lemma 2.10.6 (Killing by a finite extension).** Let $A$ be a [[noetherian|0670T59HGE]] strictly henselian ring in which $q$ is a unit, let $n \geq 2$ and $i \in \mathbb{Z}$, and let $x \in H^n(A[t^{\pm}], \mathbb{Z}/q(i))$. Then there is a finite $A$-algebra $A'$ such that the kernel of $A \to A'$ is contained in the nilradical of $A$ and $x|_{A'[t^{\pm}]} = 0$.

Lean: `GlobalTheory.T.laurent_cohomology_finite_killing`.

**Lemma 2.10.7 (Levels of the Čech nerve).** Let $n \in \mathbb{Z}$. Suppose that $H^m(B[t^{\pm}], \mathbb{Z}/q(j)) = 0$ for every noetherian strictly henselian ring $B$ in which $q$ is a unit, every $j$, and every $m$ with $2 \leq m < n$. Let $A$ be such a ring and $A'$ a finite $A$-algebra. Then $H^s(A'_p[t^{\pm}], \mathbb{Z}/q(i)) = 0$ for all $p \geq 0$, all $i$, and all $s$ with $2 \leq s < n$.

Lean: `GlobalTheory.T.laurentCechNerve_level_cohomology_subsingleton`.

**Lemma 2.10.8 (Reduction to noetherian rings).** Suppose that $H^n(B[t^{\pm}], \mathbb{Z}/q(i)) = 0$ for every noetherian strictly henselian ring $B$ in which $q$ is a unit, every $n \geq 2$ and every $i$. Then the same holds for every strictly henselian ring $B$ in which $q$ is a unit.

Lean: `GlobalTheory.T.laurentCohomology_vanishing_of_noetherian_henselian`.

A strictly henselian ring is a filtered colimit of noetherian strictly henselian rings, and cohomology with coefficients $\mathbb{Z}/q(i)$ commutes with such colimits.

### The inductive step

**Theorem 2.10.9 (Inductive step).** Let $q \geq 1$ and let $n \in \mathbb{Z}$ with $n \geq 2$. Suppose that $H^m(A[t^{\pm}], \mathbb{Z}/q(j)) = 0$ for every noetherian strictly henselian ring $A$ in which $q$ is a unit, every $j \in \mathbb{Z}$, and every $m$ with $2 \leq m < n$. Then $H^n(A[t^{\pm}], \mathbb{Z}/q(i)) = 0$ for every such ring $A$ and every $i \in \mathbb{Z}$.

Lean: `GlobalTheory.T.laurentPolynomial_tateTwistCohomology_vanishing_inductive` (also `GlobalTheory.EtC.GmStep.gm_vanishing_step`).

*Proof.* Let $x \in H^n(A[t^{\pm}], \mathbb{Z}/q(i))$.

Step 1. By the lemma on killing, there is a finite $A$-algebra $A'$, with kernel in the nilradical, such that $x|_{A'[t^{\pm}]} = 0$. Let $f : \operatorname{Spec} A'[t^{\pm}] \to \operatorname{Spec} A[t^{\pm}]$ and $g : \operatorname{Spec} A' \to \operatorname{Spec} A$ be the two maps. Both are integral. Both are surjective: every prime contains the nilradical, so it contains the kernel, and a prime that contains the kernel of an integral ring map lies under a prime.

Step 2. By descent along $f$, it is enough to show that the pullback $y$ of $x$ to $\check{C}(f)$ is zero. The level $p$ of $\check{C}(f)$ is $\operatorname{Spec} A'_p[t^{\pm}]$, and the diagonal $\operatorname{Spec} A'[t^{\pm}] \to \check{C}(f)$ is an isomorphism on $0$-simplices. The pullback of $y$ along the diagonal is $x|_{A'[t^{\pm}]} = 0$. By part 1 of the vanishing criterion, it is enough to show that for $1 \leq p \leq n$ the row of $\check{C}(f)$ in degree $s = n - p$ is exact at the place $p$. We treat three cases of $s$.

Step 3, $s \geq 2$. Then $s < n$, and the lemma on levels gives $H^s(A'_p[t^{\pm}], \mathbb{Z}/q(i)) = 0$ for all $p$. So the row is zero, and it is exact.

Step 4, $s = 0$. The maps of part 4 of the facts over a strictly henselian base are bijections from the row in degree $0$ of $\check{C}(g)$ to the row in degree $0$ of $\check{C}(f)$, and they commute with the faces. So it is enough to show that the row in degree $0$ of $\check{C}(g)$ is exact at every place $p \geq 1$. By part 3 of the facts, the levels of $\check{C}(g)$ have no cohomology in positive degrees. By descent along $g$ and the acyclicity of $A$, $H^m(\check{C}(g), \mathbb{Z}/q(i)) \cong H^m(A, \mathbb{Z}/q(i)) = 0$ for $m > 0$. Part 2 of the vanishing criterion gives the exactness.

Step 5, $s = 1$. The maps $\Phi_p$ of part 5 of the facts are bijections from the row in degree $0$ of $\check{C}(g)$, with twist $i - 1$, to the row in degree $1$ of $\check{C}(f)$. They commute with the faces, because pullback commutes with the cup product and because the class $\kappa(t)$ on each level is the pullback of the one class $\kappa(t)$ on $A[t^{\pm}]$. The argument of step 4, at twist $i - 1$, shows that the first row is exact at every place $p \geq 1$. So the second row is exact too.

So every row is exact where it must be, and $x = 0$. $\square$

### The theorem

**Theorem 2.10.10 (Vanishing below a bound).** Let $q \geq 1$ and $k \geq 0$. For every noetherian strictly henselian ring $A$ in which $q$ is a unit, and all integers $m$ and $i$ with $2 \leq m < 2 + k$, the group $H^m(A[t^{\pm}], \mathbb{Z}/q(i))$ is zero.

Lean: `GlobalTheory.LaurentCohomologyVanishing.vanishing_below`.

*Proof.* Induction on $k$. For $k = 0$ there is no such $m$. Suppose that the claim holds for $k$, and let $2 \leq m < 3 + k$. If $m < 2 + k$, the claim for $k$ applies. If $m = 2 + k$, the claim for $k$ is the hypothesis of [Theorem 2.10.9](/entry/laurent-polynomial-tate-twist-cohomology-vanishing-inductive/) for $n = 2 + k$, and that theorem gives the vanishing in degree $m$. $\square$

**Theorem 2.10.11 (Cohomology of the punctured line).** Let $q \geq 1$, let $A$ be a strictly henselian ring in which $q$ is a unit, and let $n, i \in \mathbb{Z}$.

1. If $n \geq 2$, then $H^n(A[t^{\pm}], \mathbb{Z}/q(i)) = 0$.
2. There is an isomorphism of groups $H^1(A[t^{\pm}], \mathbb{Z}/q(i)) \cong \mathbb{Z}/q$.

Lean: `GlobalTheory.EtC.laurentPolynomial_cohomology_strictlyHenselian_vanishing` (also `GlobalTheory.T.multiplicativeGroup_cohomology_strictlyHenselian`, `GlobalTheory.gm_cohomology_strictlyHenselian`, `GlobalTheory.LaurentCohomologyVanishing.laurent_cohomology`).

*Proof.* For part 1, let $B$ be a noetherian strictly henselian ring in which $q$ is a unit, and let $m \geq 2$. [Theorem 2.10.10](/entry/vanishing-below/) with $k = m - 1$ gives $H^m(B[t^{\pm}], \mathbb{Z}/q(j)) = 0$ for every $j$. The reduction to noetherian rings then gives part 1 for $A$.

For part 2, the map $\Phi$ of part 2 of the facts over a strictly henselian base is an isomorphism $H^0(A, \mathbb{Z}/q(i-1)) \cong H^1(A[t^{\pm}], \mathbb{Z}/q(i))$, and part 1 of the facts gives $H^0(A, \mathbb{Z}/q(i-1)) \cong \mathbb{Z}/q$. $\square$

The proof gives more than part 2 says. Since $H^0(A, \mathbb{Z}/q(0)) = \mathbb{Z}/q$ with generator $1$, the group $H^1(A[t^{\pm}], \mathbb{Z}/q(1))$ is generated by $\kappa(t)$, as in the field case.

**Remark 2.10.12 (Formalization).** The theorem is the condition $C_5$ of the package of axioms on étale cohomology in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L116), and its statement does not name the generator $\kappa(t)$. The theorem has four names. The wrapper [MultiplicativeGroupCohomologyStrictlyHenselian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MultiplicativeGroupCohomologyStrictlyHenselian.lean#L13) tries six tactics in turn and declares its theorem outside any namespace. The wrapper [LaurentPolynomialTateTwistCohomologyVanishingIndStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LaurentPolynomialTateTwistCohomologyVanishingIndStatement.lean#L3) imports Mathlib twice and raises the heartbeat limit. The proof of the theorem applies the bound with $k = m$, one more than needed: [LaurentCohomology.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LaurentCohomology.lean#L33). The lemmas of the inputs are separate statements. We opened their statements and the proof of the descent lemma, which reduces to strictly henselian bases, but not the other proofs. The reasons we give after the lemmas are ours.
