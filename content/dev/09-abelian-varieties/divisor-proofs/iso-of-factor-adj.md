---
id: iso-of-factor-adj
title: The image of an idempotent is isomorphic to any group uniformised by its data
kind: theorem
decl: GlobalTheory.MumIsoAdj.iso_of_factor_adj
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IdempotentImageIsoUniformisedFactorOfAdjointPair
covers: 310
status: drafted
drafted_by: writer@claude
---
This theorem compares two groups with degeneration data $D$: the image $G$ of an idempotent $e$ on a uniformised $G'$, and a group $G_0$ uniformised by $D$. It gives an isomorphism $G \cong G_0$ and an adjoint pair between $G'$ and $G_0$. The [statement entry](/entry/idempotent-image-iso-uniformised-factor-with-adjoint-pair/) repeats it. Through that copy it is step 2 of [`image_unif`](/entry/image-unif/), which then moves the uniformisation of $G_0$ to $G$.

## Statement

Use the notation of [`image_unif`](/entry/image-unif/): $R$ with `Base R`, data $D, D'$, a factor $F$ of $D$ in $D'$ with `F.Alg`, a ring $O$ with involution and $e, f \in O$, an $O$-linear uniformised $G'$ with bundle $L_{G'}$, and a semi-abelian $G$ with $i_G \colon G \to G'$, $p_G \colon G' \to G$, $p_G i_G = 1$, $i_G p_G = e$.

Call homomorphisms $u \colon G_1 \to G_2$ and $u' \colon G_2 \to G_1$ *adjoint* for bundles $L_1, L_2$ (`GAdj`) if $(u \times 1)^* \Lambda(L_2) \cong (1 \times u')^* \Lambda(L_1)$ on $G_1 \times G_2$.

**Theorem.** Let $G_0$ be semi-abelian over $R$ with a uniformisation $U_0$ by $D$ and bundle $L_{G_0}$. Then there are homomorphisms $u \colon G' \to G_0$ and $u' \colon G_0 \to G'$ such that:

1. $\varepsilon = u \, i_G \colon G \to G_0$ is an isomorphism;
2. $u' u = e^* f e$ as endomorphisms of $G'$;
3. $u$ and $u'$ are adjoint for $L_{G'}$ and $L_{G_0}$.

## Proof

From `F.Alg` take $e^* f e = e^* f^* e$ and $g \in O$ with $g \, e^* f e = e$.

1. `T.idempotentFactor_projection_adjointPair`: on the data, the projection $p \colon A_{D'} \to A_D$ and the map $e^* f \, i \colon A_D \to A_{D'}$ form an adjoint pair, with lattice maps $\xi'$ and $e^* f \xi$.
2. `T.uniformisedGroups_adjointHomPair_closedForm`: this pair extends to $u \colon G' \to G_0$ and $u' \colon G_0 \to G'$, adjoint for the bundles. Each one is *linear*: on every thickening $R/\mathfrak{m}^{k+1}$ it lies over the given map of abelian parts and restricts to the torus map of the given lattice map (`LinHom`).
3. By `OLinear`, each $a \in O$ acts on $G'$ linearly, over $a$ on $A_{D'}$ and $a^*$ on $X'$.
4. `linHom_unique`: two linear endomorphisms over the same pair of maps are equal. It rests on `MumUniq.main`: an endomorphism of a uniformised semi-abelian scheme is fixed by its formal data. The maps $u' u$ and $e^* f e$ lie over the same pair, by the identities of the factor. So $u' u = e^* f e$.
5. In the same way $u \, (e g) \, u' = 1$ on $G_0$, by $g \, e^* f e = e$ and $e^* e^* = e^*$.
6. The inverse of $\varepsilon$ is $p_G \, g \, u'$. Indeed $p_G g u' u i_G = p_G (g e^* f e) i_G = p_G e i_G = 1$, and $u i_G p_G g u' = u (e g) u' = 1$.

## In the Lean code

The theorem is in [IdempotentImageIsoUniformisedFactorOfAdjointPair.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageIsoUniformisedFactorOfAdjointPair.lean#L32), and `linHom_unique` is at [line 22](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageIsoUniformisedFactorOfAdjointPair.lean#L22). We read the statements of the lemmas in steps 1 and 2 and of `MumUniq.main`, not their proofs. None has an entry.

The proof discards the first clause of `F.Alg`, that $e^* e$ is a positive multiple of $e^* f e$. It never names the hypothesis `hG` that $G$ is semi-abelian; that fact also follows from clause 1. Lean writes composition in diagrammatic order, so $u' u = e^* f e$ is `u ≫ u' = oG.act (star F.e * F.f * F.e)`.
