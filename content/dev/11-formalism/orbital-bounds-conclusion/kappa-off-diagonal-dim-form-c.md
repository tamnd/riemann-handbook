---
id: kappa-off-diagonal-dim-form-c
title: A lower bound for the dimension of the space C_u by the mass of lattices
kind: theorem
decl: kappa_off_diagonal_dim_form_C
module: Formalism.PeriodIntegrals.OrbitalBoundsConclusion.UnitaryDimensionFormula
covers: 302
status: drafted
drafted_by: writer@claude
---
This theorem proves `DimFormC`: a lower bound for the complex dimension of a space $C_u$ by a mass of lattices, times the dimension of a representation space, times a constant $\Gamma_1$. It lies below the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). It is a pass-through. The real content is in `dimFormC_of_steps`, which has no entry in the outline. The name comes from the namespace `KappaOffDiagonal`; the statement is a dimension bound, not an off-diagonal estimate.

## Statement

For every datum $D$, setting $X$, full family $Y$ and word $u$ with `ConcTie X Y`:
$$0 \leq \Gamma_1 \quad\text{and}\quad \Gamma_1 \cdot \sum_{\Lambda \in Y(u)} \frac{1}{\#\operatorname{Aut}(\Lambda)} \cdot \dim_{\mathbb C} V_\pi(u) \leq \dim_{\mathbb C} C_u.$$
Here $\Gamma_1$ is the real part of the product of local factors `gamProd` at $1$, $\operatorname{Aut}(\Lambda)$ is the group `autLz` of the flag and the lattice $\Lambda$, and $C_u$ is a space of linear maps from $V_\pi(u)$ to functions on $H_\infty \times H_{\mathrm{fin}}$. We have not unfolded `ConcTie`, `gamProd` or `Cu`.

## Proof

The proof is one line. `dimFormC_of_three` adds two more proved inputs, `orbitCount` and `kuStab`, and calls `dimFormC_of_steps`. The three inputs passed here are:

- `transport_holds` (`Transport`): each $\gamma$ in the group `Gam X u` moves the lattice $\mathrm{latS}(h)$ by an element of the flag stabilizer;
- `stabBound_holds` (`StabBound`): the elements $\gamma$ that link two points over $\Lambda$ lie in a set of at most $\#\operatorname{Aut}(\Lambda)$ elements;
- `indexGe` (`IndexGe`): over each $\Lambda$ there are at least `Gam1 Y.TR` points in distinct cosets of $K_u$. We have not checked that this equals the $\Gamma_1$ above, `(Y.tO u u).Gam1`.

## In the Lean code

The theorem is in [UnitaryDimensionFormula.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UnitaryDimensionFormula.lean#L6). `DimFormC` is in [DimFormC.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DimFormC.lean#L80), and `dimFormC_of_three` in [DimFormCOfThree.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/RankTwoDimensionFormula/DimFormCOfThree.lean#L78). The inputs are stated in [DimFormCOfSteps.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/RankTwoDimensionFormula/DimFormCOfSteps.lean#L23).
