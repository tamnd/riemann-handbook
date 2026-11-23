---
id: odd-block-supply
title: The odd block supply from minors of a flag
kind: theorem
decl: GlobalTheory.oddBlock_supply
module: Development.AbelianVarietyTheory.Proofs.UnramifiedDepth.OddLevelBlockBoundAttained
covers: 576
status: drafted
drafted_by: writer@claude
---
This theorem proves the two forms `BiSupply` and `RF.BiSupply` of the odd block supply. It applies [`window_letterDet`](/entry/window-letter-det/), which does the work, to the first $n$ letters that a flag lists. It is used under the second name [`oddLevelBlock_bound_attained`](/entry/odd-level-block-bound-attained/).

## Statement

Let $X$ be a row datum (`RowData`) with modulus $d$, over a field with a valuation $v$ and a prime $\ell$ with $v(\ell) = 1$. For a side $g \in \{0, 1\}$ and a type $a \in \mathbb{Z}/d$, let $r(g, a)$ be the number of letters of side $g$ and type $a$. A *flag* $F$ is an injective list $F_{g,a}(1), \dots, F_{g,a}(r(g, a))$ of these letters. The axiom `rk_big` of $X$ says that $r(g, a) = n + j$ when $(g, a)$ is big.

`BiSupply` says: for every such $X$ and $F$ with $X$ alternating, $\ell \ge 5$ and $n \ge 1$, every big $(g, a)$ and every odd $i < d$, the set of $y$ for which `bi g a i y` attains the block bound $B(y)$ contains $0$ and meets every interval $[Y_0, Y_0 + S_0)$, with $S_0 = \lceil 64 n^2(i + 3 + 3\log_\ell(n + 1))\rceil$. Here `bi g a i y` is the jet value of $\Delta^{\ell^i y}\Delta'^{y}$, where $\Delta$ is the $n \times n$ minor on the letters $F_{g,a}(1), \dots, F_{g,a}(n)$ and $\Delta'$ the minor on $F_{1-g,a+i}(1), \dots, F_{1-g,a+i}(n)$. The bound $B(y)$ and the jet value are as in [`window_letterDet`](/entry/window-letter-det/).

`RF.BiSupply` is the same statement in the namespace `RF`, with the count $r$ written `rkF`.

**Theorem.** `BiSupply` and `RF.BiSupply` hold.

## Proof

The two parts have the same proof.

1. Since $(g, a)$ is big, $r(g, a) = n + j \ge n$. So the first $n$ letters $F_{g,a}(1), \dots, F_{g,a}(n)$ exist and are distinct.
2. Since $X$ is alternating ($d$ even, and $(0, b)$ big exactly when $b$ is even) and $i$ is odd, $(1 - g, a + i)$ is also big (`big_shift`). So $r(1 - g, a + i) \ge n$ as well.
3. `window_letterDet` applied to these two lists of $n$ letters gives the window property for the determinants `letterDet`.
4. `rename_minor` says that `letterDet` is the generic minor `minorK` with its variables renamed to the letters. This rewrites the result into the form of `bi`.

## In the Lean code

The theorem is at [OddLevelBlockBoundAttained.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/OddLevelBlockBoundAttained.lean#L155), with `big_shift` at line 24 and `rename_minor` at line 44. `BiSupply` is in [ContentLargeFromSupplies.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentLargeFromSupplies.lean#L72) and `RF.BiSupply` in [ContentZeroAt.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentZeroAt.lean#L78). We did not unfold `ValOf` or the attainment predicate beyond the description in `window_letterDet`.

Odd points:

- `RowData.rk` ([ContentLargeFromSupplies.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentLargeFromSupplies.lean#L15)) and `RowData.rkF` ([ContentZeroAt.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentZeroAt.lean#L21)) have the same definition, and `BiSupply`, `RF.BiSupply` have the same text. The proof is copied twice (lines 156 to 176).
- All users take only `RF.BiSupply`.
- `window_letterDet` is in the namespace `GlobalTheory.MinorShiftJet`, which the file name does not show.
