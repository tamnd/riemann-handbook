---
id: window-letter-det
title: Minor determinants meet the odd block bound in every window
kind: theorem
decl: GlobalTheory.MinorShiftJet.window_letterDet
module: Development.AbelianVarietyTheory.Proofs.UnramifiedDepth.OddLevelBlockBoundAttained
covers: 572
status: drafted
drafted_by: writer@claude
---
This theorem does the work of [the odd block supply](/entry/odd-block-supply/). It bounds the valuation of a jet value made from two powers of $n \times n$ minors, for $y = 0$ and for at least one exponent $y$ in each interval of a fixed length. `oddBlock_supply` applies it to the first $n$ letters of a flag and gets both forms of `BiSupply`.

## Statement

Let $K$ be a field with an additive valuation $v$ into $\mathbb{R} \cup \{\infty\}$, and $\ell \ge 5$ a prime with $v(\ell) = 1$. Let $X$ be a row datum (`RowData`) with modulus $d$: two finite sets of letters $I_0, I_1$ with types in $\mathbb{Z}/d$, integers $n, j, j'$, a predicate "big" on pairs $(g, a)$, series $h(g, a, a')$, and axioms that we do not unfold. Put $m = j + j'$. Suppose $X$ is alternating: $d$ is even, and $(0, a)$ is big exactly when $a$ has an even representative in $[0, d)$.

Fix a big pair $(g, a)$, an odd $i < d$, and $n \ge 1$. Let $p_1, \dots, p_n$ be distinct letters of $I_g$ of type $a$, and $p'_1, \dots, p'_n$ distinct letters of $I_{1-g}$ of type $a + i$. Take $n$ copies $x_\rho$ of the variables, and let $\Delta = \det(x_{\rho, p_c})$, $\Delta' = \det(x_{\rho, p'_c})$. For a polynomial $P$ and series $f_1, \dots, f_n$ put

$$\mathrm{Val}(P; f) = \Bigl[P(\partial) \prod_{\rho} f_\rho(x_\rho)\, e^{h(g, a, a+i)(x_\rho)}\Bigr]_{x = 0}.$$

Let $\gamma_\ell = \ell/(\ell^2 - 1)$, $B(0) = 0$ and, for $y \ge 1$,

$$B(y) = n y\bigl((\ell^i + 1)\gamma_\ell - 1\bigr) + n(\log_\ell n + 1) + \frac{(i+1)\, m\, (\ell^i + 1)\, y}{\ell - 1}.$$

Let $G$ be the set of $y \ge 0$ for which there are standard coordinates $t$ (`IsT`) and germs $f_\rho$ in the integral germs of $t$ with $v\bigl(\mathrm{Val}(\Delta^{\ell^i y} \Delta'^{y}; f)\bigr) \le B(y)$.

**Theorem.** $0 \in G$, and each interval $[Y_0, Y_0 + S)$ meets $G$, where $S = \lceil 64 n^2 (i + 3 + 3\log_\ell(n+1)) \rceil$.

The bound is an upper bound on $v$: the value is not too divisible by $\ell$.

## Proof

1. `rowData_mainTerm_normalForm_and_levelOne` (part `LemmaM`), applied to the coordinate vectors of the $p_c$ and $p'_c$, gives $n_0 \le n$ with $n - n_0 \le (i+1) m$ and a normal form of the main term.
2. `mainTerm_implies_rowHypothesis` turns it into the row identity and the weight conditions `HM1`, `HM2` for a series $h_1$ in $n_0 \times n_0$ variables.
3. `block_of_normal_form` reduces to a model. For each $y$ it gives germs with $v(\mathrm{Val}) \le v(J_y)$, where $J_y$ is the value at $0$ of $\det(\partial_L)^{\ell^i y} \det(\partial_R)^y$ on a product series built from $h_1$ (`BiF`).
4. If $n_0 = 0$, `blockValue_on_rows_eq` gives $J_y = ((\ell^i y)!\, y!)^n$, and the first half of `content_and_window` bounds it. Every $y$ is in $G$.
5. If $n_0 \ge 1$, the second half of `content_and_window` gives a good $y$ in each window of length $S_0(\ell, i, n_0) \le S$ (`mono_resι_var`).

For $y = 0$, $J_0 = 1$ and $B(0) = 0$. The rest is bookkeeping.

## In the Lean code

The theorem is in [OddLevelBlockBoundAttained.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/OddLevelBlockBoundAttained.lean#L89). It calls `GlobalTheory.T.rowData_mainTerm_normalForm_and_levelOne`, `GlobalTheory.T.mainTerm_implies_rowHypothesis`, `block_of_normal_form` ([BlockOfNormalForm.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/BlockOfNormalForm.lean#L317)), `GlobalTheory.T.blockValue_on_rows_eq` and `GlobalTheory.OddBlock.content_and_window` ([SumEqOfIsHomogeneous.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/SumEqOfIsHomogeneous.lean#L1084)). `RowData` and `ValOf` are in [Interface.lean](lean:Formalism/LocalToGlobal/CharacterGerms/Interface.lean#L103).

Odd points:

- `RowData` is a package of axioms (`R1`, `R2`, `G0`, `C_eq`, `CH` and others). The theorem is conditional on it. We did not check that the axioms have a model.
- `blockBd` and `Windows` are defined twice with the same text, in [ValuationChoiceHypothesis.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ValuationChoiceHypothesis.lean#L34) and in the namespace `RF` of [ContentZeroAt.lean](lean:Formalism/LocalToGlobal/CharacterGerms/ContentZeroAt.lean#L11). So `oddBlock_supply` gives the same proof twice.
