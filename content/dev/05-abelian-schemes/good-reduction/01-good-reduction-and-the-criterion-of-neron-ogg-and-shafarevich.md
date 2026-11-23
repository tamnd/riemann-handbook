---
title: Good reduction and the criterion of Néron, Ogg and Shafarevich
decls:
  - UpperTheory.Lit.serreTateGoodReduction
  - UpperTheory.Lit.neronOggShafarevich
  - UpperTheory.Lit.Nos.Nos.neronOggShafarevich
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good reduction and the criterion of Néron, Ogg and Shafarevich

This section defines good reduction of an abelian variety over the fraction field of a discrete valuation ring, and the action of the inertia group on its torsion points and on its Tate modules. It states three theorems of Serre and Tate (*Good reduction of abelian varieties*, Ann. of Math. 88 (1968)): the criterion of Néron, Ogg and Shafarevich, the criterion for potential good reduction, and potential good reduction of abelian varieties with complex multiplication. Their conjunction is one of the inputs of [the CM and abelian variety inputs from the literature](/step/cm-abelian-inputs-from-literature/). The proof of the criterion uses one deep implication, that unramified torsion gives good reduction. That implication is proved in Sections 2 to 4 of this chapter, and we use it here.

### The setting

Throughout, $R$ is a [[discrete valuation ring|MGM3CNJW9V]] with fraction field $K$ and residue field $k$, and $\Omega$ is a separable closure of $K$. Background on discrete valuation rings, Néron models and good reduction is in [the abelian varieties chapter](/learn/abelian-varieties/#neron-models-and-good-reduction) of Volume 1.

**Definition 3.1.1 (Valuation ring above $R$).** Let $L$ be a field extension of $K$. A subring $V$ of $L$ *lies above* $R$ if $V \cap K = R$, that is, if the preimage of $V$ under $K \to L$ is the image of $R$.

If $V$ is a [[valuation ring|QSX12D8RQM]] of $\Omega$ above $R$, then the valuation of $V$ restricts to the valuation of $R$ on $K$. Such a $V$ exists, since every valuation of $K$ extends to every algebraic extension.

**Definition 3.1.2 (Abelian variety, good reduction).** An *[[abelian variety|R7W03TXRS9]]* over $K$ is a commutative group scheme $A$ over $K$ that is an [[abelian scheme|JDDXZ89N33]] over $\operatorname{Spec} K$. It has *good reduction over $R$* if there are an abelian scheme $G$ over $R$ and an isomorphism of group schemes $G \times_R K \cong A$.

By Volume 1, such a $G$ is the Néron model of $A$, so it is unique up to unique isomorphism.

**Definition 3.1.3 (Potential good reduction).** An abelian variety $A$ over $K$ has *potential good reduction over $R$* if there are a finite extension $L$ of $K$ and a discrete valuation ring $W$ with fraction field $L$ that lies above $R$, such that $A \times_K L$ has good reduction over $W$.

**Definition 3.1.4 (Decomposition and inertia groups).** Let $V$ be a valuation ring of $\Omega$ above $R$, with residue field $\kappa(V)$. The *decomposition group* of $V$ is the group $D_V$ of $\sigma \in \operatorname{Gal}(\Omega/K)$ with $\sigma(V) = V$. Each such $\sigma$ induces an automorphism of $\kappa(V)$. The *inertia group* $I_V \subseteq D_V$ is the kernel of the map $D_V \to \operatorname{Aut}(\kappa(V))$.

See [decomposition groups, inertia and Frobenius](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius) in Volume 1.

**Definition 3.1.5 (Galois action on points).** Let $A$ be an abelian variety over $K$ and $A(\Omega)$ the group of morphisms $x : \operatorname{Spec} \Omega \to A$ over $K$. For $\sigma \in \operatorname{Gal}(\Omega/K)$ put $\sigma x = x \circ \operatorname{Spec}(\sigma)$. This is a left action of the Galois group on $A(\Omega)$ by group automorphisms. For a prime $\ell$, the [[Tate module|4CSMQFTGD8]] $T_\ell A$ is the inverse limit of the groups $A(\Omega)[\ell^n]$ over $n$, and $\sigma$ acts on it through its action on each $A(\Omega)[\ell^n]$. We write $\rho_\ell : \operatorname{Gal}(\Omega/K) \to \operatorname{Aut}_{\mathbb{Z}_\ell}(T_\ell A)$ for this action.

In terms of rings, a point $x$ is a homomorphism $\mathcal{O}(U) \to \Omega$ on an affine open $U$ of $A$, and $\sigma x$ is its composite with $\sigma$.

**Definition 3.1.6 (Unramified torsion, unramified Tate module).** Let $V$ be a valuation ring of $\Omega$ above $R$ and $m \geq 0$ an integer. The $m$-torsion of $A$ is *unramified at $V$* if $\sigma x = x$ for each $\sigma \in I_V$ and each $x \in A(\Omega)$ with $mx = 0$. For a prime $\ell$, the Tate module $T_\ell A$ is *unramified at $V$* if $\rho_\ell(\sigma) = 1$ for each $\sigma \in I_V$.

**Definition 3.1.7 (Complex multiplication).** Let $F$ be a number field. An abelian variety $A$ over $K$ *has complex multiplication by $F$* if $A$ is smooth of relative dimension $d$ over $K$ with $[F : \mathbb{Q}] = 2d$, and there is a ring $O$ with fraction field $F$ and a ring homomorphism from $O$ to the ring of endomorphisms of the group scheme $A$.

### The three theorems

**Theorem 3.1.8 (Criterion of Néron, Ogg and Shafarevich).** Let $R$ be a discrete valuation ring whose residue field $k$ is perfect, $K$ its fraction field, $\Omega$ a separable closure of $K$, and $V$ a valuation ring of $\Omega$ above $R$. Let $A$ be an abelian variety over $K$. The following are equivalent.

1. $A$ has good reduction over $R$.
2. For each integer $m$ with $m \neq 0$ in $k$, the $m$-torsion of $A$ is unramified at $V$.
3. The set of integers $m$ with $m \neq 0$ in $k$ such that the $m$-torsion of $A$ is unramified at $V$ is infinite.
4. There is a prime $\ell$ with $\ell \neq 0$ in $k$ such that $T_\ell A$ is unramified at $V$.

Lean: `UpperTheory.Lit.Nos.Nos.neronOggShafarevich` (also `UpperTheory.Lit.neronOggShafarevich`, a second name).

*Proof.* We prove $1 \Rightarrow 2$, $2 \Rightarrow 3$, $2 \Rightarrow 4$, $4 \Rightarrow 3$ and $3 \Rightarrow 1$.

$1 \Rightarrow 2$. Let $G$ be an abelian scheme over $R$ with generic fibre $A$. For $m$ invertible in $R$, the kernel $G[m]$ is finite étale over $R$. After passage to a strict henselization of $R$, which does not change the inertia group, every point of $A[m](\Omega)$ is defined over the fraction field of the strict henselization, and that field is fixed by $I_V$ (Volume 1, [the proof of $1 \Rightarrow 2$](/learn/abelian-varieties/#neron-models-and-good-reduction)). This implication does not use that $k$ is perfect.

$2 \Rightarrow 3$ and $2 \Rightarrow 4$. There are infinitely many primes, and only one of them can be zero in $k$. Choose a prime $\ell$ with $\ell \neq 0$ in $k$. Then $\ell^n \neq 0$ in $k$ for all $n$, so by 2 the inertia group fixes $A(\Omega)[\ell^n]$ for every $n$. This gives the infinite set $\{\ell^n\}$ of 3, and it shows that $I_V$ acts trivially on the inverse limit $T_\ell A$, which is 4.

$4 \Rightarrow 3$. Let $\ell \neq 0$ in $k$ with $T_\ell A$ unramified. The group $A(\Omega)[\ell^n]$ is the image of $T_\ell A$, so it is fixed by $I_V$ for every $n$, and again the powers of $\ell$ form an infinite set as in 3. The surjectivity of $T_\ell A \to A(\Omega)[\ell^n]$ holds because $A(\Omega)$ is $\ell$-divisible with finite $\ell^n$-torsion, as $\ell \neq 0$ in $K$ and $\Omega$ is separably closed.

$3 \Rightarrow 1$. This is [Theorem 3.4.7](/entry/has-good-reduction-of-infinite-torsion-unramified/) of Section 4. $\square$

The statement 4 asks for one prime $\ell$. Together with $1 \Rightarrow 2$ it follows that $T_\ell A$ is unramified for every prime $\ell \neq 0$ in $k$ as soon as it is unramified for one.

**Theorem 3.1.9 (Potential good reduction).** In the setting of the criterion, let $\ell$ be a prime with $\ell \neq 0$ in $k$. Then $A$ has potential good reduction over $R$ if and only if the set $\rho_\ell(I_V)$ is finite.

Lean: `UpperTheory.Lit.potentialGoodReduction`.

*Proof.* Both directions are deduced from the criterion above. The classical argument is that of Serre and Tate, §2. If $\rho_\ell(I_V)$ is finite, its kernel is an open subgroup of $I_V$. It cuts out a finite extension $L$ of $K$ over which the inertia group acts trivially on $T_\ell$, so $A \times_K L$ has good reduction by the criterion. Conversely, if $A \times_K L$ has good reduction for a finite extension $L$, the criterion over $L$ shows that the inertia group of $L$ acts trivially on $T_\ell A$, and it has finite index in $I_V$. $\square$

**Theorem 3.1.10 (Complex multiplication).** Let $R$ be a discrete valuation ring with finite residue field $k$, and $K$ its fraction field. Let $A$ be an abelian variety over $K$, and $F$ a number field such that $A$ has complex multiplication by $F$. Then $A$ has potential good reduction over $R$.

Lean: `UpperTheory.Lit.cmPotentialGoodReduction` (also `UpperTheory.Lit.cmPotentialGoodReduction_of_nos`).

*Proof.* Let $\Omega$ be a separable closure of $K$, and choose a valuation ring $V$ of $\Omega$ above $R$. Choose a prime $\ell$ with $\ell \neq 0$ in $k$. Then $\ell \neq 0$ in $K$. The proof has four steps.

1. Since $A$ has complex multiplication by $F$, the automorphisms $\rho_\ell(\sigma)$ for $\sigma \in \operatorname{Gal}(\Omega/K)$ commute with each other (Serre and Tate, §4).
2. Since $k$ is finite and the image is commutative, there is an integer $N \geq 1$ with $\rho_\ell(\sigma)^N = 1$ for every $\sigma \in I_V$.
3. Let $d$ be the dimension of $A$. The group $A(\Omega)[\ell^2]$ has $\ell^{4d}$ elements, so it is finite. A commutative group of automorphisms of $T_\ell A$ of bounded exponent is finite when $A(\Omega)[\ell^2]$ is finite, so $\rho_\ell(I_V)$ is finite.
4. By the theorem on potential good reduction, $A$ has potential good reduction over $R$.

Each step is a result of other chapters, which we have not unfolded here, except step 4. $\square$

**Theorem 3.1.11 (Serre and Tate).** The criterion of Néron, Ogg and Shafarevich, the theorem on potential good reduction and the theorem on complex multiplication hold, in the forms above.

Lean: `UpperTheory.Lit.serreTateGoodReduction`.

*Proof.* The criterion is proved above. The second theorem is deduced from it, and the third theorem is deduced from the first two. $\square$

**Remark 3.1.12 (Formalization).** `UpperTheory.Lit.neronOggShafarevich` is a second name for `UpperTheory.Lit.Nos.Nos.neronOggShafarevich` ([SerreTate.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/SerreTate.lean#L7)). The definitions are in [TateUnramifiedOfTorsionUnramified.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/TateUnramifiedOfTorsionUnramified.lean#L30). The implications $1 \Rightarrow 2$, $2 \Rightarrow 3, 4$ and $4 \Rightarrow 3$ are the results `GlobalTheory.T.torsionUnramified_of_hasGoodReduction_alt`, `GlobalTheory.T.torsionUnramified_imp_tateModule_and_infinite` and `GlobalTheory.T.infinite_torsionUnramified_of_tateModuleUnramified`; we read their statements but not their proofs, and the arguments above are the classical ones. The first two need weaker hypotheses than the theorem: no perfect residue field, and for the second no valuation ring above $R$. In the step $4 \Rightarrow 3$ the primality of $\ell$ is introduced and not used ([NeronOggShafarevich.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/NeronOggShafarevich.lean#L28)). The two directions of potential good reduction are `GlobalTheory.T.finite_image_inertia_of_potentialGoodReduction_alt` and `GlobalTheory.T.hasPotentialGoodReduction_of_finite_image_inertia_alt`, not opened. The definition of complex multiplication `HasCMBy` asks neither that the ring homomorphism $O \to \operatorname{End}(A)$ be injective nor that $F$ be a CM field, and the theorem on complex multiplication is local: $R$ is any discrete valuation ring with finite residue field. The same file checks the definitions on an example, `exists_cm_curve`: an elliptic curve over $\mathbb{Z}_5$, built from a square root of $-1$ in $\mathbb{Z}_5$ and an action of $\mathbb{Z}[i]$, has good and potential good reduction ([line 256](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/TateUnramifiedOfTorsionUnramified.lean#L256)).
