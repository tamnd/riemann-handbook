---
id: exists-per
title: A twelfth root of the discriminant, a theta function and a unit period
kind: theorem
decl: GlobalTheory.MomN.exists_per
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.LawsAndChart
covers: 401
status: drafted
drafted_by: writer@claude
---
This theorem supplies the data that [the moments of the unit period translates](/entry/moments-fin/) start from: a twelfth root $\delta_0$ of a discriminant, an even theta function $\theta$ and a $p$-adic period $\Omega_0$ of norm 1. It is an assembly. Each part comes from a lemma that it calls, and the main input is `PeriodData.laws_and_chart` in the same file.

## Statement

Let $d$ be a prime with $d \equiv 7 \pmod{16}$ and let $K = \mathbb{Q}(\sqrt{-d})$. Let $p$ be a prime that splits in $K$ in the sense of `Split`: $p = 2$ and $d \equiv 7 \pmod 8$, or $p \neq 2$ and $\left(\frac{-d}{p}\right) = 1$. Let $\iota \colon \mathbb{C} \to \mathbb{C}_p$ be a field isomorphism. Then there are $\delta_0 \in \mathbb{C}$, $\theta \colon \mathbb{C} \to \mathbb{C}$ and $\Omega_0 \in \mathbb{C}_p$ with `Per d ι δ₀ θ Ω₀`. That is:

1. $\theta$ satisfies `IsTh d`: it is entire and even, $\theta(0) = 1$, it is fixed by the operators $W_1(x)$ for $x \in \mathcal{O}_K$, and its zeros lie in $\tfrac12 + \mathcal{O}_K$;
2. $\delta_0^{12} = \Delta(\mathcal{O}_K)$ and $\delta_0 \neq 0$;
3. for every field isomorphism $\iota'$ there is $\Omega'$ of norm 1 with `ThetaLaws ι' d (Ω' / ι' δ₀) θ`;
4. $\|\Omega_0\| = 1$, the theta laws hold for $\Omega_0/\iota\delta_0$, and there is a model `M : Mdl q` with `M.ι = ι`, lattice an order of $K$, and multiplicative chart $\Omega_0/\iota\delta_0$.

The theta laws are integrality of the transformed theta series at torsion of order prime to $p$, and the action of the Weil operators by roots of unity. I did not unfold `Mdl` or `MChart` beyond their first layer.

## Proof

1. $\mathbb{C}$ is algebraically closed, so $\Delta(\mathcal{O}_K)$ has a twelfth root $\delta_0$.
2. `exists_imagQuadOrder_pair_and_evenTheta` gives a lattice $L$ with `IsOK d L` and discriminant $\Delta(\mathcal{O}_K)$, and a function $\theta$ with `IsTh d θ`.
3. The proof gets $\delta_0 \neq 0$ from a field of the output of `GenusOne.thetaLaws_unit_period`.
4. `laws_and_chart` at $\iota$ gives $\Omega_0$, its norm, its theta laws and the model $M$.
5. `laws_and_chart` at each $\iota'$ gives the third clause. Its model part is dropped.

## In the Lean code

The theorem is at [LawsAndChart.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LawsAndChart.lean#L38), and `laws_and_chart` is at line 12. The predicate `Per` is at [LatIntZero.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LatIntZero.lean#L30). `Split`, `IsTh` and `ThetaLaws` are in [CmLatticeCommutatorPairingPowEqOneOfGoodLift.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/CmLatticeCommutatorPairingPowEqOneOfGoodLift.lean#L14). Step 3 calls a large lemma for a small fact. The discriminant of the lattice is not 0, so $\delta_0 \neq 0$ follows from $\delta_0^{12} = \Delta$. The proof of `thetaLaws_unit_period` in [ThetaLawsUnitPeriod.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/ThetaLawsUnitPeriod.lean#L56) repeats most of the proof of `laws_and_chart`.
