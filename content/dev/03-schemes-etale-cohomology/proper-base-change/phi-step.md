---
id: phi-step
title: Frobenius at places above ℓ is controlled by the Hecke polynomial
kind: theorem
decl: UpperTheory.Ru.crystallineComparison.phiStep
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.SmoothModelCrystalline
covers: 1031
status: drafted
drafted_by: writer@claude
---
This theorem proves `PhiStep`, one of the 17 fields of [Steps holds](/entry/steps-holds/): a Galois representation cut out of the cohomology of a tower is crystalline at a place $w$ above $\ell$, and the characteristic polynomial of a Frobenius on its Weil-Deligne representation divides a power of the Hecke polynomial at $w$. This gives clause 4 of the Galois row in [GeoOne holds](/step/geo-one-holds/).

## Statement

Let $E$ be a number field with algebraic closure $\Omega$, $\ell$ a prime and $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ an isomorphism. Let $H$ be a tower over $E$: a scheme $Z$ over $E$ with correspondences $Y_g \rightrightarrows Z$ for $g$ in a set $\Gamma$. Assume $Z$ is smooth and projective and the maps $Y_g \to Z$ are finite étale. Let $\theta \colon \Gamma \to \overline{\mathbb{Q}}_\ell$ be a system of Hecke eigenvalues.

Let $\rho \colon G_E \to \mathrm{GL}_d(\overline{\mathbb{Q}}_\ell)$ be continuous and a *piece* of $H$ for $\theta$. That is, there is a representation $\rho_0$ that is the Galois action on a basis of the $\theta$-eigenspace of $\overline{\mathbb{Q}}_\ell \otimes H^*(Z_\Omega)$. This $\rho_0$ is block triangular, and $\rho$ is its block-diagonal part.

Let $w \mid \ell$ be a place of $E$ with norm $Nw$. Let $\vartheta_0, \dots, \vartheta_n \in \overline{\mathbb{Q}}_\ell$, and put
$$P_w(X) = \sum_{j=0}^{n} (-1)^j (Nw)^{\binom{j}{2}} \vartheta_j X^{n-j}.$$
Assume a *congruence at $w$*: there is a smooth projective model of a finite étale Galois quotient of $Z$ over $\mathcal{O}_w$, with correspondences $T_0, \dots, T_n$ that satisfy a point identity `PtId` and lie over Hecke correspondences $\gamma_j$ with multiplicity $m_j$, where $\theta(\gamma_j) = m_j \vartheta_j$. Assume $\vartheta_0 \neq 0$ and $\iota(P_w) = \iota(\vartheta_0) \prod_{r \in R} (X - r)$ for a multiset $R \subset \mathbb{C}$.

**Theorem.** Then $\rho|_{D_w}$ is crystalline, and there are an element $g$ of the Weil group at $w$ of degree $-1$ and an $m \in \mathbb{N}$ such that the characteristic polynomial of $g$ on $\mathrm{WD}(\rho|_{D_w})$ divides $\prod_{r \in R}(X - r)^m$.

## Proof

1. **Two inputs.** `finAll` proves `FinAll`, a relation of Eichler-Shimura type. For a smooth model $M$ over the ring of integers of a finite extension $K$ of $\mathbb{Q}_\ell$ with residue field of size $\ell^f$, correspondences $T_i$ with `PtId` and their actions $A_i$ on $V = H^j(M_{\overline{K}})$, some $N$ gives $\sum_i (-1)^i (\ell^f)^{\binom{i}{2}} (A_i \otimes \varphi^{f(n-i+N)}) x = 0$ on invariant vectors $x$ of $V \otimes B_0$. `smoothModel_crystalline` proves `SmoothModelCrystalline`: for a smooth model, $V$ is $B_{\mathrm{cris}}$-admissible. This has the form of the crystalline comparison $C_{\mathrm{cris}}$ (Faltings, 1989).
2. **The local side.** `geoSide_of` combines them through `geoLoc`, with `congBC` and `Seam.locTower_holds`. It gives `GeoSide`: $\rho_0|_{D_w}$ embeds in $\overline{\mathbb{Q}}_\ell \otimes V$ for a crystalline $V$ on which $P_w$ of the crystalline Frobenius vanishes and $T_j$ acts by $\vartheta_j$.
3. **From $\rho_0$ to $\rho$.** `phiStep_of` applies `joinQ`. It passes to the block-diagonal part $\rho$ and gives a crystalline model of $\rho|_{D_w}$ over a finite extension of $\mathbb{Q}_\ell$, on which $P_w$ of Frobenius is nilpotent. Then `nilToPhi` gives crystallinity and the divisibility of characteristic polynomials.

The rest is bookkeeping: a rewrite that matches the two forms of $P_w$.

## In the Lean code

The theorem is in [SmoothModelCrystalline.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/SmoothModelCrystalline.lean#L13). The lemmas it calls:

- `phiStep_of` in [PhiStepOf.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/PhiStepOf.lean#L10), with `joinQ` and `nilToPhi`.
- `geoSide_of` in [PGeoSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PGeoSide.lean#L6).
- `finAll` and `smoothModel_crystalline`, in the same file. `FinAll` is stated in [LocFacts.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/LocFacts.lean#L32), and `SmoothModelCrystalline` in [SemistableModelSemistable.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/SemistableModelSemistable.lean#L46).

`PhiStep` is stated in [HodgeTrAt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/HodgeTrAt.lean#L122). We have not unfolded `PtId`, `IsHk`, the period datum $B_0$, `Model.Good` or `wdAt`. The ring $B_{\mathrm{cris}}$ is defined as the subring of $B_{\mathrm{dR}}$ generated by the image of a map `iC`, $1/\ell$ and $1/t$; we have not unfolded `iC`.
