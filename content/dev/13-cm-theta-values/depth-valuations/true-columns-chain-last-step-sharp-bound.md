---
id: true-columns-chain-last-step-sharp-bound
title: The sharp column bound for each twisted chain of a true column choice
kind: theorem
decl: GlobalTheory.LvT.Built.TrueCols.trueColumns_chain_last_step_sharp_bound
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.TrueColumnsRowSharpBounds
covers: 2364
status: drafted
drafted_by: writer@claude
---
This lemma proves the sharp column bound for the twisted chain at each tuple of a true column choice. It checks the hypotheses of a general stability theorem for built chains and keeps the first half of its conclusion. Its user is [sharp column bounds for the datum of a true column choice](/entry/row-true/), which applies it at the reference tuple and at each other tuple.

## Statement

Let $B$ be a base, $X$ a `PreX` over $B$ and $I$ a true column choice `TC B X`. Let $l$ be laws for $I$, $l_0$ a law at level $0$ and $Z$ later stages. Let $D$ be the datum `I.rec7 l Z` and $\mathrm{Tw}$ the twisted forms `I.tw l l0 Z`. [Sharp column bounds for the datum of a true column choice](/entry/row-true/) describes these objects.

**Lemma.** Assume `I.Ok`, `I.JetsIn` and `BaseSigns B`. Then for each word $u$ and each tuple $a \in \iota$, the chain `tw Tw u a` satisfies `GlobalTheory.LvT.Conclusion5Sharp`.

For a chain with lattices $\Lambda_i$ and column map $\mathrm{col}$, this predicate says: for each place $w$ over $T_u$ and each $c$ with $v_w(c) \ge e_w\, m\, E_T(w)$, the map $\varphi \mapsto c \cdot \mathrm{col}(\varphi)$ sends $N_\lambda(w)$ into the $w$-part of $\Lambda_m$.

## Proof

1. [The five point laws for true chains](/entry/five-point-laws-true-chains/) give a built datum `Bd : Built.Dat D u` with these properties: its chain is `tw Tw u a`; each lattice $A_i$ with $i \le m$ splits over $T_u$; `Bd.Sees` holds; for each $i < m$ there is a kernel with the five laws `KerEq`, `KerDil`, `KerUK`, `KerBar` and `KerP`; and `Bd` is `dat I l Z u a`.
2. The inequality $[E:\mathbb Q]\, N_m + 1 < T_u$. The CM field has $[E:\mathbb Q] = 2f$ (`finrank_cmField`). `PreX` gives a real number $a$ with $2 f N_m + 1 < 4a$ (`a_gt`) and $4a < T_u$ (`T_gt`). Combine the two.
3. The weight signs. `wtSigns_assemble_iff` says that `WtSigns` for a chain of the assembled datum is the same as `BaseSigns B`. So `BaseSigns B` gives `WtSigns` for the chain.
4. `sharpBound_stability_latticeColumnChain` takes the splittings, `Sees`, the kernels, the inequality and the weight signs. It gives `Conclusion5Sharp` and `FormsStable` for the chain of `Bd`. Keep the first part and rewrite the chain to `tw Tw u a`.

## In the Lean code

The lemma is in [TrueColumnsRowSharpBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TrueColumnsRowSharpBounds.lean#L17). It calls:

- `GlobalTheory.T.fivePointLaws_trueChains` in [FivePointLawsTrueChainsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FivePointLawsTrueChainsStatement.lean#L8), a relay of `laws_true_fam`.
- `wtSigns_assemble_iff` in [EFirstGeOfULastNonpos.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/EFirstGeOfULastNonpos.lean#L249).
- `sharpBound_stability_latticeColumnChain` in [SharpBoundStabilityLatticeColumnChain.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/SharpBoundStabilityLatticeColumnChain.lean#L17).

We have not unfolded `Split`, `Sees` or the five kernel laws. This entry only passes them from the five point laws to the stability theorem. The real work is in those two theorems.

The name says "last step", but the lemma is not about a last step. It proves the sharp bound for every tuple $a$. The second part of the stability theorem, `FormsStable`, is dropped. The hypothesis `BaseSigns B` is used only in step 3. The weight signs do not depend on the chain or the word, since `wtSigns_assemble_iff` holds for every chain of the assembled datum.
