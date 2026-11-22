---
id: exists-zarhin-data-sieg-ker-by
title: Zarhin data for Siegel objects of kernel d
kind: theorem
decl: GlobalTheory.UPel.HT.exists_zarhin_data_siegKerBy
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsZarhinTrickFamilySiegelKernelKilled
covers: 352
status: drafted
drafted_by: writer@claude
---
This theorem gives step 1 of [the representability of Siegel moduli with kernel killed by $d$](/entry/sd-rep-of-coprime/): an explicit ring $O$ of matrices, and three lemmas. [Its statement form](/entry/exists-zarhin-trick-family-siegel-kernel-killed/) repeats it.

## Statement

Siegel objects, "of kernel $d$" and "principal" are as in [that entry](/entry/sd-rep-of-coprime/). Write $\lambda_c$ for the level structure of $c$. A *right action* of $O$ on an abelian scheme $A$ is a map $\alpha \colon O \to \operatorname{End}(A)$ with $\alpha(1) = 1$, $\alpha(a + b) = \alpha(a) + \alpha(b)$ and $\alpha(ab) = \alpha(b) \circ \alpha(a)$. It is *adjoint to* $a \mapsto \bar a$ for a bundle $P$ on $A \times A$ if $(\alpha(a) \times 1)^* P \cong (1 \times \alpha(\bar a))^* P$ for all $a$.

**Theorem.** Let $h \geq 1$, $M \geq 3$ odd, $d \geq 1$, $\gcd(M, d) = 1$. Then there are a ring $O$ with an additive map $a \mapsto \bar a$, a $\mathbb{Z}$-spanning family $b_1, \dots, b_r$, an integer matrix $W$ with $W + W^{\mathsf T}$ positive definite, an integer $d_0 > 0$ with $\sum_{i,j} W_{ij}\, b_j \bar b_i = d_0$, an idempotent $e$, a homomorphism $j \colon \mathbb{Z}^{2h} \to \mathbb{Z}^{16h}$, elements $o_1, \dots, o_m \in O$ and homomorphisms $\kappa_1, \dots, \kappa_m \colon \mathbb{Z}^{16h} \to \mathbb{Z}^{2h}$, as follows. Let $c$ be an object of genus $h$, level $M$ and kernel $d$ over $S$, a scheme over $B_M = \mathbb{Z}[\zeta_M, 1/M]$ on which $d$ is a unit.

1. There are a principal object $z$ of genus $8h$ over $S$ and a right action $\alpha$ of $O$ on $A_z$, adjoint to the bar map for the bundle of $z$, and homomorphisms $\iota \colon A_c \to A_z$ and $p \colon A_z \to A_c$ such that $p \circ \iota = 1$, $\iota \circ p = \alpha(e)$, the bundle of $c$ is $(\iota \times \iota)^*$ of that of $z$, $\iota \circ \lambda_c = \lambda_z \circ j$, and $\lambda_z(a) = \sum_k \alpha(o_k)\, \iota\, \lambda_c(\kappa_k a)$.
2. Two such pairs $(z, \alpha)$ for $c$ are isomorphic over $S$, compatibly with bundles, levels and actions.

## Proof

Four squares (Lagrange) for $d - 1$ give an integer $4 \times 4$ matrix $Q$ with $Q^{\mathsf T} Q = Q Q^{\mathsf T} = (d - 1)\, I$. These are inverse:

$$\Phi = \begin{pmatrix} I & Q^{\mathsf T} \\ Q & dI \end{pmatrix}, \qquad \Phi^{-1} = \begin{pmatrix} dI & -Q^{\mathsf T} \\ -Q & I \end{pmatrix}.$$

$O$ is the ring of $8 \times 8$ integer matrices, in $4 + 4$ blocks, with lower left block divisible by $d$. The bar map is $N \mapsto \Phi N^{\mathsf T} \Phi^{-1}$, and $e = E_{11}$.

Then `GlobalTheory.T.exists_zarhin_order_spanning_family_posDef_matrix` gives $b_i$, $W$, $d_0$; `GlobalTheory.T.exists_principal_zarhin_object_of_siegKerBy` gives $j$, $o_k$, $\kappa_k$ and clause 1; `GlobalTheory.T.zarhinTrick_principal_objects_iso_unique` gives clause 2.

The genus $8h$ and $Q$ match Zarhin's trick, a principal polarization on $(A \times A^\vee)^4$ (Zarhin, Math. Notes 21 (1977), 415 to 419). We have not opened the construction of $z$ to check that $A_z$ is this product.

## In the Lean code

The theorem is in [ExistsZarhinTrickFamilySiegelKernelKilled.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsZarhinTrickFamilySiegelKernelKilled.lean#L11). `GlobalTheory.ZarhinFam.ord d`, `quat`, `form` ($\Phi$), `formInv`, `bar` and `idem` are in [FormMulTransposeMulFormInvMem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FormMulTransposeMulFormInvMem.lean#L42). `IsRAct` and `Adj` are in [ToRingActOpOfRingAct.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRingActOpOfRingAct.lean#L15). Clauses 1 and 2 are `ZRel` and `ActPB`, in [IsQProjOverCompImmersion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsQProjOverCompImmersion.lean#L15). We have not opened the three proofs.

The statement asks only that the bar map be additive; since $\Phi$ is symmetric, it is an involution that reverses products. The uniqueness lemma holds for all $j$, $o_k$, $\kappa_k$, not only those of step 2.
