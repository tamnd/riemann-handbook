---
id: ck-relations-of-model
title: The Chern number relations by a chain of model refinements
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CkTop.ckRelations_of_model
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModels
covers: 708
status: drafted
drafted_by: writer@claude
---
This theorem proves the relations `CkRelations` for the bundles of a lattice family on a model over a discrete valuation ring. Its statement form is [`lattice_family_ckRelations`](/entry/lattice-family-ck-relations/), which feeds [the relations for flag pairs](/entry/top-rel-relations/). The proof is the top of a chain of seven theorems. Each link either replaces the model by a finer one, on which one more condition on the charts holds, or proves one more condition directly. The last link, [`stage5`](/entry/stage5/), proves the relations.

## Statement

The statement is that of [`lattice_family_ckRelations`](/entry/lattice-family-ck-relations/), with the same names: $O$ of characteristic $0$, coordinates $x$ whose ideal is a model of dimension $d$ with function field $\Omega$, a prime $p$, $w$, $\chi$, $\varphi$, a lattice family $D$ and chart bundles $\mathrm{Lie}, W, \Omega_1, \Omega_{\mathrm{HT}}$ with the lattices of $D$. The conclusion is `CkRelations` for these bundles.

## Proof

**Refinement and descent.** A refinement of $x$ is a second set of coordinates $z$ in $\Omega$ such that the joined coordinates $(x, z)$ (`joinCoord x z`) are again a model of dimension $d$. The charts of $(x, z)$ restrict to charts of $x$. The pulled family (`pullFamily`) has, on each chart of $(x, z)$, the lattices of $D$ spanned over the larger chart ring. The lemma `descend` says: if `CkRelations` holds for all bundles of the pulled family on $(x, z)$, it holds for all bundles of $D$ on $x$. Its proof uses three lemmas.

- `lattice_family_injective_model`: the pulled family is a lattice family, the chart conditions below pass to it, and each set of bundles of $D$ has a pullback (`IsPull`) to bundles of the pulled family.
- `chart_rings_noetherian_fraction`: the chart rings are Noetherian, and the function field of $(x, z)$ is again $\Omega$.
- `model_over_prime_perm_module_lattice`: `CkRelations` descends along `IsPull`, given that $\mathrm{Lie}$ and $W$, and $\Omega_1$ and $\Omega_{\mathrm{HT}}$, have the same generic fibre. `sameGeneric_of` proves this from the inclusions of $D$.

**The chain.** On a chart with ring $R$, write $\mathfrak{a}_\tau$ for the lattice `af`, the preimage of $M + pR^{F^n}$ under the map that $\chi_\tau$ defines. The conditions are added in this order.

| Link | Condition added | Lemma |
|---|---|---|
| this theorem | `Good₁`: lattices are locally free and some subspaces are direct summands | `lattice_family_model_facts`, by refinement |
| [`stage1`](/entry/stage1/) | normal charts: each chart ring is integrally closed in $\Omega$ | `model_refinement_exists`, by refinement |
| [`stage1b`](/entry/stage1b/) | $w R^n \subseteq \mathfrak{a}_\tau$ | `hodge_annihilator_lattice_holds`, on the same model |
| [`stage2`](/entry/stage2/) | `Good₂`: more summand and freeness conditions | `lattice_family_model_comparison`, by refinement |
| [`stage3`](/entry/stage3/) | the ideals `xId` are lines | `lattice_family_model_chern`, by refinement |
| [`stage4`](/entry/stage4/) | normal charts again, on the newest model | `model_refinement_exists`, by refinement |
| [`stage5`](/entry/stage5/) | the relations | `model_over_mod_p_lattice_eigen_split` |

In this theorem, `lattice_family_model_facts` gives a refinement $z$ with `Good₁` for the pulled family. Then `stage1` on $(x, z)$ and `descend` give the relations on $x$.

## In the Lean code

The theorem is in [DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L156), and `descend` is at [line 82](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L82). The helper `inj_of_model` (line 22) shows that $O \to \Omega$ is injective, from the condition in `IsModelOver` that the model meets the constants $O$ in $0$. The lemmas in the table are statement forms; we have not opened their proofs. The names `stage1`, `stage1b` and so on do not say what each link adds.
