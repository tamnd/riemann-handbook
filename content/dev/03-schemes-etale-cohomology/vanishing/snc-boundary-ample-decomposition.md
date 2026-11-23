---
id: snc-boundary-ample-decomposition
title: Kawamata-Viehweg vanishing for a divisor on an snc boundary, second name
kind: theorem
decl: GlobalTheory.T.snc_boundary_ample_decomposition
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.SncBoundaryAmpleDecompositionStatement
covers: 594
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`vanishing_ample_snc_cartier`](/entry/vanishing-ample-snc-cartier/). It has the same statement, and its proof only calls that theorem. The [vanishing theorem on a log resolution](/entry/vanishing-log-res-floor/) uses it as its last step. That entry and the entries below this one have the content. Below this theorem are 594 declarations.

## Statement

Let $k$ be a field of characteristic $0$ and $Y$ an integral scheme, smooth of dimension $n$ and projective over $k$. Let $K_Y$ be its canonical bundle. Let $B \subseteq Y$ be a closed set whose reduced ideal is a simple normal crossings divisor. Let $\Gamma$ be an effective Cartier divisor with support in $B$, and $e \in \mathbb{N}$ with $\operatorname{mult}_z \Gamma < e$ at each point $z$. Let $Q$ and $A$ be line bundles, $A$ ample, with

$$e\,[Q] = e\,[K_Y] + [\mathcal{O}(\Gamma)] + [A] \quad \text{in } \operatorname{Pic} Y.$$

Then $H^i(Y, Q) = 0$ for all $i > 0$.

This is a case of Kawamata-Viehweg vanishing (Kawamata, Math. Ann. 261, 1982; Viehweg, J. reine angew. Math. 335, 1982): $Q - K_Y$ is $\mathbb{Q}$-linearly equivalent to $\Gamma/e + A/e$, where $\Gamma/e$ has snc support and coefficients in $[0, 1)$, and $A/e$ is ample.

## Proof

The proof is `vanishing_ample_snc_cartier` applied to the same arguments.

## In the Lean code

The theorem is in [SncBoundaryAmpleDecompositionStatement.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/SncBoundaryAmpleDecompositionStatement.lean#L11). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with the name `GlobalTheory.Div.SncBoundary.vanishing_ample_snc_cartier` in each branch. The two statements are identical, letter for letter. The conclusion is stated for the sheaf `twist (structureModule Y) Q`, that is $\mathcal{O}_Y \otimes Q$. The only use of this name is in [MultiplierVanishingNefTwist.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierVanishingNefTwist.lean#L113), in the proof of `vanishing_logRes_floor`.
