---
id: leaf-good
title: The depth bound at good places of a leaf, from the local depth bound
kind: theorem
decl: GlobalTheory.GoodDepth.leafGood
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthTableGoodPrimeLeaf
covers: 865
status: drafted
drafted_by: writer@claude
---
This theorem proves `LeafDepthGood` for a leaf object whose exponents come from depth data. It turns the bound on the local depth $\nu_W$ at one place, [`goodPlaceDepthBound_proof`](/entry/good-place-depth-bound-proof/), into the four parts of `LeafDepthGood`. Its alias [`depthTable_goodPrimeLeaf`](/entry/depth-table-good-prime-leaf/) gives it to [`leafGood_run`](/entry/leaf-good-run/).

## Statement

Use the leaf object $O$, the depth $e_0(v,j)$, the constants $C, k, m, f, T, Y, b, L$, the weights $\theta, a$ and the term $a_E(j,\ell)$ from [the entry for `leafDepth_all_run`](/entry/leaf-depth-all-run/), which also states `LeafDepthGood`.

**Theorem** (`LeafGoodSt`). For each $C_1 \ge 0$ there is $C_0$ with the following property. Let $E$ be a CM field with a host $H$, a level with integer $M$, moduli spaces $X_i$ for data $D_{w,i}$, a coefficient field $F$, depth data $D$ (`DepData`), a numerical datum $N$, a map $\iota \colon J \to \mathbb{N}$ and $F_0$ (`IndefNum`). Assume:

1. $C_0 \le C$;
2. the exponents $E(v,j)$ and elements $\sigma(v,j)$ of $O$ are those built from $D$ (`EAt`, `sigAt`), and the bad primes $g_1, g_2, q_1, d, s_m$ of $O$ are those of $D$ and of $N$ (`TiePrimes`);
3. $\pi_i \bar\pi_i = g_{i+1}$ (`PiSplit`), $M = g_1 g_2$ (`LevelQ`), and the star on $\mathcal{O}_E$ is complex conjugation;
4. for each $j$: every algebraic integral point of $X_{\iota(j)}$ has an integral chart (`IntChartEx`), the seven package statements `PkgSt` hold, and `GoodPage` holds with $C_1$, $b$ and $L$;
5. `PlaceTie`, `NumTie` (the constants of $O$ match those of $N$, and $a = 0$), `LeafPage`, and $F_0 = $ the content of $N$.

Then `LeafDepthGood N O` holds.

## Proof

Let $C_c$ be the constant that [`goodPlaceDepthBound_proof`](/entry/good-place-depth-bound-proof/) gives for $C_1$, and put $C_0 = \max(C_c, 20)$.

1. $\theta(l) \ge 0$, as a supremum of positive numbers, and $a = 0$ by `NumTie`. So the sum with $a$ is $0$, and $\sum_{p \in Q} \theta(p) \log p \le 20/k \le C/k$ by `sum_level_tail_mul_log_primes_le`.
2. Let $w$ be a good place with $\ell = \ell(w)$, and let $v$ be $w$ or $\bar w$. Let $\lambda$ be the place of $F$ below $v$. `onObj_exponent_eq_rounded_depth` gives $e_0(v,j) \le T_D \nu_W(\lambda)/e_\lambda + 1$, with $T_D$ the integer $T$ of $D$, and $e_0(v,j) = 0$ if $\nu_W(\lambda) = 0$. Since $M = g_1 g_2$ and $\ell \ne g_1, g_2$, $\ell \nmid M$. So the local bound applies: $T_D\nu_W(\lambda)/e_\lambda \le F_0(w,j) + C_c \cdot \mathrm{err}(\ell)$, with the error term $\mathrm{err}(\ell)$ of [`nuGood`](/entry/nu-good/). The lemma `err_mono_leaf` shows $C_c \cdot \mathrm{err}(\ell) \le a_E(j,\ell)$ since $C_c \le C$.
3. Let $D_F$ be the total weight of the datum (`DF`). `NumTie` gives $D_F \le C \cdot D_F(O) = Y$. So if $\ell > Y$, then $D_F < \ell$, the local bound gives $\nu_W(\lambda) = 0$, and $e_0 = 0$. `forcedContent_bounds_programmeValue_goodPrime` gives $F_0(w,j) \ge 0$.

## In the Lean code

The theorem is in [DepthTableGoodPrimeLeaf.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthTableGoodPrimeLeaf.lean#L42). Besides the alias `goodPlaceDepthBound_proof`, it calls `onObj_exponent_eq_rounded_depth` ([NormalizedLatticeExponentEqRoundedDepthGoodPlaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/NormalizedLatticeExponentEqRoundedDepthGoodPlaceStatement.lean#L6)), `sum_level_tail_mul_log_primes_le`, `forcedContent_bounds_programmeValue_goodPrime`, and two small lemmas of the same file.

The hypothesis $T = T_D$ (named `hT`) is not used: $T$ enters $a_E$ only through $T \cdot a(\ell)$, and $a = 0$.
