---
id: theorem-bqd-main-alt-alt
title: The bound at the primes q and d from the setup
kind: theorem
decl: GlobalTheory.TheoremBQD.main_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainOfAltAlt
covers: 1324
status: drafted
drafted_by: writer@claude
---
This theorem gives a bound on the congruence module at twisted primes $\ell \in \{q, d\}$, for each hub datum with the setup `SetupAlt`. It is restated as [the bound at q and d, restated](/entry/embedding-jumps-aux2-of-setup/), which goes to [the closing of the family bound](/entry/nlink-close-main-alt-alt/). Most of the proof only passes hypotheses along. The content is in [the Selmer length bound at twisted places](/entry/twisted-place-selmer-length-bound-of-local-duality/).

## Statement

**Theorem.** Let $C = 2080$ and $Q = 260\, X_0^2 X_2^2 (X_1 + X_2)$. Assume the seven hypotheses $\mathrm{Hyp}_2$. Let $D$ be a datum, $L$ size data and $X$ a hub datum with the setup `SetupAlt` for some $C_2$. Let $i$ be an index with $\ell = \ell_i \in \{q, d\}$, with twisted local character and with $\ell > x^{2C_t + 5}$, where $x$ and $C_t$ come from $L$. Let $\pi$ be a good point. Suppose that the Selmer group at $\pi$ is finite and that the groups $Ш_e$ for $0 < e < t$ are finite. Then

$$v_{\mathrm{cc}}(\pi) \le B_\ell + \sum_{0<e<t} \operatorname{len} Ш_e + v_\ell(h_E) + s_\pi + \ell^{-2},$$

with $B_\ell = C f \bigl(r (b/\ell + S_c + t + \eta + \log b) + m b\bigr) + Q(f, r, t) \log b$. Here $f, r, t, m$ are integers of $D$, and $b, S_c, \eta$ are sizes in $L$.

## Proof

The proof applies `main_of_alt` to `twistedPlace_selmerLengthBound_of_localDuality`. The lemma `main_of_alt` takes that statement as a hypothesis and checks its inputs:

- the admissibility conditions G1 to G6, the tame generator conditions and the Iwahori condition at $\ell \in \{q, d\}$ come from `set_pt_of_setup_not_twisted`, with $\ell \notin \{g_0, g_1\}$;
- the lattice index theorem comes from `lengthBound_of_rowConditions_and_dualityTheorems`, with Artin reciprocity, Bloch-Kato, Tate duality and the Euler characteristic;
- the condition at twisted places comes from the field `kill` of the setup;
- the Hodge jumps come from `hodgeJumpParameters_of_setup`;
- the inequality $260 f^2 t^2 (r+t) \le Q(f, r, t)$ is `polyB_val`.

Conditions that do not depend on $\pi$ use a good point chosen by `exists_good`. The rest is bookkeeping.

## In the Lean code

The theorem is in [MainOfAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainOfAltAlt.lean#L55). The bound is `EmbeddingTypeJumps.Conclusion2` in [EmbeddingTypeJumps.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/EmbeddingTypeJumps.lean#L65). $Q$ is `polyB` in [PolynomialBoundSetup.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PolynomialBoundSetup.lean#L28).

- The hypothesis `hc` of [main_of_alt](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainOfAltAlt.lean#L18) is exactly the statement of a proved lemma. The split into two theorems adds nothing.
- The closing lemma gives three conclusions. `main_of_alt` keeps only the third.
- The condition $\ell > x^{2C_t+5}$ with $\ell \in \{q, d\}$ asks a fixed prime of the host to be large. We have not checked when it can hold.
- `TwLoc` is defined twice, in `EmbeddingTypeJumps` and in [TwistedPlaces.lean](lean:Development/AutomorphicArithmetic/ResidueCharacters/TwistedPlaces.lean#L77), with the same meaning: the character $\mu$ at the place $w_i$ is not $\mu_0$.
