---
id: lift-surjection-good-crystalline-lattices
title: Lifting crystalline classes along a surjection of good lattices (statement)
kind: theorem
decl: GlobalTheory.T.lift_surjection_good_crystalline_lattices
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LiftSurjectionGoodCrystallineLatticesStatement
covers: 2790
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`liftF_of_isGood`](/entry/lift-f-of-is-good/). [`TheoremTClosing.main`](/entry/theorem-tclosing-main/) calls it in step 5 of its proof, after it has made the two lattices good. The real content is in the entry for `liftF_of_isGood`.

## Statement

The statement is word for word the statement of [`liftF_of_isGood`](/entry/lift-f-of-is-good/). In short: assume `BhattScholzeCrystallineLattices` and `FontaineBcris`. Let $\ell$ be a prime, $e + 1 = \ell^a$, and let the coefficient field $L$ contain the unramified extension of degree $a$ and a primitive $e$-th root of unity. Let $N, \eta, H, \Sigma \subset \mathbb{Z}/e$ and $U \subset \mathbb{Z}$ satisfy the numerical conditions `Numerics`, which include $40(HN^2 + N^3) < \ell$. Let $g \colon T_1 \to T_2$ be a map of lattices of $G_{\mathbb{Q}_\ell}$ onto $T_2$, with $T_1$ and $T_2$ good for $(\Sigma, U)$. Then

$$\ell^{\,7(Nr + \eta(N + r))} Z^1_f(T_2) \subset g_* Z^1_f(T_1) + B^1(T_2),$$

where $r$ is the largest Frobenius period of a difference of two elements of $\Sigma$.

## Proof

The proof is one line: `exact @GlobalTheory.TheoremT.liftF_of_isGood`. It passes all hypotheses along.

## In the Lean code

The theorem is in [LiftSurjectionGoodCrystallineLatticesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftSurjectionGoodCrystallineLatticesStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `liftF_of_isGood` in each slot; the first branch closes the goal. The pair of a "Statement" file and a proof file is a pattern of this folder: the statement is stated twice, once in each file.
