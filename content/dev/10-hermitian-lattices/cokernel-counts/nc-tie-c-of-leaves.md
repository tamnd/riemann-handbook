---
id: nc-tie-c-of-leaves
title: The normalizing constant from the two global identities and the local leaves
kind: theorem
decl: Formalism.L2.SG.Pf.NcLeaves.ncTieC_of_leaves
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.DualFamilyCounting.NcLeaves
covers: 310
status: drafted
drafted_by: writer@claude
---
This lemma proves the closed form $c_{\mathrm{expl}} = n_0 g / (\alpha \kappa)$ for the record `bCF`, once a number $a' > 0$ is fixed that satisfies the finite split identity and the real identity. Its only caller is [`ncTieAllS_of`](/entry/nc-tie-all-s-of/), which makes $a'$ from `SplitOm` and the real identity from `RealBracket`. It joins two lemmas; the arithmetic is in `normalizing_arithmetic_holds`.

## Statement

The data, the record $B = $ `bCF` and the conclusion `NcTieC` are as in [`ncTieC_of_closed`](/entry/nc-tie-c-of-closed/). Let $a' > 0$. Assume:

1. the facts `Pos`, `InMass`, ..., `InVolumes` about $B$ and $\mathrm{vol}_{H a'} = \mathrm{vol}_G$, as in [`ncTie0All_of`](/entry/nc-tie0-all-of/);
2. $\psi$ is a character of $\mathbb{A}_F / F$ (`IsCharAF`) and is standard (`IsStdChar`);
3. $T_u \equiv T_{u'} \pmod{g_S^2}$, and `IsRowReps` for the set $S$ of row lattices;
4. the finite split: $\mu_K\, a' = \mu_{H'} \prod_v \omega_v(K_v \cdot Y)$, where $Y$ is the frame of $u'$ and $\omega_v$ is the fibre measure over its Gram matrix;
5. the real identity: $c_X(u,u')\, \mathrm{vol}_H\, \mathrm{vol}_N\, \mathrm{vol}_{N'} = a'\, 2^{kd} \big(\pi^k/(k-1)!\big)^d\, T_u^{-kd}\, \lvert d_F \rvert^{e}$, with $e = -(8r^3 + 6r^2 + 6kr^2 + r)/3$, as in [`RealBracket_holds`](/entry/real-bracket-holds/);
6. the local inputs `VolOrdV`, `VolTypV`, `IndexTypC`, `OmV`, `FieldDict` and `ProdConv`.

**Lemma.** Then `NcTieC` holds for $c_{\mathrm{expl}}$.

## Proof

1. `ncTieC_of'` reduces `NcTieC` to the identity `NcValueC`:
$$c_{\mathrm{expl}}\, \alpha = c_X(u,u')\, \mathrm{vol}_H\, \mathrm{vol}_N\, \mathrm{vol}_{N'} \cdot \frac{U}{Z} \cdot \frac{\mu_{K,\mathrm{nat}}}{\mu_{H'}} \cdot n_g.$$
Here $U/Z$ is the ratio `unitLevelVolume / volZZ` of $B$, and $n_g$ is `ngFac D`. The reduction uses `nc_iff`, the definition $C_{\infty} = \kappa_N\, c_X(u,u')$ of the field `Coo`, $\kappa_N \neq 0$, and $\mathrm{vol}_B = \mathrm{vol}_{Ha}$, which follows from `InVolumes` and $\mathrm{vol}_{Ha'} = \mathrm{vol}_G$.
2. `normalizing_arithmetic_holds` proves `NcValueC`. It also needs two facts that this lemma supplies:
   - `diffProd_holds`: $\prod_v \lvert \mathfrak d_v \rvert_v = \lvert d_F \rvert^{-1}$ over the finite places, where $\mathfrak d_v$ has the valuation of the different at $v$;
   - `row_lattice_mass`: when $T_u \equiv T_{u'} \pmod{g_S^2}$, the mass of the row lattices is $c\, T_u^{k [F:\mathbb Q]} \prod_{\mathfrak p \mid T_u} (1 - \eta(\mathfrak p)^k N\mathfrak p^{-k})$, with $c = $ `cMass E F k`.

In `normalizing_arithmetic_holds`, $\alpha$ is split into ordinary and typed parts, the ordinary part written with the Euler products of $L(i, \eta)$ for $k < i \le R$ from `FieldDict`. We have not followed the rest of that proof.

## In the Lean code

The lemma is in [NcLeaves.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcLeaves.lean#L28). Its proof is one term that calls:

- `NcAsm.ncTieC_of'` and `NcValueC` in [NcTieCOf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcTieCOf.lean#L26);
- `NcGlob.normalizing_arithmetic_holds` in [NcGlob.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcGlob.lean#L91), which proves the statement `NcArith` of [NcArith.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcArith.lean#L33);
- `NcVal.diffProd_holds` and `CntFormula.RowsMassW.row_lattice_mass`.
