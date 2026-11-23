---
id: ch-bound-host
title: A lower bound on chart values over the host field at all places
kind: theorem
decl: GlobalTheory.PlaceInt.HostChart.chBound_host
module: Development.AbelianVarietyTheory.Proofs.RingsOfIntegers.HarmonicValuationLowerBoundHostFieldAllPlaces
covers: 438
status: drafted
drafted_by: writer@claude
---
This theorem gives one lower bound on the chart values of an integral chart, for every complete discrete valuation ring $T$. It joins two cases, an unramified one and a ramified one, into one formula that the [literature layer](/step/every-character-of-literature/) can use at all places.

## Statement

Let $E$ be the host field of a datum $D$. Let $N$ = `condN` be the product $Q_S \cdot q \cdot d$ of three numbers of the host ([ConjEMemHostFIff.lean](lean:Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean#L54)). For a prime $p$, let $\delta_p = v_p(|\operatorname{disc} E|) / [E : \mathbb{Q}]$ (`vdH`), with the [[discriminant|E0VZTNPJXA]] of $E$. Let $X_o$ be a moduli scheme over $E$ with a coefficient datum $c$, and suppose that the star operation on $\mathcal{O}_E$ is the conjugation of the datum. Let $T$ be a complete discrete valuation ring with valuation $v$, $y$ an integral framed point over $T$, and $C$ an integral chart at $y$. Let $e > 0$, let $w$ be a weight, and let $\mathrm{DF}_w$ be a natural number at least $\mathrm{DF}(w) = \sum_{\tau, i} w(\tau, i)$.

**Theorem.** `ChBound C e ρ w n` holds with
$$\rho = \sum_{p \mid N} \frac{v(p)}{e} \cdot \delta_p \cdot \frac{\mathrm{DF}_w}{2}.$$
That is, each chart value of an integral germ under an integral polynomial of weight $w$ has $v/e \geq -\rho$.

## Proof

Each term of the sum is at least $0$, since $v(p) \geq 0$ (`vV_nat_nonneg`) and $\delta_p \geq 0$. `hostField_galois_degree_discr_conj_moves_primes` says that $E$ is [[Galois|0QMZAQ6QQ4]] over $\mathbb{Q}$, that each prime that divides $\operatorname{disc} E$ divides $N$, and that each $p \mid N$ is prime with a condition on conjugation at the primes above $p$.

1. **Each $p \mid N$ is a unit in $T$.** Then $\operatorname{disc} E$ is a unit in $T$. `harmonic_value_integral_of_unit_discriminant` gives `ChBound` with $\rho = 0$. Since $\rho \geq 0$, `chBound_mono` gives the claim.
2. **Some $p \mid N$ is not a unit in $T$.** `harmonicValue_bound_integralChart_ramified` gives `ChBound` with the term for $p$, with $\mathrm{DF}(w)$ in place of $\mathrm{DF}_w$. This is at most the term with $\mathrm{DF}_w$, which is at most the full sum. Then `chBound_mono` gives the claim.

## In the Lean code

The theorem is in [HarmonicValuationLowerBoundHostFieldAllPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/HarmonicValuationLowerBoundHostFieldAllPlaces.lean#L36). The helpers `vV_nat_nonneg` and `chBound_mono` are in the same file. `ChBound` is in [AdaptStd.lean](lean:Development/AbelianVarietyTheory/Definitions/PlaceAdaptation/AdaptStd.lean#L165).

The host $H$ in the statement is any host over `D.host.E`. It need not be the host of $D$. In case 2 the proof uses only one prime $p$, so the sum over all $p \mid N$ is weaker than what the proof gives.
