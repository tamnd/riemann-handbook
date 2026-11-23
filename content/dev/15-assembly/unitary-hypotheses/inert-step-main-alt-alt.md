---
id: inert-step-main-alt-alt
title: The admissibility conditions at twisted inert primes
kind: theorem
decl: GlobalTheory.NLink.InertStep.main_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsFurtherBis
covers: 3369
status: drafted
drafted_by: writer@claude
---
This theorem proves that the family of representations in a hub datum is admissible at each twisted index whose prime is inert. Its statement is restated as [the admissibility at inert primes in range](/entry/adm-at-inert-of-range/), which gives the inert case of [the rows of the hub](/entry/rows-ad-in-setting-alt/). That result goes up to [the closing of the family bound](/entry/nlink-close-main-alt-alt/) and so to the step [the hypotheses are not empty](/step/nonempty-hyps/).

## Statement

Assume $\mathrm{Hyp}_2$. This is a list of seven named statements: `FontaineBcris`, `GlobalArtinReciprocity`, `BlochKatoLocal`, `LocalTateDualityK`, `LocalEulerCharK`, `LocalFinitenessK` and `BhattScholzeIntegral`. We have not unfolded them. Fix a datum $D$, size data $L$, a hub datum $X$ (families $r_i$ of rank $n_V$ and $\rho_i$ of rank $r$, row and column data, constants $c_B$) and a real $C_2 \ge 1$. Suppose that $X$ satisfies the setup `SetupAlt` with $C_2$, that the local lifting corollary holds for $C_2$, and that the joint hub conditions hold for the row constants $(C_2, 320, 25, 23, 32, 32)$.

**Theorem.** Let $i$ be an index with twisted local character, with $\ell_i \notin \{g_0, g_1\}$, with $\ell_i$ in the admissible range of $L$, and with $\ell_i$ inert. Then for each good point $\pi \in Z_i^{\mathrm{good}}$ the quadruple $(r_i, \rho_i, \pi)$ is admitted with the data of $X$ at $i$.

"Admitted" is a list of 20 conditions. Among them: the characteristic polynomials of $r_x(g)$ have coefficients in the Hecke algebra $T_i$; each $r_x$ is absolutely irreducible and its residual polynomial is that of $\bar\rho$ times $\prod_{c=1}^{t}(X - \chi^c)$; $r$ is unramified outside $\ell$, $S_i$ and $Q_i$; $r(\pi) \cong \rho(\pi) \oplus \bigoplus_c \chi^{c+1}$; a tame bound at places above $\ell$; a length bound at the row places; a lift exponent condition at the column places; and a bound by $v_\ell(h_E)$ on the unramified Hom group.

## Proof

1. Seventeen conditions come from `set_pt_of_setup_not_twisted`, which needs only $\ell_i \notin \{g_0, g_1\}$.
2. `closingFamilyX_alt_alt` gives a Wach module $M_0$ and a tame bound. With the Bloch-Kato, Tate and Euler hypotheses, `localBlochKatoCondition_of_wachModules` turns them into the tame condition at $c_B$.
3. `eleven_le` gives $\ell_i \ge 11$, from inertness and a split bound $\ge 10$.
4. The row length bound splits in two cases. If $\ell_i$ is a row B prime, `longOrbits_rowColength_inertLocalisation` applies, with the lifting corollary. If not, `rowsCD_rowCondition_localBounds` applies, with [local lifting theorem B](/entry/local-lifting-theorem-b-of-bloch-kato-tate-duality-euler-char/) at 320 and [the bound 25](/entry/prv-twenty-five-of-bloch-kato-tate-duality-euler-char/). In both cases the input is the joint hub condition.
5. The lift exponent condition holds because the column set is empty at inert primes.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ImportsFurtherBis.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherBis.lean#L15). "Admitted" is `TruncatedSeriesCountingIdentities.admitted` in [DecompositionData.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DecompositionData.lean#L316). We have not unfolded `TBAt`, `RowAt` and `LiftAt`.

- The lift exponent condition is vacuous here: the field `col` of `DataAD` makes the column set empty at inert primes, and `simp` closes it.
- The name `set_pt_of_setup_not_twisted` ([SetPointGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SetPointGood.lean#L11)) says "not twisted", but this theorem applies it at a twisted index. Its hypothesis is only $\ell_i \notin \{g_0, g_1\}$.
- `eleven_le` is in [InertPlacesGoodSet.lean](lean:Development/AbelianVarietyTheory/Counterexamples/HeckeCharacterExamples/InertPlacesGoodSet.lean#L22), in a folder named `Counterexamples`. It is not a counterexample.
