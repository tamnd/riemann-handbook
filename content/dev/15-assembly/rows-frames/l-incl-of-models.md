---
id: l-incl-of-models
title: A prime power lattice inclusion from local models
kind: theorem
decl: GlobalTheory.ExpTie.lIncl_of_models
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.PrimePowerLatticeInclusionOfLocalModels
covers: 1050
status: drafted
drafted_by: writer@claude
---
This theorem bounds, at one place $w$ of residue characteristic $p$, the power of $p$ that moves one lattice of forms into another, by the coarse weight bound of a weight datum. The proof uses local models. Its only user is [its restatement](/entry/prime-power-lattice-inclusion-of-local-models/), which [the bound on the lattice exponent](/entry/jexp-u-le-jrec7/) calls.

## Statement

Let $w$ be a finite place of a number field $K$, and $p$ its residue characteristic (`plc w`). For an $\mathcal O_K$-module $\Lambda$ let $\Lambda_{(w)}$ be its localization at $w$ (`localization₂`).

A block datum $B$ (`BlockDat`) has a finite set of classes $c$, a hermitian $K$-space $V$ and $\mathcal O_K$-lattices $\nabla_c$ and $\Delta_c$ in $V$. From a level $\ell$ and a space $Z$ of forms on the classes, the code builds a linear map $E$ from $K^d$ to the forms (`fE`), and the lattices

$$\Lambda_\nabla = \{u : (Eu)(c) \in \nabla_c \text{ for all } c\}, \qquad \Lambda_\Delta = \{u : (Eu)(c) \in \Delta_c \text{ for all } c\}$$

(`cutZ` and `delZ`). Write $\mathrm{LIncl}(J)$ for $p^J \Lambda_\nabla \subseteq (\Lambda_\Delta)_{(w)}$.

A Hida setting $X$ (`HidaSetting`) has, among other data, a Noetherian local domain $O$ of characteristic $0$, a level $\Gamma$ and a multiplicative set $S$ of Hecke operators. $X$ has an inclusion of exponent $J$ at $l$ (`Incl l J`) if, after localization at $S$, $l^J$ moves each form of level $\Gamma$ with values in $\bigotimes_\tau \nabla(\lambda_\tau)$ into the forms with values in $\bigotimes_\tau \Delta(\lambda_\tau)$. ($\nabla$: dual Weyl modules, $\Delta$: Weyl modules.)

Let $W$ be a weight datum (`Wts`) with weights $\lambda_\tau$, for parameters $P$. Let $e_\tau(l)$ be the least $e$ with $l^e \nabla(\lambda_\tau) \subseteq \Delta(\lambda_\tau)$ (`LA.exZ`, through `InclZ`, which we did not unfold). The coarse weight bound is $c_W(l) = \sum_\tau c_\tau(l)$, with $c_\tau(l) = e_\tau(l)$ for $\tau \notin T_2$ and $c_\tau(l) = \min(e_\tau(l), c'_\tau(l))$ for $\tau \in T_2$, where $c'_\tau(l)$ is explicit (`cFloorCoarse`).

**Theorem.** Suppose that $(P, W)$ satisfy `NumOk`, that $p$ is prime and that $p$ is in the range of $W$ (`WRange`). Let $\mathrm{fr}, \mathrm{cj}$ be Frobenius data, and $(X_i)_{i \in I}$ Hida settings for the weights $\lambda$. Suppose:

1. (`Covers`) for each $J$, if every $X_i$ has an inclusion of exponent $J$ at $p$, then $\mathrm{LIncl}(J)$;
2. for each $i$, $p$ is not a unit in $O_i$, and `WInputsLink` (finiteness of $O_i/p$, lattice links at each $\tau \in T_2$, and other conditions) holds for $X_i$, $p$ and $W$ with Frobenius data $\mathrm{fr}, \mathrm{cj}$.

Then $\mathrm{LIncl}(c_W(p))$ holds.

## Proof

1. `expo_frob_indep` shows that $W' = W$ with $\mathrm{fr}, \mathrm{cj}$ still satisfies `Ok`, and that $c_{W'}(p) = c_W(p)$ for $p$ in the range.
2. By `Covers`, it is enough that each $X_i$ has an inclusion of exponent $c_{W'}(p)$.
3. `weight_inputs_of_linkage_holds` turns `WInputsLink` into the weight inputs `WInputs`.
4. `inclusion_w_seven_real_holds` gives the inclusion of exponent $c_{W'}(p)$. Its proof gets a smaller exponent from `Down.inclusion_w_real_holds`, which we did not unfold, and uses that `Incl` is monotone in $J$. Step 1 then gives $c_W(p)$.

## In the Lean code

The theorem is in [PrimePowerLatticeInclusionOfLocalModels.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PrimePowerLatticeInclusionOfLocalModels.lean#L15). The lemmas:

- `GlobalTheory.expo_frob_indep`, in [ExpoFrobIndep.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExpoFrobIndep.lean#L10);
- `weight_inputs_of_linkage_holds`, in [WeightBounds.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/WeightBounds.lean#L587);
- `Top.inclusion_w_seven_real_holds` ([CorollaryOfParamsSevenLinkageAlt.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/CorollaryOfParamsSevenLinkageAlt.lean#L9)), which is `Down7.inclusion_w_seven_real_holds` ([CorollaryOfParamsSevenLinkage.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/CorollaryOfParamsSevenLinkage.lean#L39)).

Odd points:

- The hypothesis that $p$ is prime is always true: `plc_prime` proves it for every $w$.
- The estimates `Rows` and `Big` in `NumOk` are not used.
- The Frobenius data of $W$ play no part.
- `HidaLatticeInclusionAtCoarseWeightBound` has three definitions. The one in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L455) has an extra hypothesis `LemmaDGraded`. The proof uses one without it.
