---
id: thm-pactual-cpt-of-leaves
title: The compact form of Theorem P from three leaf facts
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_leaves
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutSETopHer
covers: 383
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThmPActualCpt`, the compact form of Theorem P, from three facts about the densities at the first level: `OneLetterDens`, `DensSmoothCls` and `RadDecay`. Its only user is [the compact form of Theorem P from the spectral identity](/entry/thm-pactual-cpt-of-spec/), which supplies the three facts. The proof builds the step expansion `StepExp0` and passes it on.

## Statement

Use the setting of [the compact form of Theorem P](/entry/actual-compact-theorem/). Each fact below is for all data with `IsData`, $1 \le l_0 \le k$ and a matching real place datum, and only for the level $l = 0$. Let $D(t) = \mathrm{Dens}(\mu, l, u, v, c)(t)$ be the density of a pair $u, v$ in the class `ClsE`, at a point $c$ of `OmX`.

- `DensSmoothCls`: $D$ is $C^n$ on $t \ne 0$ for every $n$, and $u, v$ are square integrable at level $l + 1$.
- `OneLetterDens`: for each letter with real point there are $e$ and a Wirtinger derivative $\partial$ such that acting by the letter changes $D$ to $D + e\, \partial D'$. Here $D'$ is the density of $u$ and a modified $v$.
- `RadDecay`: for radial vectors $\Phi, \Psi$ that agree on `DomR` with restrictions of nice coefficients, and multiplication by $f_s(c_l)$, the pairing `LocFacts₂` is at most $C (1 + |s|)^{-(n + 3)}$, for each $n$.

**Theorem.** These three facts imply `ThmPActualCpt`.

## Proof

1. `decayPair2_of_smooth` gets `DecayPair2` (continuity of $D$ at $t \ne 0$) from `DensSmoothCls`.
2. `clsDecayJ_of` turns `RadDecay` into a decay statement. With `wave_outgoing_orbital`, `decayPair3_of` gives $|\int f_s(t) D(t)\, dt| \le C (1 + |s|)^{-(n+3)}$ (`DecayPair3`). With also `site_multiplication_orbital`, `decayPair4_of` gives the same bound with the weight $(1 + |t|^2)^2$ (`DecayPair4`).
3. `stepExp0_of_open` combines these with `OneLetterDens` and `DensSmoothCls` into `StepExp0`. For each allowed word, `ph` is a finite sum of derivatives of decaying functions, and the integral of its order-zero terms is `RRform` (`DerivCombInt`).
4. `thmPActualCpt_of_stepExp0` gives `ThmPActualCpt`, through `theorem_P_compact_of_step_density` and `level_transport_hermitian`.

We have not unfolded `Dens`, `LocFacts₂` or `wirt`.

## In the Lean code

The theorem is at [CutSETopHer.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSETopHer.lean#L13), and `stepExp0_of_leaves` at line 9. The three facts are in [CutSE2.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSE2.lean#L263), at lines 263, 320 and 362. The decay lemmas are in [CutSEDecayAsm.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSEDecayAsm.lean#L326). `StepExp0` is in [TheoremPCompactOfStepDensity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/TheoremPCompactOfStepDensity.lean#L120).
