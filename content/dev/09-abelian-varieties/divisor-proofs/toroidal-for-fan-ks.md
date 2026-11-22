---
id: toroidal-for-fan-ks
title: Toroidal compactifications for a fan, with the log Kodaira-Spencer isomorphism
kind: theorem
decl: GlobalTheory.TorKSField.toroidalForFanKS
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ToroidalCompactificationFanLogKodairaSpencerIso
covers: 5077
status: drafted
drafted_by: writer@claude
---
This theorem proves `ToroidalForFanKS`: each unitary moduli scheme of the proof has a smooth projective compactification with fan charts at the boundary and a log Kodaira-Spencer isomorphism. The theorem `toroidal_for_fan_ks_of_literature` cites it with no change. It is one of the 15 inputs of `topCovolSlim2_use_alt_alt`, the volume branch of [EveryCharacter from the literature](/step/every-character-of-literature/). Below this theorem are 5,077 declarations of the proof.

## Statement

Let $E$ be a CM field with a host $H$, and let $D$ be a Hermitian $\mathcal{O}_E$-datum of signature $(p, q)$ with $p + q \geq 1$. Let $\varphi$ be an invariant function (`InvFun`) that satisfies `IsPolFan` and `NoSelfInt` in rank at most $\min(p, q)$. Let $l$ be a level, $X$ the moduli scheme `Moduli D l`, $F$ a coefficient field and $n = \tfrac{[E:\mathbb{Q}]}{2}\, p q$. [Rigid boundary charts for a fan](/entry/rigid-for-fan-holds/) defines these objects.

**Theorem.** There are a projective model $Y$ of $X_F$ over $F$, an effective Cartier divisor $B$ on $Y$ and integers $d, k \geq 1$ with:

1. $Y$ is smooth of relative dimension $n$, and its boundary is a strict normal crossings divisor;
2. the support of $B$ lies in the boundary;
3. each boundary point has a fan chart (`HasChartOf φ Y B d x`), on which $B$ is the divisor of $d\varphi$;
4. if $\omega_Y$ is a line bundle, then $\omega_Y^{k}(-B)$ is ample;
5. `HasLogKS`: the Kodaira-Spencer map identifies the log derivations along the boundary with a module of balanced matrices. See [the log Kodaira-Spencer isomorphism](/entry/has-log-ks/).

The statement has the shape of the existence theorem for [toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications). Faltings and Chai prove that theorem for the Siegel case (*Degeneration of abelian varieties*, 1990), and K.-W. Lan proves it for PEL type (*Arithmetic compactifications of PEL-type Shimura varieties*, 2013). We have not checked that the Lean clauses match those theorems.

## Proof

The proof composes two theorems.

1. [The citation](/entry/rigid-boundary-charts-for-fan-unitary-datum/) of [rigid boundary charts for a fan](/entry/rigid-for-fan-holds/) proves `RigidForFan`. That statement has clauses 1 to 4, and in place of clause 5 it has a rigid chart at each closed boundary point.
2. [The log Kodaira-Spencer isomorphism from rigid charts](/entry/toroidal-fan-kodaira-spencer-of-rigid-boundary-charts/) proves `RigidForFan → ToroidalForFanKS`.

All the work is in these two theorems.

## In the Lean code

The theorem is in [ToroidalCompactificationFanLogKodairaSpencerIso.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToroidalCompactificationFanLogKodairaSpencerIso.lean#L8). Its proof is one line:

```
GlobalTheory.T.toroidalFanKodairaSpencer_of_rigidBoundaryCharts GlobalTheory.T.rigidBoundaryChartsForFan_unitaryDatum
```

The statement is in [ToroidalCompactificationBis.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ToroidalCompactificationBis.lean#L45). Clause 1 is stated for the fibre `genStr Y`, which is $Y \times_F F$. The lemmas `smooth_gen_iff` and `snc_gen_iff` move it to $Y$. The lemma `exists_model_of_fan` removes the hypothesis of clause 4 with `isLB_detOm_of_smooth`.
