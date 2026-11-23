---
id: pb-built-bounds2-cpt-of-mk-top
title: The built bounds from the top truncation statement
kind: theorem
decl: Formalism.FourierDecayAlt.P.pb_builtBounds2Cpt_of_mkTop
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.PbBuiltBounds2CptOfMkTop
covers: 1012
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves `BuiltBounds2Cpt` from the hypothesis `MkTop`. It turns `MkTop` into the head formula `HeadTop` and passes that to [the built bounds from the head formula](/entry/built-bounds-compact-of-head-top/), which has the real content. Its only user is [the built bounds, from the top truncation](/entry/built-bounds-compact/), which proves `MkTop`. `BuiltBounds2Cpt` is stated in [the built bounds at the infinite places, restated](/entry/pb-built-bounds2-cpt/).

## Statement

Fix the data $p$ at one real place, with parameters $k$ and $r$ and representations $\sigma$, $\sigma'$ on $W_p$, $W_q$. Write $Z$ for an $r \times r$ complex matrix and $y$ for a point of the top level (a matrix of size $k \times (r - r)$ in the Lean code). Call $\Phi(Z, y) \in \operatorname{Hom}(W_q, W_p)$ *equivariant* if $\Phi(Z, h y h') = \sigma(h) \Phi(Z, y) \sigma'(h')$ for $h$, $h'$ in two given sets (`UWset`), and $\Phi(Z u, y) = \psi(u) \Phi(Z, y)$ for each upper unipotent $u$, with a fixed function $\psi$ (`psiU`).

`MkTop` says: for each such $p$ there are smooth compactly supported real functions $b$, $b'$ on a chart space, a function $\beta$ that is smooth on the invertible matrices $Z$, and $\kappa \neq 0$, such that

1. each compact set $K$ in the top domain $U_T$ has a compact $K' \subseteq U_T$ that contains each $(Z, y)$ with $\beta(Z) \neq 0$ and some unipotent translate $(Z u, y)$ in $K$;
2. for each equivariant $\Phi$, each invertible $Z$ and each $y$ in the level set, the top pullback of the chart function built from $b$, $b'$ and $\beta \Phi$ is $\kappa \, \Phi(Z, y)$.

So each equivariant $\Phi$ is, up to the constant $\kappa$, the top pullback of a function with compact cutoffs. We have not unfolded the pullback `pbTop` or the chart function `F2`.

**Theorem.** If `MkTop` holds, then `BuiltBounds2Cpt` holds.

## Proof

The proof is one line:

```
built_bounds_compact_of_head_top (pb_headTop_of_mkTop hM)
```

`pb_headTop_of_mkTop` proves `HeadTop` from `MkTop`. It first gets an exhaustion picture `ExhPic` from `pb_exhPic_of_mkTop`, which gives `MkTop` and eighteen proved facts to `CutEX.exhPic_of_leaves`. Then `pb_headTop_of` with `top_unipotent_integral` gives `HeadTop`. The entry for `built_bounds_compact_of_head_top` states `HeadTop`.

## In the Lean code

The theorem is in [PbBuiltBounds2CptOfMkTop.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/PbBuiltBounds2CptOfMkTop.lean#L6). `MkTop` is in [CutEX2.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutEX2.lean#L93) and `pb_headTop_of_mkTop` in [PbHeadTopOfMkTop.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/PbHeadTopOfMkTop.lean#L26).

The size of this theorem is 1,012 and that of `built_bounds_compact_of_head_top` is 1,011. So `pb_headTop_of_mkTop` is not in the count here: `head_top` in [RadialExhaustion.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RadialExhaustion.lean#L6) also uses it, and proves `HeadTop` outright. With `head_top`, this theorem and `built_bounds_compact` are not needed.

In `MkTop` and `CutEX2.lean`, the top level has types such as `Mt P.k (P.r - P.r)` and `Fin (2 * (r - r) + k + 1)`. Since $r - r = 0$, these are the level $j = r$ of a family indexed by $r - j$.
