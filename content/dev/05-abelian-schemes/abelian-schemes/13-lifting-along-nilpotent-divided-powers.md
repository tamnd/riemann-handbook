---
title: Lifting along nilpotent divided powers
decls:
  - GlobalTheory.T.abelianSchemeHomLiftingNilDP_of_hodge_cube_duality_unobstructed
  - GlobalTheory.SqLift.abelianLifting_of_known_theorems
  - GlobalTheory.LiftFour.abelianLifting_of_four
  - GlobalTheory.abelianScheme_hom_lifting_nilpotent_dividedPowers
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lifting along nilpotent divided powers

Let $R \to R_0$ be a surjection whose kernel $I$ has nilpotent divided powers. This section proves that abelian schemes and their homomorphisms lift from $R_0$ to $R$ according to their Hodge filtrations (Theorem (Lifting along nilpotent divided powers)). An abelian scheme over $R_0$ with one lift to $R$ has a lift for each admissible submodule. A homomorphism over $R_0$ lifts, and lifts uniquely, when it respects the Hodge filtrations. This is the theorem of Grothendieck and Messing in the form that the development uses. The proof does induction on the nilpotence exponent. Each step is a square zero thickening, where the classification of the last section applies.

Let $R$ be a ring, $I \subset R$ an ideal with divided powers $\kappa = (\kappa_n)$, and $\pi : R \to R_0$ a surjective ring map with kernel $I$. The divided powers are *nilpotent of exponent $N$* if every product $\kappa_{n_1}(x_1) \cdots \kappa_{n_k}(x_k)$ with all $x_j \in I$ and $n_1 + \dots + n_k \geq N$ is zero. They are *nilpotent* if they are nilpotent of some exponent. If $I^2 = 0$, the divided powers $\gamma$ of the last section are nilpotent of exponent 2.

For an abelian scheme $A_0$ over $R_0$, let $D_\kappa(A_0)$ be the $R$-dual of the primitive part of the first crystalline cohomology of $A_0$ relative to $(R, I, \kappa)$, as in the last section with $\kappa$ in place of $\gamma$. A *lift* of $A_0$ is an abelian scheme $A$ over $R$ with a morphism $i : A_0 \to A$, compatible with the group laws, that makes $A_0$ the base change of $A$ to $R_0$. A lift gives a map $\gamma_A : D_\kappa(A_0) \to D_{\mathrm{dR}}(A)$, and we put $\mathrm{Fil}_\kappa(A) = \gamma_A^{-1}(\mathrm{Fil}(A))$. A homomorphism $f_0 : A_0 \to B_0$ gives a map $f_{0*} : D_\kappa(A_0) \to D_\kappa(B_0)$, the dual of the pullback of primitive classes. Admissible submodules of $D_{\mathrm{dR}}(A')$ are as in the last section.

**Definition 1.13.1 (Lifting).** We say that *lifting holds for $(\kappa, \pi)$* if these two conditions hold.

1. (Objects.) Let $A_0$ be an abelian scheme over $R_0$ and $(A', i')$ a lift of $A_0$, smooth of relative dimension $g$. For each admissible $F \subset D_{\mathrm{dR}}(A')$, there is a lift $(A, i)$ of $A_0$, smooth of relative dimension $g$, with $\mathrm{Fil}_\kappa(A) = \gamma_{A'}^{-1}(F)$.
2. (Homomorphisms.) Let $(A, i)$ and $(B, j)$ be lifts of $A_0$ and $B_0$, smooth of relative dimensions $g$ and $g'$, and $f_0 : A_0 \to B_0$ a homomorphism with $f_{0*}(\mathrm{Fil}_\kappa(A)) \subset \mathrm{Fil}_\kappa(B)$. Then there is exactly one homomorphism $f : A \to B$ with $f \circ i = j \circ f_0$, that is, $f$ restricts to $f_0$ on $A_0$.

We say that *lifting holds* if it holds for every $(\kappa, \pi)$ with $\kappa$ nilpotent.

**Definition 1.13.2 (Inputs).** Besides the Hodge and de Rham structure of the last section, and the unobstructedness of the section on the cohomology of the structure sheaf, we use three statements.

1. The *theorem of the cube*: for an abelian scheme $A$ over a scheme $S$, a line bundle $L$ on $A$, and points $a, b, c$ of $A$ with values in an $S$-scheme $T$, the line bundle $L(abc) \otimes L(ab)^{-1} \otimes L(ac)^{-1} \otimes L(bc)^{-1} \otimes L(a) \otimes L(b) \otimes L(c) \otimes L(1)^{-1}$ on $T$ is trivial, where $L(x)$ is the pullback of $L$ along $x$.
2. The *dual abelian scheme*: every abelian scheme $A$ over a scheme $S$ has a dual $(B, P)$ with $B$ abelian, keeping the dimension of $A$, and such that $(A, s^* P)$ is a dual of $B$.
3. *Poincaré duality in de Rham homology*: let $A$ and $B$ be abelian schemes over $R$, smooth of relative dimension $g$, $(B, P)$ a dual of $A$, and $\varphi : D_{\mathrm{dR}}(A) \times D_{\mathrm{dR}}(B) \to R$ the pairing attached to $P$. Then $\varphi$ is perfect, and $\varphi(x, y) = 0$ for $x \in \mathrm{Fil}(A)$ and $y \in \mathrm{Fil}(B)$.

We use the following facts.

1. (De Rham structure.) The Hodge and de Rham structure, the theorem of the cube, the dual abelian scheme and Poincaré duality imply the *de Rham structure*: for each abelian scheme $A$ over a ring $R$, smooth of relative dimension $g$, (a) all classes are primitive, $H^1_{\mathrm{dR}}(A)$ is finite projective of rank $2g$, and $\bigwedge^2 H^1_{\mathrm{dR}}(A) \cong H^2_{\mathrm{dR}}(A)$ by cup product; (b) the primitive classes of 1-forms are a direct summand, finite projective of rank $g$; (c) these modules commute with base change; (d) for each nilpotent divided power thickening $R \to R_0$ with $A_0 = A \times_R R_0$, the map $\gamma_A$ is bijective; (e) for a line bundle $L$ on $A$, the form on $D_{\mathrm{dR}}(A)$ attached to $L$ vanishes on $\mathrm{Fil}(A) \times \mathrm{Fil}(A)$, and it is perfect if $K(L)$ is trivial.
2. (Square zero, from classified lifts.) Assume the de Rham structure. Let $I^2 = 0$, and suppose that the three conclusions of [Theorem 1.12.3](/entry/abelian-scheme-lifts-of-hodge-de-rham/) (Square zero lifts) hold for $(R, I, \pi)$. Then lifting holds for $(\gamma, \pi)$.
3. (Noetherian rings suffice.) Assume the de Rham structure. If lifting holds for $(\gamma, \pi)$ whenever $I^2 = 0$ and $R$ is noetherian, it holds for $(\gamma, \pi)$ whenever $I^2 = 0$.
4. (Steps.) Let $\kappa$ be nilpotent of exponent $N + 2$. Then $\pi$ factors as $R \to R_1 \to R_0$, where the first map is surjective with kernel $J \subset I$ and $J^2 = 0$, the second is surjective with kernel $I_1$, and $I_1$ has divided powers $\kappa_1$, nilpotent of exponent $N + 1$. Both maps respect the divided powers: $\gamma$ on $J$ goes to $\kappa$, and $\kappa$ goes to $\kappa_1$.
5. (Objects in a step.) Assume the de Rham structure and unobstructedness, and let $\pi$ factor as in fact 4. If condition 1 of lifting holds for $(\gamma, R \to R_1)$ and for $(\kappa_1, R_1 \to R_0)$, it holds for $(\kappa, \pi)$.
6. (Homomorphisms in a step.) Assume the de Rham structure, and let $\pi$ factor as in fact 4. If condition 2 of lifting holds for $(\gamma, R \to R_1)$ and for $(\kappa_1, R_1 \to R_0)$, it holds for $(\kappa, \pi)$.

In fact 4, $J$ is the ideal generated by the products of divided powers of total degree at least $N + 1$.

**Lemma 1.13.3 (Induction on the exponent).** Assume the de Rham structure and unobstructedness. If lifting holds for $(\gamma, \pi)$ whenever $I^2 = 0$, then lifting holds.

Lean: `GlobalTheory.SqLift.abelianLifting_of_sqLifting`.

*Proof.* We prove by induction on $n$ that lifting holds for $(\kappa, \pi)$ whenever $\kappa$ is nilpotent of exponent $n + 1$. For $n = 0$, the exponent is 1, so $x = \kappa_1(x) = 0$ for each $x \in I$. So $I = 0$, $I^2 = 0$, and $\kappa = \gamma$, since $\kappa_0 = \gamma_0 = 1$, $\kappa_1 = \gamma_1$ is the identity, and $\kappa_n(0) = 0 = \gamma_n(0)$ for $n \geq 2$. Lifting holds by hypothesis.

Let $n \geq 0$, and let $\kappa$ be nilpotent of exponent $n + 2$. Fact 4 factors $\pi$ as $R \to R_1 \to R_0$ with a square zero kernel $J$ and with $\kappa_1$ nilpotent of exponent $n + 1$. Lifting holds for $(\gamma, R \to R_1)$ by hypothesis and for $(\kappa_1, R_1 \to R_0)$ by induction. So fact 5 gives condition 1 and fact 6 gives condition 2 for $(\kappa, \pi)$.

Now let $\kappa$ be nilpotent, of exponent $N$. A product of total degree at least $N + 1$ has total degree at least $N$, so $\kappa$ is also nilpotent of exponent $N + 1$, and the induction applies with $n = N$. $\square$

**Proposition 1.13.4 (Square zero lifting).** Assume the de Rham structure and unobstructedness, and that the three conclusions of Theorem (Square zero lifts) hold for every noetherian $R$ and every $I$ with $I^2 = 0$. Then lifting holds.

Lean: `GlobalTheory.SqLift.abelianLifting_of_schemeLifts`.

*Proof.* Let $R$ be noetherian, $I^2 = 0$ and $\pi$ as above. By hypothesis the three conclusions hold for $(R, I, \pi)$, so lifting holds for $(\gamma, \pi)$ by fact 2. By fact 3, lifting holds for $(\gamma, \pi)$ whenever $I^2 = 0$. By Lemma (Induction on the exponent), lifting holds. $\square$

**Theorem 1.13.5 (Lifting from five inputs).** Suppose that the Hodge and de Rham structure, the theorem of the cube, the dual abelian scheme, Poincaré duality in de Rham homology and unobstructedness hold. Then lifting holds.

Lean: `GlobalTheory.SqLift.abelianLifting_of_known_theorems` (also `GlobalTheory.T.abelianSchemeHomLiftingNilDP_of_hodge_cube_duality_unobstructed`, a second name).

*Proof.* By fact 1, the first four inputs give the de Rham structure. By [Corollary 1.12.4](/entry/abelian-scheme-lifts-of-abelian-hodge-de-rham/) (Square zero lifts from de Rham cohomology), the Hodge and de Rham structure gives the three conclusions of Theorem (Square zero lifts) for every noetherian $R$. Proposition (Square zero lifting) applies, with unobstructedness as the last input. $\square$

**Corollary 1.13.6 (Lifting from four inputs).** Suppose that the Hodge and de Rham structure, the dual abelian scheme, Poincaré duality in de Rham homology and unobstructedness hold. Then lifting holds.

Lean: `GlobalTheory.LiftFour.abelianLifting_of_four`.

*Proof.* The theorem of the cube holds for abelian schemes over any base (`GlobalTheory.T.theoremOfCubeAbelianScheme_over_arbitrary_base`; compare [Volume 1](/learn/abelian-varieties/#the-theorem-of-the-cube)). Apply Theorem (Lifting from five inputs). $\square$

**Theorem 1.13.7 (Lifting along nilpotent divided powers).** Let $R$ be a ring, $I \subset R$ an ideal with nilpotent divided powers $\kappa$, and $\pi : R \to R_0$ a surjective ring map with kernel $I$. Then lifting holds for $(\kappa, \pi)$.

Lean: `GlobalTheory.abelianScheme_hom_lifting_nilpotent_dividedPowers`.

*Proof.* The four inputs of Corollary (Lifting from four inputs) are proved. The Hodge and de Rham structure is [Theorem 1.15.1](/entry/ab-coh-abelian-hodge-de-rham/). The dual abelian scheme is [Theorem 1.6.4](/entry/dual-abelian-scheme/) (Dual abelian scheme). Poincaré duality in de Rham homology follows from these two (`GlobalTheory.PoincareDeRhamDualityProof.poincareDeRhamDuality_of_hodge`). Unobstructedness is [Theorem 1.11.4](/entry/abelian-unobstructed/) (Unobstructedness). So the corollary applies. $\square$

The theorem is used on the way to [EveryCharacter](/step/every-character/).

**Remark 1.13.8 (Formalization).** Lifting for $(\kappa, \pi)$ is `GlobalTheory.Published.GrothendieckMessing.LiftObj` and `GlobalTheory.Published.GrothendieckMessing.LiftHom`, and lifting is `GlobalTheory.Published.AbelianLifting`. The inputs are `GlobalTheory.Published.AbelianHodgeDeRham`, `GlobalTheory.Published.CubeTheorem`, `GlobalTheory.Published.DualAbelianScheme`, `GlobalTheory.Published.PoincareDeRhamDuality` and `GlobalTheory.Published.AbelianUnobstructed`, and the de Rham structure is `GlobalTheory.Published.AbelianDeRham`. Nilpotence of exponent $N$ is `GlobalTheory.SqLift.NilExp`, and $\mathrm{Fil}_\kappa$ is `liftFil`. Facts 1 to 6 are `GlobalTheory.T.abelianSchemeDeRhamStructure_of_cube_dual_poincare`, `GlobalTheory.T.grothendieckMessingLiftAbelianScheme_of_squareZero` with `GlobalTheory.T.grothendieckMessingLiftHomomorphism_of_squareZero`, `GlobalTheory.T.squareZeroLifting_of_noetherian_case`, `GlobalTheory.SqLift.exists_isStep_nilExp`, `GlobalTheory.T.liftAbelianScheme_along_squareZero_factorization` and `GlobalTheory.SqLift.liftHom_of_isStep`. They are cited by their statements; the sentences on why they hold are not read from proofs. The base case of the lemma is `GlobalTheory.SqLift.NilExp.eq_sqDP`. `AbelianLifting` asks for neither a prime $p$ nilpotent in $R$ nor the condition `Canonical`, which are both part of `GlobalTheory.Published.GrothendieckMessing`. Condition 1 needs a given lift $A'$, so it does not give existence of a lift by itself. The corollary named `abelianLifting_of_four` supplies the theorem of the cube itself, and the module of the theorem with five inputs is named `AbelianSchemeHomLiftingNilDPOfFiveStatements`. All four inputs of the main theorem are proved, so the theorem has no hypotheses. The main theorem calls the Hodge and de Rham structure and the dual abelian scheme by their second names, `GlobalTheory.T.abelianScheme_deRham_locallyFree_hodgeDegenerates` and `GlobalTheory.T.dualAbelianScheme_exists_biduality`. The second name of the five input theorem is closed by a `first` list under `set_option maxHeartbeats 1000000`.
