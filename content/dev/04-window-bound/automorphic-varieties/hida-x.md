---
id: hida-x
title: A Hecke ideal that cuts out the automorphic points
kind: theorem
decl: UpperTheory.V.Th.hidaX
module: Development.AutomorphicArithmetic.AutomorphicVarieties.TheoremsMuLinked.GaloisRepresentationTypes.HidaX
covers: 316
status: drafted
drafted_by: writer@claude
---
This theorem gives the ideal $J$ of the universal ordinary determinant ring that [the theorem on ordinary adjoint cocycles](/entry/ord-van2/) uses in step 3. It only collects four lemmas. The real content is in `hdEx`, `jEx`, `jPT` and `levelX`.

## Statement

**Theorem.** Assume $\mathrm{HypothesesH}$. Let $s$ be a Hida setting over a CM field $L$, let $V$ be a level with $S' = S$, let $n \ge 1$, let $r$ be a residual datum of dimension $n$ and let $B$ be its universal ordinary determinant ring. Let $\Lambda$ be a level datum and $\iota \colon \overline{\mathbb{Q}}_l \cong \mathbb{C}$. Then there is an ideal $J$ of $B$ with two properties:

1. `PT`: $J \subseteq \ker x$ for each arithmetic point $x$ of $B$ that comes from a continuous $\rho \colon G_L \to \mathrm{GL}_n(\overline{\mathbb{Q}}_l)$ with $2 \le n \le 4$, attached to a cuspidal conjugate self-dual representation through $\iota$, trivial on the inertia at $v_0$, with a flag at each $v \mid l$ and with $\psi_{v,i} \ne \psi_{v,j} \bar\varepsilon$ for all $i, j$;
2. `LevelX`: there is a Taylor-Wiles base for $J$ with the level and weight conditions. We have not unfolded `TWBase`, `LevAt` or `CtrlH`.

## Proof

`hdEx` gives a Hida datum $R$ for the empty set of auxiliary places. The level $K$ is then trivial. `jEx` gives an ideal $J$ with `IsJ` for $R$ and $K$. `jPT` proves `PT` from `IsJ`, and `levelX` proves `LevelX` from it.

## In the Lean code

The theorem is in [HidaX.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/GaloisRepresentationTypes/HidaX.lean#L8). The lemmas: [`hdEx`](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeckeAlgebras/OrdinaryHeckeCharacters/HdEx.lean#L14), [`jEx`](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeckeAlgebras/OrdinaryHeckeCharacters/AbsH.lean#L67), [`jPT`](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeckeAlgebras/OrdinaryHeckeCharacters/JPT.lean#L9) and [`levelX`](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/HidaOrdinaryHecke/LevelX.lean#L201). `HidaX` is in [OrdinaryHeckeAlgebraIntegral.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdinaryHeckeAlgebraIntegral.lean#L197).

`IsJ` allows $J = B$ when the Hecke module is zero. Then `PT` says that no point of the kind in property 1 exists.
