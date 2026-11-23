---
id: enlarge-good
title: The base can be enlarged until the torsor is good
kind: theorem
decl: GlobalTheory.KeyOriginEnlarge.enlarge_good
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.StrictHenselisationEnlargeGoodAtOrigin
covers: 466
status: drafted
drafted_by: writer@claude
---
This theorem replaces the noetherian base of a cyclic torsor by a larger one until the torsor is good. It is restated as [the good enlargement](/entry/strict-henselisation-enlarge-good-at-origin/), which is step 1 of [the torsor point over a noetherian normal model](/entry/torsor-point-of-ess-finite-type/). The proof composes three enlargement lemmas, and each adds one property.

## Statement

Take $T$, $\varphi \colon T[X]_P \to O$, $q$ and the data $(A, i, E_A, Q_A, j_A, \psi_A, D_A)$ with $R = (E_A)_{Q_A}$ as in [the torsor point theorem](/entry/torsor-point-of-ess-finite-type/).

**Theorem.** There are:

1. a noetherian, integrally closed local domain $A'$, essentially of finite type over $\mathbb{Z}$, with $q$ a unit in $A'$, an étale $A'[X]$-algebra $E_A'$ and a prime $Q_A'$ of $E_A'$ over $(\mathfrak{m}_{A'}, X)$; put $R' = (E_A')_{Q_A'}$;
2. a retraction $\rho' \colon R' \to A'$ of $A' \to R'$ with kernel $(X)$;
3. ring maps $j_A' \colon R' \to O$ and $\psi_A' \colon R'_K \to O_K$, where $\psi_A'$ extends $j_A'$;
4. a $\mathbb{Z}/q$-torsor $D_A'$ over $R'_K$ that is good for $\rho'$;
5. ring maps $\beta \colon R_K \to R'_K$ and $h \colon D_A \to D_A'$ with $\psi_A' \circ \beta = \psi_A$ and $h$ over $\beta$.

*Good* is defined in [the torsor point theorem](/entry/torsor-point-of-ess-finite-type/): the integral closure of $R'$ in $D_A'$ is étale over $R'$ above the primes of height at most 1 of $A'$, and it has a ring map to $\operatorname{Frac}(A')$ over $\rho'$.

## Proof

Call the data *fitting* if they satisfy the conditions of the torsor point theorem on $i$, $q$, $Q_A$, $j_A$, $\psi_A$ and $D_A$ (the predicate `Fits`). Each step below takes fitting data and returns fitting data with maps $\beta_k$, $h_k$ as in item 5.

1. `enlarge_strictHenselisation_retract_mod` adds a retraction $\rho_1 \colon R_1 \to A_1$ with kernel $(X)$, such that $i_1(\rho_1(x)) - j_1(x) \in X \cdot O$ for all $x \in R_1$ (the predicate `Retracts`).
2. `enlarge_base_separable_point_integralClosure` keeps `Retracts` and adds the second half of goodness: a ring map from the integral closure to $\operatorname{Frac}(A_2)$ over $\rho_2$ (the predicate `PointAtZero`).
3. [`etale_enlarge_by_uniformiser_roots`](/entry/etale-enlarge-by-uniformiser-roots/) keeps `Retracts` and makes the torsor good.

The result is the last data, with $\beta = \beta_3 \circ \beta_2 \circ \beta_1$ and $h = h_3 \circ h_2 \circ h_1$. The rest is bookkeeping.

## In the Lean code

The theorem is in [StrictHenselisationEnlargeGoodAtOrigin.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/StrictHenselisationEnlargeGoodAtOrigin.lean#L14). `Fits`, `Retracts` and `PointAtZero` are in [PointAtZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PointAtZero.lean#L12). The lemmas it calls are aliases of `KeyOriginEnlarge.enlarge_retract`, `KeyOriginEnlargePoint.enlarge_point` and `KeyOriginEnlarge.etale_enlarge`. We have not opened their proofs.

The conclusion forgets some of what the proof has. It does not keep the map $i_3 \colon A_3 \to T$, the condition that $i_3$ is injective and local, the compatibility of $j_A'$ with $A'[X] \to T[X] \to O$, or the congruence modulo $X$ in `Retracts`. The hypotheses on $T$, $P$ and $\varphi$ are only passed to the three lemmas.

The statement of the first lemma has a conjunct `Retracts ... ∧ True`, and the proof discards the `True`.
