---
id: om-vz-holds-x
title: The local fibre volume of the frame at a finite place
kind: theorem
decl: Formalism.L2.SG.Pf.NcX.OmVSt.omVZ_holdsX
module: Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ValuationLocalVolumes.OmVBadTHoldsX
covers: 1068
status: drafted
drafted_by: writer@claude
---
This theorem proves `OmV`: a closed formula for a local volume at each finite place $v$ of $F$. The volume is the measure of the $K_v$-orbit of the frame of a word $u'$, in the fibre over its Gram matrix. The theorem [`omV_holdsX`](/entry/om-v-holds-x/) is a renaming of it, and [`ncTie0All_of`](/entry/nc-tie0-all-of/) uses that name. The proof puts ten lemmas into `omV_of`, which does a split into two cases.

## Statement

Let $X$ be a setting with a CM extension $E/F$, a Hermitian form $J$ on $E^n$ and a lattice $L$. Let $Y$ be the frame of $u'$, a tuple of $a = 2r+1$ vectors, where $r$ is `D.R.rS`. Let $T = T_{u'}$ be a positive integer. For a finite place $v$, let $q_v$ be the norm of $v$, let $\eta_v$ be $1$ if $E \otimes F_v$ splits and $-1$ if not, and let $\lvert \mathfrak d_v \rvert_v$ be the absolute value of a local generator of the different. Let $\omega_v$ be the fibre measure over the Gram matrix of $Y$ at $v$ (`omAt`).

**Theorem.** If $\psi$ is a character of $\mathbb A_F$ that is standard (`IsStdChar`), then for every finite place $v$,
$$\omega_v(K_v \cdot Y) = \lvert \mathfrak d_v \rvert_v^{\,na - a^2/2} \prod_{i=i_0}^{n} \bigl(1 - \eta_v^i q_v^{-i}\bigr),$$
with $i_0 = k$ if $v \mid T$ and $i_0 = k+1$ if not. Here $k$ is `D.R.k`, and the code uses $n - a = k$.

The measure `omAt` is defined by choice. It is the fibre family of the self-dual measure over the Gram map, and $0$ if no such family exists. We have not unfolded `IsFibreFamily`.

## Proof

The proof is in `omV_of` ([NcXOmVTop.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcXOmVTop.lean#L57)). Let $Y'$ be the tuple `yTup`: the vectors of $Y$ scaled by local elements $\alpha_i$ and $\alpha_i^{-1}$.

1. By `OmVScale`, $\omega_v(K_v \cdot Y) = \omega_v(K_v \cdot Y')$.
2. If $v \mid T$, use `OmVBadT`. It needs $L_v$ self-dual (`OmVSD`), $E/F$ unramified at $v$ (`OmVUnram`) and $Y'$ primitive in $L_v$ (`OmVPrim`). It gives the product from $n - a = k$ to $n$.
3. If $v \nmid T$, use `OmVLocU`, which is `omLocU_closed`. The Gram matrix of $Y'$ equals that of $Y$ (`OmVGram`), and its determinant is a unit at $v$ (`OmVDet`). It gives the product from $k+1$ to $n$.

The ten inputs come from `omega_standard_holds`, `omega_lattice_holds`, `omVSD_holdsX`, `omega_unramified_holds`, `omVPrim_holdsX`, `omVGram_holds`, `omVDet_holds`, `omVScale_holdsX`, `omVBadT_holdsX` and `omVLocU_holds`. We have not unfolded their proofs, except as below.

## In the Lean code

The theorem is in [OmVBadTHoldsX.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/OmVBadTHoldsX.lean#L45). The target `OmV` is in [DiffProd.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/DiffProd.lean#L26), and the conditions are in [NcXOmVSt.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcXOmVSt.lean#L26).

`OmVUnram` asks that $E/F$ is unramified at every finite place. `omega_unramified_holds` gets this from the CM data by `unramAt_of_cm`, so the CM data of the code must contain this condition.

The lattice is written `abelian₂ X` ([NcXOmVSt.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcXOmVSt.lean#L24)). This is only an abbreviation for `X.B.I.L` and has no relation to abelian varieties.

The same file has `omV_holds` (line 28), a second proof of `OmV` through `omV_of_rest`.
