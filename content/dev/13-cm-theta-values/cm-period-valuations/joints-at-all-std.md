---
id: joints-at-all-std
title: Joints at every tuple from a column part
kind: theorem
decl: GlobalTheory.Svd.jointsAt_all_std
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JointsAtAllStd
covers: 429
status: drafted
drafted_by: writer@claude
---
This theorem gives the first input of [`modelsAt_of_part`](/entry/models-at-of-part/): a tied kernel entry with joints at every tuple, and an identity of twisted forms at step zero. It opens the column part of an object and passes its fields to [`kernel_relation_true_columns_joints_all_tuples`](/entry/kernel-relation-true-columns-joints-all-tuples/). The mathematics is further down, in [`joints_all_true`](/entry/joints-all-true/).

## Statement

Let $B$, $f$, $T$, the column datum $w$, the later stage $Z$, the datum $D = w.D(Z)$ and the object $O$ over $D$ be as in [`modelsAt_of_part`](/entry/models-at-of-part/), where the structure `Part` is also described.

**Theorem.** Suppose that $O$ has a part at $(w, Z)$ and that the lattice instances of $O$ are tied (`LatTied O.gatT O.Gx O.Gy`). Then:

1. there is a tied kernel entry $t$ of $O.\mathrm{ex}$ with `JointsAt t μ` for every tuple $\mu$;
2. for every word $u$, $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$, where $e_0$ and $e_{\mu_0}$ are the twisted forms of $O.\mathrm{ex}$ and $\mu_0$ is the reference tuple of $D$.

`JointsAt t μ` is stated in [`modelsOK_of_joints`](/entry/models-ok-of-joints/): at each site whose residue characteristic is not in $Q_p(\mu)$, there is a joint.

## Proof

1. `Part.kerTie` gives, from the part, the equality $O.\mathrm{ex.tw} = w.\mathrm{tw}(Z)$, the equality of the components $\pi_T$ of the error data of $O$ and of $w$, and a tied kernel entry $t$ with the standard kernel condition `StdKer`.
2. The first half of `chiD_values_and_cc_top` gives: each value $\chi_D(z)$ is the image under `embLL` of an element of the coefficient field `LL` of $D$.
3. The equality `ker_eq` of the part identifies the extra data of $O$ with that of the column. This is bookkeeping with `subst`.
4. `kernel_relation_true_columns_joints_all_tuples`, applied to the column input $w.I$, its laws, the column fields (`std`, `stdLv`, `stdDt`, `herm_eq`, `forms_eq`), the pin fields `isTw` and `jets`, and the facts of steps 1 and 2, gives the conclusion.

## In the Lean code

The theorem is at [JointsAtAllStd.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointsAtAllStd.lean#L11). It calls:

- `GlobalTheory.Svd.Part.kerTie` in [KerTie.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KerTie.lean#L10);
- `GlobalTheory.Mem.ChiDVal.chiD_values_and_cc_top` in [ChiDValuesAndCcTop.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ChiDValuesAndCcTop.lean#L114);
- `GlobalTheory.T.kernel_relation_true_columns_joints_all_tuples`.

The proof drops four facts that `Part.kerTie` gives: the equality of the components $\pi_G$, `QpIs`, `t.Adapted` and `t.TopPinned`. It also drops the second half of `chiD_values_and_cc_top` ($t.c_c = \top$). The entry in the conclusion is not the entry $t$ of the part: [`oneTie_jointsAt_all`](/entry/one-tie-joints-at-all/) replaces $t$ by another entry. The proof passes the tuple datum `tp` and the field `col.stdLv` to a theorem that does not use them.
