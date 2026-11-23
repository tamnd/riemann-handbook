---
id: exists-s-rest-top
title: A row isometry and a spectral restriction after redivision
kind: theorem
decl: GlobalTheory.Mem.SRe.exists_sRest_top
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsSpectralLevelObjectsReplacedStages
covers: 350
status: drafted
drafted_by: writer@claude
---
This theorem finds a finite adelic point $t$ and an isometry $j$ from the space $E_E$ of a datum $D$ onto the good rows of a spectral pack $P$. Then it carries $j$ to each redivision of $D$. Its copy [`exists_spectralLevel_objects_replacedStages`](/entry/exists-spectral-level-objects-replaced-stages/) passes the result up toward [the unitary hypotheses node](/proof/unitary-hypotheses/). The proof is assembly from seven lemmas.

## Statement

Fix a datum $D$, real data $R$, a face $F$, forms $F_0$ of degree 0, and a linear map $e_E \colon E_E \to H$ into the space of $R$. A *spectral pack* $P$ (`SPack D F0`) holds a Hida setting $X$, a lattice datum $Y$, column dictionaries, a good operator $G$ and other data. Write $H_X$ for the rows of $X$ and $E_C$ for the good rows `EEC X G`.

**Theorem.** Assume five literature statements, among them `DSInfChar`, `HarishChandraFinite` and `CuspRapidDecay`, and thirteen conditions on $D$, $R$, $F$, $P$, $e_E$. Among them: `GapHyp D`, the range of $e_E$ is the preimage of the level $F$ part of $H$, and $\|e_E(x)\|^2 = n_P \|x\|^2$. Then there are $t$, $c > 0$ and $j$ with:

1. $\dim_{\mathbb{C}} H_X = D_{\mathrm{all}}$;
2. `SeeAt`: $t$ is finite, and conjugation by $t$ carries the level and character of $R$ to those of $X$;
3. `EvalTieT`: evaluation at a unit vector, then translation by $t$, is an isomorphism onto $E_C$ that multiplies squared norms by $c$;
4. `RowJ`: almost everywhere, $j(x)$ is a positive multiple of that evaluation of $e_E(x)$;
5. for each redivision of $D$ and forms with the same levels and values as $F_0$, the redivided $Y$ is finite and the redivided pack has a spectral restriction $S$ (`SRest`) with $S.j = j$.

## Proof

1. `exists_finiteAdelicPoint_carries_rowLevel` gives $t$.
2. `lowestVector_evaluation_identifies_levelRows_conj` gives the unit vector and $c$. It uses four literature statements and `GapHyp`.
3. `evaluation_goodRows_to_conjugate_goodRows` gives `EvalTieT`.
4. `levelColumnsGoodRows_le_principal_and_finiteDimensional` puts the level $F$ part inside the principal part. It uses `HarishChandraFinite` and `CuspRapidDecay`.
5. `exists_rowIsometry_conjugatedGoodRows_finrank` gives the dimension and $j$.
6. For a redivision, `finX_spectralRedivisionFullChoices` gives finiteness, and `exists_sRest_re` gives $S$.

## In the Lean code

The theorem is in [ExistsSpectralLevelObjectsReplacedStages.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralLevelObjectsReplacedStages.lean#L24). `exists_sRest_re` is in [ExistsSRestRe.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSRestRe.lean#L82); the other lemmas are in `*Statement` files of the same folder. `SPack` and `SRest` are in [SameDegreeZeroFormsSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/SameDegreeZeroFormsSelf.lean#L18), `SeeAt` and `RowJ` in [ConcreteLevelAdelicSubset.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ConcreteLevelAdelicSubset.lean#L38). We have not unfolded `HidaSetting`, the column dictionaries or most literature statements.

Each hypothesis is used. Step 4 keeps only the first half of its lemma. The map `eEECre` in clause 5 is the identity isometry ([ColDictIsomReTr.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ColDictIsomReTr.lean#L25)), so $S.j = j$ in substance.
