---
id: image-unif
title: The image of an idempotent on a uniformised group is uniformised
kind: theorem
decl: GlobalTheory.MumDesc.image_unif
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IdempotentImageUniformisedByFactorData
covers: 328
status: drafted
drafted_by: writer@claude
---
Let a ring $O$ with involution act on a uniformised semi-abelian scheme $G'$, and let $G$ be the image of an idempotent $e \in O$. This theorem says that $G$ is uniformised by the degeneration data that $e$ cuts out of the data of $G'$, with the polarisation that an element $f$ induces. The [statement entry](/entry/idempotent-image-uniformised-by-factor-data/) repeats it, and that copy is used below [`exists_chart_at`](/entry/exists-chart-at/).

## Statement

Let $R$ be a local domain with `Base R`, as in [`hasSemiAbelianUniformisation_complete_normal_base`](/entry/has-semi-abelian-uniformisation-complete-normal-base/). Let $D, D'$ be degeneration data over $R$, with abelian parts $(A_D, L_D)$ and $(A_{D'}, L_{D'})$, lattices $X, X'$ and periods $\tau, \tau'$. Write $\Lambda(L)$ for the Mumford bundle on the square (`abelian₂`).

A *factor* $F$ of $D$ in $D'$ (`Mum.Factor`) has:

- a ring $O$ with involution $*$ that acts on $X'$ and on $A_{D'}$, compatibly with the points and the periods of $D'$;
- $e, f \in O$ with $e^2 = e$;
- homomorphisms $i \colon A_D \to A_{D'}$, $p \colon A_{D'} \to A_D$ with $p i = 1$ and $i p = e$, and maps $\xi \colon X \to X'$, $\xi' \colon X' \to X$ with $\xi' \xi = 1$ and $\xi \xi' = e$, compatible with the points;
- $\Lambda(L_D) \cong (i \times f i)^* \Lambda(L_{D'})$, and $\tau(a, b) = \tau'(\xi a, f \xi b)$ up to this isomorphism;
- $y \mapsto e^* f \xi(y)$ is a bijection from $X$ onto $e^* X'$.

`F.Alg` asks that $e^* e = k \, e^* f e$ for some integer $k > 0$, that $e^* f e = e^* f^* e$, and that $g \, e^* f e = e$ for some $g \in O$.

**Theorem.** Let $F$ satisfy `F.Alg`. Let $G'$ be semi-abelian over $R$ with a uniformisation $U'$ by $D'$, let $O$ act on $G'$ and on its generic fibre, and let $U'$ be $O$-linear (`OLinear`: the actions agree on the generic fibre, on the abelian quotient of each thickening, and on the torus through $*$). Let $G$ be semi-abelian with homomorphisms $i_G \colon G \to G'$, $p_G \colon G' \to G$, $p_G i_G = 1$, $i_G p_G = e$. Then there is a uniformisation $U$ of $G$ by $D$ with

$$\Lambda(L_G) \cong (i_G \times f i_G)^* \Lambda(L_{G'}).$$

## Proof

1. [`hasSemiAbelianUniformisation_complete_normal_base`](/entry/has-semi-abelian-uniformisation-complete-normal-base/): Mumford's construction gives some $G_0$ with a uniformisation $U_0$ by $D$.
2. [`idempotent_image_iso_uniformised_factor_with_adjoint_pair`](/entry/idempotent-image-iso-uniformised-factor-with-adjoint-pair/): there are an isomorphism $\varepsilon = u i_G \colon G \to G_0$ and maps $u \colon G' \to G_0$, $u' \colon G_0 \to G'$, adjoint for the bundles, with $u' u = e^* f e$.
3. `T.exists_uniformisation_along_group_iso_lbIso`: transport $U_0$ along $\varepsilon$. This gives $U$ with $L_G \cong \varepsilon^* L_{G_0}$.
4. `T.semiAbelian_groupAction_star_adjoint_bundle`: $x$ and $x^*$ are adjoint on $G'$ for each $x \in O$.
5. `T.mumfordBundle_retract_of_adjoint_pairs`, with $E = e$, $E' = e^*$ and $f$: from $e i_G = i_G$, $u' u = e^* f e$ and the two adjunctions, it gives the bundle identity.

The rest is bookkeeping.

## In the Lean code

The theorem is in [IdempotentImageUniformisedByFactorData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IdempotentImageUniformisedByFactorData.lean#L18). We read the statements of the lemmas in steps 3 to 5, not their proofs; they have no entry in the outline. The generic fibre of $U$ is the $A_0$ of step 1. In Lean the factor is called `Factor`, and its "image" is the retract $G$, given as a hypothesis, not built.
