---
id: act-rep-finite-unramified
title: Adjoint actions of an order are represented by a finite unramified scheme
kind: theorem
decl: GlobalTheory.EndLoc.actRep_finite_unramified
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AdjointActionsOrderFiniteUnramifiedScheme
covers: 603
status: drafted
drafted_by: writer@claude
---
This theorem proves [its statement form](/entry/adjoint-actions-order-finite-unramified-scheme/). It says that the actions of a ring $O$ on an abelian scheme that are adjoint for a line bundle $Q$ form a scheme that is [[finite|N9C4X7XKE4]] and [[formally unramified|1JQX6HD8E5]] over the base. The statement form is used twice, both times on a Siegel family: in `GlobalTheory.UPel.HT.exists_finite_rep_oActN_rosati`, for the order of a PEL datum, and in [the Siegel action entry](/entry/act-sieg-exists-rep/), for a general $O$. Both callers use only the finiteness.

## Statement

Let $S$ be a locally noetherian scheme and $A \to S$ an abelian scheme (smooth, proper, with geometrically connected fibres, commutative). Let $Q$ be a line bundle on $A \times_S A$ with these properties:

- $Q$ is trivial on $\{0\} \times A$ and on $A \times \{0\}$;
- $Q \cong s^*Q$, where $s$ swaps the factors;
- $\Delta^*Q$ is relatively ample over $S$ (the Lean predicate `Out.RelAmple`, stated with sections of a power over each affine open of $S$).

Let $O$ be a ring, not necessarily commutative, and $a \mapsto \bar a$ an additive map $O \to O$. Let $e_1, \dots, e_r$ generate $O$ as an abelian group. Let $W \in M_r(\mathbb{Z})$ with $W + W^{\mathsf T}$ positive definite, and let $d > 0$ with $\sum_{i,j} W_{ij}\, e_j \bar e_i = d$ in $O$.

For $T \to S$, an *adjoint action* on $A_T$ is a map $\alpha \colon O \to \operatorname{End}(A_T)$ into homomorphisms with $\alpha(1) = 1$, $\alpha(a+b) = \alpha(a) + \alpha(b)$, $\alpha(ab) = \alpha(b) \circ \alpha(a)$ (a right action), and $(\alpha(a) \times 1)^*Q_T \cong (1 \times \alpha(\bar a))^*Q_T$ for each $a$.

**Theorem.** There is a scheme $H$ with $\pi \colon H \to S$ and an adjoint action on $A_H$ that is universal: for each $T \to S$ and each adjoint action on $A_T$, there is a unique $S$-map $h \colon T \to H$ such that $A_T \cong h^*A_H$ carries the given action to the universal one. The map $\pi$ is finite and formally unramified.

## Proof

1. [The finiteness entry](/entry/exists-finite-scheme-adjoint-actions-abelian/) gives a universal $H$ with $\pi$ finite.
2. `GlobalTheory.T.formallyUnramified_adjointRingAction_scheme` says that $\pi$ is formally unramified for every representing object of this kind. It needs only that $A$ is an abelian scheme.

## In the Lean code

The theorem is in [AdjointActionsOrderFiniteUnramifiedScheme.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AdjointActionsOrderFiniteUnramifiedScheme.lean#L12). The representing object is the structure `ActRep A Q bar` in [ToRingActOpOfRingAct.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRingActOpOfRingAct.lean#L22), and the adjoint action is the pair `IsRAct`, `Adj` in the same file. The lemmas it calls:

- `GlobalTheory.T.exists_finite_scheme_adjoint_actions_abelian`;
- `GlobalTheory.T.formallyUnramified_adjointRingAction_scheme`, whose proof we have not opened.

The universal property of `ActRep` asks for uniqueness of $h$ only, not of the isomorphism $A_T \cong h^*A_H$. The map `bar` need only be additive: it is not asked to be an involution or anti-multiplicative. In `exists_finite_rep_oActN_rosati`, $O$ is the opposite ring of the order, so the right action is a left action of the order, and `exists_spanning_posDef_relation_harrisTaylorOrder` supplies $e$, $W$ and $d$. The abelian scheme hypothesis contains commutativity, which the statement also takes as a separate instance.
