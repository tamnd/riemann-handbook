---
id: ramified-coefficient-chains-prv-twenty-five
title: The ramified coefficient bound with constant 25
kind: theorem
decl: GlobalTheory.ramifiedCoefficientChains_prv_twenty_five
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RamifiedCoefficientChainsPrvTwentyFive
covers: 1335
status: drafted
drafted_by: writer@claude
---
This theorem proves a local bound on cokernel lengths of maps of lattices (local lifting theorem C) with the constant $C = 25$. It is restated as [the bound 25 from three local statements](/entry/prv-twenty-five-of-bloch-kato-tate-duality-euler-char/), which goes to [the admissibility conditions at twisted inert primes](/entry/inert-step-main-alt-alt/). Its proof is a short assembly. The bound itself comes from [the theorem from literature hypotheses](/entry/theorem-of-literature-hypotheses/).

## Statement

Assume `BlochKatoLocal`, local Tate duality `LocalTateDualityK` and the local Euler characteristic formula `LocalEulerCharK` (Serre, *Galois Cohomology*, Chapter II, Section 5).

For a map $F \colon T_1 \to T_2$ of lattices with Galois action, write $\mathrm{col}(F)$ for the $O$-length of the finite cocycles of $T_2$ modulo the image of those of $T_1$ and the coboundaries, and $\lambda$ for the length of $O/(p)$.

**Theorem.** Let $D$ be a datum with Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$. Let $\ell$ be a prime, $K$ and $L$ finite extensions of $\mathbb{Q}_\ell$ with $(K, L)$ good, and $W$ the Wach module at $(K, L)$, with index set $\mathbb{Z}/n$. Take $d$, lattices $T_1, T_2$, a map $F$, integers $b(i)$, $S$, $\eta$, $m$ with the setting `SetCS`:

- `CaseA`, $\ell \ge 11$, $n$ even, $O$ a discrete valuation ring with fraction field $L$, and $L$ contains a primitive $\ell$-th root of unity;
- `Sur`, and the jumps of $T_1$ at $i$ lie in $[b(i), b(i)+S] \cup [-\eta, \eta]$ or in the mirror window, by the parity of $i + d$;
- the multiplicities of $T_2$ on $[-\eta, \eta]$ sum to at most $m$;
- $2a_R(\ell, H) + \eta + 1 \le b(i)$ and $H_0/2 \le b(i)$ for each $i$, where $H_0 = \max b + S$ and $H = H_0 + \eta$.

Then there is an integer $e$ with

$$e \le \frac{32H}{\ell^2} + 4S + \frac{10\eta}{\ell - 1} + 25\bigl(\log_\ell(2H) + 1\bigr),$$

$$\frac{\mathrm{col}(F)}{\lambda} \le (n+1)re + 4nme' + \tfrac32 n\Bigl(rS + 2m\bigl(\tfrac{H+1}{\ell-1} + 1\bigr)\Bigr),$$

and, if $m = 0$, $\ell^{e+3S}$ kills each finite cocycle of $T_2$ modulo the image of $T_1$ (`LiftF`). Here $r$ is the dimension of the $L$-space of $T_2$, $a_R$ is an explicit function, and $e'$ is a lift exponent that we have not unfolded.

## Proof

1. `localLifting_theoremC_hypotheses_admitted` gives the 19 admitted conditions with the constants $(10, 23, 32, 32)$. This is the only step that uses the three hypotheses.
2. `jumps_exact_adm`, `letterConditionGlobal_of_N1used`, `AdmHerrLocal.main`, `one_place_admissible_of_gap_constant_le` and `fontaine_fullFaithful_exact_psi` give the five inputs `adm23`, the letter condition, the Herr class condition, `adm22` and `LitFont`.
3. [`ramified_coefficient_chains_of_hypotheses`](/entry/ramified-coefficient-chains-of-hypotheses/) turns the five inputs into the implication "admitted implies the bound". Step 1 gives the premise.

## In the Lean code

The theorem is in [RamifiedCoefficientChainsPrvTwentyFive.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RamifiedCoefficientChainsPrvTwentyFive.lean#L17). The bound is `aux₃` and `ConclusionL` in [RamifiedCoefficientChains.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RamifiedCoefficientChains.lean#L322), with the setting `SetCS` at [line 60](lean:Formalism/SharpRestriction/LevelLetterCocycles/RamifiedCoefficientChains.lean#L60). Step 1 renames `TheoremCAdm.admissible_ranks_of_CMDatum` in [LocalLiftingTheoremCHypothesesAdmitted.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremCHypothesesAdmitted.lean#L22).

Odd points. `admissible_ranks_of_CMDatum` is about neither ranks nor CM data, and the name is used three times in the source. The fourth admitted condition is called `ArchimedeanSignatureMatching` ([line 342](lean:Formalism/SharpRestriction/LevelLetterCocycles/RamifiedCoefficientChains.lean#L342)), but it is a lattice lemma `lem3`. Unlike theorem B, the bound does not ask $K$ to be unramified.
