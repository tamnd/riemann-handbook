---
id: twisted-place-bound-closing
title: The congruence bound at the twisted places from local duality
kind: theorem
decl: GlobalTheory.TwistedPlaceBound.closing
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TwistedPlaceSelmerLengthBoundOfLocalDuality
covers: 1269
status: drafted
drafted_by: writer@claude
---
This theorem bounds the length of the congruence module at the twisted places over the two auxiliary primes $q$ and $d$. It proves five inputs of the bound from four literature hypotheses. Its user is its [second name](/entry/twisted-place-selmer-length-bound-of-local-duality/), which [the bound at the primes q and d from the setup](/entry/theorem-bqd-main-alt-alt/) calls.

## Statement

Let $D$ be a datum with CM field $E$, auxiliary primes $q$ and $d$, local data $HW$, $F$, $Cm$, and size parameters $f$, $r$, $t$, $m$, $b$, $S$, $\eta$, $x$, $C_t$. Let $\sigma$ and $\rho$ (`r` and `ρ` in Lean) be families of representations of $G_E$ over the rings $\mathcal{O}_i$ at the places $i$ of $D$.

**Theorem.** Assume global Artin reciprocity, `BlochKatoLocal`, local Tate duality and the local Euler characteristic formula. Let $C \ge 2080$, and let $Q$ be a polynomial with $260 f^2 t^2 (r + t) \le Q(f, r, t)$ for all $f, r, t$. Assume thirteen conditions on $\sigma$, $\rho$ and the size data, among them Hodge-Tate windows at $q$ and $d$, tame generators, and $S + \eta + t + 2 \le b$. Then:

1. For each place $w$ of $E$ over $\ell \in \{q, d\}$, $K_w = K_0(\sqrt{-\ell})$ with $K_0$ its maximal unramified subfield, $[K_w : K_0] = 2$, and a degree formula holds for a field $K_s \supseteq K_w$.
2. $q \equiv d \equiv 3 \pmod 4$. Each place of $E$ over $q$ or $d$ has ramification index 2 and is not fixed by complex conjugation. At $q$ the decomposition group preserves the CM type. At $d$ each nontrivial element of inertia sends the CM type to its complement.
3. Let $i$ be a twisted place over $\ell \in \{q, d\}$ with $x^{2C_t + 5} < \ell$. Let $\pi$ be a good parameter at $i$ that meets the Selmer condition `sFin`, and assume the Sha lengths for $0 < e < t$ are finite. Then
$$v_{cc}(\pi) \le C f \bigl( r(b/\ell + S + t + \eta + \log b) + m b \bigr) + Q(f, r, t) \log b + \sum_{0 < e < t} \mathrm{sha}(\ell, e) + v_\ell(h_E) + s(\pi) + \ell^{-2}.$$
Here $v_{cc}(\pi)$ is the normalized length of $\mathcal{O}/\mathfrak{c}(\pi)$ for a congruence ideal $\mathfrak{c}(\pi)$, and $s(\pi)$ is the length of a Selmer group.

## Proof

Parts 1 and 2 are `T.local_fields_at_auxiliary_primes D`, which has no hypotheses. The user takes only part 3.

Part 3 is `T.theoremB_of_admittedHypotheses` with the local constant 160. It needs $13 \cdot 160 \le C$, that is $C \ge 2080$. The proof supplies five of its inputs and passes the other hypotheses unchanged:

- `admW`, from `T.wachHypothesis_crystallineLattices`, `T.wachModuleLocalConclusions_usedForms` and `crysOnCond_all`;
- `admA 160`, from [the local colength bound](/entry/local-lifting-of-bloch-kato-tate-duality-euler-char/);
- `admTB`, from `T.theorem_tb_of_local_blochKato_duality_euler`;
- `admBK`, from `T.blochKatoLocal_all_of_tateDuality_eulerChar`;
- the literature inputs at $q$ and $d$, from the tame generator hypothesis, `T.blochKatoDim_at_auxiliary_prime_places`, `TateTop.tateH2_of_duality_loc`, `T.integral_tate_H2_top`, `FontaineAdm.fontaineProperties_all_places`, `BridgeTie.localCoefficientCompatibility` and `T.unramifiedClassFieldBound_of_artin`.

## In the Lean code

The theorem is in [TwistedPlaceSelmerLengthBoundOfLocalDuality.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedPlaceSelmerLengthBoundOfLocalDuality.lean#L28). The conclusions are in [EmbeddingTypeJumps.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/EmbeddingTypeJumps.lean#L65). We have not unfolded the thirteen conditions, the field $K_s$, or `theoremB_of_admittedHypotheses`.

- Artin reciprocity is used only in `unramifiedClassFieldBound_of_artin`.
- The name says "Selmer length bound", but part 3 bounds the congruence length. The Selmer length $s(\pi)$ is a term on the right.
- The finiteness hypothesis is on `GaloisCohomology.shaLen` of the local data. The sum in the bound uses `D.what₂.shaLen`, a field $\mathbb{N} \to \mathbb{N} \to \mathbb{Q}$ of [DataRows.lean](lean:Formalism/LocalRingCardinality/DataRows.lean#L166) whose only stated property there is $\ge 0$. We found nothing that ties the two.
