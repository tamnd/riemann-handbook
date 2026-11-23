---
id: rest-tm-exists
title: The box bound for bad shares from the model lattice bound
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.restTM_exists
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.RestTMExists
covers: 1715
status: drafted
drafted_by: writer@claude
---
This theorem proves the box bound `RestTM` with $C_M = 1$ from four hypotheses on an instance. The entry above it, [`restTM_closed`](/entry/rest-tm-closed/), proves the four hypotheses. This theorem cuts the box of top vectors into progressions and applies to each one the model lattice bound of [`alternative_mean_value_theorem`](/entry/alternative-mean-value-theorem/).

## Statement

An instance $X$ (`flipOneThree.Inst`) with constants $C_0, C_{E1}, C_{E2}$ gives a prime $p$, sizes $s, r$, a parameter $Y$ (`X.L.Y`) and $t$ ties at top positions $u(1), \dots, u(t)$. For each digit class $\delta$ in a finite set `clSet` there is a box $B(\delta)$ of window vectors $a \in \mathbb{N}^s$ with digits compatible with $\delta$ (`cbox`), and a set $I(\delta, a)$ of pairs $x = (b, \ell)$ of a kept block and a level (`idx`).

For $a$ and $x$ the code builds a polynomial space $Y(a, x)$ over $\mathbb{Q}_p$ (`dimY`). Let $\mathrm{bad}_Y(a, x; D)$ (`bY`) be the rank of its $\mathbb{Z}_p$-integral lattice minus the largest $n$ with $x_1, \dots, x_n, y_1, \dots, y_n$ in the lattice and $\beta(x_i, y_j) = p^{D}\delta_{ij}$, for the tie-twisted Fock pairing $\beta$. Let $\kappa = 3(s+2)r^2\lambda$ with $\lambda = \log_p(8a_L + r) + 1$, and $D_1(C_M) = t(Y\kappa + C_M\kappa) + C_M\kappa$ (`D1r`).

`RestTM` $C_M$ says: for each $\delta$, each $a_0 \in B(\delta)$ and each $x \in I(\delta, a_0)$,

$$ \sum_{a \in B(\delta)} \mathrm{bad}_Y\bigl(a, x; \lfloor D_1(C_M) \rfloor\bigr) \le \frac{30 + C_M}{Y} \sum_{i=1}^{t} \sum_{a \in B(\delta)} \dim Y\bigl(\mathrm{upd}_i(a), x\bigr), $$

where $\mathrm{upd}_i(a)$ replaces the coordinate $u(i)$ of $a$ by the largest window value allowed by $\delta$ (`topA`).

**Theorem.** There is $C_M \ge 1$ such that for all $D$, all constants and every $X$: if $X$ satisfies the window hypotheses `HI`, `RestFree` (the set $I(\delta, a)$ does not depend on $a \in B(\delta)$), `RestTMSize` (size bounds on the model instances) and `RestTMEps` $C_M$ (each model error $\varepsilon_i$ is at most $(30 + C_M)/Y$), then `RestTM` $C_M$ holds.

## Proof

Take $C_M = 1$ and apply `restTM_of`.

1. `restTMHyp_of` turns `HI` and `RestTMSize` into `RestTMHyp`: each model instance `XMof` $(\delta, a, x)$ of type `InstM` satisfies `InstM.Hyp`. The model has steps $d_i = 1$ and $E = Y\kappa$, so its depth is $\lfloor D_1(1) \rfloor$ (`exponent_matrix_first_depth_eq`).
2. `restTM_of_rests` fixes $\delta$, $a_0$, $x$. By `RestFree`, $x \in I(\delta, a)$ for all $a$ in the box. `box_of_fibres` reduces the sum over the box to sums over fibres where only the $t$ tie coordinates move. On each fibre, `fibre_ineq` applies `ModelLatticeRank` to the model instance, with each $\varepsilon_i \le 31/Y$ by `RestTMEps` 1.

## In the Lean code

The theorem is in [RestTMExists.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestTMExists.lean#L14), with `restTM_of` at line 9. The lemmas:

- `restTMHyp_of` and `RestTMSize` in [RestTMHypOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestTMHypOf.lean#L58).
- `restTM_of_rests`, `fibre_ineq`, `RestTMHyp` and `RestTMEps` in [ExponentMatrixFirstDepthEq.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ExponentMatrixFirstDepthEq.lean#L193).
- `box_of_fibres` in [BoxOfFibres.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BoxOfFibres.lean#L89).
- `RestTM`, `RestFree`, `bY` and `dimY` in [BlockBoundUniformiser.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockBoundUniformiser.lean#L134); `XMof` in [DimYOvr.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/DimYOvr.lean#L130).

The existential over $C_M$ is filled with $C_M = 1$, the only value at which `restTM_of_rests` applies, since the model depth is $D_1(1)$. The quantifier over $D$ (`_D`) is idle: $D$ goes only to `ModelLatticeRank`, whose definition does not read it. We have not unfolded `HI`, `clSet`, `cbox`, `idx`, `upd` or the construction of the model letters `lLL`.
