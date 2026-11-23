---
id: fin-all
title: The Frobenius relation holds for all smooth models
kind: theorem
decl: UpperTheory.Ru.crystallineComparison.finAll
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.SmoothModelCrystalline
covers: 761
status: drafted
drafted_by: writer@claude
---
This theorem proves `FinAll`, the first of the two inputs of [the Frobenius step](/entry/phi-step/). The proof is one line. It applies [the reduction lemma](/entry/fin-all-of/) to the lemma `cIn`. The real content is in the chain [fin-all-of](/entry/fin-all-of/), [final](/entry/final/) and [the comparison theorem](/entry/crystalline-comparison-top/).

## Statement

**Theorem.** `FinAll` holds. This is the relation of Eichler-Shimura type stated in [the parent entry](/entry/phi-step/): for a smooth model $M$ over the integers of a finite extension $K$ of $\mathbb{Q}_\ell$ with residue field of size $\ell^f$, for correspondences $T_i$ with `PtId` that act by $A_i$ on $V = H^j(M_{\overline{K}})$, and for each period datum $B_0$, there is $N$ with
$$\sum_{i=0}^{n} (-1)^i (\ell^f)^{\binom{i}{2}} \, (A_i \otimes \varphi^{f(n-i+N)})\, x = 0$$
for each Galois-invariant $x$ in $V \otimes B_0$.

## Proof

1. `finAll_of` reduces `FinAll` to the claim `CIn l K r f` for each residue datum $r$ and each $f > 0$.
2. `cIn` proves this claim. It joins three existence lemmas. `pinEx` gives $N$ with $f \mid N$, a Teichmüller congruence, a datum `F : Pb.Fac r N` and the field `Pin`. `endEx`, with `etSide_sm_holds` as input, gives the line data `Amp`, the facts `(per l K).Facts`, `EtSide`, the laws and the maps `BMap` and `PMap`. `bInEx` gives the last field `BIn`.

## In the Lean code

- The theorem is in [SmoothModelCrystalline.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/SmoothModelCrystalline.lean#L9). `cIn` is in [CIn.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/CIn.lean#L10).
- The name `finAll` does not say what it proves.
- `FinAll` does not mention the residue datum $r$ or `CIn`. These are only tools of the proof.
- We have not unfolded `pinEx`, `endEx` or `bInEx`.
