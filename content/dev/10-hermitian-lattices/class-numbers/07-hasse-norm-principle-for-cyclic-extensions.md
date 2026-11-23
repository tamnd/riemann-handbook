---
title: The Hasse norm principle for cyclic extensions
decls:
  - GlobalTheory.T.hasseNormPrinciple_of_isCyclic
  - GlobalTheory.CNorm.np_cyclic
  - GlobalTheory.CNorm.hasseNormPrinciple_cyclic_of_finrank
  - GlobalTheory.CNorm.np_of_finrank_prime
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hasse norm principle for cyclic extensions

This section proves Hasse's norm theorem: in a cyclic extension $E/F$ of number fields, a nonzero element of $F$ that is a norm at every place is a norm from $E$. The proof is an induction on the degree. A cyclic group of composite order $n$ has a subgroup of prime order $p$, and its fixed field $M$ cuts $E/F$ into a cyclic extension $M/F$ of degree $n/p$ and a cyclic extension $E/M$ of degree $p$. The norm principle in prime degree and a lemma on cyclic towers then close the induction. The theorem is used in the proof of the [theorem on global matching of product test functions](/entry/g4/) of Volume 8, for base change along a cyclic extension. The first six sections of this chapter worked with groups given by equations; this section and the rest of the chapter work with number fields, Hermitian forms and their unitary groups.

### Local norms

Let $F$ be a number field and $E$ a finite extension of $F$. For a field $L$ that contains $F$, the ring $L \otimes_F E$ is a finite $L$-algebra, and it has a norm $N_{L \otimes_F E / L} \colon L \otimes_F E \to L$, the [[determinant|00KDZRW4C0]] of multiplication. For a place $v$ of $F$ let $F_v$ be the completion ([places and completions](/learn/number-fields/#places-and-completions)). The algebra $F_v \otimes_F E$ is the product of the completions $E_w$ for the places $w$ of $E$ above $v$, and its norm is the product of the local norms $N_{E_w/F_v}$.

**Definition 1.7.1 (Local norm).** Let $x \in F$. We say that $x$ is a *local norm at $v$* if there is $y \in F_v \otimes_F E$ with $N_{F_v \otimes_F E / F_v}(y) = x$. We say that $x$ is an *everywhere local norm* if $x$ is a local norm at every finite place $v$ of $F$ and, for every ring homomorphism $a \colon F \to \mathbb{R}$, there is $y \in \mathbb{R} \otimes_{F,a} E$ with $N_{\mathbb{R} \otimes E / \mathbb{R}}(y) = a(x)$.

Lean: `GlobalTheory.CNorm.LocNorm`.

The real embeddings of $F$ are the real places. At a complex place $v$ every element of $F_v = \mathbb{C}$ is a norm, so the definition asks nothing there. An element $N_{E/F}(y)$ with $y \in E$ is an everywhere local norm, because the norm commutes with the base change $F \to F_v$.

**Definition 1.7.2 (Hasse norm principle).** We say that $E/F$ *satisfies the norm principle* if every nonzero $x \in F$ that is an everywhere local norm is a norm: there is $y \in E$ with $N_{E/F}(y) = x$.

Lean: `GlobalTheory.CNorm.NP`.

**Example 1.7.3.** Let $F = \mathbb{Q}$ and $E = \mathbb{Q}(i)$. The norms from $E$ are the sums of two squares. The element $3$ is not a local norm at $3$, since $x^2 + y^2 = 3$ has no solution in $\mathbb{Q}_3$. The element $-1$ is not a local norm at the real place. The element $2 = 1^2 + 1^2$ is a norm. Hasse's theorem says that a positive rational number which is a sum of two squares in each $\mathbb{Q}_p$ is a sum of two rational squares.

### Prime degree and towers

We take three results as given. They are proved in another part of the development; this chapter does not treat their proofs.

**Theorem 1.7.4 (Quadratic extensions).** Let $E/F$ be an extension of number fields with $[E : F] = 2$. Then $E/F$ satisfies the norm principle.

Lean: `GlobalTheory.T.np_of_finrank_two'`.

**Theorem 1.7.5 (Odd prime degree).** Let $p$ be an odd prime and $E/F$ a Galois extension of number fields with $[E : F] = p$. Then $E/F$ satisfies the norm principle.

Lean: `GlobalTheory.T.np_of_odd_prime_degree'`.

**Theorem 1.7.6 (Cyclic towers).** Let $F \subseteq M \subseteq E$ be number fields with $E/F$ Galois and $\mathrm{Gal}(E/F)$ cyclic. If $E/M$ and $M/F$ satisfy the norm principle, then $E/F$ satisfies the norm principle.

Lean: `GlobalTheory.T.hasseNormPrinciple_of_cyclic_tower`.

The tower theorem is not a formal consequence of the transitivity of the norm. If $x$ is an everywhere local norm from $E$, then it is an everywhere local norm from $M$, so $x = N_{M/F}(y)$ with $y \in M$. But $y$ need not be a local norm from $E$ at every place, and the cyclic hypothesis is used to change $y$ so that it is.

**Lemma 1.7.7 (Prime degree).** Let $p$ be a prime and $E/F$ a Galois extension of number fields with $[E : F] = p$. Then $E/F$ satisfies the norm principle.

Lean: `GlobalTheory.CNorm.np_of_finrank_prime`.

*Proof.* If $p = 2$, this is the theorem on quadratic extensions. If $p$ is odd, this is the theorem on odd prime degree. $\square$

A Galois extension of prime degree is cyclic, since a group of prime order is cyclic. So the lemma is the case of Hasse's theorem in prime degree.

### The induction

**Lemma 1.7.8 (Degree one).** Let $E/F$ be an extension with $[E : F] = 1$. Then $E/F$ satisfies the norm principle.

Lean: `GlobalTheory.CNorm.np_of_finrank_one`.

*Proof.* For $x \in F$ the norm of $x$, as an element of $E = F$, is $x^1 = x$. $\square$

**Theorem 1.7.9 (Hasse norm principle in degree $n$).** Let $n \geq 1$ and let $E/F$ be a Galois extension of number fields of degree $n$ with $\mathrm{Gal}(E/F)$ cyclic. Then $E/F$ satisfies the norm principle.

Lean: `GlobalTheory.CNorm.hasseNormPrinciple_cyclic_of_finrank`.

*Proof.* We use strong induction on $n$. If $n = 1$, apply the lemma on degree one. Let $n > 1$ and write $G = \mathrm{Gal}(E/F)$, so $|G| = n$. Choose a prime $p$ that divides $n$. By Cauchy's theorem there is $g \in G$ of order $p$ ([groups](/learn/algebra/#groups)). Let $H$ be the subgroup generated by $g$. It has order $p$. Since $G$ is cyclic, it is abelian, so $H$ is normal in $G$.

Let $M = E^H$ be the fixed field of $H$ ([Galois theory](/learn/algebra/#galois-theory)). Then $M$ is a number field, $E/M$ is Galois with group $H$, and $[E : M] = |H| = p$. Since $H$ is normal, $M/F$ is Galois, and restriction to $M$ is a surjection $G \to \mathrm{Gal}(M/F)$. A quotient of a cyclic group is cyclic, so $\mathrm{Gal}(M/F)$ is cyclic. From $[M : F]\,[E : M] = n$ and $p > 1$ we get $[M : F] < n$.

By the lemma on prime degree, applied to $E/M$, the extension $E/M$ satisfies the norm principle. By the induction hypothesis, applied to $M/F$, the extension $M/F$ satisfies the norm principle. The theorem on cyclic towers, applied to $F \subseteq M \subseteq E$, gives the norm principle for $E/F$. $\square$

**Theorem 1.7.10 (Norm principle for cyclic extensions).** Let $E/F$ be a Galois extension of number fields with $\mathrm{Gal}(E/F)$ cyclic. Then $E/F$ satisfies the norm principle.

Lean: `GlobalTheory.T.hasseNormPrinciple_of_isCyclic` (also `GlobalTheory.CNorm.np_cyclic`).

*Proof.* This is the [theorem in degree $n$](/entry/hasse-norm-principle-cyclic-of-finrank/) applied to $n = [E : F]$. $\square$

**Remark 1.7.11 (Classical form).** Hasse's norm theorem reads: let $E/F$ be a cyclic extension of number fields and $x \in F^\times$; then $x$ is a norm from $E$ if and only if $x$ is a local norm at every place of $F$ (J. Neukirch, *Algebraic Number Theory*, Chapter VI, §4). The theorem above is the direction "if". The direction "only if" is the paragraph after the definition of local norms, and it is not part of the statement proved here. The local conditions are stated for the algebras $F_v \otimes_F E$ at finite places and $\mathbb{R} \otimes_{F,a} E$ at real embeddings $a$. The complex places are left out, since there the condition is empty.

**Remark 1.7.12 (Formalization).** In [HasseNormPrincipleOfIsCyclic.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/HasseNormPrincipleOfIsCyclic.lean#L18) the lemma on prime degree assumes that $E/F$ is Galois, but the quadratic branch (line 22) does not use it; the quadratic input has no Galois hypothesis. The lemma on degree one (line 12) does not assume that $E$ is a number field. In `GlobalTheory.CNorm.LocNorm`, at [MemPowSub.lean](lean:Development/AbelianVarietyTheory/Definitions/AdelicHermitianForms/MemPowSub.lean#L102), the real condition quantifies over all $F$-algebra structures on $\mathbb{R}$, that is, over all ring homomorphisms $F \to \mathbb{R}$, and the finite condition uses the adic completions of $F$ at its height one primes. The three given results are proved in the files that the statement files `NpOfFinrankTwoStatement.lean`, `NpOfOddPrimeDegreeStatement.lean` and `HasseNormPrincipleOfCyclicTowerStatement.lean` wrap; we have opened only their statements. The wrapper `GlobalTheory.T.hasseNormPrinciple_of_isCyclic` restates `GlobalTheory.CNorm.np_cyclic` without change.
