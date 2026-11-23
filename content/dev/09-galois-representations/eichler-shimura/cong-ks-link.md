---
id: cong-ks-link
title: The congruence relation on Kuga-Sato powers
kind: theorem
decl: UpperTheory.Gal.crystallineComparison.Mod.congKS_link
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.AnnihilatorModels.QuotObjLink
covers: 591
status: drafted
drafted_by: writer@claude
---
This theorem proves `CongKS`, the field `cong` of the bundle [mIn](/entry/m-in/). It says that the Hecke correspondences $T_0, \dots, T_n$ on a fibre power of the universal abelian scheme satisfy a pointwise congruence relation at $p$. The proof is one line that joins four inputs. Below it are 591 declarations.

## Statement

`CongKS` is in [CongKSOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/CongKSOf.lean#L16). Take a PEL datum $D$, a discrete valuation ring $O$ of characteristic $0$, a base point $b$, a level $N$, an integer $r$ and a maximal ideal $w$, with `Std f b N r w`. `Std` asks that $p$ lies in the maximal ideal of $O$, the residue field has $p^f$ elements, $N \ge 3$ is prime to $p$, $m = a = 1$, $(p, \omega - r) \le w$ and $w$ has norm $p^f$. Take a model $M$, a uniformizer $\varpi$, an ideal $\mathfrak{a}$ prime to $w$ that contains a power of $(p, \omega - r)$, and a flat map $\pi$ from an `EtModel` $E$ at $\mathfrak{a}$ to $M$. Then for every $k$ there are:

- correspondences $T_j$ on $M$ for $j = 0, \dots, n$, each given by a $p$-isogeny whose kernel is killed by $w$ (`TjD`, `IsTj`);
- lifts $L_j$ of $T_j$ to $E$, and degrees $d_j$, such that $L_j$ on the $k$-th fibre power is finite, étale off $p$ and of constant degree $d_j$ (`KSOKE`);
- the identity `PtId` with $q = p^f$.

`PtId` is in [GenericMulOfProd.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/GenericMulOfProd.lean#L149). At each generic point of the special fibre, with $F$ the $q$-power map, it asks an equality of weighted multisets of points: the sum over even $j$ of $q^{j(j-1)/2} F^{n-j} T_j$ equals the same sum over odd $j$. This is the shape of a congruence relation $\sum_j (-1)^j q^{j(j-1)/2} F^{n-j} T_j = 0$. I have not unfolded `fn`, which builds the fibre at $\varpi$.

## Proof

The proof is in [QuotObjLink.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/QuotObjLink.lean#L13). It is `congKS_holds` applied to four inputs in the same file:

- `esGen_link`: Hecke correspondences exist where $p$ is inverted;
- `esNorm_link`: a consequence of `esGen_link`;
- `ordGen_link`: points at the generic points of the special fibre are $w$-ordinary;
- `quotObj_link`: a quotient by a finite étale subgroup gives a $p$-isogeny with `IsTj`.

[congKS_holds](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/IdealSplitHolds.lean#L149) calls `congKS_of`. That lemma chooses $T_j$ and $L_j$, gets the degrees and an ordinary-point fact from `OrdKSE`, and turns that fact into `PtId` with `PtIdOfOrd`.

## In the Lean code

The namespace `crystallineComparison.Mod` suggests a crystalline comparison theorem. The statement is a congruence relation and has no crystalline content. The mathematics is below `ordKSE_holds` and `ptIdOfOrd_holds`, which I have not unfolded.
