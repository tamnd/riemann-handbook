---
title: Coherent cohomology of projective space
decls:
  - GroundTheory.Arith.SchemeCoh.ProjSpace.serre_step
  - GroundTheory.Arith.SchemeCoh.ProjSpace.serre_all
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Coherent cohomology of projective space

The next three sections leave étale cohomology and prove a theorem on coherent sheaves: for a proper scheme $X$ over a Noetherian ring $A$ and a coherent sheaf $\mathcal{F}$ on $X$, each group $H^p(X, \mathcal{F})$ is a finitely generated $A$-module. This is the finiteness theorem of Grothendieck. The proof of [EveryCharacter](/step/every-character/) uses it through the theorem of Section 6.10. This section proves the case $X = \mathbb{P}^n_A$, together with the vanishing theorem of Serre. The proof is a descending induction on the degree $p$, which starts above $n$ and uses the global generation of twists at each step.

### Coherent sheaves and their cohomology

Let $A$ be a commutative ring and $n \ge 0$. Let $\mathbb{P}^n_A = \operatorname{Proj} A[x_0, \dots, x_n]$, with the standard grading of the polynomial ring and its structure map to $\operatorname{Spec} A$. For $k \in \mathbb{Z}$ let $\mathcal{O}(k)$ be the twisting sheaf: on the standard open $D_+(x_j)$ its sections are the fractions $f / x_j^e$ with $f$ homogeneous of degree $k + e$. For a sheaf $\mathcal{G}$ of $\mathcal{O}$-modules on $\mathbb{P}^n_A$ we write $\mathcal{G}(k) = \mathcal{G} \otimes \mathcal{O}(k)$. The twists satisfy $\mathcal{G}(k)(l) \cong \mathcal{G}(k + l)$ and $\mathcal{G}(0) \cong \mathcal{G}$, and twisting is an exact functor, since $\mathcal{O}(k)$ is invertible.

**Definition 6.8.1 (Coherent sheaf).** Let $X$ be a scheme. A sheaf $\mathcal{F}$ of $\mathcal{O}_X$-modules is *coherent* if it is quasi-coherent and, for each affine open $U \subseteq X$, the $\Gamma(U, \mathcal{O}_X)$-module $\Gamma(U, \mathcal{F})$ is finitely generated.

Lean: `GroundTheory.Arith.SchemeCoh.IsCoherent`.

On a locally Noetherian scheme this is the usual notion (Hartshorne, *Algebraic Geometry*, II §5). The definition asks for finiteness on every affine open. So it needs no choice of a cover.

**Definition 6.8.2 (Cohomology as an $A$-module).** Let $X$ be a scheme over $\operatorname{Spec} A$ and $\mathcal{F}$ a sheaf of $\mathcal{O}_X$-modules. Then $H^p(X, \mathcal{F})$ is the $p$-th derived functor of global sections, applied to the underlying sheaf of abelian groups of $\mathcal{F}$. The ring $A$ acts on it through $A \to \Gamma(X, \mathcal{O}_X)$.

Lean: `GroundTheory.Arith.SchemeCoh.algebraOfOver` (the action), with Mathlib's `Sheaf.H` of `modulesAb F`.

By Hartshorne III, Proposition 2.6, this is also the derived functor cohomology computed in $\mathcal{O}_X$-modules. A short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$ gives a long exact sequence of $A$-modules. We use two consequences. If $A$ is Noetherian and $H^p(\mathcal{F})$ and $H^{p+1}(\mathcal{F}')$ are finitely generated, then $H^p(\mathcal{F}'')$ is finitely generated: it is an extension of a submodule of $H^{p+1}(\mathcal{F}')$ by a quotient of $H^p(\mathcal{F})$. If $H^p(\mathcal{F}) = 0$ and $H^{p+1}(\mathcal{F}') = 0$, then $H^p(\mathcal{F}'') = 0$.

### Three inputs

**Theorem 6.8.3 (Cohomology of the twisting sheaves).** Let $A$ be a commutative ring. For each $k \in \mathbb{Z}$ and $p \ge 0$, the $A$-module $H^p(\mathbb{P}^n_A, \mathcal{O}(k))$ is finitely generated. If $k \ge 0$ and $p > 0$, then $H^p(\mathbb{P}^n_A, \mathcal{O}(k)) = 0$.

Lean: `GroundTheory.Arith.SchemeCoh.ProjSpace.finite_H_twistingSheaf`, `GroundTheory.Arith.SchemeCoh.ProjSpace.subsingleton_H_twistingSheaf`.

*Proof.* This is the computation of Hartshorne III, Theorem 5.1. The standard opens $D_+(x_0), \dots, D_+(x_n)$ are affine, and so are their intersections. So the Čech complex of this cover computes the cohomology of each quasi-coherent sheaf. For $\mathcal{O}(k)$ the Čech complex is the degree $k$ part of the complex of localizations $A[x_0, \dots, x_n]_{x_{i_0} \cdots x_{i_p}}$. Its cohomology vanishes in the degrees $0 < p < n$. In degree $n$ it is the free $A$-module on the Laurent monomials $x_0^{m_0} \cdots x_n^{m_n}$ with all $m_i < 0$ and $\sum m_i = k$. In degree $0$ it is the free module on the monomials of degree $k$ with all $m_i \ge 0$. In each degree there are finitely many such monomials, so each group is finitely generated. If $k \ge 0$, a sum of $n + 1$ negative integers is never $k$, so $H^n = 0$. $\square$

**Proposition 6.8.4 (Vanishing above the dimension).** Let $A$ be a commutative ring and $\mathcal{G}$ a quasi-coherent sheaf on $\mathbb{P}^n_A$. Then $H^p(\mathbb{P}^n_A, \mathcal{G}) = 0$ for all $p > n$.

Lean: `GroundTheory.Arith.SchemeCoh.ProjSpace.subsingleton_H_of_lt`.

*Proof.* The cover by the $n + 1$ standard opens has affine intersections. So the Čech complex of the cover computes $H^p(\mathbb{P}^n_A, \mathcal{G})$, as in Hartshorne III, Theorem 4.5. The alternating Čech complex of a cover by $n + 1$ opens has no terms in degrees above $n$. $\square$

**Theorem 6.8.5 (Serre, global generation).** Let $A$ be a commutative ring and $\mathcal{G}$ a coherent sheaf on $\mathbb{P}^n_A$. Then there is $q_0 \ge 0$ such that for every $q \ge q_0$ the sheaf $\mathcal{G}(q)$ is generated by finitely many global sections: there are a finite set $I$ and an epimorphism $\mathcal{O}^{I} \to \mathcal{G}(q)$.

Lean: `GroundTheory.Arith.SchemeCoh.ProjSpace.exists_generatingSections_twist`.

*Proof.* This is Hartshorne II, Theorem 5.17. For each $j$ the module $\Gamma(D_+(x_j), \mathcal{G})$ is finitely generated. For each generator $s$ there is $m_s$ such that for all $m \ge m_s$ the section $x_j^m s$ of $\mathcal{G}(m)$ over $D_+(x_j)$ extends to a global section. Let $q_0$ be the maximum of the finitely many $m_s$. For $q \ge q_0$ the extended sections generate $\mathcal{G}(q)$ on each $D_+(x_j)$, because multiplication by $x_j^q$ is an isomorphism $\mathcal{G} \to \mathcal{G}(q)$ over $D_+(x_j)$. $\square$

### The descending induction

For a coherent $\mathcal{G}$ and $p \ge 0$, let $S(p, \mathcal{G})$ be the statement: $H^p(\mathbb{P}^n_A, \mathcal{G})$ is finitely generated over $A$, and if $p > 0$ there is $q_0$ with $H^p(\mathbb{P}^n_A, \mathcal{G}(q)) = 0$ for all integers $q \ge q_0$.

**Lemma 6.8.6 (The induction step).** Let $A$ be a Noetherian ring and $p \ge 0$. Assume that for each coherent sheaf $\mathcal{R}$ on $\mathbb{P}^n_A$ the module $H^{p+1}(\mathbb{P}^n_A, \mathcal{R})$ is finitely generated and that there is $q_0$ with $H^{p+1}(\mathbb{P}^n_A, \mathcal{R}(q)) = 0$ for all $q \ge q_0$. Then $S(p, \mathcal{G})$ holds for each coherent sheaf $\mathcal{G}$ on $\mathbb{P}^n_A$.

Lean: `GroundTheory.Arith.SchemeCoh.ProjSpace.serre_step`.

*Proof.* By the Theorem 6.8.5, take $q_0$ and an epimorphism $\psi : \mathcal{O}^I \to \mathcal{G}(q_0)$ with $I$ finite. Its kernel $\mathcal{K}$ is coherent, since $A$ is Noetherian and the kernel of a map of coherent sheaves on a Noetherian scheme is coherent. For each $k \in \mathbb{Z}$, twisting gives a short exact sequence
$$0 \to \mathcal{K}(k) \to \mathcal{O}(k)^I \to \mathcal{G}(q_0 + k) \to 0.$$
*Finiteness.* Take $k = -q_0$. The module $H^p(\mathcal{O}(-q_0)^I)$ is a finite direct sum of the modules of the Theorem 6.8.3, so it is finitely generated. The module $H^{p+1}(\mathcal{K}(-q_0))$ is finitely generated by the hypothesis, applied to the coherent sheaf $\mathcal{K}(-q_0)$. The long exact sequence shows that $H^p(\mathcal{G})$ is finitely generated.
*Vanishing.* Let $p > 0$. The hypothesis, applied to $\mathcal{K}$, gives $q_1$ with $H^{p+1}(\mathcal{K}(q')) = 0$ for $q' \ge q_1$. Let $q \ge q_0 + q_1$ and take $k = q - q_0 \ge q_1$. Then $H^{p+1}(\mathcal{K}(k)) = 0$, and $H^p(\mathcal{O}(k)^I) = 0$ by the second part of Theorem 6.8.3, since $k \ge 0$ and $p > 0$. The long exact sequence gives $H^p(\mathcal{G}(q)) = 0$. $\square$

**Theorem 6.8.7 (Finiteness and vanishing on projective space).** Let $A$ be a Noetherian ring and $d \ge 0$. Then $S(p, \mathcal{G})$ holds for each $p$ with $n < p + d$ and each coherent sheaf $\mathcal{G}$ on $\mathbb{P}^n_A$.

Lean: `GroundTheory.Arith.SchemeCoh.ProjSpace.serre_all`.

*Proof.* Induction on $d$. If $d = 0$, then $p > n$. The Proposition 6.8.4 gives $H^p(\mathcal{G}) = 0$ and $H^p(\mathcal{G}(q)) = 0$ for all $q$, so $S(p, \mathcal{G})$ holds with $q_0 = 0$. For the step from $d$ to $d + 1$, let $n < p + d + 1$. Then $n < (p + 1) + d$, so the induction hypothesis gives $S(p + 1, \mathcal{R})$ for every coherent $\mathcal{R}$. Since $p + 1 > 0$, this is the hypothesis of the [Lemma 6.8.6](/entry/serre-step/), which gives $S(p, \mathcal{G})$. $\square$

With $d = n + 1$ every $p$ is covered. For the vanishing we also need one bound $q_0$ that works for all $p > 0$ at once. Only the degrees $1 \le p \le n$ need a bound, since the higher ones vanish for all twists.

**Corollary 6.8.8 (Serre).** Let $A$ be a Noetherian ring and $\mathcal{G}$ a coherent sheaf on $\mathbb{P}^n_A$. Then $H^p(\mathbb{P}^n_A, \mathcal{G})$ is a finitely generated $A$-module for each $p \ge 0$. There is $q_0$ such that $H^p(\mathbb{P}^n_A, \mathcal{G}(q)) = 0$ for all $q \ge q_0$ and all $p > 0$.

Lean: `GroundTheory.Arith.SchemeCoh.ProjSpace.finite_H`, `GroundTheory.Arith.SchemeCoh.ProjSpace.exists_subsingleton_H_twist`.

*Proof.* The [Theorem 6.8.7](/entry/serre-all/) with $d = n + 1$ gives the finiteness and, for each $p$, a bound $q_0(p)$. Take $q_0 = q_0(1) + \cdots + q_0(n)$. For $p \le n$ we have $q_0 \ge q_0(p)$. For $p > n$ the Proposition 6.8.4 applies to $\mathcal{G}(q)$. $\square$

This is Hartshorne III, Theorem 5.2. The proof follows Hartshorne's proof. Hartshorne reduces to sheaves of the form $\mathcal{O}(k)^I$ through an epimorphism $\mathcal{O}(-q_0)^I \to \mathcal{G}$, which is the sequence above with $k = -q_0$.

**Remark 6.8.9 (Formalization).** The cohomology groups are Mathlib's derived functor groups `Sheaf.H` with a universe parameter, and the existence of the Ext groups (`HasExt`) is an instance argument. In `serre_step` the finiteness half of the conclusion holds for all $p$, including $p = 0$; only the vanishing half carries the condition $p > 0$. The two input results on $\mathcal{O}(k)$ and the vanishing above the dimension hold for every commutative ring $A$ ([PSpaceFinite.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProjectiveCohomology/PSpaceFinite.lean#L310) has no Noetherian hypothesis). The Noetherian hypothesis enters through the coherence of the kernel and through the long exact sequence.
