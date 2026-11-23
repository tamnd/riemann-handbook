---
id: act-sieg-exists-rep
title: Principal Siegel objects with an action of an order have a fine moduli scheme
kind: theorem
decl: GlobalTheory.ActSieg.exists_rep
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsRepPrincipalSiegelAdjointOrderAction
covers: 567
status: drafted
drafted_by: writer@claude
---
This theorem builds a quasi-projective moduli scheme for principal Siegel objects with an action of a ring $O$ compatible with the polarization. It is step 2 of [the representability of Siegel moduli with kernel killed by $d$](/entry/sd-rep-of-coprime/), where $O$ comes from the trick of step 1. [Its statement form](/entry/exists-rep-principal-siegel-adjoint-order-action/) repeats it.

## Statement

Use $B_M = \mathbb{Z}[\zeta_M, 1/M]$ and the Siegel objects $(A, P, \lambda)$ of genus $h$ and level $M$ from [the parent entry](/entry/sd-rep-of-coprime/), and the principal ones. An *$O$-action* on $A/S$ (`IsRAct`) is a map $o \mapsto [o]$ from $O$ to group endomorphisms of $A$ with $[1] = \mathrm{id}$, $[a + b] = [a] + [b]$ and $[ab] = [b] \circ [a]$, so a right action. It is *adjoint* for an additive map $\bar{\ } \colon O \to O$ (`Adj`) if $([a] \times 1)^* P \cong (1 \times [\bar a])^* P$ for each $a \in O$.

**Theorem.** Let $h \geq 1$ and $M \geq 3$ odd. Let $O$ be a ring with an additive map $\bar{\ }$, generators $e_1, \dots, e_r$ of $O$ as an abelian group, an integer matrix $W$ with $W + W^{\mathsf{T}}$ positive definite, and $d_0 > 0$ with $\sum_{i,j} W_{ij} e_j \bar e_i = d_0$. Then there is a scheme $H$, quasi-projective over $B_M$ and locally noetherian, with a principal Siegel object $z_H$ and an adjoint $O$-action on it, such that each principal Siegel object $z$ over $S$ with an adjoint $O$-action is the pullback of $z_H$, with its level structure, line bundle (up to isomorphism) and action, along a unique $g \colon S \to H$ over $B_M$ (`ActPB`).

## Proof

1. `exists_sFam_cycAway` gives a Siegel family $F$: a smooth quasi-projective $X$ over $B_M$ with a universal principal object.
2. $B_M$ is a Dedekind domain (`isDedekindDomain_cycAway`), so $X$ is locally noetherian.
3. `adjointActions_order_finite_unramified_scheme` gives a finite map $\pi \colon H \to X$ that represents adjoint $O$-actions on pullbacks of the universal abelian scheme (the structure `ActRep`). The hypotheses on $O$, $W$ and $d_0$ are used only here.
4. $H$ is quasi-projective over $B_M$, since $\pi$ is finite and $B_M$ is noetherian. The pullback $z_H$ of the universal object to $H$ is principal (`siegPre_pullback`).
5. *Existence.* Given $(S, z, [\cdot])$, [the classification by the Siegel family](/entry/siegel-family-exists-unique-classify-scheme/) gives a unique $f \colon S \to X$ along which the universal object pulls back to $z$. `adj_of_lbIso` moves adjointness along the isomorphism of line bundles. Then `ActRep.rep` gives a unique $g \colon S \to H$ over $f$ that matches the actions.
6. *Uniqueness.* For another $g'$, the uniqueness of $f$ gives $\pi \circ g' = f$. The rigidity lemma `SiegRigid.eq_of_sRelBy` (level $M \geq 3$, $M$ odd) shows that the two maps of abelian schemes over $f$ are equal. Then the uniqueness in `ActRep.rep` gives $g' = g$.

The rest is bookkeeping with squares of pullbacks.

## In the Lean code

The theorem is in [ExistsRepPrincipalSiegelAdjointOrderAction.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRepPrincipalSiegelAdjointOrderAction.lean#L119). `IsRAct`, `Adj` and `ActRep` are in [ToRingActOpOfRingAct.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRingActOpOfRingAct.lean#L15), `ActPB` in [IsQProjOverCompImmersion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsQProjOverCompImmersion.lean#L15), and `SFam` in [IsSeparatedOfIsQProjOver.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSeparatedOfIsQProjOver.lean#L18). The pullback $z_H$ is `onPull`, in the same file.

Step 3 also gives that $\pi$ is formally unramified; the proof drops this. We have not opened the proof of step 3 or of the rigidity lemma. The map $\bar{\ }$ is only assumed additive; it need not be an involution or reverse products. The action is a right action: `IsRAct` asks `act (a * b) = act a ≫ act b`, and `≫` is composition in diagram order.
