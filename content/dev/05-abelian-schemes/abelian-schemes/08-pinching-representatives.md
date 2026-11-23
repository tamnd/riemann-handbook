---
title: Pinching representatives
decls:
  - GlobalTheory.Pinch.hasRep_pinched
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pinching representatives

This section proves Theorem (Pinching), stated in the section on the reduced case and used there in the noetherian induction: good representatives over $\mathrm{Spec}\, R'$ and over $\mathrm{Spec}\, R/\mathfrak{c}$ give one over $\mathrm{Spec}\, R$. The proof checks the criterion of the last section, Theorem (Descent from a finite cover): near each point, the representative over $\mathrm{Spec}\, R'$ must come from a smooth family over $\mathrm{Spec}\, R$. We first pinch a smooth $R$-scheme $U$ from smooth pieces over $R'$ and $R/\mathfrak{c}$, and then patch a line bundle on $A \times U$ from the two pieces.

Throughout, $R$ is a noetherian ring, $R'$ a finite $R$-algebra with $R \to R'$ injective, and $\mathfrak{c}$ an ideal of $R$ with the condition of Theorem (Pinching): for $x \in \mathfrak{c}$ and $r \in R'$ there is $y \in \mathfrak{c}$ with $y = x r$ in $R'$. We put $S = \mathrm{Spec}\, R$, $S' = \mathrm{Spec}\, R'$, $Z = \mathrm{Spec}\, R/\mathfrak{c}$, and $Z' = S' \times_S Z = \mathrm{Spec}\, R'/\mathfrak{c} R'$. Products are over $S$ unless we say otherwise.

**Definition 1.8.1 (Pinched chart).** Let $b' : B' \to S'$ and $e : C \to Z$ be morphisms, and let $Y$ be a scheme with morphisms $i : Y \to B'$ and $q : Y \to C$. Let $x \in B'$. A *pinched chart of dimension $g$ at $x$* consists of an $S$-scheme $U$, smooth of relative dimension $g$, and morphisms $p : U' \to U$, $j : U' \to B'$, $n : V \to U$ and $k : V \to C$ with these properties.

1. The square formed by $p$, $b' \circ j$, $U \to S$ and $S' \to S$ is cartesian, so $U' = U \times_S S'$. The square formed by $n$, $e \circ k$, $U \to S$ and $Z \to S$ is cartesian, so $V = U \times_S Z$.
2. $j$ is an open immersion, and $x$ lies in its image.
3. For each scheme $T$ and all $a : T \to U'$ and $a' : T \to V$ with $p \circ a = n \circ a'$, there is $y : T \to Y$ with $i \circ y = j \circ a$ and $q \circ y = k \circ a'$.

So $U \times_S S'$ is an open piece of $B'$, $U \times_S Z$ maps to $C$, and the two maps are compatible through $Y$.

We use the following facts.

1. (Comparison.) Let $(b' : B' \to S', P')$ be a representative of the dual of $A$ over $S'$ and $(e : C \to Z, Q)$ one over $Z$. Then there is a $Z$-morphism $q : B' \times Z \to C$ such that the square formed by $q$, $b' \circ \mathrm{pr}_{B'}$, $C \to S$ and $S' \to S$ is cartesian, and $P'$ at $\mathrm{pr}_{B'}$ agrees with $Q$ at $q$.
2. (Away from the closed part.) Let $b' : B' \to S'$ be smooth of relative dimension $g$, and let $e$, $Y$, $i$, $q$ be as in the definition. If the image of $x \in B'$ in $S$ does not lie in $Z$, there is a pinched chart of dimension $g$ at $x$.
3. (Standard smooth neighbourhoods.) Let $e : C \to Z$ be smooth of relative dimension $g$. Each point of $C$ has an affine open neighbourhood $O$ such that for each $r \in \Gamma(O, \mathcal{O})$, the ring $\Gamma(D(r), \mathcal{O})$ is a standard smooth $R/\mathfrak{c}$-algebra of relative dimension $g$.
4. (Saturated affine open sets.) Let $i : Y \to B'$ be a closed immersion and $q : Y \to C$ finite, and suppose that each finite set of points of $B'$ lies in an affine open set. Let $y \in Y$ and let $O$ be an affine open neighbourhood of $q(y)$. Then there are an affine open set $V' \ni i(y)$ of $B'$ and $r \in \Gamma(O, \mathcal{O})$ with $i^{-1}(V') = q^{-1}(D(r))$.
5. (Restriction.) Suppose that the two squares of Proposition (Local pinched charts) below are cartesian. Let $V' \subseteq B'$ and $V \subseteq C$ be open with $i^{-1}(V') = q^{-1}(V)$. Then the restricted squares for $V'$, $V$ and $i^{-1}(V')$ are cartesian, and a pinched chart at a point of $V'$ for the restricted data is one for the original data.
6. (Flat base change of the conductor square.) Let $X$ be a flat $S$-scheme, $X' = X \times_S S'$ with projection $p$, and $X_Z = X \times_S Z$ with projection $i$. Then for each affine open set $W$ of $X$, the map $p^* : \mathcal{O}(W) \to \mathcal{O}(p^{-1} W)$ is injective, and for each $x \in \mathcal{O}(W)$ with $i^* x = 0$ and each $r \in \mathcal{O}(p^{-1} W)$ there is $y \in \mathcal{O}(W)$ with $i^* y = 0$ and $p^* y = p^* x \cdot r$.
7. (Descent of additive families.) Let $U$ be a locally noetherian $S$-scheme, $p : U' \to U$ finite and surjective, and $N'$ an additive family on $A \times U'$. Let $c \in \mathrm{Pic}(A \times U)$ with $(1 \times p)^* c = [N']$. Then there is an additive family $M$ on $A \times U$ such that $M$ at $p$ agrees with $N'$ at $\mathrm{id}_{U'}$.

Fact 1 holds because $B' \times_S Z = B' \times_{S'} Z'$ and $C \times_S S' = C \times_Z Z'$ both represent the dual of $A$ over $Z'$. Fact 2 holds because away from $Z$ the map $S' \to S$ is an isomorphism: for $f \in \mathfrak{c}$ the conductor condition gives $R_f = R'_f$.

**Lemma 1.8.2 (Lifting a standard smooth algebra).** Let $C'$ be a smooth $R'$-algebra and $D$ a standard smooth $R/\mathfrak{c}$-algebra of relative dimension $g$. Let $E$ be a ring with maps $\pi : C' \to E$ and $\psi : D \to E$ such that $E = C' \otimes_R R/\mathfrak{c}$ through $\pi$ and $E = D \otimes_R R'$ through $\psi$. Then there are a standard smooth $R$-algebra $F$ of relative dimension $g$, an element $t \in C'$, and maps $\alpha : F \to C'_t$, $\beta : F \to D$ and $\tau : C'_t \to E$, such that $\alpha$ gives $F \otimes_R R' \cong C'_t$, $\beta$ gives $F \otimes_R R/\mathfrak{c} \cong D$, $\tau$ restricted to $C'$ is $\pi$, and $\tau \circ \alpha = \psi \circ \beta$.

Lean: `GlobalTheory.Pinch.exists_standardSmooth`.

*Proof.* Choose a standard smooth presentation of $D$ over $R/\mathfrak{c}$ with variables $\nu$ and relations $\sigma$, so $|\nu| - |\sigma| = g$. The map $\pi$ is surjective with kernel $\mathfrak{c} C'$. Choose generators $\xi$ of $C'$ over $R'$, indexed by $X = \kappa \sqcup \nu$ for a finite set $\kappa$, such that $\pi(\xi_s) = 0$ for $s \in \kappa$ and $\pi(\xi_s)$ is the image in $E$ of the $s$-th generator of $D$ for $s \in \nu$. Adding the variables $\kappa$ with value $0$ and one relation each gives a presentation of $D$ with variables $X$ and relations $\kappa \sqcup \sigma$, still of relative dimension $g$. By the conductor condition, each relation lifts to a polynomial $F_s$ over $R$ whose image over $R'$ vanishes at $\xi$. Since $C'$ is flat over $R'$, a Nakayama argument gives $H$ over $R$, zero modulo $\mathfrak{c}$, such that $H + 1$ multiplies the kernel of $R'[X] \to C'$ into $(F_s)$. Let $\Delta$ be the Jacobian determinant of the $F_s$, and let $F = R[X]/(F_s)$ localized at $\Delta (H + 1)$. Then $F$ is standard smooth of relative dimension $g$, its base change to $R'$ is $C'_t$ with $t$ the image of $\Delta (H + 1)$, and its base change to $R/\mathfrak{c}$ is $D$, where $\Delta(H + 1)$ maps to the Jacobian of the presentation, a unit. So $t$ maps to a unit of $E$, which gives $\tau$. $\square$

**Lemma 1.8.3 (Affine pinched charts).** In the situation of Lemma (Lifting a standard smooth algebra), take $B' = \mathrm{Spec}\, C'$, $C = \mathrm{Spec}\, D$, $Y = \mathrm{Spec}\, E$, with $i$ and $q$ given by $\pi$ and $\psi$. Then for each $y \in Y$ there is a pinched chart of dimension $g$ at $i(y)$.

Lean: `GlobalTheory.Pinch.pinched_spec`.

*Proof.* Take $F$, $t$, $\alpha$, $\beta$, $\tau$ from the last lemma, and put $U = \mathrm{Spec}\, F$, $U' = \mathrm{Spec}\, C'_t$, $V = \mathrm{Spec}\, D$, with $j : U' \to B'$ the open immersion of $D(t)$ and $k$ the identity. Then $U$ is smooth of relative dimension $g$ over $S$, and the two base change isomorphisms give property 1. The point $i(y)$ lies in $D(t)$ because $\tau$ exists. For property 3, let $a : T \to U'$ and $a' : T \to V$ with $p \circ a = n \circ a'$. The two composites $T \to \mathrm{Spec}\, C' \to S$ and $T \to Z \to S$ agree, and $Y = \mathrm{Spec}\, C' \times_S Z$, so they give $y : T \to Y$ with $i \circ y = j \circ a$. Then $q \circ y = a'$, as one checks after the closed immersion $V \to U$ given by $\beta$, using $\tau \circ \alpha = \psi \circ \beta$. $\square$

**Proposition 1.8.4 (Local pinched charts).** Let $b' : B' \to S'$ and $e : C \to Z$ be smooth of relative dimension $g$, and suppose that each finite set of points of $B'$ lies in an affine open set. Let $Y$, $i : Y \to B'$ and $q : Y \to C$ be such that $Y$ is the fibre product of $B'$ and $Z$ over $S$ (by $i$ and $e \circ q$) and of $C$ and $S'$ over $S$ (by $q$ and $b' \circ i$). Then each $x \in B'$ has a pinched chart of dimension $g$.

Lean: `GlobalTheory.Pinch.pinched`.

*Proof.* If the image of $x$ in $S$ is not in $Z$, use fact 2. Otherwise, since $Y = B' \times_S Z$, we have $x = i(y)$ for some $y \in Y$. The map $i$ is a closed immersion, as a base change of $Z \to S$, and $q$ is finite, as a base change of $S' \to S$. Fact 3 gives an affine $O \ni q(y)$, and fact 4 gives an affine $V' \ni x$ and $r$ with $i^{-1}(V') = q^{-1}(D(r))$. By fact 5 we may replace $B'$, $C$ and $Y$ by $V'$, $D(r)$ and $i^{-1}(V')$. Now $B' = \mathrm{Spec}\, C'$ is affine and smooth over $R'$, and $C = \mathrm{Spec}\, D$ with $D$ standard smooth of relative dimension $g$ over $R/\mathfrak{c}$. Both squares are cartesian, so $E = \Gamma(Y, \mathcal{O})$ satisfies the hypotheses of Lemma (Lifting a standard smooth algebra). Lemma (Affine pinched charts) gives a pinched chart at $x = i(y)$. $\square$

**Lemma 1.8.5 (Patching line bundles).** Let $p : X' \to X$ be finite and $i : Z_X \to X$ a closed immersion, let $Z'_X = X' \times_X Z_X$ with projections $i' : Z'_X \to X'$ and $p' : Z'_X \to Z_X$, and suppose that $p$ and $i$ satisfy the condition of fact 6. Let $c' \in \mathrm{Pic}(X')$ and $d \in \mathrm{Pic}(Z_X)$ with $i'^* c' = p'^* d$. Then there is $c \in \mathrm{Pic}(X)$ with $p^* c = c'$.

Lean: `GlobalTheory.Pinch.exists_pic_patch`.

*Proof.* Let $L'$ and $N$ be line bundles in the classes $c'$ and $d$, with $w : i'^* L' \cong p'^* N$. Let $x \in X$. The fibre of $p$ over $x$ is finite, so there is an open $W \ni x$ such that $L'$ has local generators $a$ on $p^{-1}(W)$ and $N$ has local generators $b$ on $i^{-1}(W)$. Through $w$, the generators $i'^* a$ and $p'^* b$ differ by a unit on $Z'_X$; shrinking $W$, it lifts to a unit on $p^{-1}(W)$, and after multiplying $a$ by the lift, $a$ and $b$ match on $Z'_X$. The condition of fact 6 gives the patching of units: a unit on $p^{-1}(W)$ and a unit on $i^{-1}(W)$ that agree on $Z'_X$ come from a unique unit on $W$. So the transition functions of $L'$ and $N$ in the matched generators come from transition functions on $X$, and they define a line bundle $L$ on $X$ with $p^* L \cong L'$. $\square$

We can now prove the theorem of the section on the reduced case.

**Theorem 1.8.6 (Pinching).** Let $A$ be an abelian scheme over $S$, smooth of relative dimension $g$. Suppose that $\mathrm{Rep}^{\mathrm{af}}_g(A, S')$ and $\mathrm{Rep}_g(A, Z)$ hold. Then $\mathrm{Rep}_g(A, S)$ holds.

Lean: `GlobalTheory.Pinch.hasRep_pinched`.

*Proof.* Let $(b' : B' \to S', P')$ and $(e : C \to Z, Q)$ be good representatives of dimension $g$, with finite sets of points of $B'$ in affine open sets. The map $S' \to S$ is finite, and it is surjective by lying over, since $R \to R'$ is injective and integral. By Theorem (Descent from a finite cover) of the last section, it suffices to find a local lift at each $x \in B'$.

Let $Y = B' \times Z$, with $i$ the projection to $B'$, and let $q : Y \to C$ be the morphism of fact 1. By Proposition (Local pinched charts), $x$ has a pinched chart $(U, p, j, n, k)$. Let $W = U' \times_U V$, with projections $a$ and $a'$. Property 3 gives $y : W \to Y$ with $i \circ y = j \circ a$ and $q \circ y = k \circ a'$.

Let $N' = P'_j$ on $A \times U'$; it is additive, since $P'$ is. Pulling back along $y$ the agreement of fact 1 shows that $N'$ and $Q_k$ have isomorphic pullbacks to $A \times W$. The square of $A \times W$, $A \times U'$, $A \times V$ and $A \times U$ is cartesian, with $1 \times p$ finite and $1 \times n$ a closed immersion. The $S$-scheme $A \times U$ is flat, since $A$ and $U$ are smooth over $S$, so fact 6 gives the condition of Lemma (Patching line bundles). That lemma gives $c \in \mathrm{Pic}(A \times U)$ with $(1 \times p)^* c = [N']$.

The scheme $U$ is locally of finite type over $R$, so locally noetherian, and $p$ is finite and surjective. By fact 7 there is an additive family $M$ on $A \times U$ such that $M$ at $p$ agrees with $N'$. Let $r : U \times S' \to U'$ be the isomorphism given by property 1, with $p \circ r = \mathrm{pr}_U$. Then $j \circ r : U \times S' \to B'$ is an open immersion over $S'$ whose image contains $x$, and $M$ at $\mathrm{pr}_U = p \circ r$ agrees with $N'$ at $r$, which is $P'$ at $j \circ r$. So $(U, M, j \circ r)$ is a local lift at $x$. $\square$

**Remark 1.8.7 (Formalization).** Facts 1 to 7 are `GlobalTheory.T.representsAdditiveLineBundleFamilies_compare`, `GlobalTheory.T.pinched_chart_off_closed_part_from_base`, `GlobalTheory.T.exists_affine_nbhd_basicOpen_standardSmooth`, `GlobalTheory.T.exists_affine_open_saturated_basicOpen_preimage`, `GlobalTheory.T.pinched_charts_restrict_matching_opens`, `GlobalTheory.T.conductorSquare_flat_baseChange_schemes` and `GlobalTheory.T.exists_additiveFamily_of_pullback_finiteSurjective`. They are cited by their statements only. The affine case of Proposition (Local pinched charts) is `GlobalTheory.T.pinched_charts_affine_of_spectra`, which takes Lemma (Affine pinched charts) as a hypothesis ([HasRepresentingSchemePinchedBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasRepresentingSchemePinchedBase.lean#L164)). The steps of the proof of Lemma (Lifting a standard smooth algebra) are cited results whose proofs were not opened. Lemma (Patching line bundles) does not say that $c$ restricts to $d$. In the affine case of Proposition (Local pinched charts), the smooth $R'$-algebra $C'$ has no condition on its dimension. Two local facts, that $U \to S$ and $A \to S$ are smooth (lines 256 and 257), appear unused.
