---
id: classified-of-complete
title: A Siegel family classifies principal objects over complete noetherian local rings
kind: theorem
decl: GlobalTheory.SFamCompl.classified_of_complete
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelFamilyClassifiesCompleteNoetherianLocal
covers: 401
status: drafted
drafted_by: writer@claude
---
This theorem proves that a Siegel family classifies each principal Siegel object over a complete noetherian local ring $R$. It classifies the object over each Artinian quotient $R/\mathfrak{m}^{e+1}$ by [the Artinian case](/entry/siegel-point-lifts-to-artinian/), glues the maps to one map from $\operatorname{Spec} R$, and then checks that the pullback of the universal object is the given one. [Its statement form](/entry/siegel-family-classifies-complete-noetherian-local/) repeats it for [the noetherian local case](/entry/exists-point-of-principal/).

## Statement

Use $B_n = \mathbb{Z}[\zeta_n, 1/n]$, Siegel objects, the pullback relation $c \cong f^*u$ and Siegel families $(X, s, u)$ as in [the affine entry](/entry/exists-classify-affine/).

**Theorem.** Let $g \geq 1$ and $n \geq 3$ odd, and let $(X, s, u)$ be a Siegel family of genus $g$ and level $n$. Let $R$ be a noetherian local ring, complete for its maximal ideal $\mathfrak{m}$. Let $\beta \colon B_n \to R$ and let $c$ be a principal Siegel object over $\operatorname{Spec} R$. Then there is $f \colon \operatorname{Spec} R \to X$ with $sf = \operatorname{Spec} \beta$ and $c \cong f^*u$.

## Proof

Let $R_e = R/\mathfrak{m}^{e+1}$ and $i_e \colon \operatorname{Spec} R_e \to \operatorname{Spec} R$.

1. **Artinian quotients.** Each $R_e$ is local (`quot_local`) and Artinian (`quot_artin`: it is noetherian of dimension $0$).
2. **Points over the quotients.** Let $c_e$ be a pullback of $c$ to $R_e$. It is principal (`siegPre_pull_ringChange`). [The Artinian case](/entry/siegel-point-lifts-to-artinian/) gives $x_e \colon \operatorname{Spec} R_e \to X$ over $B_n$ with $c_e \cong x_e^*u$.
3. **Compatibility.** The restriction of $c_{e+1}$ to $R_e$ is $c_e$ (`SiegelPullComp.pb_cancel`). So $x_{e+1}$ restricted to $R_e$ also classifies $c_e$, and the uniqueness lemma `siegelFamily_classifyingMap_unique` gives that it equals $x_e$.
4. **Gluing.** `exists_glue_spec_complete_localRing_thickenings` gives $f \colon \operatorname{Spec} R \to X$ with $f i_e = x_e$ for all $e$. We have not opened its proof.
5. **The base.** The maps $sf$ and $\operatorname{Spec} \beta$ agree after each $i_e$. Since $R$ is $\mathfrak{m}$-adically separated, two ring maps into $R$ that agree modulo each $\mathfrak{m}^{e+1}$ are equal (`ext_affine`, proved in the file). So $sf = \operatorname{Spec} \beta$.
6. **The object.** Let $c' = f^*u$, a principal object over $R$. By steps 2 and 4, $c$ and $c'$ both restrict to $c_e$ on each $R_e$. The lemma `alg` concludes $c \cong c'$, so $c \cong f^*u$ (`SiegelPullComp.pb_comp`).

The proof of `alg` has two parts. First, `tower` picks maps of abelian schemes $A_{c_e} \to A_{c_{e+1}}$ that are compatible with the maps to $A_c$ and to $A_{c'}$. Compatibility holds because a map of a Siegel object into a principal one of odd level $n \geq 3$ over a given base map is unique (`SiegRigid.eq_of_sRelBy`). Second, `assemble` is `siegelObjects_pullback_of_compatibleTower_adic`: over a noetherian ring complete for an ideal $I$, two Siegel objects that are linked by such a compatible tower over the quotients $R/I^{e+1}$ are isomorphic, if one of them is principal. We have not opened its proof.

## In the Lean code

The theorem is in [SiegelFamilyClassifiesCompleteNoetherianLocal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesCompleteNoetherianLocal.lean#L127). The helper lemmas `glue`, `ext_affine`, `srel_comp`, `tower`, `assemble`, `alg`, `quot_local` and `quot_artin` are in the same file, from [line 19](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFamilyClassifiesCompleteNoetherianLocal.lean#L19). The lemmas from other files:

- `GlobalTheory.T.siegel_point_lifts_to_artinian`, where the deformation content is;
- `GlobalTheory.T.siegelFamily_classifyingMap_unique`, a statement form;
- `GlobalTheory.T.exists_glue_spec_complete_localRing_thickenings` and `GlobalTheory.T.siegelObjects_pullback_of_compatibleTower_adic`, statement forms;
- `GlobalTheory.SiegelRingChange.siegPre_pull_ringChange`, `GlobalTheory.SiegelPullComp.pb_cancel` and `pb_comp`;
- `GlobalTheory.SiegRigid.eq_of_sRelBy` in [PrincipalSiegelObjectOddLevelRigid.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PrincipalSiegelObjectOddLevelRigid.lean#L107).

`glue` and `assemble` are only new names for the two statement forms. The rigidity lemma needs a base datum: `cycBase` gives $\zeta_n$ as a unit of $B_n$ with $\zeta_n^n = 1$, and $n$ as a unit.
