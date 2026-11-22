---
id: link-of-local-closed
title: The bound LinkG from local data on a closed class
kind: theorem
decl: Formalism.L2.G.link_of_local_closed
module: Formalism.LocalToGlobal.GroupLattices.AdmissibleFamilyNoKernel
covers: 1950
status: drafted
drafted_by: writer@claude
---
This theorem proves the family bound `LinkG` on a family class from `Loc` and four closed local hypotheses. It is the step where the record `Loc`, and through it [Statement E](/entry/stmt-e/), enters the proof of `LinkG`. Its only user is [LinkG from group compatibility](/entry/link-g-concrete-no-ker/), which derives three of the four local hypotheses from one. That theorem feeds [the concrete LinkG theorem](/entry/link-g-concrete5/), and so the branch below [the shape theorem](/entry/shape-closed-link-n-of-green/).

## Statement

Use the notation of [LinkG from group compatibility](/entry/link-g-concrete-no-ker/): $\mathrm{Ev}_F(P)$ means that $P(x,i)$ holds for all large $x$ and all $i$, and $\mathrm{Closed}(\mathcal{C}, P)$ is the predicate of [the definition Closed](/step/closed-def/).

**Theorem.** Let $\mathcal{C}$ be a family class. Assume `Loc` and

1. $\mathrm{Closed}(\mathcal{C}, F \mapsto \mathrm{Ev}_F(\mathrm{TrivialStabiliserFiniteClasses}))$: eventually, each local datum `D.gat u w` of $D(x,i)$ has trivial stabilisers and finitely many classes;
2. $\mathrm{Closed}(\mathcal{C}, F \mapsto \mathrm{Ev}_F(\mathrm{StdSubAt}))$: eventually, at each place $v$ of each local datum, there is a discrete valuation ring $O_s$ with fraction field $K_s$ in an unramified quadratic setting (`UnramifiedQuadraticSetting`) and a finite map $O_s \to O$ that carries its data to the given data;
3. $\mathrm{Closed}(\mathcal{C}, \mathrm{Adm2F})$;
4. $\mathrm{Closed}(\mathcal{C}, \mathrm{NPDescF})$.

Then $\mathrm{Closed}(\mathcal{C}, \mathrm{LinkG})$.

`LinkG F` says: there are $C$, $x_0$ and $\delta$ with $\delta(x) \to 0$ such that `LinkG_at` holds for all $x \ge x_0$ and all $i$, with the instance $G_x(x,i)$, the constants of $F$, $C$ and $b^{\delta(x)}$. `LinkG_at` is a list of local bounds: a bound `LocLe` and a bound on `lenMN` at the places $w$ off the prime of the word $u$, a bound $S_v \le 2 m N_v a / p$ for each prime $p$, bounds on gains and on von Mangoldt class sums at small inert places, and two conditions `ServedOrbitsContained` and `MeanKappaBound`. We have not unfolded `Adm2F`, `NPDescF` or the terms of `LinkG_at`.

## Proof

The proof combines ten closed statements with `Closed.and` and applies `linkG_fam_noKer` to each family.

1. **The second theorem.** `second_theorem_absolute_constant` gives one $C_0 \ge 0$ such that `aux₃ D C₀` holds for all $D$. It uses `Loc` through `local_model_results`. `second_theorem_closed_form` turns this into the closed statement `SecondTheoremAtFamily`.
2. **The first theorem.** `first_theorem_threshold_functions` and `first_theorem_closed_form` give the closed statement `FirstTheoremAtFamily`. They also use `local_model_results` and `local_flatness_results`.
3. **Constants.** `signs_closed`, `ones_closed`, `cb_closed` and `family_log_bound_closed` give $0 <$ `GK.La`, $1 \le$ `cX.Ce`, the bound `CbLarge` and the bound `FamilyWindowLogBound`. These are proved outright.
4. The four hypotheses, unchanged.

For one family, `linkG_fam_noKer` builds the nine admissibility conditions `Adm1F` to `Adm9F`, the lattice bounds `OrbitLatticeBounds` and the sandwich `LatticeSandwich`, and calls `linkG_without_kernels`. That theorem replaces the chain part of the lattice datum $G_y$ by zero (`zeroCh`), proves the admissibility `AdmF` for the new datum by `admissible_family_no_kernel`, gets the family conclusion from `AuxBlock8.Pf.stmtF`, and ends with `linkG_at_of`.

## In the Lean code

The theorem is at [AdmissibleFamilyNoKernel.lean line 272](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L272).

- `Loc` is used only through its field `p14R`, in `local_model_results` (line 43). `extremal_projector_tools_of_loc` (line 40) and `local_flatness_results` (line 62) take `h : Loc` and do not use it.
- `linkG_without_kernels` (line 224) uses the zero chain. For it, the valuation bounds `vKge` hold for every exponent, because the zero vector lies in each submodule (`vKge_zero`, line 178). So the bounds `unitBoundAtTwistedPlaces` and `ServiceLowerValuation` carry no content on this route. This is sound, because `LinkG_at` reads only $G_x$ and the constants, not $G_y$.
- The second theorem enters only as one constant for all $D$. This is possible because `aux₃ D C` does not read $D$; see [Statement E](/entry/stmt-e/).
