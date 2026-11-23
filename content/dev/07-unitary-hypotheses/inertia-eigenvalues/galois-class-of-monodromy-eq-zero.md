---
id: galois-class-of-monodromy-eq-zero
title: A Breuil-Kisin element with zero monodromy gives a crystalline class (statement)
kind: theorem
decl: GlobalTheory.T.galoisClass_of_monodromy_eq_zero
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.GaloisClassOfMonodromyEqZeroStatement
covers: 317
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`classOf_of_mon_eq_zero`](/entry/class-of-of-mon-eq-zero/). Step 5 of [`liftF_of_isGood`](/entry/lift-f-of-is-good/) calls it: an element of the Breuil-Kisin module of $T_1$ with zero monodromy gives a crystalline cocycle $\kappa_1 \in Z^1_f(T_1)$. The statement and its proof are in the entry for `classOf_of_mon_eq_zero`.

## Statement

The statement is word for word that of [`classOf_of_mon_eq_zero`](/entry/class-of-of-mon-eq-zero/). In short: assume `FontaineBcris` and standard period data. Let a pack datum with heights $\eta < H$ be tied to a lattice $T$ of $G_{\mathbb{Q}_\ell}$, with $8H + 1 < \ell$. Let $y$ be an element of the pack, fixed by the descent datum, with $E^\eta y \in M$ and monodromy $0$. If $\ell^c \zeta(y)$ lies in the divided power lattice $S\varphi^*M$, then some crystalline cocycle $\kappa_1 \in Z^1_f(T)$ is a class of $\ell^c y$.

## Proof

The proof is one line, `exact @GlobalTheory.BKGal.classOf_of_mon_eq_zero`. It passes all hypotheses along.

## In the Lean code

The theorem is in [GaloisClassOfMonodromyEqZeroStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GaloisClassOfMonodromyEqZeroStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `classOf_of_mon_eq_zero` in each slot, under `maxHeartbeats 1000000`.
