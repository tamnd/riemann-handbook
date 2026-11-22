---
id: integrality-from-metric-of-large-constant
title: The local colength bound for each constant C at least 160, from 29 leaf lemmas
kind: theorem
decl: Formalism.MainNotions.N.Ln34.integrality_from_metric_of_large_constant
module: Formalism.SharpRestriction.LevelLetterCocycles.DvrLatticeRank.MainFinal
covers: 1152
status: drafted
drafted_by: writer@claude
---
For each $C \ge 160$, this theorem proves that the 13 admitted conditions `Adm1` imply the local colength bound `Conclusion1 D C`. It has three side hypotheses: the Wach functor is exact, $D_{\mathrm{dR}}$ has full rank, and a rank condition on Wach modules. [The version for $160 \le C$](/entry/integrality-from-metric-of-le/) proves them outright and calls this theorem, and [`integrality_from_metric_of_160_le`](/entry/integrality-from-metric-of-160-le/) restates that for [the closing of theorem A](/entry/theorem-a-closing/).

## Statement

For $\ell \ne 2$ and a good pair $(K, L)$, let $n = [K_0 : \mathbb{Q}_\ell]$ and $e = [K : K_0]$. Let

$$B(C) = C(ne+1)\, r \Bigl(\frac{eh}{\ell} + eS + e \log_\ell h + 1 + \eta\Bigr) + n e (e+1)\, m\, C (h+1).$$

`thmA` says: let $f \colon T_1 \to T_2$ be a surjection of crystalline lattices with $r = \dim_L T_2$. Suppose that at each embedding $\tau$ the jumps of $T_1$ lie in $[b_\tau, b_\tau + S] \cup [-\eta, \eta]$ (or in $[-b_\tau - S, -b_\tau] \cup [-\eta, \eta]$), with $\eta < b_\tau$. Suppose that the multiplicities of the jumps of $T_2$ in $[-\eta, \eta]$ add up to at most $m$, that all jumps of $T_1$ lie in $[-h, h]$, and that $e = 2$ or the choice of side depends only on $\tau|_{K_0}$. Then $\mathrm{col}(f) \le B(C)\, k$, where $k$ is the length `lenOl` of $\mathcal{O}_L/(\ell)$.

**Theorem.** Let $D$ be a datum with local data $HW$, $F$, $C_m$, and let $C_A, C_B, C_K, C$ be reals with $C \ge 160$. Assume:

1. (`FontExAll`) for each short exact sequence of lattices, the Wach functor gives a short exact sequence;
2. (`DdRFull`) $\dim_L D_{\mathrm{dR}}(T, \tau) = \dim_L T$ for each crystalline $T$ and each $\tau$;
3. (`DiRank`) each piece $\iota_{\mathrm{Di}}(T, c)$ of the Wach module of a crystalline $T$ has dimension $\dim_L T$.

If `Adm1 D HW F Cm CA CB CK` holds, then `thmA` holds at each $\ell \ne 2$ and each good pair $(K, L)$.

## Proof

The proof is `lifting_theorem_of_uniform_link u1link_pf`, which gives 29 leaf lemmas to `local_theorem_of_leaf_lemmas`. They give three facts at each good pair:

1. (`genA`) the finite cocycles of $T_2$ are spanned, modulo coboundaries, by at most $g = 2(ne+1)r$ cocycles;
2. (`liftA`) $f$ lifts with exponent `expLift l h J` for a set $J \subseteq [-h, 2h]$ with $0 \notin J$;
3. (`killA`) there are at most $ne(e+1)m$ cocycles $s_0$ such that $\ell^{Y}$ kills each finite cocycle modulo $\mathrm{span}(s_0) + \mathrm{Im}\, f$, with an explicit $Y$.

The third fact uses most leaf lemmas and all three side hypotheses. Then `colLe_of_twoStep` gives $\mathrm{col}(f) \le (g Y + ne(e+1)m \cdot \mathrm{expLift})\, k$. `Ynum` bounds $Y$ by 80 times the bracket in $B(C)$, and `valuationSumBound` gives $\mathrm{expLift} \le 18h$. Since $2 \cdot 80 = 160 \le C$ and $18h \le C(h+1)$, this is at most $B(C)\, k$ (`thmA_of_claim`).

## In the Lean code

The theorem is at [MainFinal.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/MainFinal.lean#L10), with `lifting_theorem_of_uniform_link` at [MainPf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/MainPf.lean#L38) and `local_theorem_of_leaf_lemmas` at [LocalTheoremOfLeafLemmas.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalTheoremOfLeafLemmas.lean#L13). `Adm1`, `IntegralityFromMetric` and `thmA` are in [ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L157). The numerical step is at [LocalTheoremOfGoodExtensions.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalTheoremOfGoodExtensions.lean#L171). We have not unfolded the 29 leaf lemmas.

- The name says "integrality from metric", but the statement is a colength bound for lattices. In the same folder, three other files define a different `IntegralityFromMetric` (for example [SumRepresentations.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/SumRepresentations.lean#L402)), and twelve other files define a different `Conclusion1`.
- `FontExAll` is used only by the `KerLamStep` leaf lemma. `FontExAll` and `DiRank` take arguments `_F` and `_Cm` that they do not use.
