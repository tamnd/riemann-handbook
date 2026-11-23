---
id: theorem-s-rec3-p
title: Theorem S for one pair, with the carrier supplied
kind: theorem
decl: Formalism.L2.SG.PoincareAmplitudeLowerBounds.theoremS_rec3P
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.TheoremSClosedP
covers: 917
status: drafted
drafted_by: writer@claude
---
This theorem is one step in the chain from [Theorem S](/entry/theorem-s-closed-p/) down to the abstract pair bound [`pbApplied`](/entry/pb-applied/). It removes one hypothesis of [`theoremS_rec2P`](/entry/theorem-s-rec2-p/), the carrier condition `CarrierFull`, with the global hypothesis `CarrierP`. The proof only chooses constants and passes hypotheses along. Its only user is `theoremS_closedP`.

## Statement

Assume `LocalModelAt`, `DensInputAt` and `RowsInputP` for each datum, the row bound `RowNGP` and the carrier bound `CarrierP` (see [`carrierP`](/entry/carrier-p/)). Then the conclusion of `theoremS_rec2P` holds, with these changes:

- the constant $C_4 \ge 1$ is now chosen by the theorem;
- the global size datum $G_0$, the words $d_e, d_e'$ and the index $l$ are not free. They are $G_0 = $ `gOf D e`, $d_e = $ `deOf D τ u`, $d_e' = $ `deOf D τ u'` and $l = $ `lOf` of these, for a bijection $e$ from the infinite places of $E$ to the index set `Tau` and an index $\tau$;
- the hypothesis `CarrierFull` is replaced by the four hypotheses of `CarrierP`: $i_0 = i_0'$, `PtRepExists`, `NuQPin`, and the condition that $e$ is compatible with the embeddings of $X$.

The conclusion is the same pair of bounds:
$$\|K_0(u,u')\|^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}, \qquad \|K_D(u,u')\|_{\mathrm{HS}}^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}.$$

## Proof

`CarrierP` gives $C_4 \ge 1$ and a threshold $C_{A,0}$. Apply `theoremS_rec2P` with $C_4$ and the threshold $\max(C_{\mathrm{thr}}, C_{A,0})$. This gives $C_A$, which is then at least $C_{A,0}$, so `CarrierP` applies at $C_A$ and gives a bound $k_{0,c}$ and constants $C'_1, C_{l,1}$. Take $k_0$ and the constant thresholds to be the maxima of the two. For a pair $(u, u')$, `CarrierP` gives `CarrierFull` at `gOf D e`, and `theoremS_rec2P` gives the bounds. The rest is bookkeeping.

## In the Lean code

The theorem is at [TheoremSClosedP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSClosedP.lean#L127). `CarrierP` is in the same file at line 20, and `gOf`, `deOf`, `lOf` are in [SpectralTiesReal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/SpectralTiesReal.lean#L294).

The file [SpectralTiesReal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/SpectralTiesReal.lean#L496) has a parallel theorem, `theoremS_recursion_constants`, with the same steps. It uses `CarrierC` and `RowNGC` in place of `CarrierP` and `RowNGP`. These are stronger: they do not assume `Ties D`, $c_b > 0$ or $c_{Tf} > 0$. No other file uses that version.
