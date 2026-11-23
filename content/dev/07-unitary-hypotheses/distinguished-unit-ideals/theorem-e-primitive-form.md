---
id: theorem-e-primitive-form
title: Theorem E for lattices over power series, in primitive form
kind: theorem
decl: Formalism.ExponentWindows.E.theorem_E_primitive_form
module: Formalism.DistinguishedUnitIdeals.DistinguishedOrderProofs.ThmEPrim
covers: 397
status: drafted
drafted_by: writer@claude
---
This theorem has the conclusion of [theorem E in final form](/entry/theorem-e-final-form/), under hypotheses that no longer mention the windows of jumps. That entry calls it after it turns each arc into a primitive arc. The proof checks the "good" conditions of the full form `theorem_E_full_form` and applies it.

## Statement

The lattices, maps, cuts and coboundaries are as in [theorem E in final form](/entry/theorem-e-final-form/). Let $H$ assign a function $\mathbb{N} \to \mathbb{N}$ to each cut, and let $j, g, G, h_h, \sigma, r, \kappa, \ell_{\max}$ be integers. Put $M = \lfloor (h_h + 2g)/(\ell - 1) \rfloor + 1$ and $A = 2\sigma + r + 2g\,\ell_{\max}$.

**Theorem.** Assume:

1. (`PrimBase`) $\ell \ge 3$ is prime and associated to $\varpi^e$ with $e \ge 1$, $\mathcal{O}$ is $\ell$-adically complete, and $\varphi, \gamma$ satisfy `E3` and `E4`;
2. (`PrimNum`) $G \le g \le h_h$, $1 \le j \le \ell_c \le \ell_{\max}$ at each cut, and `SigOK` for $\ell, j, M, g, \sigma$;
3. (`PrimLat`) for $L_1$ and $L_2$: `P9`, `P5M`, freeness, torsion conditions and pullback conditions at the cuts;
4. (`PrimUnit`) and (`PrimBK`) as in the final form;
5. (`PrimArc`) at each cut $c$, level data for both lattices, a level map, kinds, sizes and polynomials with about thirty properties.

Then for each $z \in Z_2$ there is $z' \in Z_1$ such that $\ell^E z - h(z')$ is a coboundary in $L_2$, with $E = 2r + 4\sigma + 2A + 2\kappa$.

We have not unfolded the properties in `PrimArc`.

## Proof

The full form `theorem_E_full_form` has the same conclusion with $a_0 = A$. It asks for "good" conditions, and the proof supplies them:

- `baseGood`: the base is good for $j, M, g$, from `E3` and `E4`;
- `latGood`: each of $L_1, L_2$ is good;
- `extGood`: each extension in `PrimBK` is good, from saturation and extension lemmas;
- `arcHyp`: each `PrimArc` gives the arc hypothesis `ArcHyp`;
- $M \ge 1$, and $r \le 2A$, which is clear from the definition of $A$.

## In the Lean code

The theorem is at [ThmEPrim.lean](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEPrim.lean#L477), and its statement `ThmEPrim` at [FrobeniusCoboundedArc.lean](lean:Formalism/DistinguishedUnitIdeals/FrobeniusCoboundedArc.lean#L206). The helpers are in the namespace `Prim` of the same file: `baseGood` ([line 326](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEPrim.lean#L326)), `latGood` ([line 337](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEPrim.lean#L337)), `extGood` ([line 410](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEPrim.lean#L410)) and `arcHyp` ([line 432](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEPrim.lean#L432)). `theorem_E_full_form` is at [ThmEFull.lean](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEFull.lean#L140); it has the real content.

- The inequality $r \le 2A$ is proved by `first | omega | nlinarith`.
- The parameter $\kappa$ appears in the hypotheses only inside `PrimArc`.
