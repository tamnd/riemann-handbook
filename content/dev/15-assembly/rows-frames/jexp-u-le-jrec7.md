---
id: jexp-u-le-jrec7
title: The lattice exponent at a place, bounded by the weight recursion
kind: theorem
decl: GlobalTheory.ExpTie.Asm.jexpU_le_jrec7
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExpansionOfNumericsModel
covers: 1055
status: drafted
drafted_by: writer@claude
---
This theorem bounds the lattice exponent of a block datum at one finite place $w$ by the recorded weight exponent $J^{(7)}_W(p)$, where $p$ is the residue characteristic of $w$. It splits into two cases: $p$ in the range of the weight datum, and $p$ outside it. Its user is [the exponent bound at one point](/entry/has-exp-bound-at/), which applies it at every twisted place. The inclusion in the range comes from [the inclusion from local models](/entry/l-incl-of-models/).

## Statement

Let $K$ be a number field with an involution, $w$ a finite place of $K$, and $p$ the characteristic of the residue field at $w$. Let $B$ be a block datum, $\ell$ a level and $Z$ a space of forms. They give two lattices $\Lambda_\nabla$ and $\Lambda_\Delta$ in a coordinate space $K^d$, as in [the inclusion from local models](/entry/l-incl-of-models/). Write $\mathrm{LIncl}(J)$ for $p^J \Lambda_\nabla \subseteq (\Lambda_\Delta)_{(w)}$. The lattice exponent is

$$J_B(w) = \frac{\inf\{J : w^J \Lambda_\nabla \subseteq (\Lambda_\Delta)_{(w)}\}}{e_w},$$

with $e_w$ the ramification index of $w$ over $p$ (`JexpU`).

For parameters $P$ and a weight datum $W$, the code defines two exponents at a prime $l$: $J_A(l) = \sum_\tau e_\tau(l)$, and the coarse weight bound $c_W(l) \le J_A(l)$. Then $J^{(7)}_W(l) = J_A(l)$ when $l \le l_J$, $l$ is excluded or $l$ is in the special set of $W$, and $J^{(7)}_W(l) = c_W(l)$ otherwise. The range of $W$ (`WRange`) is the set of $l$ with $l_J < l \le h$ that are not excluded and not special.

**Theorem.** Assume the cut bound `ExCut` and `NumOk` for $(P, W)$. Suppose:

1. if $p$ is not in the range of $W$, then $\mathrm{LIncl}(J_A(p))$;
2. if $p$ is in the range, there are Frobenius data and Hida settings $(X_i)$ that cover $B$ at $w$ (`Covers`), with $p$ not a unit in each $O_i$ and `WInputsLink` for each $X_i$.

Then $J_B(w) \le J^{(7)}_W(p)$.

## Proof

`plc_prime` shows that $p$ is prime. `exponent_of_record_vs_formulas` uses `ExCut` and `NumOk`. It gives $J_A(p) \le J^{(7)}_W(p)$ off the range and $c_W(p) = J^{(7)}_W(p)$ in the range. The only hard case is $p > h$ with $p$ not excluded and not special. There $J^{(7)}_W(p) = c_W(p)$, and `ExCut` is used to show $J_A(p) = 0$.

- In the range, [`primePowerLatticeInclusion_of_localModels`](/entry/prime-power-lattice-inclusion-of-local-models/) gives $\mathrm{LIncl}(c_W(p))$ from hypothesis 2.
- Off the range, hypothesis 1 gives $\mathrm{LIncl}(J_A(p))$.

In both cases `exponent_datum_le_of_primePowerLatticeInclusion` turns $\mathrm{LIncl}(J)$ into $0 \le J_B(w) \le J$. Its idea: $w^{J e_w} \subseteq p^J \mathcal O_{K,(w)}$, so the numerator of $J_B(w)$ is at most $J e_w$. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExpansionOfNumericsModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExpansionOfNumericsModel.lean#L22). `JexpU` is in [RowLat.lean](lean:Formalism/LocalToGlobal/Divisibility/RowLat.lean#L161). The lemmas:

- `Formalism.EigenvalueLevelCeiling.plc_prime`;
- `GlobalTheory.exponent_of_record_vs_formulas`, in [ExponentOfRecordVsFormulas.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExponentOfRecordVsFormulas.lean#L11);
- `GlobalTheory.T.primePowerLatticeInclusion_of_localModels`;
- `GlobalTheory.T.exponent_datum_le_of_primePowerLatticeInclusion`.

Odd points:

- The infimum in `expW` ([RowLat.lean](lean:Formalism/LocalToGlobal/Divisibility/RowLat.lean#L39)) is `sInf` on $\mathbb N$. If no $J$ works, the exponent is $0$, not infinity. Here an inclusion is always assumed, so this does no harm.
- The name `Jrec7` and the namespace `Asm` do not refer to any object that we found. The "7" is not explained in the code.
