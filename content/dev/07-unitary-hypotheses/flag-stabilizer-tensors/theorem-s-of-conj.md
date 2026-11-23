---
id: theorem-s-of-conj
title: Theorem S from the conjunction of its hypotheses
kind: theorem
decl: Formalism.L2.SG.TheoremSConclusion.theoremS_of_conj
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.TheoremSConclusion
covers: 923
status: drafted
drafted_by: writer@claude
---
This theorem is Theorem S with its 19 hypotheses packed into one proposition, `TheoremSClosedHypotheses`. [`offDiag`](/entry/carrier-gap-off-diag/) gets that proposition from [`theoremS_leaves_of_carrierG`](/entry/theorem-s-leaves-of-carrier-g/) and calls this theorem to bound the off-diagonal entries $K_0(u, u')$. The proof only passes hypotheses along. The content is in [`theoremS_closedP`](/entry/theorem-s-closed-p/) and below it.

## Statement

**Theorem.** Assume `TheoremSClosedHypotheses`, the conjunction of the 19 conditions listed in [the nineteen hypotheses of Theorem S](/entry/theorem-s-leaves-of-carrier-g/). Then the conclusion of [`theoremS_closedP`](/entry/theorem-s-closed-p/) holds: for each real $C_{\mathrm{thr}}$ there are constants such that, for each datum $D$, size data $L$ with scale $b \ge 0$, tie package $T$ and words $u \neq u'$ that meet the size and standing hypotheses,
$$\|K_0(u,u')\|^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}, \qquad \|K_D(u,u')\|_{\mathrm{HS}}^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}.$$

## Proof

Split the conjunction into its 19 parts and apply `theoremS_closedP` to them, in the same order.

## In the Lean code

The theorem is at [TheoremSConclusion.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSConclusion.lean#L68). The definition `TheoremSClosedHypotheses` is in the same file, at line 58. The proof is two lines: an `obtain` of the 19 parts and one call of `theoremS_closedP`.

The statement is word for word the statement of `theoremS_closedP`, with its 19 hypotheses replaced by their conjunction. A different definition with the same short name, `ThmSOwn.TheoremSClosedHypotheses`, is a conclusion and not a list of hypotheses (see [the nineteen hypotheses of Theorem S](/entry/theorem-s-leaves-of-carrier-g/)).
