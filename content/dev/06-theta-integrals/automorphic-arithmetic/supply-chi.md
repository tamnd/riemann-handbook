---
id: supply-chi
title: Hosts for one character from the window bound
kind: theorem
decl: UpperTheory.Top.supplyChi
module: Development.AutomorphicArithmetic.CharacterBoxes.SupplyChi
covers: 1462
status: drafted
drafted_by: writer@claude
---
This theorem turns the window bound for one primitive character $\psi$ into hosts on windows of scale $\lambda = \tfrac32$ that meet the requirement of $\psi$. It is the only place where [VWin](/step/vwin-def/) enters the branch [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/): there `zeroFreeAll_of_topG` receives `supplyChi ψ (hV ψ)` for each $\psi$. The theorem is a short wrapper. The real content is in [`supplyOfAdm`](/entry/supply-of-adm/).

## Statement

**Theorem.** Let $\psi$ be a primitive [[Dirichlet character|JR4QSEFXWF]] (a `PChar`). If `VWinAt ψ 401` holds, then `HostExW (3/2) (GChi ψ).req` holds.

`VWinAt ψ 401` is the statement of [the step VWin](/step/vwin-def/) for one $\psi$. `HostExW λ P` and the requirement `GChi ψ` are stated in [the entry on `supplyOfAdm`](/entry/supply-of-adm/). In short, `GChi ψ` asks for the conditions `EAtH` at the level `Level.cyc ψ` and the bound `VVle` on the field of the host.

## Proof

The proof applies `supplyOfAdm ψ hψ`. That theorem has one more hypothesis: for suitable frames $\varphi$ there are ranks $R$ with `RankVal s R` and `admitted R H0`. The proof gets this from `admissibleClassesTwistedChar`. The two extra hypotheses of `supplyOfAdm` on $\varphi$ (its order $o$ is the order of `Level.cyc ψ`, and `KerChi ψ H0`) are not used. The requirement `(GChi ψ).req` unfolds by definition to the requirement in the conclusion of `supplyOfAdm`. The rest is bookkeeping.

## In the Lean code

The theorem is in [SupplyChi.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/SupplyChi.lean#L8). It calls:

- `supplyOfAdm` in [HostOfField.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/HostOfField.lean#L17);
- `admissibleClassesTwistedChar` in [AdmChi.lean](lean:Development/AutomorphicArithmetic/CoprimeRanks/AdmChi.lean#L13). It takes the ranks from `exists_ranks_rankVal_frame` and proves `admitted R H0` by `admissible_ranks_of_CMDatum`, which holds for every $R$ and $H_0$.

`GChi` is defined in [Supply.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/Supply.lean#L42).
