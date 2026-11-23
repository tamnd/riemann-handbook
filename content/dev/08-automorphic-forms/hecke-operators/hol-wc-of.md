---
id: hol-wc-of
title: The weight congruence from five inputs on Hecke data
kind: theorem
decl: UpperTheory.Esk.holWC_of
module: PositivityTheory.AutomorphicForms.PublishedInputs.JacquetLanglands.TorusKernels.FinalH
covers: 894
status: drafted
drafted_by: writer@claude
---
This theorem proves the weight congruence $\mathrm{HolWC}$ of [the weight-raising theorem](/entry/hol-wc/) from five hypotheses on the Hecke data of a level. It only passes facts along: the trace formula [`s_TF`](/entry/s-tf/) and the five hypotheses go to `pf_TrCong`, and its result goes to `pf_HolWC`, whose proof [the weight-raising entry](/entry/hol-wc/) describes. Most of the 894 declarations below it are below `s_TF`.

## Statement

Write $D_{c,\chi}$ for the datum `mkDat c χ` of a level $c$ and a character $\chi$ of the level group. The hypotheses:

- `DAx`: if $[F:\mathbb{Q}] \geq 2$, $c$ has finite support and $\chi$ has finite order, then $D_{c,\chi}$ meets the axioms `Dat.Ax`;
- `DTwo`: if $c$ is nontrivial at a place of norm 2, then finite subgroups of stabilizers of points of $\Omega$ have 2-power order;
- `DReps`: for each list $W$ of places there is a family $a$ with `IsReps c W a` (not unfolded);
- `DGood`: such a family is `Good`, and `Reg` when $W$ meets the support of $c$;
- `GTerm`: the normalized elliptic orbital terms in weights $k_0$ and $k_0 + 2t$ are $\ell$-integral and differ by at most $\max(|\ell|_\iota^N, |\ell|_\iota^r)$.

**Theorem.** These five statements imply $\mathrm{HolWC}$.

## Proof

`pf_TrCong` turns `s_TF` and `GTerm` into the trace congruence `TrCong`: the trace formula writes both traces as sums over one finite set of elliptic classes, and `GTerm` compares them term by term. Then `pf_HolWC` gives $\mathrm{HolWC}$ from `TrCong`, the lemma `Fin0` and eight facts (`H0` to `H2e`) that match automorphic forms with forms of $D_{c,\chi}$. The rest is bookkeeping.

## In the Lean code

The theorem is in [FinalH.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/FinalH.lean#L47); the hypotheses are in [IsHolVOf.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/IsHolVOf.lean#L108). The caller supplies them as `dAx`, `dTwo'`, `dGood'`, `dReps` and `pf_GTerm`.

Six facts in the same file have names about hyperbolic terms, but their statements are not: `hyperbolic_orbit_integral_holds : H0b` (finite order of $\chi$ and a sign condition), `hyperbolic_terms_setup_holds : H0`, `hyperbolic_relation_holds : H2a` (invariance and boundedness), `hyperbolic_tail_estimate_holds : H2d` (holomorphy), `hyperbolic_finite_sum_identity_holds : H2e` (bounded implies cuspidal) and `hyperbolic_terms_integrable_holds : H1`.
