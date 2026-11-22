---
id: spec-out-s
title: Eigenforms on U(2) go to U(3) or to a higher weight on U(2), with the levels fixed
kind: theorem
decl: UpperTheory.V.Z.Sym.W.specOutS
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.WeilDeligneUnramified.LevUnion
covers: 2867
status: drafted
drafted_by: writer@claude
---
This theorem takes a Hecke eigenform on a definite unitary group $U(2)$ over a CM field. It gives an eigenform on $U(3)$ with the parameters $(a, 1, a^{-1})$, or an eigenform on $U(2)$ of higher weight with the parameter $a^2$. Its only use is in [adjoint automorphy from the printed Hida window](/entry/adjoint-automorphy-w-of-printed-hida-window/), where `adjoint_lift_w_of_literal_automorphy_spec_out` turns it into the adjoint lift `AdLiftW`. The mathematics is in [the core step](/entry/core/). This theorem fixes the levels.

## Statement

Let $L$ be a CM field, unramified over its maximal totally real subfield $L^+$ at all finite places. For $n = 2, 3$ let $U(n)$ be the unitary group of the identity hermitian form for $L/L^+$, and let $K_n$ be the product of the groups $\mathrm{GL}_n(\mathcal{O}_w)$ over the finite places. For a finite set $S$ of places and local levels $V_w$, let $\mathrm{lev}(U, S, V)$ be $U$ cut down at each $w \in S$ to an Iwahori type group $J_n(V_w)$: upper unipotent matrices, diagonal matrices with entries in a group $H$, and lower unipotent matrices of depth $c$ (from `glIwa`, which we have not unfolded). The level $\mathrm{iw}$ has $c = 0$ and $H = \mathcal{O}_w^\times$. The level $\mathrm{deep}(c)$ has $H = 1 + \varpi^{c+1}\mathcal{O}_w$.

$\mathrm{EigS}(a_w)$ at $w$ says: for each $t$ with $|t| < 1$, the double coset of $\mathrm{diag}(t, t^{-1})$ acts by the scalar of the character $(a_w, 1)$. $\mathrm{EigT}(a_w, 1, a_w^{-1})$ is the same on $U(3)$ for all strictly dominant diagonal elements.

**Theorem.** Let $S_0$ be a finite set of places of $L$, split over $L^+$, at most one over each place of $L^+$, and with a place over each place of $L^+$ above 2. Let $j \ge 1$. There is $c_0$ such that for each $c \ge c_0$ there is an open subgroup $U_2 \subseteq K_2$ with this property. Let $S_1$ be disjoint from $S_0$, with $S_0 \cup S_1$ as for $S_0$ and $U_2 \supseteq K_2 \cap U(2)(L_w)$ for $w \in S_1$. Let $\varphi \ne 0$ be a form of weight $\mathrm{Sym}^j \otimes \det^e$ and level $\mathrm{lev}(\mathrm{lev}(K_2, S_0, \mathrm{deep}(c)), S_1, \mathrm{iw})$, with $\mathrm{EigS}(a_w)$ on $S_0 \cup S_1$. Then:

1. there is a form $\varphi' \ne 0$ on $U(3)$ of weight `repG j` and the same level, with $\mathrm{EigT}(a_w, 1, a_w^{-1})$ on $S_0 \cup S_1$; or
2. there is a form $\varphi' \ne 0$ on $U(2)$ of weight $\mathrm{Sym}^{2j+1}$ and level $\mathrm{lev}(U_2, S_1, \mathrm{iw})$, with $\mathrm{EigS}(a_w^2)$ on $S_1$.

## Proof

`bridgeEx` writes $L \cong L^+(\sqrt{\Delta})$ and matches $U(3)$ and $SU(2)$ over $L$ with groups over $L^+$. Take $c_0 = 0$ and fix $c$. `fitEx` gives local data $A_0$ over $L^+$ that fit $(S_0, \mathrm{deep}(c))$. `repsEx` with `classRep` gives a finite set of double coset representatives. `congLev` and `congEx` give a principal congruence subgroup of level $m \ge 3$, and this is $U_2$.

Given $S_1$ and $\varphi$, put $S = S_0 \cup S_1$, with $\mathrm{deep}(c)$ on $S_0$ and $\mathrm{iw}$ on $S_1$. `fitEx` gives data $A$ and a character $b$ that fit $S$, and `fitExt` shows that $A$ extends $A_0$. `lev_union` rewrites the level as $\mathrm{lev}(K_2, S, V)$, and `baseK'` gives a space of quaternionic forms. Then [`core`](/entry/core/) gives the dichotomy. Its first case is case 1. In its second case, the private lemma `second` (through `kNon`, `kRes`, `levExt`, `outS`) turns the quaternionic form into a form on $U(2)$ at level $\mathrm{lev}(U_2, S_1, \mathrm{iw})$. The rest is bookkeeping.

## In the Lean code

`SpecOutS` is at [LevUnion.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/LevUnion.lean#L138), and the theorem at [line 150](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/LevUnion.lean#L150).

- The proof takes $c_0 = 0$, so every $c$ works.
- $U_2$ depends on $c$, $S_0$ and $j$, not on $S_1$ or $\varphi$.
- Case 2 has no condition on $S_0$, and its weight has $e = 0$.
