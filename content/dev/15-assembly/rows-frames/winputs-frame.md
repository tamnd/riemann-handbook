---
id: winputs-frame
title: The lattice link of a Hida setting, from a frame and Galois data
kind: theorem
decl: GlobalTheory.ExpModel.winputs_frame
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ModelStatementOfFrameGalois
covers: 433
status: drafted
drafted_by: writer@claude
---
This theorem is step 4 of the proof of [the model statement from frames and Galois data](/entry/model-st-of-small-frame-gal/). For one maximal ideal $\mathfrak m$ of the Hecke algebra of a frame $F$, it proves `WInputsLink` for the Hida setting $X_{\mathfrak m}$ of $F$ at $\mathfrak m$. The proof is mostly assembly.

## Statement

Let $E$ be a CM field, $\ell$ a prime, $\iota$ a finite index set with embeddings $\mathrm{inc} \colon \iota \to \{E \to \overline{\mathbb{Q}}_\ell\}$, $P$ a parameter set of rank $N_r$ and $W$ weights with `W.Ok P`. Let $fr, cj$ be the maps of the [parent entry](/entry/model-st-of-small-frame-gal/), and $W'$ the weights $W$ with these maps (`reFr`). Assume:

- `ChebotarevDegreeOne`;
- the lattice link: for each highest weight $\mu$ that is `Linked` and `BlockFor`, `LatticeLink` holds at every $\tau$ for the restriction of $\mu(\tau)$;
- a good frame $F$ with Hecke algebra $T$ and coefficient ring $\mathcal{O}$, a predicate `Bk` with `GalSide`, a level map $j_K$, and a Hecke action on the forms with values in $\nabla_T$;
- $\mathcal{O}/\ell$ is finite and $\ell$ is not a unit in $\mathcal{O}$;
- a maximal ideal $\mathfrak m$ of $T$ and an eigensystem $\theta_0$ of $F$ with `Bk` $\theta_0$, over $\mathfrak m$.

Then `WInputsLink` $P$ $W'$ $X_{\mathfrak m}$ $\ell$ holds. This says: there are a uniformizer-type $\varpi$ with $\ell \mid \varpi^{n_0}$, projectors $e$ and a family of modules $L_\mu$ with Hecke actions, with the frame conditions `FrameA`, `FrameT`, `SimpleFacts`, such that each $L_\mu$ that is a subquotient of $\nabla_T / \varpi$ and has nonzero localization at $\mathfrak m$ satisfies `LatticeLink` at each $\tau$ in `W.T2`. We have not unfolded `FrameA`, `FrameT`, `SimpleFacts` or `LatticeLink`.

## Proof

1. `exists_unif_dvd` gives $\varpi$ with $\varpi \mid \ell$ and $\ell \mid \varpi^{n_0}$.
2. `ExpFrame.exists_unique_isProj` gives the projectors $e$.
3. Let $G$ be a simple subquotient of $\nabla_T / \varpi$. `ExpFrame.HeckeMod.hecke_module` gives a Hecke action on the forms with values in $G$. `T.simpleSubquotient_dualWeyl_embeds_highestWeight` gives a highest weight $\mu$ of $G$. `T.heckeStable_of_heckeFrame_polynomial_action` makes the Hecke maps natural. If the localization at $\mathfrak m$ is nonzero, `T.latticeLink_of_surviving_simple_subquotient` gives `LatticeLink` for $\mu$.
4. `winputs_of_simple` takes the simple subquotients themselves as the family $L_\mu$ and assembles `WInputsLink`, with `ExpFrame.alg_chainB_stable` for `FrameA`.

## In the Lean code

The theorem is in [ModelStatementOfFrameGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ModelStatementOfFrameGalois.lean#L87), and `winputs_of_simple` is at [L63](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ModelStatementOfFrameGalois.lean#L63) of the same file. `WInputsLink` is in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L403).

The Chebotarev hypothesis, the lattice link, `GalSide`, `Bk` and $\theta_0$ go only to `T.latticeLink_of_surviving_simple_subquotient`. That lemma has the content of this theorem; it has no entry of its own. The theorem proves `LatticeLink` at every $\tau$, more than the $\tau \in$ `W.T2` that `WInputsLink` asks for.
