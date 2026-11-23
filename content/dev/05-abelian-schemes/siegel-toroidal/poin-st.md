---
id: poin-st
title: A normalized blowup of the theta compactification along a boundary ideal
kind: theorem
decl: GlobalTheory.PoincTop.poinSt
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormalisedBlowupAmpleDivisorCompactification
covers: 448
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{PoinSt}$. On a projective normal compactification $Z$ of the Siegel moduli scheme, it finds a boundary ideal $J$ with the valuations of $d\varphi$, blows $Z$ up along $J$, normalizes, and shows that the divisor of the blowup gives an ample twist. Through [the statement form](/entry/normalised-blowup-ample-divisor-compactification/) it is input 3 of [the toroidal compactification](/entry/siegel-toroidal-pol-charts/).

## Statement

Let $g \geq 1$, let $n \geq 3$ be odd, let $\Lambda_n = \mathbb{Z}[\zeta_n, 1/n]$, and let $X$ be the base of a Siegel family `SFam` (see [the volume 8 entry](/entry/siegel-toroidal-integral-of-literature/)). A *theta compactification* (`IsThetaCompact`) is $z \colon Z \to \operatorname{Spec} \Lambda_n$ with $i \colon X \to Z$ such that $Z$ is projective over $\Lambda_n$ and normal, $i$ is an open immersion over $\Lambda_n$ with dense image, and there is an $8 \times 8$ integral matrix $W$ with `IsE8 W` ($W + W^{T}$ is positive definite of determinant 1) and `ThetaInt F W i` (theta constants are integral on normal models over $Z$).

A *trait* (`Trait`) is a complete discrete valuation ring $V$ of characteristic zero with uniformizer $\varpi$, a point $y$ of $X$ over $\operatorname{Frac} V$, and a semi-abelian scheme over $V$ that extends the pullback by $y$ of the universal abelian scheme, uniformized by degeneration data monomial in $\varpi$ with a symmetric form $\beta$. For an ideal $J$ on a scheme $T$, a map $k \colon X \to T$ and $d \in \mathbb{N}$, `ValOn` says: for each trait and each $\xi \colon \operatorname{Spec} V \to T$ that extends $k \circ y$, the pullback $\xi^* J$ is $(\varpi^{a})$ with $a = d\,\varphi(\beta)$.

**Theorem** ($\mathrm{PoinSt}$). Let $(Z, i)$ be a theta compactification, $\mathcal{O}_Z(1)$ an ample line bundle and $\varphi$ a polarization function for $g$. Then there are $d \geq 1$, an ideal $J$ on $Z$, $\pi \colon S \to Z$, $j \colon X \to S$ and an effective Cartier divisor $B$ on $S$ with:

1. $\operatorname{supp} J \cap i(X) = \emptyset$, and `ValOn` holds for $(i, J, d)$;
2. $\pi$ is a normalized blowup of $J$ (`IsNormBl`: $S$ is normal, and $\pi$ is a finite map $S \to S_0$, birational in the sense of an isomorphism over dense opens, followed by the blowup $S_0 \to Z$ of $J$), and $S$ is projective over $\Lambda_n$;
3. $j$ is an open immersion with dense image, $\pi \circ j = i$ and $\pi^{-1}(i(X)) = j(X)$;
4. $\mathcal{O}(-B) = J\mathcal{O}_S$, and `ValOn` holds for $(j, \mathcal{O}(-B), d)$;
5. $\pi^*\mathcal{O}_Z(k) \otimes \mathcal{O}(-B)$ is ample for all large $k$.

## Proof

1. [`exists_fanOrder_ideal_thetaCompactification`](/entry/exists-fan-order-ideal-theta-compactification/) gives $d$ and $J$ with clause 1.
2. `exists_normalised_blowup_cyclotomicAway_projective`, applied to the dense open $i(X)$, gives $S$, $\pi$ and $B$ with clause 2 and $\mathcal{O}(-B) = J\mathcal{O}_S$. Also $\pi$ is an isomorphism over $i(X)$, and $\pi^{-1}(i(X))$ is dense.
3. Put $j = (\pi|_{\pi^{-1}(i(X))})^{-1} \circ i$. Clause 3 follows.
4. For $\xi$ through $j$, the map $\pi \circ \xi$ goes through $i$. By `idlAlong_comap_eq`, $\xi^*(J\mathcal{O}_S) = (\pi \circ \xi)^* J$. This gives clause 4.
5. $\Lambda_n$ is a noetherian domain (`finiteType_cycAway`). Then `ample_twist_normalisedBlowup_noetherian_domain` gives clause 5.

The rest is bookkeeping.

## In the Lean code

The theorem is in [NormalisedBlowupAmpleDivisorCompactification.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormalisedBlowupAmpleDivisorCompactification.lean#L18). `PoinSt`, `IsThetaCompact`, `Trait`, `ValOn` and `IsNormBl` are in [IsThetaCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsThetaCompact.lean#L85). Steps 2 and 5 cite renamings of `NormBlowupInt.exists_normBl` and `BlowAmpleNoeth.ample_twist_of_blowup`, whose proofs we have not opened. The hypothesis that $\mathcal{O}_Z(1)$ is a line bundle (`hOZ`) is never used. The matrix $W$ and `ThetaInt` only go to step 1. We have not unfolded `ThetaInt` in full, `IsPolFan`, `IsMonomial`, `Unif` or `FinalTheorems.Blowup`.
