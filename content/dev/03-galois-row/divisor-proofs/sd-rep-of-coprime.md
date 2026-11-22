---
id: sd-rep-of-coprime
title: Siegel moduli with polarization kernel killed by d are representable
kind: theorem
decl: GlobalTheory.UPel.HT.sdRep_of_coprime
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelKernelBoundedRepresentableOfCoprime
covers: 1048
status: drafted
drafted_by: writer@claude
---
This theorem proves that abelian schemes with a symmetric rigidified line bundle whose polarization kernel is killed by $d$, and with a symplectic level $M$ structure, have a quasi-projective fine moduli scheme. It reduces this to the principally polarized case with an action of an order. [Its statement form](/entry/siegel-kernel-bounded-representable-of-coprime/) repeats it for [the quasi-projective representing family](/entry/exists-rep-fam-qproj/).

## Statement

Let $B_M = \mathbb{Z}[\zeta_M, 1/M] \subset \mathbb{C}$ with $\zeta_M = e^{2\pi i/M}$. For $s \colon S \to \operatorname{Spec} B_M$, a *Siegel object* of genus $h$ and level $M$ is:

- an abelian scheme $A/S$ and a line bundle $P$ on $A \times_S A$, trivial along $0 \times A$ and $A \times 0$ and symmetric under the swap;
- an additive map $\lambda \colon \mathbb{Z}^{2h} \to A(S)$ with $M\lambda = 0$, such that at each geometric point $\lambda$ has kernel $M\mathbb{Z}^{2h}$ and image $A[M]$, and the Weil pairing of $\Delta^*P$ on $\lambda(a), \lambda(b)$ is $\zeta_M^{2\omega(a,b)}$, with $\omega$ the standard symplectic form.

The object is *of kernel $d$* if $\Delta^*P$ is relatively ample and each point $x$ with $(x, \mathrm{id})^*P$ trivial has $dx = 0$. It is *principal* if each such $x$ is $0$.

**Theorem.** Let $h \geq 1$, $M \geq 3$ odd, $d \geq 1$ and $\gcd(M, d) = 1$. Then there is a scheme $X$, quasi-projective over $B_M$ with $d$ a unit on $X$, and a Siegel object $u$ of kernel $d$ over $X$, such that each Siegel object of kernel $d$ over $S$, with $d$ a unit on $S$, is the pullback of $u$ along a unique $S \to X$.

## Proof

1. `exists_zarhinTrick_family_siegel_kernelKilled` gives a ring $O$ with an additive map $\bar{\ }$, a positive form $W$ with $\sum W_{ij} e_j \bar e_i = d_0 > 0$, an idempotent $e \in O$, and linear maps between $\mathbb{Z}^{2h}$ and $\mathbb{Z}^{16h}$. Each Siegel object $c$ of kernel $d$ is the $e$-part of a principal object $z$ of genus $8h$ with a compatible $O$-action, and $z$ is unique up to isomorphism.
2. `exists_rep_principalSiegel_adjoint_orderAction` gives a quasi-projective, locally noetherian $H$ that represents principal objects of genus $8h$ with such an $O$-action.
3. `siegel_family_idempotent_image_open_locus` gives a quasi-compact immersion $j \colon Y \to H$ and an object $c$ of kernel $d$ over $Y$ that represents the pairs ($g \colon T \to H$, an object of kernel $d$ on $T$ that is the $e$-part of the pullback of the universal object). So $Y$ is quasi-projective over $B_M$.
4. By steps 1 to 3, $Y$ and $c$ have the universal property. The rest is bookkeeping.

The name of step 1 refers to Zarhin's trick: $(A \times A^\vee)^4$ has a principal polarization (Zarhin, Math. Notes 21 (1977), 415 to 419). The genus $8h = 4 \cdot 2h$ matches. We have not opened its proof, so we do not claim that it uses this construction.

## In the Lean code

The theorem is in [SiegelKernelBoundedRepresentableOfCoprime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelKernelBoundedRepresentableOfCoprime.lean#L14). `SDRep` is in [TwoLeFinrankLa.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwoLeFinrankLa.lean#L32), `SiegPre` in [Clauses.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/Clauses.lean#L16), and `ActPB`, `ZRel` and `isQProjOver_comp_immersion` in [IsQProjOverCompImmersion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsQProjOverCompImmersion.lean#L15). The three lemmas are statement forms; we have not opened their proofs, and we have not unfolded `IsRAct` and `Adj`.

The Weil pairing has the factor 2. We read it as the pairing of $\Delta^*P$, which gives twice the polarization of $P$; we have not unfolded `Out.WeilIs` to check this. Since $M$ is odd, $\zeta_M^2$ is still primitive. In step 1 the conditions on $O$, $W$ and $e$ are weak: the content is in the two clauses on existence and uniqueness of $z$.
