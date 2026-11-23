---
id: exists-dual
title: The dual abelian scheme, glued from affine pieces
kind: theorem
decl: GlobalTheory.DualExist.exists_dual
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsDualAbelianSchemePoincare
covers: 799
status: drafted
drafted_by: writer@claude
---
This theorem builds the dual of an abelian scheme $A \to S$ over an arbitrary base. It makes the dual over affine opens on which $A$ has constant relative dimension and glues the pieces. The second name [exists_dual_abelianScheme_poincare](/entry/exists-dual-abelian-scheme-poincare/) passes it to [the dual abelian scheme with biduality](/entry/dual-abelian-scheme/). The construction over an affine base is in [hasRep_affine](/entry/has-rep-affine/).

## Statement

Let $A$ be an abelian scheme over a scheme $S$. Then there are an abelian scheme $B$ over $S$ and a line bundle $P$ on $A \times_S B$ such that $P$ makes $B$ the dual of $A$ (`IsDual`), and `DimLe A B` holds: each base change $T \to S$ along which $A_T \to T$ is smooth of relative dimension $g$ makes $B_T \to T$ smooth of relative dimension $g$.

Let $S' \to S$ be an $S$-scheme. A *representative of rank $g$ over $S'$* (`HasRep A g S'`) is an $S$-scheme $B$ with a map $b \colon B \to S'$ and a line bundle $P$ on $A \times_S B$ with two properties. First, $P$ is an additive line bundle, and for each $T$ over $S'$ and each additive line bundle $N$ on $A \times_S T$ there is exactly one $x \colon T \to B$ over $S'$ with $N \cong (1 \times x)^* P$ (`Rep`). Second, $b$ is proper, smooth of relative dimension $g$ and geometrically connected (`Good`).

## Proof

1. `abelianScheme_locally_constant_relDim`: each $s \in S$ has an affine open neighbourhood $V_s$ over which $A$ is smooth of some relative dimension $g_s$.
2. [`hasRep_affineOpen`](/entry/has-rep-affine-open/): over each $V_s$ there is a representative of rank $g_s$. Its proof base-changes $A$ to $\operatorname{Spec} \Gamma(V_s)$, which is again an abelian scheme (`isAbelianScheme_of_isGrpPullback`). It applies [the affine case](/entry/abelian-scheme-dual-representable-affine-base/) there, and moves the result back with `hasProperSmoothDualRepresentative_grpPullback_iff` and the isomorphism $\operatorname{Spec} \Gamma(V_s) \cong V_s$ (`hasRep_of_iso`).
3. `exists_additiveFamily_representative_zariski_glue` glues these into one $B$ over $S$ and one $P$. Then $B$ represents additive line bundles over all of $S$, and over each $V_s$ it is proper, smooth of relative dimension $g_s$ and geometrically connected.
4. `representing_additiveFamilies_isDual_comm` gives a commutative group structure on $B$ for which $P$ makes $B$ the dual of $A$.
5. Smoothness, properness and geometric connectedness are local on the base. So step 3 makes $B$ an abelian scheme.
6. `relDimPreserved_of_equal_local_relDims` gives `DimLe A B` from the equal relative dimensions over the cover. It uses that $A \to S$ is surjective, which follows from geometric connectedness.

## In the Lean code

The theorem is at [ExistsDualAbelianSchemePoincare.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDualAbelianSchemePoincare.lean#L63). `Rep`, `HasRep`, `Good` and `DimLe` are in [SameIdIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SameIdIff.lean#L28).

- The lemmas from `GlobalTheory.T` in steps 1 to 4 and 6 are second names of theorems in `GlobalTheory.DualCon`. We have read their statements, not their proofs.
- This proof only assembles. The work is in the gluing lemma and in the affine case, `abelianScheme_dual_representable_affine_base`. It claims a dual that is a scheme, proper and smooth over $\operatorname{Spec} R$, for each commutative ring $R$. It has no noetherian or projectivity hypothesis. [The parent entry](/entry/dual-abelian-scheme/) notes that this may ask for more than the published results give.
- The fourth output of `representing_additiveFamilies_isDual_comm`, additivity of the swapped bundle, is dropped here.
