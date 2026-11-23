---
id: link-g-fam-no-ker
title: LinkG for one family, from the two theorems and local data
kind: theorem
decl: Formalism.L2.G.linkG_fam_noKer
module: Formalism.LocalToGlobal.GroupLattices.AdmissibleFamilyNoKernel
covers: 708
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `LinkG` for one family. It takes the first and second theorems at the family, a few constant conditions, and the four local hypotheses. [LinkG from local data](/entry/link-of-local-closed/) applies it to each family of a closed class. It builds the nine admissibility conditions and two lattice bounds, and passes them to [LinkG without kernels](/entry/link-g-without-kernels/).

## Statement

Use the notation of [LinkG from local data](/entry/link-of-local-closed/): $F$ is a family with data $D(x,i)$, size data $L(x,i)$, instances $G_x(x,i)$ and $G_y(x,i)$, and constants $K$ (`Fm.GK`). $\mathrm{Ev}_F(P)$ means that $P(x,i)$ holds for all large $x$ and all $i$.

**Theorem.** Assume:

1. `SecondTheoremAtFamily F`: there is $C \ge 0$, at most six given constants of $K$, with $\mathrm{Ev}_F(\mathrm{aux}_3(D(x,i), C))$;
2. `FirstTheoremAtFamily F`: there are $C_H, C \ge 0$ under given bounds by constants of $K$, with the family conclusion `flipOneThree.Conclusion2Family`;
3. $0 < K.\mathrm{La}$, $1 \le$ `Fm.cX.Ce`, and $\mathrm{Ev}_F$ of `CbLarge`: $N_1 \le K.C_N \log x$;
4. $\mathrm{Ev}_F$ of `TrivialStabiliserFiniteClasses` and of `StdSubAt`, `Adm2F F` and `NPDescF F`;
5. the window bound `FamilyWindowLogBound F`.

Then `LinkG F`.

## Proof

The proof finds the hypotheses of `linkG_without_kernels`.

- `Adm6F` comes from the second theorem, by `family_second_bound_of_theorem`.
- `Adm7F` comes from `family_kappa_bound`, and `Adm8F` from the first theorem by `family_first_bound_of_theorem`. Both use the fact `kapIDefF`, which each family carries.
- `Adm9F` is built with the constant `Fm.cX.Ce`, from `weyl_sandwich_of_factors`, `weylSandwich_of_model` and `expBound_of`.
- `Adm1F`, `Adm3F`, `Adm4F` and `Adm5F` come from `family_first_lemma`, `family_orders_first_part`, `family_orders_bound_of_lemma` and `family_sizes_bound`. `Adm3F` uses the order estimate with constant 100 from `field_lemmas_except_seven`.
- The orbit lattice bounds `OrbitLatticeBounds` come from `linear_programming_input_of_hypotheses`, with `Adm6F`, `Adm7F`, `StdSubAt`, `hypIAt_ev`, `hypIIAt_fam` and `CbLarge`.
- The sandwich `LatticeSandwich` comes from `Adm9F`, by `sandwich_of_exponent_clause`.
- `OperatorsPreserveLattices` holds for every datum, by `Model.operators_preserve_lattices`.

Then `linkG_without_kernels` gives `LinkG F`. The rest is bookkeeping.

## In the Lean code

The theorem is at [AdmissibleFamilyNoKernel.lean line 241](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L241). `SecondTheoremAtFamily`, `FirstTheoremAtFamily` and the conditions `Adm1F` to `Adm9F` are in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L900).

- Every hypothesis is used. `TrivialStabiliserFiniteClasses`, `Adm2F` and `NPDescF` are only passed on.
- `field_lemmas_except_seven` proves eight conclusions. The proof uses one of them, `Conclusion4 D 100`. The lemma is in the namespace `UnusedSlot33`, and the name does not fit this use ([CMFieldLemmas.lean line 21](lean:Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/CMFieldLemmas.lean#L21)).
- The second theorem enters only through $\mathrm{aux}_3(D, C)$, which does not read $D$; see [Statement E](/entry/stmt-e/).
- We have not unfolded `Conclusion2Family`, `adm6`, `adm8` or `adm9`.
