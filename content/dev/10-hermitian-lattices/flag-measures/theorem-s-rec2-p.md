---
id: theorem-s-rec2-p
title: Theorem S for one pair, with the non-generic row bound supplied
kind: theorem
decl: Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec2P
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.TheoremSClosedP
covers: 916
status: drafted
drafted_by: writer@claude
---
This theorem is one step in the chain from [Theorem S](/entry/theorem-s-closed-p/) down to the abstract pair bound [`pbApplied`](/entry/pb-applied/). It takes [`theoremS_rec`](/entry/theorem-s-rec/) and removes its hypothesis on the non-generic rows, `RowNG`, with the global row bound `RowNGP`. It also fixes the exponent $c_5 = \tfrac13$ and moves the loop hypotheses from the abstract size datum $G_0$ to the datum $D$. Its only user is [`theoremS_rec3P`](/entry/theorem-s-rec3-p/). The proof is bookkeeping.

## Statement

Assume `LocalModelAt`, `DensInputAt` and `RowsInputP` for each datum, and `RowNGP`. Let $C_4 \ge 1$ and $C_{\mathrm{thr}}$ be real. The conclusion has the shape of `theoremS_rec`, with these changes:

- there is a new layer of constants $C_g, c_b, C_w, c_{Tf}, C_T, C_{0f}$ (with $c_b, c_{Tf} > 0$), and then $C_n \ge 0$ and thresholds $C'_0, C_{l,0}$ for the counting constants $C' \ge C'_0$, $C_l \ge C_{l,0}$;
- the data are a tie package $T$ (`STies`) in place of $X$, $h_b$, $Y$, $\psi$;
- the hypotheses `Ties D`, `Hyp0`, `Stand`, `ConcTie` and absolute convergence of $t_O(u, u')$ are added;
- `RowBig` and `RowNotScalar` are stated with $\varepsilon_L = \exp(-\tfrac13 k f \log k)$ and $d = d(u) d(u') / D^*$ for the rank data $k, f$ of $D$, and `RowNG` is dropped;
- `PrimeHyp`, `LocTied` and the isomorphism `SIso` are dropped; they now follow from `Stand`, `ConcTie` and the field `hI` of $T$.

The conclusion is the same pair of bounds on $\|K_0(u,u')\|^2$ and $\|K_D(u,u')\|_{\mathrm{HS}}^2$ by $(1 + b^{-6})\, d(u) d(u') / D^*$.

## Proof

Take $C_A$, $C$ and $k_0$ from `theoremS_rec`. Given the new constants, `RowNGP` gives $C_4' \ge 0$ (the $C_n$ of the statement) and thresholds; for $C', C_l$ above them, it gives `RowNG` for $t_O(u, u')$ with the bound $2^{-(k-2r-5)} \exp(C_4' (2r+2)^5 f \log b)$.

Next, the carrier hypothesis `CarrierFull` contains a Hida setting whose size datum is $G_0$ and that is compatible with $D$. By `glob_f_eq`, this gives $k(G_0) = k$, $r(G_0) = r$ and $f(G_0) = f$. `ConcTie` identifies the concrete $d(u)$, $d(u')$ and $D^*$ with `duS` and `Dstar`. With these equalities the three row hypotheses take the form that `theoremS_rec` needs. `LocTied` is a component of `ConcTie`, and `primeHyp_of_stand` gives `PrimeHyp`. The rest is bookkeeping.

## In the Lean code

The theorem is at [TheoremSClosedP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSClosedP.lean#L41). `RowNGP` is in [RowsPos.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowsPos.lean#L37), and $\varepsilon_L$ is `epsL` in [RowsConc.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RowsConc.lean#L45).

The file [SpectralTiesReal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/SpectralTiesReal.lean#L323) has a parallel theorem, `theoremS_recursion_fixed`, with `RowNGC` in place of `RowNGP`. `RowNGC` does not assume `Ties D`, $c_b > 0$ or $c_{Tf} > 0$. Only `theoremS_recursion_constants` uses it.
