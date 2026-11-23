---
title: The induction on the rank
decls:
  - UpperTheory.projectiveBundleFormula_succ_of_forall
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The induction on the rank

This section proves the induction step of the projective bundle formula: if $\mathrm{PBF}_N$ holds for all spaces on which $q$ is invertible, then $\mathrm{PBF}_{N+1}$ holds for them too. Together with [Theorem](/entry/projective-bundle-formula-rank-two/) for the projective line, it gives the formula in all ranks in [Theorem](/entry/pbf-all/). The step blows up $\mathbb{P}^N$ at a point. The blowup is a $\mathbb{P}^1$-bundle over $\mathbb{P}^{N-1}$, so its cohomology is known from the rank two case and from $\mathrm{PBF}_N$. A Mayer-Vietoris argument then brings the result down to $\mathbb{P}^N$. We use the notation of the previous section: spaces $E$ on which $q$ is invertible, the projection $\pi : \mathbb{P}^{M-1}_E \to E$, and the class $\xi_M = c_1(\mathcal{L}) \in H^2(\mathbb{P}^{M-1}_E, \mathbb{Z}/q(1))$.

### Group actions and the blowup

For the proof it is convenient to describe spaces as quotients by group actions. Let $D$ be a functor from rings to sets, $G$ a functor from rings to groups, and let $G(A)$ act on $D(A)$, naturally in $A$. The *quotient space* $[D/G]$ is the nerve of the action groupoid: over $\operatorname{Spec} A$ its objects are the elements of $D(A)$, and an arrow $x \to y$ is a $g \in G(A)$ with $x = g y$. For a space $E$ we write $E \times [D/G]$ for the product. A *character* $\chi : G \to \mathbb{G}_m$ gives a line bundle $\mathcal{L}_\chi$ on $[D/G]$: on an arrow $g$ its transition function is $\chi(g)$.

With $D = \mathrm{Um}_M$, the unimodular vectors of length $M$, and $G = \mathbb{G}_m$ acting by scaling, the space $[\mathrm{Um}_M / \mathbb{G}_m]$ is the space $\mathbb{P}^{M-1}$ of the last section, and the identity character gives $\mathcal{L}$. The Lean code proves that $\mathrm{PBF}_M(E)$ is equivalent to the same statement for $E \times [\mathrm{Um}_M / \mathbb{G}_m] \to E$. From now on we use this form.

**Definition (The blowup).** Let $N \ge 1$. Let $\mathbb{G}_m^2$ act on $\mathrm{Um}_N \times \mathrm{Um}_2$ by
$$(g_1, g_2) \cdot \bigl(x, (a, b)\bigr) = \bigl(g_1 x, (g_2 g_1^{-1} a, \, g_2 b)\bigr).$$
Put $B = [\mathrm{Um}_N \times \mathrm{Um}_2 / \mathbb{G}_m^2]$. It has two maps:
$$\begin{aligned} p &: B \to \mathbb{P}^{N-1}, & (x, (a, b)) &\mapsto x, & (g_1, g_2) &\mapsto g_1, \\ \beta &: B \to \mathbb{P}^{N}, & (x, (a, b)) &\mapsto (a x_1, \dots, a x_N, b), & (g_1, g_2) &\mapsto g_2. \end{aligned}$$

The vector $(a x_1, \dots, a x_N, b)$ is unimodular: the ideal it generates contains $a$ and $b$, which generate the unit ideal. So $\beta$ is well defined. In the language of schemes, $B$ is the projective bundle $\mathbb{P}(\mathcal{O}(-1) \oplus \mathcal{O})$ over $\mathbb{P}^{N-1}$, and $\beta$ is the blowup of $\mathbb{P}^N$ at the point $P = (0 : \dots : 0 : 1)$. The map $p$ is a $\mathbb{P}^1$-bundle.

On $E \times B$ there are two line bundles: $\beta^* \mathcal{L}$, from the character $g_2$, and $p^* \mathcal{L}$, from the character $g_1$. Write $\eta = \xi_N$ on $\mathbb{P}^{N-1}_E$ and $\xi = \xi_{N+1}$ on $\mathbb{P}^N_E$. Since $c_1$ is natural, $\beta^* \xi$ and $p^* \eta$ are the first Chern classes of $\beta^* \mathcal{L}$ and $p^* \mathcal{L}$.

The two pieces of $\mathbb{P}^N$ are:

1. $Q_1$, the locus where the last coordinate is a unit: an affine space around $P$;
2. $Q_2$, the locus where the first $N$ coordinates generate the unit ideal: the complement of $P$.

They cover $\mathbb{P}^N$, and their inverse images under $\beta$ cover $B$.

### Five facts about the blowup

The proof uses five facts. Each is a separate result of the Lean code. We list them with a short reason.

1. *The blowup is a projective line bundle.* The pair $(p; 1, \beta^* \xi)$ over $E$ has the Leray-Hirsch property. Over the locus of $\mathbb{P}^{N-1}$ where the coordinate $x_i$ is a unit, the bundle $p$ is trivial: it is isomorphic to the projection of $\mathbb{P}^1$ times that locus, and $\beta^* \mathcal{L}$ becomes the tautological bundle. So [Theorem](/entry/projective-bundle-formula-rank-two/) applies on each such locus. A separate result glues the Leray-Hirsch property from these loci to all of $\mathbb{P}^{N-1}_E$.
2. *The Chern class on the two pieces.* On $\beta^{-1}(Q_1)$ the class $\beta^* \xi$ vanishes, since $b$ is a unit there and trivializes $\beta^* \mathcal{L}$. On $\beta^{-1}(Q_2)$ the classes $\beta^* \xi$ and $p^* \eta$ agree, since $a$ is a unit there and the two line bundles become isomorphic.
3. *The affine piece.* The projection $Q_1 \times E \to E$ is a cohomological equivalence for each $\mathbb{Z}/q(i)$, and so is the map $\beta^{-1}(Q_1) \to \mathbb{P}^{N-1}_E$ induced by $p$. Both are affine space bundles, and the Lean proofs use the rank one case of the projective bundle formula and homotopy invariance.
4. *Away from the centre.* The map $\beta^{-1}(Q_2) \to Q_2$ is a cohomological equivalence.
5. *The intersection.* The map $\beta^{-1}(Q_1 \cap Q_2) \to Q_1 \cap Q_2$ is a cohomological equivalence.

Facts 4 and 5 hold because the blowup changes nothing away from $P$. Their Lean proofs also use homotopy invariance and the rank one case.

**Lemma (Powers of the Chern class).** Let $g_1 : U \to Y$ and $g_2 : V \to Y$ be a cover of a space $Y$, let $q$ be invertible on $Y$, and let $\xi, h \in H^2(Y, \mathbb{Z}/q(1))$. Assume $g_1^* \xi = 0$ and $g_2^* \xi = g_2^* h$. Then for all $j \ge 0$
$$\xi^{j+1} = h^j \cup \xi.$$

Lean: `UpperTheory.cpow_succ_eq_cup_of_two_cover`.

*Proof.* The class $\xi$ vanishes on $U$, and $\xi - h$ vanishes on $V$. A cup product of two classes that vanish on the two pieces of a cover is zero, so $\xi \cup (\xi - h) = 0$. Classes of degree $2$ commute under cup product, so $\xi \cup \xi = h \cup \xi$. Induction on $j$ and associativity give the claim. $\square$

By fact 2, the Lemma applies on $B$ with $\beta^* \xi$ and $h = p^* \eta$:
$$(\beta^* \xi)^{j+1} = p^* \eta^j \cup \beta^* \xi \qquad \text{for all } j \ge 0. \tag{R}$$

### The induction step

**Theorem (Induction step).** Let $N \ge 2$. Assume that $\mathrm{PBF}_N(E)$ holds for each space $E$ on which $q$ is invertible. Then $\mathrm{PBF}_{N+1}(E)$ holds for each such $E$.

Lean: `UpperTheory.projectiveBundleFormula_succ_of_forall`.

*Proof.* Fix $E$, $n$ and $i$, and write $\pi_X : \mathbb{P}^{N-1}_E \to E$ and $\pi_Y : \mathbb{P}^N_E \to E$. We show that
$$\Phi : (a_0, \dots, a_N) \mapsto \sum_{j=0}^{N} \pi_Y^* a_j \cup \xi^j, \qquad a_j \in H^{n-2j}(E, \mathbb{Z}/q(i-j)),$$
is injective and surjective. The square $\pi_X \circ p = \pi_Y \circ \beta$ commutes.

*Injectivity.* Let $\Phi(a) = 0$. Apply $\beta^*$. Since $\beta^*$ is compatible with cup products and with the square, we get $\sum_j p^* \pi_X^* a_j \cup (\beta^* \xi)^j = 0$. By (R) this sum is $p^* y_0 + p^* y_1 \cup \beta^* \xi$ with
$$y_0 = \pi_X^* a_0, \qquad y_1 = \sum_{k=0}^{N-1} \pi_X^* a_{k+1} \cup \eta^k.$$
By fact 1, $y_0 = 0$ and $y_1 = 0$. By $\mathrm{PBF}_N(E)$, $y_1 = 0$ gives $a_{k+1} = 0$ for all $k$. Since $N \ge 1$, the class $1 = \eta^0$ is one of the classes of $\mathrm{PBF}_N(E)$, so $\pi_X^*$ is injective, and $y_0 = 0$ gives $a_0 = 0$.

*A vanishing criterion.* Before surjectivity, we show: if $x \in H^n(\mathbb{P}^N_E)$ and $\beta^* x = 0$, then $x = 0$. This is a Mayer-Vietoris argument for the cover $Q_1, Q_2$ of $\mathbb{P}^N_E$ and its inverse image in $B$, with facts 3 to 5 and the injectivity of $\pi_X^*$. The Lean code proves it as a separate lemma, whose proof we did not open.

*Surjectivity.* Let $x \in H^n(\mathbb{P}^N_E, \mathbb{Z}/q(i))$. By fact 1, $\beta^* x = p^* y_0 + p^* y_1 \cup \beta^* \xi$ for some $y_0$ and $y_1$ on $\mathbb{P}^{N-1}_E$. By fact 3, the restriction of $x$ to $Q_1$ is the pullback of a class $a_0$ on $E$. Restrict both expressions for $\beta^* x$ to $\beta^{-1}(Q_1)$. There $\beta^* \xi$ vanishes by fact 2, and the map to $\mathbb{P}^{N-1}_E$ is an equivalence by fact 3. So $y_0 = \pi_X^* a_0$. By $\mathrm{PBF}_N(E)$, $y_1 = \sum_k \pi_X^* b_k \cup \eta^k$ for some classes $b_k$. Put
$$x' = x - \pi_Y^* a_0 - \sum_{k=0}^{N-1} \pi_Y^* b_k \cup \xi^{k+1}.$$
By (R), $\beta^*$ of the subtracted terms is $p^* y_0 + p^* y_1 \cup \beta^* \xi = \beta^* x$. So $\beta^* x' = 0$, and $x' = 0$ by the vanishing criterion. Hence $x = \Phi(a_0, b_0, \dots, b_{N-1})$. $\square$

For $E$ a point over $\mathbb{C}$, the argument is the familiar computation of $H^*(\mathbb{P}^N)$ from the blowup at a point: the blowup is a $\mathbb{P}^1$-bundle over $\mathbb{P}^{N-1}$, and it differs from $\mathbb{P}^N$ only over a neighbourhood of $P$, which is contractible.

**Remark.** The Lean statement asks for $N \ge 2$, but the proof uses only $N \ge 1$, which is all the called lemmas ask for. The case $N = 1$ of the step is not available because fact 1 applies the rank two formula on each chart. So the rank two case must be proved first and separately, as in the previous section. The quotient spaces, the blowup and the loci $Q_1$, $Q_2$ are defined in [SpanScale.lean](lean:Development/AutomorphicArithmetic/BlowupCategories/SpanScale.lean#L273). The vanishing criterion is [LerayHirschOfTwoElementCover.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/LerayHirschOfTwoElementCover.lean#L48).
