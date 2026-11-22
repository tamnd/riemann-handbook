---
id: exists-breuil-kisin-module-tame-descent-good-lattice
title: A tame Breuil-Kisin module for each good lattice (statement)
kind: theorem
decl: GlobalTheory.T.exists_breuilKisinModule_tameDescent_goodLattice
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsBreuilKisinModuleTameDescentGoodLatticeStatement
covers: 1018
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_pack_isOfType`](/entry/exists-pack-is-of-type/). [`liftF_of_isGood`](/entry/lift-f-of-is-good/) calls it three times in step 2 of its proof, once for each lattice of the short exact sequence $0 \to T_0 \to T_1 \to T_2 \to 0$. The real content is in the entry for `exists_pack_isOfType`.

## Statement

The statement is word for word the statement of [`exists_pack_isOfType`](/entry/exists-pack-is-of-type/). In short: assume `BhattScholzeCrystallineLattices` and `FontaineBcris`. Let $\ell \ne 2$ be a prime, $e + 1 = \ell^a$, and let the coefficient field $L$ contain the unramified extension of degree $a$ and a primitive $e$-th root of unity. Let the period rings be standard. Let $\eta, H \ge 0$, $\Sigma \subset \mathbb{Z}/e$ and $U \subset [-\eta, H]$ finite. Then each lattice $T$ of $G_{\mathbb{Q}_\ell}$ that is good for $(\Sigma, U)$ has a Breuil-Kisin pack with heights $(\eta, H)$ whose descent characters lie in $\Sigma$ and whose jumps lie in $U$.

## Proof

The proof is one line: `exact @GlobalTheory.BKGal.exists_pack_isOfType`. It passes all hypotheses along.

## In the Lean code

The theorem is in [ExistsBreuilKisinModuleTameDescentGoodLatticeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBreuilKisinModuleTameDescentGoodLatticeStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `exists_pack_isOfType` in each slot. The theorem has two direct users: `liftF_of_isGood` and `BKGal.ExtClass.main`, the proof of `crystalline_class_from_monodromy_kernel_element`, which `liftF_of_isGood` also calls.
