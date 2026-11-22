---
id: ordinary-vanishing-two-of-printed-hida
title: Ordinary adjoint cocycles are coboundaries, from Hida theory
kind: theorem
decl: UpperTheory.V.Th.ordinary_vanishing_two_of_printed_hida
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.TOrdVan
covers: 1104
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{OrdVan2Alt}$: at an automorphic point of a Hida family, each ordinary 1-cocycle of the adjoint representation is a coboundary. Its only hypothesis is $\mathrm{HypothesesH'}$. [The theorem on automorphic points](/entry/core-alt-bis/) checks the hypotheses of $\mathrm{OrdVan2Alt}$ at each locally generic automorphic point and gets $\mathrm{DenseThresholdMainCase}$.

## Statement

Fix a prime $\ell$, a CM field $L$, a Hida setting $s$ (an odd prime $\ell$, a complex conjugation, places above $\ell$, a finite set of tame places and an auxiliary place $v_0$) and a level $V$ whose set of places is the set $S$ of $s$. Let $2 \le n \le 4$, let $r$ be a residual representation that meets the condition at $v_0$, and let $x$ be an arithmetic point of the universal ordinary determinant ring of $r$. Let $\rho \colon G_{L,S} \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ be continuous with determinant $x$. Suppose:

- $\rho$ is automorphic (conjugate self-dual, in the sense of `IsAutCsdA`) and trivial on the inertia group $I_0$;
- the matrices $\rho(g)$ span $M_n(\overline{\mathbb{Q}}_\ell)$;
- $\psi_{v,i} \ne \psi_{v,j} \bar\varepsilon$ at each place $v$ above $\ell$, where $\psi_v$ are the characters of $x$ and $\bar\varepsilon$ is the [[cyclotomic character|XSGB5K2KEG]] (`cycBar`);
- the determinant is regular: some elements of the group have separable characteristic polynomial.

**Theorem.** Under $\mathrm{HypothesesH'}$, each ordinary cocycle $z$ of $\operatorname{ad} \rho$ is a coboundary: $z(g) = \rho(g) Y \rho(g)^{-1} - Y$ for some matrix $Y$.

Here a cocycle is ordinary if it is continuous, polarized, zero on the inertia groups at the tame places, and upper triangular at each place above $\ell$ in a suitable basis, after a coboundary is subtracted.

## Proof

The idea: an ordinary cocycle is a tangent vector to the ordinary deformations of $\rho$. The Hida side of the proof says that such a tangent vector does not move the traces. A cocycle that does not move the traces is a coboundary.

1. The package $\mathrm{CohP}$ of Galois cohomology facts is read off from the literature hypothesis inside $\mathrm{HypothesesH'}$. The tame part comes from `TameLocal_of_duality`.
2. The private lemma `nmAbs` does the deformation step. It conjugates $\rho$ to an integral self-dual form, finds an integral model of $\rho$ and of a multiple of $z$, and builds a point over the dual numbers. It gets a universal ring from `b0Ex (phiAll hC)` and a derivation $\delta$ of it. It proves: if $\delta$ kills all traces, then $z$ is a coboundary. This last step is `trZero`: if the $\rho(g)$ span all matrices and $\operatorname{tr}(z(g)\rho(g)) = 0$ for all $g$, then $z$ is a coboundary.
3. `lamEx` gives the local data $\Lambda'$, and `hida_x_of_printed_hida` gives a Hecke ideal $J$ with the level condition. The automorphy of $\rho$ and the flags give $J \subset \ker x$. The flags come from the ordinarity of $z$.
4. `core_o_of_literal_automorphy_n` proves $\mathrm{OrdinaryMainCase}$: an $x$-derivation that kills $\psi$ on inertia kills all traces. With step 2 this ends the proof.

The rest is bookkeeping.

## In the Lean code

The theorem is in [TOrdVan.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TOrdVan.lean#L159). It calls:

- `nmAbs`, a private lemma in the same file (line 113), with `modelF`, `modelG`, `pairF` and `shr2`;
- `regular_arithmetic_hida_of_literal_automorphy`, for the regularity of the characters $\psi_v$;
- `b0Ex`, `phiAll`, `lamEx` and `W.locCFT`;
- `hida_x_of_printed_hida` in [THidaX.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/THidaX.lean#L17);
- `core_o_of_literal_automorphy_n` in [TCoreO.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TCoreO.lean#L129).

We have not unfolded the Hida side: `hida_x_of_printed_hida`, `core_o_of_literal_automorphy_n` and the structure of the universal ordinary determinant ring.
