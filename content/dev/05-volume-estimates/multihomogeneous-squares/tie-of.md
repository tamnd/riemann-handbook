---
id: tie-of
title: A root model with a Hodge tie and a flag system, from five statements
kind: theorem
decl: SquareStatements.tie_of
module: Development.WeilBound.CoreStatements.MultihomogeneousSquares.ChooseTwoAdd
covers: 797
status: drafted
drafted_by: writer@claude
---
This theorem proves the tie statement `StTie` from five statements. In [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/), `sq_of` turns `StTie` and `StCmp` into `StSq`, which leads to the swap relation $\mathrm{I8}$.

## Statement

Let $\Psi = \mathrm{CMType}(H)$, $N = p + q$, and let $\mathrm{PB}(\mathrm{Re}, II)$ be the arithmetic intersection polynomial of a realization $\mathrm{Re}$. A *Hodge tie* $t$ on a root model $M$ is a Hodge component of $Y$ with a flag $\mathrm{Fl}$, Hodge lines $\mathrm{sing}_r$ of degree $\deg x_r$, and a realization $\mathrm{Re}_t$ of an analytic system $\mathrm{Sy}_t$ of dimension $\dim \mathrm{Fl}_{\Psi,N}$. For small parameters the lines of $M$ are $\ell_{r-1} - \ell_r$ in the lines $\ell$ of $\mathrm{Re}_t$ (`rootOnFund`), and $\delta_M = n \deg \mathrm{Fl}$. We have not unfolded `HodgeCpt`, `AnSys` and `Realis`.

**Theorem.** Assume `StX`, `StAlg`, `StHt`, `StSing`, `StBase`, $\mathrm{Given}$ and `Out.WeilSt`. Let $E$ be a CM field with host $H$ and datum $D$ with $p, q \geq 1$, $Y$ a model, $S$ a finite set of primes containing those dividing $d_E$, and $\xi_0$ a point of $Y$ with `IsCptGen`. Then there are a root model $M'$, a Hodge tie $t$ on $M'$ with $n = [F:\mathbb{Q}]$ for the coefficient field $F$, an integer $d$, and a realization $\mathrm{Re}$ of an analytic system $\mathrm{Sy}$ of dimension $d + 1$, such that:

1. $t$ has the generic point of $\xi_0$ and $R_\ell = 4$ for $\ell \in S$; $\mathrm{Re}_t$ has degree $1$; $\deg \mathrm{Fl} > 0$; $\mathrm{Sy}$ and $\mathrm{Sy}_t$ have the same degree polynomial;
2. $\mathrm{Re}$ has a flag system for $j = p$: square systems for the adjacent pairs $(a, a+1)$ with $a + 1 < p$ or $p \leq a$;
3. $\mathrm{PB}(\mathrm{Re}, II) = \mathrm{PB}(\mathrm{Re}_t, II)$ for every intersection system $II$.

## Proof

1. Take `PB.Inputs` and `ResKStatement` out of $\mathrm{Given}$. `StBase` gives a Hodge component $\mathfrak{M}$ over $\xi_0$: a cover with simple normal crossings boundary and $R_\ell = 4$ on $S$.
2. [`flag_model_exists_of_given`](/entry/flag-model-exists-of-given/) gives a flag model over $\mathfrak{M}$ with a flag and a tie. `base_metric_exists_of_given` gives a base metric with $n = |\Psi|\,pq$.
3. Count dimensions. By `choose_two_add`, $\binom{p+q}{2} = pq + \binom p2 + \binom q2$, so $\dim \mathrm{Fl}_{\Psi,N} = n + |\Psi|(\binom p2 + \binom q2)$. As $\Psi \neq \emptyset$ (`host_numbers`) and $p, q \geq 1$, this is $d + 1$ with $d \geq 0$.
4. `flagModel_arith_dimension_boundary` gives analytic flag data of dimension $d$. They are uniformised (`flag_analytic_data_uniformised`). `flag_cover_degree_one_realisation` gives $\mathrm{Re}$ with the same lines. [`flag_cover_realisation_pullback`](/entry/t-flag-cover-realisation-pullback/) gives the square systems, so $\mathrm{Re}$ has a flag system.
5. The other fields of the tie: the Hodge lines $\mathrm{sing}_r$ (`hodge_cpt_flag_xdeg`), their metrics (`StSing`), `AlgOver` (`StAlg`), the lines $x_r$ of $M'$ (`StX`), the condition `IsVBOn` (`StHt`) and birationality (`hodge_cpt_birational_arith_var`).
6. Build $M'$ with $k_A = 1$, the trivial line as $\overline A$ and $\delta = [F:\mathbb{Q}] \deg \mathrm{Fl}$, and the tie $t$. Item 3 is `PB_eq_of_lines`: equal degree and lines give equal $\mathrm{PB}$.

## In the Lean code

The theorem is in [ChooseTwoAdd.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/ChooseTwoAdd.lean#L55). The statements are in [AntisymmetryFibreSquares.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/AntisymmetryFibreSquares.lean#L37), and `HodgeTie` is in [RootOnFund.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/RootOnFund.lean#L24). The file is named after its helper `choose_two_add` (line 21), not after the theorem. `PB.Inputs` and `ResKStatement` are taken by position, `hG.2.2.2.2.2.2.2.2.2.1` and `hG.2.2.2.2.1` (lines 57 and 58). `Out.WeilSt` is used only through `StBase`. No tower appears: it enters in `StSq`.
