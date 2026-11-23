---
title: Noetherian induction over a base of finite type
decls:
  - GlobalTheory.DualCon.Step.local_rep
  - GlobalTheory.T.hasProperSmoothDualRepresentative_noetherian_induction
  - GlobalTheory.DualCon.Step.step
  - GlobalTheory.T.hasProperSmoothDualRepresentative_finiteType
  - GlobalTheory.DualConFT.hasRep_of_finiteType
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Noetherian induction over a base of finite type

This section proves that the dual of an abelian scheme over a ring of finite type over $\mathbb{Z}$ has a good representative (Theorem (Finite type)). The proof is a noetherian induction on closed subschemes of the base. The inductive step (Proposition (Inductive step)) assumes representatives over all proper closed subschemes $\mathrm{Spec}\, R/J$, $J \neq 0$. If $R$ is reduced, it works locally on $\mathrm{Spec}\, R$ and uses the reduced case of the last section. If $R$ is not reduced, it lifts a representative over a square-zero thickening. The theorem is the input of the limit argument of the next section, which treats an arbitrary ring.

Throughout, $R$ is a ring of finite type over $\mathbb{Z}$. It is noetherian by the Hilbert basis theorem, and so is each quotient and each localization $R_f$ of $R$, which are again of finite type over $\mathbb{Z}$. We use four facts on an abelian scheme $A$ over a scheme $S$, smooth of relative dimension $g$.

1. (Local on the base.) If each point of $S$ has an open neighbourhood $V$ with $\mathrm{Rep}_g(A, V)$, then $\mathrm{Rep}_g(A, S)$ holds.
2. (Square-zero thickenings.) Let $S = \mathrm{Spec}\, R$ with $R$ noetherian, and $J$ an ideal with $J^2 = 0$. If $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/J)$ holds, then $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$ holds.
3. (An affine open set over a basic open set.) Let $G$ be a group over $\mathrm{Spec}\, R$, for any ring $R$, and $s \in \mathrm{Spec}\, R$. Then there are $f \in R$ with $s \in D(f)$ and an affine open set $W$ of $G$ that meets the fibre of $G$ over each point of $D(f)$.
4. (Base change of such sets.) Let $a : R \to R'$ be a ring homomorphism, and $W$ an affine open set of $A$ that meets the fibres over all points in the image of $\mathrm{Spec}\, R' \to \mathrm{Spec}\, R$. Then $A \times_R R'$ has an affine open set that meets every fibre over $\mathrm{Spec}\, R'$.

Fact 3 has a simple reason: an affine open neighbourhood of $e(s)$ contains $e(t)$ for all $t$ in a neighbourhood of $s$, and $D(f)$ can be taken inside it. Fact 2 is a deformation statement: the obstructions to lifting the representative and its universal bundle lie in coherent cohomology groups, which vanish over an affine base.

**Lemma 1.5.1 (Square-zero ideal).** Let $R$ be a noetherian ring that is not reduced. Then there is an ideal $J \neq 0$ of $R$ with $J^2 = 0$.

Lean: `GlobalTheory.DualCon.Step.exists_sq_zero`.

*Proof.* The nilradical $N$ of $R$ is not $0$. Since $R$ is noetherian, $N$ is finitely generated, so $N^n = 0$ for some $n$. Let $n$ be the least such $n$. Then $n \geq 2$, since $N^0 = R \neq 0$ and $N^1 = N \neq 0$. Write $n = k + 1$ with $k \geq 1$, and put $J = N^k$. Then $J \neq 0$ by the choice of $n$, and $J^2 = N^{2k} \subseteq N^{k+1} = 0$, since $2k \geq k + 1$. $\square$

**Proposition 1.5.2 (Local representatives).** Let $R$ be a reduced ring of finite type over $\mathbb{Z}$ and $A$ an abelian scheme over $\mathrm{Spec}\, R$, smooth of relative dimension $g$. Suppose that $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/J)$ holds for each ideal $J \neq 0$ of $R$. Then each $s \in \mathrm{Spec}\, R$ has an open neighbourhood $V$ with $\mathrm{Rep}_g(A, V)$.

Lean: `GlobalTheory.DualCon.Step.local_rep`.

*Proof.* Fact 3 gives $f \in R$ with $s \in D(f)$ and an affine open set $W$ of $A$ that meets every fibre over $D(f)$. Let $a : R \to R_f$ be the localization and $A' = A \times_R R_f$. Then $A'$ is an abelian scheme over $R_f$, smooth of relative dimension $g$, and fact 4 gives an affine open set of $A'$ that meets every fibre. The ring $R_f$ is reduced and of finite type over $\mathbb{Z}$.

We check the last hypothesis of [Theorem 1.4.3](/entry/dual-con-step-step/) (Reduced case) for $A'$. Let $J' \neq 0$ be an ideal of $R_f$ and $J = a^{-1}(J')$. Then $J \neq 0$: if $y = x/f^m \neq 0$ lies in $J'$, then $a(x) = f^m y \in J'$ and $a(x) \neq 0$, so $x \in J$ and $x \neq 0$. By the hypothesis, $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/J)$ holds. The map $R/J \to R_f/J'$ gives a morphism $\mathrm{Spec}\, R_f/J' \to \mathrm{Spec}\, R/J$ over $\mathrm{Spec}\, R$, so $\mathrm{Rep}_g(A, \mathrm{Spec}\, R_f/J')$ holds by Lemma (Change of base), part (b), and $\mathrm{Rep}_g(A', \mathrm{Spec}\, R_f/J')$ by part (a).

So the Reduced case theorem gives $\mathrm{Rep}_g(A', \mathrm{Spec}\, R_f)$. By Lemma (Change of base), part (a), $\mathrm{Rep}_g(A, \mathrm{Spec}\, R_f)$ holds, with $\mathrm{Spec}\, R_f \to \mathrm{Spec}\, R$ the open immersion onto $D(f)$. Take $V = D(f)$. Then $\mathrm{Rep}_g(A, V)$ holds by part (b), applied to the isomorphism $V \cong \mathrm{Spec}\, R_f$ over $\mathrm{Spec}\, R$. $\square$

**Proposition 1.5.3 (Inductive step).** Let $R$ be a ring of finite type over $\mathbb{Z}$ and $A$ an abelian scheme over $\mathrm{Spec}\, R$, smooth of relative dimension $g$. Suppose that $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/J)$ holds for each ideal $J \neq 0$ of $R$. Then $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$ holds.

Lean: `GlobalTheory.DualCon.Step.step` (also `GlobalTheory.T.hasProperSmoothDualRepresentative_noetherian_induction`, a second name).

*Proof.* If $R$ is reduced, Proposition (Local representatives) gives representatives over an open cover, and fact 1 gives $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$. If $R$ is not reduced, Lemma (Square-zero ideal) gives $J \neq 0$ with $J^2 = 0$. The hypothesis gives $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/J)$, and fact 2 gives $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$. $\square$

**Theorem 1.5.4 (Finite type).** Let $R$ be a ring of finite type over $\mathbb{Z}$ and $A$ an abelian scheme over $\mathrm{Spec}\, R$, smooth of relative dimension $g$. Then $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$ holds.

Lean: `GlobalTheory.DualConFT.hasRep_of_finiteType` (also `GlobalTheory.T.hasProperSmoothDualRepresentative_finiteType`, a second name).

*Proof.* We first prove a statement on factorizations. Let $J$ be an ideal of a ring $S_0$, let $\varphi : S_0 \to S_1$ and $\psi : S_1 \to S_0/J$ be ring homomorphisms with $\psi \varphi$ the quotient map, and suppose that every abelian scheme over $S_1$ of relative dimension $g$ has a good representative of dimension $g$ over $\mathrm{Spec}\, S_1$. Then each abelian scheme $A_0$ over $S_0$ of relative dimension $g$ has $\mathrm{Rep}_g(A_0, \mathrm{Spec}\, S_0/J)$. Indeed, $A_1 = A_0 \times_{S_0} S_1$ is an abelian scheme of relative dimension $g$ over $S_1$, so $\mathrm{Rep}_g(A_1, \mathrm{Spec}\, S_1)$ holds, and by Lemma (Change of base), part (a), $\mathrm{Rep}_g(A_0, \mathrm{Spec}\, S_1)$ holds. The map $\psi$ gives a morphism $\mathrm{Spec}\, S_0/J \to \mathrm{Spec}\, S_1$ over $\mathrm{Spec}\, S_0$, and part (b) gives $\mathrm{Rep}_g(A_0, \mathrm{Spec}\, S_0/J)$.

Now we prove, for each ideal $I$ of $R$: every abelian scheme over $R/I$ of relative dimension $g$ has a good representative of dimension $g$ over $\mathrm{Spec}\, R/I$. Since $R$ is noetherian, every nonempty set of ideals has a maximal element, so we may use induction downwards on $I$: we assume the claim for all ideals strictly larger than $I$. Let $A_0$ be an abelian scheme over $R/I$. The ring $R/I$ is of finite type over $\mathbb{Z}$, so we may apply Proposition (Inductive step) to it. Let $J' \neq 0$ be an ideal of $R/I$ and $J \supseteq I$ its preimage in $R$. Then $J \neq I$, since $J' \neq 0$, so the claim holds for $R/J$. Apply the factorization statement with $S_0 = R/I$, $S_1 = R/J$, the quotient map $\varphi$, and the isomorphism $\psi : R/J \to (R/I)/J'$. It gives $\mathrm{Rep}_g(A_0, \mathrm{Spec}\, (R/I)/J')$. So the proposition gives $\mathrm{Rep}_g(A_0, \mathrm{Spec}\, R/I)$.

The theorem is the case $I = 0$. To get it in the stated form, apply Proposition (Inductive step) to $A$ once more: for $J \neq 0$, the factorization statement with $S_0 = S_1 = R$, $\varphi$ the identity and $\psi$ the quotient map, together with the claim for $R/J$, gives $\mathrm{Rep}_g(A, \mathrm{Spec}\, R/J)$. $\square$

**Remark 1.5.5 (Formalization).** Facts 1 to 4 are `GlobalTheory.T.hasProperSmoothDualRepresentative_of_local`, `GlobalTheory.T.hasProperSmoothDualRepresentative_of_sqZero`, `GlobalTheory.T.exists_basicOpen_affineOpen_meeting_fibres_grpScheme` and `GlobalTheory.T.affineOpen_meeting_fibres_pullback_specRingHom`, cited by their statements; the sentences on why facts 2 and 3 hold are not read from proofs. Fact 3 asks only for a group over $\mathrm{Spec}\, R$. The factorization statement is `GlobalTheory.DualConFT.hasRep_quot_of_factor` and the induction is `GlobalTheory.DualConFT.hasRep_quot`, by `WellFoundedGT.induction` on ideals. The final step applies the inductive step again instead of the case $I = 0$, and the hypothesis $J \neq 0$ that it receives is not used ([HasProperSmoothDualRepresentativeFiniteType.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeFiniteType.lean#L75)). The second name of the inductive step ends in `noetherian_induction`, but it states only the inductive step. The name of the proposition on local representatives does not mention the open cover. Both second names are closed by a `first` list under `set_option maxHeartbeats 1000000`.
