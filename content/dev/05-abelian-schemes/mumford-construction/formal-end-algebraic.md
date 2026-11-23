---
id: formal-end-algebraic
title: Formal endomorphisms of a Mumford uniformization are algebraic
kind: theorem
decl: GlobalTheory.Mum.formalEnd_algebraic
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MumfordFormalEndomorphismAlgebraic
covers: 379
status: drafted
drafted_by: writer@claude
---
This theorem algebraizes a compatible family of endomorphisms of the thickenings of a uniformized semi-abelian scheme. The second name [mumford_formalEndomorphism_algebraic](/entry/mumford-formal-endomorphism-algebraic/) passes it on. It lies below [EveryCharacter from the literature](/step/every-character-of-literature/). The proof goes through the generic fibre: the formal endomorphism moves ratios of sections, these ratios define an endomorphism of the generic fibre, and that endomorphism extends over $R$.

## Statement

The data follow Mumford's construction of degenerating abelian varieties (D. Mumford, Compositio Math. 24, 1972; G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, 1990).

- $R$ is a local domain with `Base R`: noetherian, integrally closed, complete for its maximal ideal $\mathfrak m$, and of characteristic $0$. $K$ is its fraction field, and $G_e = G \times_R R/\mathfrak m^{e+1}$.
- $D$ (`DegData`) is a polarized abelian scheme $B$ over $R$ with a rigidified cubical line bundle $L$, a free abelian group $X$ of finite rank, a homomorphism $c \colon X \to B(R)$, and trivializations $\psi(\chi)$ of $c(\chi)^* L^{-1}$ over $K$. The conditions: $\psi$ is even, the associated $\tau$ is bimultiplicative, $\psi(\chi) \in \mathfrak m$ for $\chi \neq 0$, and for each $n$ only finitely many $\psi(\chi)$ lie outside $\mathfrak m^n$.
- $U$ (`Unif`) says that $G$ is smooth and separated, that $G_K \cong A$, and that each $G_e$ is an extension of $B_e$ by the split torus with character group $X$, compatible in $e$ and with the line bundles. It also asks that sections of $L^k$ match families of Fourier coefficients (`ExpBij`). We have not unfolded that field.
- `EndData D a a' h h'`: $a, a'$ are endomorphisms of $B$, $a'$ is the Rosati adjoint of $a$ for $L$, $c \circ h = a \circ c$, $c \circ h' = a' \circ c$, and $\tau$ is balanced (`TauBal`).
- `FormalEnd U a h' b`: each $b_e$ is a group endomorphism of $G_e$, the $b_e$ are compatible with $G_e \to G_{e+1}$, $b_e$ lies over $a$ on $B_e$, and on the torus $b_e$ acts on characters by $h'$.

**Theorem.** If $G$ is commutative and semi-abelian, then there is a group endomorphism $g$ of $G$ with $g \times_R R/\mathfrak m^{e+1} = b_e$ for all $e$.

## Proof

Write $\mathrm{H}^0(L^k)$ for the sections of $L^k$ on $G$ (the Lean `H0`, not unfolded).

1. `mumford_thickening_endomorphism_maps_sections` gives $N \geq 1$ and maps $S \colon \mathrm{H}^0(L^k) \to \mathrm{H}^0(L^{Nk})$ with $b_e^*(s_1/s_2) = S(s_1)/S(s_2)$ on each $G_e$, in cross-multiplied form (`SecRatioEq`). For $k \geq 3$ it also gives $s_0$ with $b_0^* s_0$ and $S(s_0)$ both nonzero at one point (`SecCoNonzero`).
2. `exists_genericFibreHom_of_formalSectionRatios` gives a group endomorphism $\varphi$ of $G_K$ with $\varphi^*(s_1/s_2) = S(s_1)/S(s_2)$.
3. `semiAbelian_genericFibre_hom_extends_normal_noetherian` extends $\varphi$ to a group endomorphism $g$ of $G$. It uses that $R$ is noetherian and integrally closed.
4. `thickening_eq_of_generic_section_ratios` shows that $g$ restricts to $b_e$ on each $G_e$.

## In the Lean code

The theorem is at [MumfordFormalEndomorphismAlgebraic.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MumfordFormalEndomorphismAlgebraic.lean#L18). `EndData` and `FormalEnd` are in [FormalEnd.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FormalEnd.lean#L15), and `SecRatioEq` in [SecRatioEqRefl.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SecRatioEqRefl.lean#L15).

- The four lemmas are second names of `MumSec.main`, `Mum.GenericRatio.exists_generic_hom`, `Mum.semiAbelian_end_generic_extends` and `Mum.thick_eq_of_ratios`. We have read their statements, not their proofs.
- The maps $a'$ and $h$ enter only through `EndData`. The conclusion does not name them.
- We do not know a published statement in exactly this form.
