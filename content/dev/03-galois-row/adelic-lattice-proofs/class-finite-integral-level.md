---
id: class-finite-integral-level
title: Finiteness of class numbers at integral level, by restriction of scalars
kind: theorem
decl: GlobalTheory.ClassFin.classFinite_integralLevel
module: Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ClassNumberFiniteIntegralLevelClosedSubgroupGL
covers: 462
status: drafted
drafted_by: writer@claude
---
This theorem proves the finiteness of class numbers at integral level for a linear group over a number field $F$. It reduces the problem to a group over $\mathbb{Q}$ of determinant one matrices, by restriction of scalars from $F$ to $\mathbb{Q}$. [The double coset theorem for such groups](/entry/finite-adelic-double-cosets-of-rational-sl-subgroup/) does the rest. The class number theorem uses this result through [a second name](/entry/class-number-finite-integral-level-closed-subgroup-gl/), and that entry gives the statement in words.

## Statement

Let $G \subseteq \mathrm{GL}_n$ be cut out by a set $S$ of polynomials over $F$, and let $G(B)$ be a group for every $F$-algebra $B$. Let $K \subseteq G(\mathbb{A}_f)$ be the set of $u$ such that $u$ and $u^{-1}$ have integral entries at every finite place. Then $G(\mathbb{A}_f) = G(F) \cdot T \cdot K$ for a finite set $T \subseteq G(\mathbb{A}_f)$.

## Proof

Let $d = [F : \mathbb{Q}]$ and let $\omega$ be an integral basis of $\mathcal{O}_F$. For a basis $b$ of an $R$-algebra $A$, `emb b g` writes $g \in \mathrm{GL}_n(A)$ as an $nd \times nd$ matrix over $R$, and adds one diagonal entry $\det(g')^{-1}$, where $g'$ is that $nd \times nd$ matrix. So `emb b g` has determinant $1$.

1. **The adelic base ring.** `T.adelic_pair_reduced_basis` gives a reduced $\mathbb{Q}$-algebra $R$ and a subring $R_0$ with `AdelicPair R R₀`. It also gives an $R$-basis $b$ of $\mathbb{A}_f$ with $b_i = \omega_i$. An element of $\mathbb{A}_f$ is integral at every place if and only if its $b$-coordinates are in $R_0$. The lemma does not say what $R$ is, and we have not unfolded its proof.
2. **The $\mathbb{Q}$-group.** `T.exists_isQGroup_weilRestriction_alt` gives a set $\Gamma$ of complex matrices with `IsQGroup Γ`. Let $R$ be a reduced $\mathbb{Q}$-algebra, $A$ an $R$-algebra and $F$-algebra, and $b$ an $R$-basis of $A$ with $b_i = \omega_i$. Then the points of $\Gamma$ over $R$ are exactly the matrices `emb b g` with $g \in G(A)$. The proof uses this for $(R, \mathbb{A}_f, b)$ and for $(\mathbb{Q}, F, \omega)$.
3. **Class finiteness over $\mathbb{Q}$.** `T.finiteAdelicDoubleCosets_of_rational_SL_subgroup` gives `CF Γ R R₀`: a finite $T_0$ such that each point $y$ of $\Gamma$ over $R$ is $\gamma_0 s u_0$ with $\gamma_0$ rational, $s \in T_0$ and $u_0$ with entries in $R_0$.
4. **Back to $F$.** Let $T$ be a set of preimages of $T_0$ under `emb b` (`lift`). For $x \in G(\mathbb{A}_f)$, write `emb b x` $= \gamma_0 s u_0$. Then $\gamma_0$ comes from some $\gamma \in G(F)$ and $u_0$ from some $u \in G(\mathbb{A}_f)$. `T.glFreeAlgebraEmb_integral_and_rational` shows that $u$ and $u^{-1}$ are integral, and that `emb b` of $\gamma$ is `emb ω γ`. `emb b` is an injective homomorphism (`T.glFreeAlgebraToSpecialLinearEmb_injective_hom`), so $x = \gamma \cdot \mathrm{lift}(s) \cdot u$.

## In the Lean code

The theorem is in [ClassNumberFiniteIntegralLevelClosedSubgroupGL.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ClassNumberFiniteIntegralLevelClosedSubgroupGL.lean#L14). `pts`, `IsQGroup`, `AdelicPair`, `CF`, `res` and `emb` are in [AdelicPair.lean](lean:Development/AbelianVarietyTheory/Definitions/AdelicHermitianForms/AdelicPair.lean#L98), with `emb` at line 98. In `emb`, the extra entry is the determinant of the matrix of $g^{-1}$, which is the inverse of $\det(g')$.
