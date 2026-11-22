---
id: theorem-b-closing
title: Local lifting theorem B, from Bloch-Kato, Tate duality and the Euler characteristic
kind: theorem
decl: GlobalTheory.theoremB_closing
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingTheoremBOfBlochKatoTateDualityEulerC
covers: 1837
status: drafted
drafted_by: writer@claude
---
This theorem proves local lifting theorem B for every $C \ge 320$. It is restated as [local lifting theorem B from three local statements](/entry/local-lifting-theorem-b-of-bloch-kato-tate-duality-euler-char/), and through it goes to [the admissibility conditions at twisted inert primes](/entry/inert-step-main-alt-alt/). Its proof is a short assembly.

## Statement

Assume `BlochKatoLocal` (a dimension formula, a rational duality and an integral duality at each local datum), local Tate duality `LocalTateDualityK` and the local Euler characteristic formula `LocalEulerCharK` (Serre, *Galois Cohomology*, Chapter II, Section 5).

Let $T_1, T_2$ be lattices with Galois action, and $F \colon T_1 \to T_2$ an equivariant map. Write $\mathrm{col}(F)$ for the $O$-length of the finite cocycles of $T_2$ modulo the image of those of $T_1$ and the coboundaries. Write $\lambda$ for the length of $O/(p)$. The theorem bounds $\mathrm{col}(F)/\lambda$.

**Theorem.** For each datum $D$ with Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$, and each real $C \ge 320$, the following holds. Let $\ell \ge 11$ be prime, $K$ a finite extension of $\mathbb{Q}_\ell$ inside the maximal unramified extension, and $L$ a good coefficient field. Let $W$ be the Wach module of $HW$ at $(K, L)$. Take integers $b, w, S, \eta, m$, signs $\mathrm{up}(i)$ and sizes $\mathrm{size}(i)$ for $i \in \mathbb{Z}/n$, such that:

- the jumps (`JumpsAt`) of $T_1$ at $i$ lie in $[\mathrm{size}(i), \mathrm{size}(i) + S] \cup [-\eta, \eta]$, or in the mirror window when $\mathrm{up}(i)$ is false, and $\eta < \mathrm{size}(i)$;
- `lowCount` of $T_2$ at $i$ and $\eta$ is at most $m$;
- each $i$ that is not thick ($b \le \mathrm{size}(i) \le b + \eta$ fails) has $\mathrm{size}(i) \le w$, and some $i$ is not thick;
- $20w, 20\eta, 20S \le b$, and the conditions `CaseA`, `Sur`, `JumpsLet`.

Let $h = b + \eta + S$ if some $i$ is thick and $h = w + S$ if not, and let $r$ be the dimension of the $L$-space of $T_2$. If the signs alternate and no three consecutive indices are thick, then

$$\frac{\mathrm{col}(F)}{\lambda} \le C(n+1)r\Bigl(\frac{h}{\ell^2} + \frac{w + \eta}{\ell} + S + 1 + \log_\ell(2h) + \eta\beta\Bigr) + Cnme'.$$

Here $\beta \in \{0, 1\}$ is a band indicator and $e'$ is a lift exponent (`eLift`); we have not unfolded `eLift`. A second bound, with $R^2$ factors, holds when the signs are constant and no $R$ consecutive indices are thick.

## Proof

1. `one_place_admissible_of_gap_constant_le` gives `adm22` (a Fontaine inequality at all $\ell, K, L$), and `jumps_exact_adm` gives `adm23`.
2. `wachLattice_laterClauses_hold` and `letterConditionGlobal_of_N1used` give the global letter condition.
3. `localLifting_theoremB_hypotheses_admitted` gives the 13 admitted conditions with the constants $(10, 23, 32, 32, 8)$. This is the only step that uses the three hypotheses.
4. `theoremB_of_localFilteredHypotheses` turns steps 1 to 3 into the bound.

## In the Lean code

The theorem is in [LocalLiftingTheoremBOfBlochKatoTateDualityEulerC.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremBOfBlochKatoTateDualityEulerC.lean#L15). The conclusion is `aux₃` in [ArcLiftingSetup.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArcLiftingSetup.lean#L486), which is `TheoremBLocal`, with the bound `ThmB` in [CrystallineMapLemmas.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineMapLemmas.lean#L75).

The work is in two lemmas. Step 3 renames `TheoremBAdm.admissible_ranks_of_CMDatum` in [LocalLiftingTheoremBHypothesesAdmitted.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremBHypothesesAdmitted.lean#L26), which proves the 13 conditions with 17 lemma calls. Step 4 is a chain of two renamings down to `frobenius_statement_of_fontaine` in [FrobeniusStatementOfFontaine.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusStatementOfFontaine.lean#L218).

Odd points. The lemma `admissible_ranks_of_CMDatum` is about neither ranks nor CM data, and the same name is used for a different lemma in [AdmChi.lean](lean:Development/AutomorphicArithmetic/CoprimeRanks/AdmChi.lean#L11). The hypothesis set of the bound is called `HidaSetting` ([line 39](lean:Formalism/SharpRestriction/LevelLetterCocycles/CrystallineMapLemmas.lean#L39)), but it is a list of jump conditions with no Hida theory. The constants $(10, 23, 32, 32, 8)$ and the data $C_m$ do not appear in the conclusion.
