---
title: The second cohomology of an affine curve
decls:
  - GlobalTheory.EtC.etC_c2
  - GlobalTheory.T.subsingleton_Ht_two_of_isDedekindDomain_of_isAlgClosed
  - GlobalTheory.EtC.smoothAffineCurve_tateTwistCohomology_two_subsingleton
  - GlobalTheory.T.exists_kummerClass_agreeing_near_zeros
  - GlobalTheory.EtC.KummerStep.exists_class_agreeing_near_zeros
  - GlobalTheory.T.unit_localization_etaleNbhd_eq_unit_mul_pow
  - GlobalTheory.EtC.kummer_divisor_step
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The second cohomology of an affine curve

This section starts a new part of the chapter. It proves that a smooth affine curve over an [[algebraically closed|0PF6TM8TWT]] field has no [étale cohomology](/learn/geometry/#tale-cohomology) with coefficients $\mathbb{Z}/q(i)$ in degrees at least $2$, when $q$ is a unit in the field. This vanishing is one of the inputs of [the local steps](/entry/steps-holds/) of the chapter on Galois representations, next to the projective bundle formula of the first sections. We prove the case of degree $2$ here. The proof is elementary in spirit: it uses an excision sequence, the Kummer sequence and the divisibility of the class group of the curve, and no general theory of cohomological dimension.

Throughout, $k$ is an algebraically closed field, $q \geq 1$ is a unit in $k$, and $B$ is a [[Dedekind domain|7NPY2CN5KB]] that is a finitely generated $k$-algebra. So $\operatorname{Spec} B$ is a smooth affine curve over $k$, or a point when $B = k$. For a ring $A$ we write $H^n(A, \mathbb{Z}/q(i))$ for the étale cohomology of $\operatorname{Spec} A$ with coefficients $\mathbb{Z}/q(i)$, and for a ring map $A \to A'$ we write $x \mapsto x|_{A'}$ for the restriction map. For $f \in A$ we write $A_f$ for the localization of $A$ at the powers of $f$.

**Theorem 2.9.1 (Cohomological dimension of affine curves).** Let $X$ be an affine scheme of finite type and of dimension $d$ over a separably closed field, and let $F$ be a torsion étale sheaf on $X$. Then $H^n(X, F) = 0$ for $n > d$.

This is Artin's theorem on the cohomological dimension of affine schemes, SGA 4, Exposé XIV, §3. For $d = 1$ it gives the following theorem.

**Theorem 2.9.2 (Vanishing in degrees at least two).** For all integers $n \geq 2$ and $i$, the group $H^n(B, \mathbb{Z}/q(i))$ is zero.

Lean: `GlobalTheory.EtC.etC_c2`.

*Proof.* For $n = 2$ this is [the theorem on degree two](/entry/subsingleton-ht-two-of-is-dedekind-domain-of-is-alg-closed/) below. For $n \geq 3$ we take the vanishing as given in this section. $\square$

Lean: `GlobalTheory.T.smoothAffineCurve_tateTwistCohomology_subsingleton_of_ge_three`.

### Excision neighbourhoods and Kummer classes

**Definition 2.9.3 (Excision neighbourhood).** Let $A$ be a ring and $f \in A$. An *excision neighbourhood* of $f$ is an étale $A$-algebra $A'$ such that the map $A/fA \to A'/fA'$ is bijective.

So $\operatorname{Spec} A'$ is an étale neighbourhood of the zero set of $f$ that does not change it. The ring $A$ itself is an excision neighbourhood of every $f$. If $A'$ is an $A$-algebra, an *excision neighbourhood of $f$ over $A'$* is an excision neighbourhood $A_2$ of $f$ that is also an $A'$-algebra, such that $A \to A' \to A_2$ is the structure map of $A_2$. For an excision neighbourhood the square formed by $A$, $A_f$, $A'$ and $A'_f$ gives a long exact Mayer and Vietoris sequence
$$
\cdots \to H^{n}(A'_f) \xrightarrow{\ \partial\ } H^{n+1}(A) \to H^{n+1}(A') \oplus H^{n+1}(A_f) \to H^{n+1}(A'_f) \to \cdots,
$$
with any coefficients. We use it only through the excision step in the proof of the theorem on degree two.

**Definition 2.9.4 (Kummer class).** Let $A$ be a ring in which $q$ is a unit, and let $u \in A^\times$. The *Kummer class* $\kappa(u) \in H^1(A, \mathbb{Z}/q(1))$ is the class of the $\mu_q$-torsor of $q$-th roots of $u$. Equivalently, $\kappa$ is the boundary map of the Kummer sequence $1 \to \mu_q \to \mathbb{G}_m \xrightarrow{q} \mathbb{G}_m \to 1$ on global units.

We need three properties: $\kappa(uv) = \kappa(u) + \kappa(v)$, $\kappa(v^q) = 0$, and $\kappa$ commutes with restriction along ring maps. So $\kappa(u v^q) = \kappa(u)$.

Lean: `GlobalTheory.T.chernClass_kummerClass_additive` (also `GlobalTheory.T.cup_chern_kummer_pullback_naturality`).

### Degree two

**Theorem 2.9.5 (Degree two).** For every integer $i$, the group $H^2(B, \mathbb{Z}/q(i))$ is zero.

Lean: `GlobalTheory.T.subsingleton_Ht_two_of_isDedekindDomain_of_isAlgClosed` (also `GlobalTheory.EtC.smoothAffineCurve_tateTwistCohomology_two_subsingleton`).

*Proof.* The [[cyclotomic polynomial|08KEYFAH66]] $\Phi_q$ has a root $\zeta$ in $k$, since $k$ is algebraically closed, and $\zeta$ is a primitive $q$-th root of unity in $B$ since $q$ is a unit. With a primitive $q$-th root of unity all twists are isomorphic, so $H^2(B, \mathbb{Z}/q(i)) \cong H^2(B, \mathbb{Z}/q(1))$, and it is enough to treat $i = 1$. Let $x \in H^2(B, \mathbb{Z}/q(1))$.

Step 1. We take as given that there is $f \neq 0$ in $B$ with $x|_{B_f} = 0$. The idea is that $x$ dies on the generic point, a field of transcendence degree one over $k$, and hence on a dense open set.

Step 2. We take as given that there is an excision neighbourhood $A'$ of $f$ with $x|_{A'} = 0$.

Step 3. We take as given the following excision step. There is a class $w \in H^1(A'_f, \mathbb{Z}/q(1))$ with the following property. Suppose that there are $g \in B$ coprime to $f$, an excision neighbourhood $A_2$ of $f$ over $A'$ in which $g$ is a unit, an excision neighbourhood $C$ of $g$, and a class $a \in H^1(B_{fg}, \mathbb{Z}/q(1))$ such that $a|_{C_{fg}} = 0$ and $w|_{(A_2)_f} = a|_{(A_2)_f}$. Then $x = 0$. Here $w$ is a class with $\partial w = x$ in the sequence of the square of $A'$; the conditions say that $w$ agrees near the zeros of $f$ with a class that glues with the zero class on $C$ near the zeros of $g$, and so it has zero boundary.

Step 4. [The theorem on Kummer classes near the zeros](/entry/exists-kummer-class-agreeing-near-zeros/) below gives $g$, $A_2$, $C$ and $a$ for this $w$. So $x = 0$. $\square$

Lean: `GlobalTheory.T.tateTwistCohomology_spec_twist_independent` (also `GlobalTheory.T.exists_localization_away_pull_eq_zero_Ht_two`, `GlobalTheory.T.exists_etaleNbhd_killing_curveCohomologyClass` and `GlobalTheory.T.etaleExcision_vanishing_under_refinement`).

### Kummer classes near the zeros

**Theorem 2.9.6 (Kummer classes near the zeros).** Let $f \neq 0$ in $B$, let $A'$ be an excision neighbourhood of $f$, and let $w \in H^1(A'_f, \mathbb{Z}/q(1))$. Then there are $g \in B$ coprime to $f$, an excision neighbourhood $A_2$ of $f$ over $A'$ in which $g$ is a unit, an excision neighbourhood $C$ of $g$, and a class $a \in H^1(B_{fg}, \mathbb{Z}/q(1))$ such that $a|_{C_{fg}} = 0$ and $w|_{(A_2)_f} = a|_{(A_2)_f}$.

Lean: `GlobalTheory.T.exists_kummerClass_agreeing_near_zeros` (also `GlobalTheory.EtC.KummerStep.exists_class_agreeing_near_zeros`).

*Proof.* Step 1. We take as given that there are an excision neighbourhood $A_2'$ of $f$ over $A'$ and a unit $c$ of $(A_2')_f$ with $w|_{(A_2')_f} = \kappa(c)$. In terms of the Kummer sequence, $H^1(\mathbb{Z}/q(1))$ is an extension of the $q$-torsion of the [[Picard group|3Z9DCWYXQZ]] by units modulo $q$-th powers, and the Picard part dies on a finer neighbourhood.

Step 2. [The theorem on units near the zeros](/entry/unit-localization-etale-nbhd-eq-unit-mul-pow/) below, applied to $c$, gives $g \in B$ coprime to $f$, a unit $u$ of $B_{fg}$, an excision neighbourhood $A_2$ of $f$ over $A_2'$ in which $g$ is a unit, with a unit $v$ of $(A_2)_f$ such that $c = u v^q$ in $(A_2)_f$, and an excision neighbourhood $C$ of $g$ with a unit $v'$ of $C_{fg}$ such that $u = v'^q$ in $C_{fg}$.

Step 3. Let $a = \kappa(u)$. Then $a|_{C_{fg}} = \kappa(v'^q) = 0$. On $(A_2)_f$, by naturality,
$$
\begin{aligned}
w|_{(A_2)_f} &= \kappa(c)|_{(A_2)_f} = \kappa(u v^q) \\
&= \kappa(u) = a|_{(A_2)_f}.
\end{aligned}
$$
$\square$

Lean: `GlobalTheory.T.exists_kummerClass_on_finer_etaleNbhd_curve`.

### Units near the zeros

**Theorem 2.9.7 (Units near the zeros).** Let $f \neq 0$ in $B$, let $A_2$ be an excision neighbourhood of $f$, and let $c$ be a unit of $(A_2)_f$. Then there are $g \in B$ coprime to $f$ and a unit $u$ of $B_{fg}$ with:

1. an excision neighbourhood $A_3$ of $f$ over $A_2$, in which $g$ is a unit, and a unit $v$ of $(A_3)_f$ with $c = u v^q$ in $(A_3)_f$;
2. an excision neighbourhood $C$ of $g$ and a unit $v'$ of $C_{fg}$ with $u = v'^q$ in $C_{fg}$.

Lean: `GlobalTheory.T.unit_localization_etaleNbhd_eq_unit_mul_pow` (also `GlobalTheory.EtC.kummer_divisor_step`).

*Proof.* Since $A_2/fA_2 = B/fB$, every element of $A_2$ is congruent modulo $f$ to an element of $B$. We take as given that $c$ can be written in the form
$$
b_1 = c\, e f^m \quad \text{in } (A_2)_f,
$$
with $b_1 \in B$, $m \geq 0$ and $e \in A_2$ with $e \equiv 1 \pmod f$.

Case $b_1 = 0$. Take $g = 1$, $u = 1$, $C = B$ and $v' = 1$. Let $A_3 = (A_2)_e$, which is an excision neighbourhood of $f$ because $e \equiv 1 \pmod f$. In $(A_3)_f$ the element $c e f^m$ is a unit and equals $0$, so $(A_3)_f$ is the zero ring and every equation holds in it.

Case $b_1 \neq 0$. Step 1. We take as given the following fact on the divisors of $B$. There are $g \neq 0$ coprime to $f$, a unit $u$ of $B_{fg}$ and $n, d, t, n', d' \in B$, with $n$ and $d$ coprime to $f$ and $n'$ and $d'$ coprime to $g$, such that
$$
b_1 d = u\, n f^m \quad \text{and} \quad u\, t^q d' = n' \qquad \text{in } B_{fg}.
$$
Its proof splits the divisor of $b_1$ into the part on the zeros of $f$ and the rest, and uses that the [[class group|WQ46BD3ARY]] of $B$ is divisible by $q$, as a quotient of the group of points of the Jacobian of the complete curve. The new element $g$ carries the rest of the divisor, corrected by a $q$-th power.

Step 2. The two equations give $c\, d e = u\, n$ after restriction to $(A_2)_f$. Near the zeros of $f$ the elements $n$, $d$ and $e$ are units, since $n$ and $d$ are coprime to $f$ and $e \equiv 1$, so there $c = u \cdot n/(de)$. On the zero set of $f$, a finite set of $k$-points, it has $q$-th roots, because $k$ is algebraically closed. Adjoining a $q$-th root is étale because $q$ is a unit. We take as given that this gives an excision neighbourhood $A_3$ of $f$ over $A_2$ in which $g$ is a unit and $n/(de) = v^q$ for a unit $v$ of $(A_3)_f$.

Step 3. In the same way, $u = (n'/d') \cdot t^{-q}$, and $n'/d'$ is a unit near the zeros of $g$. We take as given that there is an excision neighbourhood $C$ of $g$ on which $n'/d'$ is a $q$-th power. Then $u$ is a $q$-th power in $C_{fg}$. $\square$

Lean: `GlobalTheory.T.exists_unit_form_localization_etale_nbhd` (also `GlobalTheory.T.smoothAffineCurve_divisor_unit_decomposition`, `GlobalTheory.T.unit_eq_mul_pow_on_etaleExcisionNbhd_zeroLocus`, `GlobalTheory.T.coprime_unit_etale_extension` and `GlobalTheory.T.classGroup_dedekind_algClosed_divisible`).

**Remark 2.9.8.** In the case $b_1 = 0$ the proof does not look for a decomposition; it inverts $e$ and shows that the target ring is zero. In that case $g = 1$, which is why the statement asks for $g$ coprime to $f$ but not for $g \neq 0$.

**Remark 2.9.9 (Formalization).** The vanishing theorem is the condition $C_2$ of a package of axioms on étale cohomology: [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L105). It says that the groups are subsingletons, which for groups means zero, and $n$ and $i$ are integers. The name of its module ends with a cut form of "le one": [SmoothAffineCurveEtaleCohomologicalDimensionLeOn.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothAffineCurveEtaleCohomologicalDimensionLeOn.lean#L9). The Kummer class is defined by a choice of a cohomology class with a cocycle built from $q$-th roots of $u$: [PullHlComp.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PullHlComp.lean#L137). Its additivity and naturality come from two lemmas on Chern and Kummer classes, whose uses we read, not their proofs. For the four steps of the theorem on degree two, step 1 of the theorem on Kummer classes and the four facts of the theorem on units, we read the statements, not the proofs, except the proof of the divisor step; the explanations of these steps are ours. The proof of the theorem on Kummer classes first proves a general lemma that takes the statements of its steps 1 and 2 as hypotheses: [ExistsKummerClassAgreeingNearZeros.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsKummerClassAgreeingNearZeros.lean#L56). The theorem on units does not ask for $q \neq 0$; this follows from $q$ being a unit in $k$. The equations of the last two theorems are asserted for every pair of ring maps between the localizations that is compatible with the given maps; such a pair is unique, by the universal property of localization. The case $b_1 = 0$ is at [UnitLocalizationEtaleNbhdEqUnitMulPow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitLocalizationEtaleNbhdEqUnitMulPow.lean#L14). The statements of this section with two names import Mathlib twice, raise the heartbeat limit, and are proved by trying three tactics in turn, for example [UnitLocalizationEtaleNbhdEqUnitMulPowStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitLocalizationEtaleNbhdEqUnitMulPowStatement.lean#L7).
