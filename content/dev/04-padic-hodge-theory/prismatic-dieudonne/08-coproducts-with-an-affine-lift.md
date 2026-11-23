---
title: Coproducts with an affine lift
decls:
  - GlobalTheory.CopEx.exists_cop
  - GlobalTheory.T.exists_coproductThickening_quotient_freeThickening
  - GlobalTheory.PDForm.CopPoincare.exists_cop_qAt
  - GlobalTheory.T.exists_coproduct_thickening_affine_lift_poincare
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Coproducts with an affine lift

This section proves that a thickening at level $n + 1$ and the thickening of an affine open of a smooth lift have a coproduct among thickenings at level $n + 1$, and that the map from the first thickening into the coproduct is a quasi-isomorphism in low degrees. The coproduct is built as a quotient of a free thickening from [the last section](/entry/exists-free/). The next section uses it to show that restriction to an affine lift is bijective in degrees one and two.

We keep the notation of the last section: thickenings, levels, the complex $K^\bullet$, quasi-isomorphisms in low degrees and free thickenings.

**Definition 5.8.1 (Crystalline datum).** A *crystalline datum* consists of a ring $R$, an ideal $I$ of $R$ with a nilpotent divided power structure $\kappa$, schemes $X$ and $X_0$, morphisms $s : X \to \mathrm{Spec}\, R$, $t : X_0 \to \mathrm{Spec}\, R$ and $i : X_0 \to X$, such that $s$ is smooth, separated and quasi-compact, and there is a morphism $s_0 : X_0 \to \mathrm{Spec}(R/I)$ such that the square formed by $i$, $s_0$, $s$ and $\mathrm{Spec}(R/I) \to \mathrm{Spec}\, R$ is a pullback and $t$ is $s_0$ followed by $\mathrm{Spec}(R/I) \to \mathrm{Spec}\, R$.

**Definition 5.8.2 (Affine lift).** Let $D$ be a crystalline datum. For an affine open $U$ of $X$ let $O(U)$ be its ring of sections and $j_U : \mathrm{Spec}\, O(U) \to X$ the canonical map. An *affine lift* $\Lambda$ of $D$ consists of a thickening $L(U)$ of $X_0$ for each affine open $U$ of $X$, a morphism $L(U) \to L(V)$ for each $V \subseteq U$, functorial in the inclusions, and $R$-algebra isomorphisms $e_U : O(U) \to B_{L(U)}$ compatible with restriction, such that $J_{L(U)} = I B_{L(U)}$, the map $i \circ x_{L(U)}$ equals $j_U \circ \mathrm{Spec}(\pi_{L(U)} \circ e_U)$, and $i \circ x_{L(U)}$ maps into $U$.

**Definition 5.8.3 (Coproduct at a level).** Fix $N$. Let $l : T \to G$ and $r : A \to G$ be morphisms. We say that $(l, r)$ is a *coproduct at level* $N$ if $G$ is at level $N$ and for each $S$ at level $N$ and morphisms $a : T \to S$ and $b : A \to S$ there is a unique $c : G \to S$ with $c \circ l = a$ and $c \circ r = b$.

**Theorem 5.8.4 (A coproduct through a quotient).** Let $D$ be a crystalline datum and $\Lambda$ an affine lift of $D$. Let $n \geq 0$, let $U$ be an affine open of $X$ and let $T$ be a thickening of $X_0$ at level $n + 1$ such that $i \circ x_T$ maps into $U$. Then there are thickenings $F$ and $G$ of $X_0$ and morphisms $u : T \to F$, $q : F \to G$ and $r : L(U) \to G$ such that:

1. $u$ is a quasi-isomorphism in low degrees and $F$ is at level $n + 1$;
2. the ring map $q$ is surjective, and $b \in J_F$ for every $b \in B_F$ with $q(b) \in J_G$;
3. $(q \circ u, r)$ is a coproduct at level $n + 1$.

Lean: `GlobalTheory.CopEx.exists_cop` (also `GlobalTheory.T.exists_coproductThickening_quotient_freeThickening`, a wrapper).

*Proof.* We take as given these results. First, $O(U)$ is smooth over $R$. Second, for a thickening $S$ and an $R$-algebra map $y : O(U) \to B_S$, the map $j_U \circ \mathrm{Spec}(\pi_S \circ y)$ equals $i \circ x_S$ if and only if there is a morphism $b : L(U) \to S$ with $b(e_U(z)) = y(z)$ for all $z$. Third, if $i \circ x_S$ maps into $U$, then there is a ring map $g : O(U) \to B_{S,0}$ with $j_U \circ \mathrm{Spec}(g) = i \circ x_S$ and $g$ compatible with $R$. Fourth, two ring maps $g, g' : O(U) \to C$ with $j_U \circ \mathrm{Spec}(g) = j_U \circ \mathrm{Spec}(g')$ are equal. Fifth, for a sub divided power ideal $\mathfrak{b}$ of $B_S$ there is a quotient $q : S \to S'$ with $q$ surjective, kernel $\mathfrak{b}$, $J_{S'} = q(J_S)$, every level of $S$ also a level of $S'$, and a unique factorization through $q$ of each morphism that kills $\mathfrak{b}$. Sixth, the ideal spanned by the $\delta_j(x)$ with $j \geq 1$ and $x$ in a subset of $J$ is a sub divided power ideal.

1. *A presentation.* Since $O(U)$ is of finite type over $R$, choose $m$ and a surjection $\mathrm{pr} : R[X_1, \ldots, X_m] \to O(U)$. Let $g : O(U) \to B_{T,0}$ be the map of the third input, and choose $b_l \in B_T$ with $\pi_T(b_l) = g(\mathrm{pr}(X_l))$.
2. *A free thickening.* By the theorem on finitely many free variables of the last section, take $(u, \tau)$ free at level $n + 1$ with $m$ elements, $u : T \to F$. Let $\psi : R[X_1, \ldots, X_m] \to B_F$ be the $R$-algebra map with $\psi(X_l) = u(b_l) + \tau_l$. Since $\tau_l \in J_F$, the maps $\pi_F \circ \psi$ and $u_0 \circ g \circ \mathrm{pr}$ agree on constants and on the $X_l$, so they are equal. So $\psi$ maps the kernel of $\mathrm{pr}$ into $J_F$.
3. *The quotient.* Let $\mathfrak{b}$ be the ideal spanned by the $\delta_{F,j}(\psi(k))$ with $j \geq 1$ and $\mathrm{pr}(k) = 0$. By the sixth input it is a sub divided power ideal; let $q : F \to G$ be the quotient of the fifth input. Then $G$ is at level $n + 1$. Since $\delta_{F,1}(\psi(k)) = \psi(k)$, the map $q \circ \psi$ kills the kernel of $\mathrm{pr}$, so it gives $y : O(U) \to B_G$ with $y \circ \mathrm{pr} = q \circ \psi$. By step 2, $\pi_G \circ y = (q \circ u)_0 \circ g$, so $y$ satisfies the condition of the second input, which gives $r : L(U) \to G$ with $r \circ e_U = y$.
4. *Condition 2.* The map $q$ is surjective. If $q(b) \in J_G = q(J_F)$, then $q(b) = q(j)$ with $j \in J_F$, so $b - j \in \mathfrak{b} \subseteq J_F$ and $b \in J_F$.
5. *Existence of maps.* Let $S$ be at level $n + 1$, $a : T \to S$ and $b : L(U) \to S$. By the fourth input, $\pi_S(b(e_U(z))) = a_0(g(z))$ for all $z$. So $c_l = b(e_U(\mathrm{pr}(X_l))) - a(b_l)$ lies in $J_S$. Freeness gives $g' : F \to S$ with $g' \circ u = a$ and $g'(\tau_l) = c_l$. Then $g' \circ \psi = b \circ e_U \circ \mathrm{pr}$, since both send $X_l$ to $a(b_l) + c_l$. So for $j \geq 1$ and $\mathrm{pr}(k) = 0$ we get $g'(\delta_{F,j}(\psi(k))) = \delta_{S,j}(g'(\psi(k))) = \delta_{S,j}(0) = 0$, and $g'$ kills $\mathfrak{b}$. So $g' = c \circ q$ for a morphism $c : G \to S$. Then $c \circ q \circ u = a$, and $c \circ r = b$, since both agree on $e_U(\mathrm{pr}(p))$ for every $p$.
6. *Uniqueness.* If $c'$ also has these properties, then $c' \circ q$ satisfies the conditions that fix $g'$: we have $\tau_l = \psi(X_l) - u(b_l)$, so $c'(q(\tau_l)) = b(e_U(\mathrm{pr}(X_l))) - a(b_l) = c_l$. So $c' \circ q = g' = c \circ q$, and $c' = c$ by the uniqueness of the factorization through $q$. $\square$

**Theorem 5.8.5 (Coproduct with an affine lift).** Let $D$, $\Lambda$, $n$, $U$ and $T$ be as in the last theorem. Then there are a thickening $G$ of $X_0$ and morphisms $l : T \to G$ and $r : L(U) \to G$ such that $(l, r)$ is a coproduct at level $n + 1$ and $l$ is a quasi-isomorphism in low degrees.

Lean: `GlobalTheory.PDForm.CopPoincare.exists_cop_qAt` (also `GlobalTheory.T.exists_coproduct_thickening_affine_lift_poincare`, a wrapper).

*Proof.* Take $F$, $G$, $u$, $q$ and $r$ from the last theorem and put $l = q \circ u$. We use the inputs of the last proof, and that $O(U)$ is formally smooth over $R$.

1. *The kernel of $q$ is nilpotent.* Let $N$ be such that all products of divided powers in $J_F$ of total degree at least $N$ vanish. For $x_1, \ldots, x_N \in J_F$ we have $x_1 \cdots x_N = \delta_1(x_1) \cdots \delta_1(x_N) = 0$. So $J_F^N = 0$. By condition 2 the kernel of $q$ lies in $J_F$, so it is nilpotent.
2. *A lift of the sections.* Put $y = r \circ e_U : O(U) \to B_G$. Since $O(U)$ is formally smooth and $q$ is surjective with nilpotent kernel, there is an $R$-algebra map $y' : O(U) \to B_F$ with $q \circ y' = y$.
3. *The reductions agree.* The map $q_0$ is injective: if $q_0(\pi_F(b)) = 0$, then $q(b) \in J_G$, so $b \in J_F$. It is surjective since $q$ is. So $\mathrm{Spec}(q_0)$ is an isomorphism. By the second input in one direction, $j_U \circ \mathrm{Spec}(\pi_G \circ y) = i \circ x_G$. Since $\pi_G \circ q = q_0 \circ \pi_F$, $x_G = x_F \circ \mathrm{Spec}(q_0)$ and $\mathrm{Spec}(q_0)$ is an isomorphism, we get $j_U \circ \mathrm{Spec}(\pi_F \circ y') = i \circ x_F$. The second input gives $b' : L(U) \to F$ with $b' \circ e_U = y'$. Then $q \circ b' = r$, since both agree on $e_U(z)$ for all $z$.
4. *A section of $q$.* The coproduct property for $S = F$, $a = u$ and $b = b'$ gives $s : G \to F$ with $s \circ l = u$ and $s \circ r = b'$. Then $q \circ s \circ l = l$ and $q \circ s \circ r = q \circ b' = r$, so $q \circ s$ is the identity of $G$ by uniqueness.
5. *Cohomology.* Write $H(f)$ for the map that $f$ induces on $H^j$, for $j \leq 2$. Then $H(q) H(s)$ is the identity and $H(s) H(l) = H(u)$ is bijective. So $H(s)$ is surjective, and it is injective since it has a left inverse. So $H(s)$ is bijective, and $H(l) = H(s)^{-1} H(u)$ is bijective. $\square$

The coproduct is built as a quotient of a free thickening, so it is not unique as a construction, but the universal property fixes it up to a unique isomorphism among thickenings of level $n + 1$. The level matters: the coproduct property is tested only against thickenings at level $n + 1$, and the next section works one level at a time.

**Remark 5.8.6 (Formalization).** The two theorems are in [ExistsCoproductThickeningQuotientFreeThickening.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCoproductThickeningQuotientFreeThickening.lean#L17) and [ExistsCoproductThickeningAffineLiftPoincare.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCoproductThickeningAffineLiftPoincare.lean#L41), with the nilpotence of step 1 as `isNilpotent_of_isNilDP` at line 16 and the retract fact of step 5 from `qAt_formal` in FourTermComplexQuasiIsoAtFormalProperties.lean. The crystalline datum is `Data` in [BijectiveCechDeRhamComparisonDegreeOne.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/BijectiveCechDeRhamComparisonDegreeOne.lean#L16), and coproducts and affine lifts are `IsCop` and `Lift` in [DivPowerCompatTwoFormDerivativeCompOneForm.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivPowerCompatTwoFormDerivativeCompOneForm.lean#L223). The second, third and fourth inputs of the first proof are three parts of one statement on affine lifts, and the fifth is a separate statement on quotients; we read their statements only. An affine lift gives a thickening for every affine open of $X$, with no condition of level; that statement on affine lifts also gives one level that works for all of them.
