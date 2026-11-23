---
id: mult-poly-holds
title: A polynomial bound on the folding multiplicity
kind: theorem
decl: Formalism.L2.SG.Closed.MultPoly_holds
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedVolumeStatements.WuDefiniteHolds
covers: 379
status: drafted
drafted_by: writer@claude
---
This theorem proves `MultPoly`: the number of rational points that move a point of a compact set into another compact set grows at most polynomially in the archimedean norm. Its only caller is [`foldOKC_holds_of`](/entry/fold-okc-holds-of/), which uses it to prove the folding conditions `FoldOK`. The theorem is a pass-through: it applies [`multPoly_holds_of''`](/entry/mult-poly-holds-of-prime-prime/) to the covering statement `OmCover_holds`.

## Statement

Fix a setting $X$. Let $\Gamma = G(F)$ be the rational points in $G(\mathbb A)$. For a set $\Omega \subseteq G(\mathbb A)$ and $x \in G(\mathbb A)$, the multiplicity is
$$\operatorname{mult}(\Omega, x) = \sup_{y \in G(\mathbb A)} \#\{\gamma \in \Gamma : x^{-1} \gamma y \in \Omega\}.$$
For $g \in G(F_\infty)$ let $\lVert g \rVert = \prod_{v \mid \infty} \lVert g_v \rVert_{\mathrm{op}}$, and let $N_1 = 4n^2\sqrt{2q}$ with $q$ the largest of the integers `qAt v`, which we have not unfolded.

**Theorem.** For all compact $\Omega, C \subseteq G(\mathbb A)$ there is a real $C_0$ such that, for all $c \in C$ and $g \in G(F_\infty)$,
$$\operatorname{mult}\big(\Omega, c\,(g, 1)\big) \le C_0 \lVert g \rVert^{N_1}.$$

## Proof

`MultPoly_holds` is `multPoly_holds_of''` applied to `OmCover_holds`. `OmCover` says: each compact $\Omega$ is covered by finitely many right translates by elements $(1, a)$ of the sets `Count.Om I r K'`, with radii $r \ge 0$ and a subgroup $K'$ of the level set. It is `omCover_holds`, proved by a finite subcover and the polar decomposition.

`multPoly_holds_of''` adds `tauTrans_holds` and `normPow_holds` and calls `multPoly_of`. That proof bounds the multiplicity on each translate by a lattice count $C_\Omega / \tau_1(x)^{k}$ with $k = 4n^2 f$. Here $\tau_1$ is a size function of `LitS.Size` that we have not unfolded. It bounds $\tau_1(c)$ from below on $C$ by a minimum, uses `TauTrans` to compare $\tau_1(c (g,1))$ with $\tau_1(c)$, and uses `NormPow` to raise the exponent from $4n^2$ to $N_1$.

## In the Lean code

The theorem is in [WuDefiniteHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/WuDefiniteHolds.lean#L39). `MultPoly` is in [InHHCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHCut.lean#L317), `OmCover` and `multPoly_of` in [IUnfold.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/IUnfold.lean#L102), and `omCover_holds` in [SCompact.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/SCompact.lean#L32).

`OmCover_holds` in the same file is a wrapper of the form `first | exact omCover_holds I | exact omCover_holds (I := I)`. The two branches state the same term, so the wrapper only renames `omCover_holds`. `WuDefinite_holds` and `ColBound_holds` in that file have the same form.
