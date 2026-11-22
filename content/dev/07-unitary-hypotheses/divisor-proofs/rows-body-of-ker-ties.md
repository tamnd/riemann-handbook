---
id: rows-body-of-ker-ties
title: The body of the column rows for tied kernel entries
kind: theorem
decl: GlobalTheory.ColRows.rowsBody_of_kerTies
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MemberRowsOfKernelDatumSizes
covers: 1049
status: drafted
drafted_by: writer@claude
---
This theorem restates [the body of the column rows at one member](/entry/rows-body-col-face/) for the data of one record of tied kernel entries. It packs the ties and the size bounds into two structures, `KerTies` and `KerSizes`. The proof only unpacks them and passes them on. The real content is in [the body of the column rows at one member](/entry/rows-body-col-face/). The result goes, through [its statement form](/entry/member-rows-of-kernel-datum-sizes/), to [the rows from the column pins](/entry/rows-u-of-col-pins-alt/).

## Statement

Let $t$ be a record `KerEntTied ex` of kernel entries tied to a datum $D$ with size data $L$. It holds a field record $X = t.X$, a seam, primes, characters, a selection of primes, a word $t.\mathrm{word}(u)$ for each word $u$ of $D$, a tuple, a constant and a character index for each tuple $\mu$ of $D$, a level $m_2$, and many tie conditions. Let $\Delta, h_0 \in \mathbb{N}$ and let $N$ be the number datum `ofRecord D L Δ h0`.

`KerTies t W Δ h0` has eight fields: the host, weight and character ties for $N$ and the analytic tie for $D$; the tuple at $\mu_0$ is $1$; its constant is sharp; $m_2 = m - 2$; and `FieldOfDefinition` at every word. `KerSizes t W Δ h0 C_Y C_T` has three: `Sizes`, `SizeRowsS` $C_Y$ at the letter of each word, and $\log T(u) \le C_T\, m\, L$ for each word $u$.

**Theorem.** For all reals $C_Y$ and $C_T \ge 0$ there is $C_0$ such that the following holds. Take the column data of [the body of the column rows at one member](/entry/rows-body-col-face/), with tuples pulled back from $D$ through a map `tup` with `tup μ0 = μ0`. Let $R$ be the record `RecNums.ofNum` built from $N$, the letter of $u$, $T(u)$ and seven reals with their facts `NumFacts`. If `KerTies` and `KerSizes` hold, $C_0 \le C_h$, and the positivity and evaluation hypotheses hold, then `RowsBody` holds at $u$ and the frames of `MramH` at $t.\mathrm{word}(u)$ have unit determinant.

## Proof

Take $C_0$ from [the statement form of the body of the column rows](/entry/columns-member-rows-of-log-level-le/). Read each field of `KerTies` and `KerSizes`. Rewrite $T(t.\mathrm{word}\,u) = T(u)$ with `t.T_rec`. `NumReads.ofNum_reads` gives `Reads` for $R$. Then open $t$, substitute $m_2 = m - 2$ and the curve ideal, and apply the theorem. The rest is bookkeeping.

## In the Lean code

The theorem is in [MemberRowsOfKernelDatumSizes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MemberRowsOfKernelDatumSizes.lean#L10). It calls `GlobalTheory.T.columnsMemberRows_of_logLevel_le` and `NumReads.ofNum_reads`. Each field of `KerTies` and `KerSizes` is used. Most fields of $t$ are not used. The structures are in [KerSizes.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/KerSizes.lean#L17), and `KerEntTied` is in [FirstKernelLawReading.lean](lean:Formalism/LocalToGlobal/KernelLattices/FirstKernelLawReading.lean#L395).
