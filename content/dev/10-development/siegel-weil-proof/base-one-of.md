---
id: base-one-of
title: The rank one Siegel-Weil measure identity from the local mass fact
kind: theorem
decl: PositivityTheory.Rg.Base1.baseOne_of
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.BaseOneSide.BaseOneOf
covers: 478
status: drafted
drafted_by: writer@claude
---
This theorem proves `BaseOne`, the Siegel-Weil identity for a Hermitian form of rank one, from the local fact `MassOne`. [`baseOne`](/entry/base-one/) applies it to the proved `massOne`, and [`densEq`](/entry/dens-eq/) uses the result as the base of an induction on the rank. The proof assembles four statements about the theta measure of the sphere $\{X: J(X,X)=\beta\}$ in a line of $E$. Each statement comes from a wrapper in the namespace `GlobalTheory.T`.

## Statement

Let $E/F$ be a CM extension with conjugation $\sigma$, and let $e_v$ and $Nv$ be as in [`densEq`](/entry/dens-eq/). For a $1\times1$ Hermitian $J\neq0$ and $\beta\in F^{\times}$, let $\mathrm{EP}(\beta,c)$ say that the theta measure of $\{X:J(X,X)=\beta\}$ (`thetaMeas`, built from a Haar measure and a fundamental domain of $U(J)$; I have not unfolded it) is an Euler product with constant $c$. The local factors are $m_\infty(\beta)$ and $(1-e_v/Nv)^{-1}m_v(\beta)$, with $m_v$ the Gram fibre measures. `IsEulerProd` says that, for $S$ large, the integral of a pure test function is $c$ times the product of its local integrals over $\infty$ and $S$ and of the local masses of the lattice outside $S$.

**Theorem.** Assume `MassOne`: at almost all $v$, $(1-e_v/Nv)^{-1}$ times the fibre measure of the standard lattice at a unit is $1$. Then for every $1\times1$ nondegenerate $J$ and $T\neq0$ there is $c$ with $\mathrm{EP}(T,c)$, and $c=\Lambda/2$ for every limit $\Lambda$ of $\prod_v(1-e_vNv^{-s})$ as $s\to1^{+}$.

## Proof

`siegel_weil_rank_one_base_case` takes four statements and returns `BaseOne`. They are:

1. `Prop1`: for each $\beta\neq0$ there is $c$ with $\mathrm{EP}(\beta,c)$. It comes from `length_formula_of_total_mass_one` and `MassOne`.
2. `Simil`: if $\beta$ and $\beta'$ are both represented by $J$, then $\mathrm{EP}(\beta,c)$ implies $\mathrm{EP}(\beta',c)$. It comes from `scalar_fibration_formula`, which says how the fibre measures change when $X$ is scaled by an element $x$ with norm $n$.
3. `Hasse`: if the fibre measure at $\beta$ is nonzero at $\infty$ and at every $v$, then $\beta$ is represented. This is `hasse_principle_hermitian`.
4. `Cnt`: if one $\kappa$ satisfies $\mathrm{EP}(\beta,\kappa)$ for all $\beta\neq0$, then $\kappa=\Lambda/2$. It comes from `counting_formula_of_components` with eight inputs. Among them: `Tate`, the residue at $s=1$ of an idelic zeta integral; `Ratio`, which removes the twist by $e_v$ at the cost of the factor $\prod_v(1-e_vNv^{-s})$; `HEx`, an open subgroup of index $2$ of the ideles made of $F^{\times}$ times norms; and `ThetaId`, which writes the theta mean as $\kappa$ times an idelic theta series of a pure function that vanishes off that subgroup.

I have not unfolded the wrappers or the theorem `CompanionTheory.Base1.baseOne_of_parts` that `siegel_weil_rank_one_base_case` calls. So I do not say how the four statements give `BaseOne`.

## In the Lean code

The theorem is in [BaseOneOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/BaseOneSide/BaseOneOf.lean#L23). `MassOne` is used twice: in `length_formula_of_total_mass_one` and in `local_density_of_mass_one`, which feeds `ThetaId`. `equidistribution` and `scalar_fibration_formula` are also used twice.

- `Prop1`, `Simil`, `Hasse`, `Cnt`, `EP`, `ForOne` and the eight inputs of `Cnt` are in [PsiSide.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/BaseOneSide/PsiSide.lean#L141).
- `siegel_weil_rank_one_base_case` is in [SiegelWeilRankOneBaseCaseStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SiegelWeilRankOneBaseCaseStatement.lean#L6). The other wrappers are in files of the same folder, one per name.
- `BaseOne` and `MassOne` are in [Pieces.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/Pieces.lean#L10). `SWMeasC`, `cfac` and `IsLamLim` are in [SWMeasCAll.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelDensities/SWMeasCAll.lean#L19).
