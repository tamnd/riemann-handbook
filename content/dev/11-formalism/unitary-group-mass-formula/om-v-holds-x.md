---
id: om-v-holds-x
title: The local fibre volume, under a second name
kind: theorem
decl: Formalism.L2.SG.Pf.NcVal.OmVSt.OmVZ.omV_holdsX
module: Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ValuationLocalVolumes.OmVBadTHoldsX
covers: 1069
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It states `OmV`, the formula for the local fibre volume of the frame of a word $u'$ at each finite place. Its proof is the theorem [`omVZ_holdsX`](/entry/om-vz-holds-x/) with the same arguments. That entry has the statement and the proof.

## Statement

For a setting $X$, a word $u'$ and a character $\psi$ of $\mathbb A_F$, the proposition `OmV X u' ψ` holds. In words: if $\psi$ is standard, then at each finite place $v$ the measure of the $K_v$-orbit of the frame, in the fibre over its Gram matrix, is $\lvert \mathfrak d_v \rvert_v^{\,na - a^2/2} \prod_{i=i_0}^{n} (1 - \eta_v^i q_v^{-i})$. Here $a = 2r+1$, and $i_0$ is $k$ or $k+1$ as $v$ divides $T_{u'}$ or not.

## Proof

The proof is one term: `Formalism.L2.SG.Pf.NcX.OmVSt.omVZ_holdsX X u' ψ`.

## In the Lean code

The theorem is at [OmVBadTHoldsX.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/OmVBadTHoldsX.lean#L57). Its one caller in the spine is [`ncTie0All_of`](/entry/nc-tie0-all-of/), which passes it as the hypothesis `hOm` of `ncTieAllS_of`.

The name `omV_holdsX` is in the namespace `NcVal.OmVSt.OmVZ`, and `omVZ_holdsX` is in `NcX.OmVSt`. The only role of the wrapper is to give the result a name in the first namespace. The same namespace and file also hold `omV_holds` (line 28), a second proof of `OmV` through `omV_of_rest`. So the file has two proofs of one statement.
