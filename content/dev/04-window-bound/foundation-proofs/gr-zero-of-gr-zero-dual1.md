---
id: gr-zero-of-gr-zero-dual1
title: The ordinary Selmer group vanishes if the dual one does
kind: theorem
decl: GlobalTheory.Ord2.grZero_of_grZero_dual1
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinarySelmerVanishesOfDualVanishes
covers: 349
status: drafted
drafted_by: writer@claude
---
This theorem passes the vanishing of an ordinary Selmer group from the Tate dual $W^*$ of a two-dimensional representation $W$ back to $W$. Under the name [`ordinarySelmer_vanishes_of_dual_vanishes`](/entry/ordinary-selmer-vanishes-of-dual-vanishes/) it is the third step of [`es_vanish`](/entry/es-vanish/).

## Statement

Let $\ell$, $e$, $S$, $A$ and $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ satisfy the normal form $\mathrm{Nf}(e, S, A, W)$, as in [the unramified zeta theorem](/entry/zeta-ur/). In particular $\ell$ is odd and $W$ is upper triangular on the [[decomposition group|7X92G8CQ33]] $D_A$ of the place $A$ above $\ell$. Let $W^* = W \otimes \bar\chi\,(\det W)^{-1}$, where $\bar\chi$ is the [[cyclotomic character|XSGB5K2KEG]]. Since $W^\vee \cong W \otimes (\det W)^{-1}$ in dimension two, $W^*$ is the Tate dual $W^\vee(1)$.

For a continuous cocycle $c \colon G_\mathbb{Q} \to \overline{\mathbb{Q}}_\ell^2$ of $W$:

- $c$ is *unramified* ($\mathrm{Unr}$) if for each prime $w \neq \ell$ there is a place over $w$ on whose inertia group $c$ is a coboundary;
- $c$ is *ordinary at $A$* ($\mathrm{Gr}$) if there is $x$ with $c(s)_2 = W(s)_{22}\,x - x$ for all $s \in D_A$: the image of $c$ in $H^1$ of $D_A$ with values in the quotient line is zero.

$\mathrm{GrZero}(W, A)$ says: every continuous cocycle of $W$ that is unramified and ordinary at $A$ is a coboundary. This is the vanishing of an ordinary Selmer group. The condition is on all of $D_A$, not only on inertia.

**Theorem.** Assume $\mathrm{LitCoh}$, the twelve literature statements on Galois cohomology (Poitou-Tate, local Tate duality, Euler characteristics, Greenberg-Wiles and others). If $\mathrm{Nf}(e, S, A, W)$ and $\mathrm{GrZero}(W^*, A)$ hold, then $\mathrm{GrZero}(W, A)$ holds.

## Proof

Suppose that $\mathrm{GrZero}(W, A)$ fails.

1. `exists_dualSelmer_classes_unbounded_order` gives a coefficient ring $\mathcal{O}$ that contains the entries of $W$ and, for each $m$, a level $n$ and a cocycle $z$ of $W^*$ modulo $\ell^n$ with values in $\mathcal{O}^2$. This $z$ is trivial on the kernel of $G_\mathbb{Q} \to G_S$, a coboundary modulo $\ell^n$ on inertia at each $q \in S$ prime to $\ell$, ordinary at $A$ modulo $\ell^n$, and $\ell^m z$ is not a coboundary modulo $\ell^n$.
2. `dualSelmer_unbounded_order_nonzero_ordinaryClass` turns this family into a failure of $\mathrm{GrZero}(W^*, A)$. This contradicts the hypothesis.

The first lemma scales the class of $W$ to be integral and then uses `greenbergWiles_dualSelmer_lower_bound_mod_prime_pow` with two bounds on sizes of Selmer groups modulo $\ell^m$. The name points to the Greenberg-Wiles formula (A. Wiles, Ann. of Math. 141 (1995), Proposition 1.6). We have not unfolded these bounds, nor the proof of the second lemma.

## In the Lean code

The theorem is at [line 10 of OrdinarySelmerVanishesOfDualVanishes.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OrdinarySelmerVanishesOfDualVanishes.lean#L10). $\mathrm{Unr}$, $\mathrm{Gr}$, $\mathrm{GrZero}$ and $W^*$ (`dual1`) are in [FinalTheorems.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/FinalTheorems.lean#L68).

- `GlobalTheory.T.exists_dualSelmer_classes_unbounded_order`, equal to `GwCount.dual_classes_unbounded` in [ExistsDualSelmerClassesUnboundedOrder.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsDualSelmerClassesUnboundedOrder.lean#L16).
- `GlobalTheory.T.dualSelmer_unbounded_order_nonzero_ordinaryClass`, equal to `gw_limit` in [DualSelmerUnboundedOrderNonzeroOrdinaryClass.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/DualSelmerUnboundedOrderNonzeroOrdinaryClass.lean#L22).

The proof body is four lines. Both lemmas use $\mathrm{LitCoh}$.
