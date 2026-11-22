---
id: rest-tm-closed
title: The mean bound on bad counts over a box of tops
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.restTM_closed
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.EpsilonBoundMConstant
covers: 1784
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `RestTM` that [`openE_of_open4`](/entry/open-e-of-open4/) needs for the chain of reductions below [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/). It gives one constant $C_M$ that works for all instances. It proves the four inputs of [`restTM_exists`](/entry/rest-tm-exists/), and the main input there is the mean value theorem [`alternative_mean_value_theorem`](/entry/alternative-mean-value-theorem/).

## Statement

Instances $X$, the window $A$, the lattices $Y_\ell$, the bad count and the depth $D_1$ are as in [`openE_of_open4`](/entry/open-e-of-open4/). A *digit class* $\delta$ runs over the finite set `clSet`. The box $\mathrm{cbox}(\delta) \subseteq A^s$ is the set of tops compatible with $\delta$. The index set $I(\delta, a)$ is the set of pairs $(b, \ell)$ of a kept block $b$ with digits $\delta$ and a level $\ell$ of $b$. For a top $a$ and a tie $i \le t$, $u_i(a)$ is $a$ with the entry at the $i$-th tie position replaced by the largest compatible element of $A$ (`upd`).

`RestTM` $C_M$: for each $\delta$, each $a_0 \in \mathrm{cbox}(\delta)$ and each $(b, \ell) \in I(\delta, a_0)$,

$$ \sum_{a \in \mathrm{cbox}(\delta)} \mathrm{bad}\bigl(Y_\ell(a, b), \lfloor D_1 \rfloor\bigr) \le \frac{30 + C_M}{Y} \sum_{i=1}^{t} \sum_{a \in \mathrm{cbox}(\delta)} \dim Y_\ell\bigl(u_i(a), b\bigr). $$

**Theorem.** There is $C_M \ge 1$ such that for each datum $D$, all constants with $C_{Yb} \ge 2$, $C_b \ge 1$, $C_D \ge 0$, $C_0 \ge 1$, $C_{E1}, C_{E2} \ge 0$, and each instance $X$ with the window hypotheses `HI`, `RestTM` $C_M$ holds.

## Proof

`restTM_exists` gives $C_M = 1$ and the implication: `HI`, `RestFree`, `RestTMSize` and `RestTMEps` $C_M$ imply `RestTM` $C_M$. For each $(\delta, a, b, \ell)$ the code builds a model instance (`XMof`) with $E = Y\kappa$. Its constants are $\varepsilon_i = 2S_i/Y_i + (2\kappa + 2S_i\lambda/Y_i)/E$, with $S_i$ a number attached to tie $i$ (`InstM.Si`, not unfolded here) and $Y_i$ the length of a progression of tops. The statement `ModelLatticeRank`, which `alternative_mean_value_theorem` proves, bounds the mean of the bad counts over the progression by $\sum_i \varepsilon_i$ times the mean of the dimensions at the updated tops, and `restTM_of_rests` turns this into `RestTM`. The theorem proves the four inputs.

1. `segFacts` turns `HI` and the bounds on the constants into `SegFacts`, eleven numerical facts about $X$.
2. `restFree_proved` proves `RestFree`: $I(\delta, a)$ does not depend on $a \in \mathrm{cbox}(\delta)$.
3. `restTMSize_proved` proves `RestTMSize`, size bounds for the model instance (for example degrees at most $2a$).
4. `restTMEps_proved` proves `RestTMEps` $C_M$: $\varepsilon_i \le (30 + C_M)/Y$. First `epsFacts` gets $k^2Y^2 \le p$ and $kY^2b' \le a/2$ from `HI`. Then `restTMEps_of` shows $S_i/Y_i \le 7/Y$ (from `Yl_bound` and `S_bound`) and $24\lambda \le \kappa$. Last, `epsilon_bound_M_constant` is elementary: if $Y \ge 1$, $S_i/Y_i \le 7/Y$ and $24\lambda \le \kappa$, then
$$ \varepsilon_i \le \frac{14}{Y} + \frac{2}{Y} + \frac{2 \cdot 7 \cdot \frac{1}{24}}{Y} \le \frac{17}{Y} \le \frac{30 + C_M}{Y}. $$

## In the Lean code

The theorem is in [EpsilonBoundMConstant.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/EpsilonBoundMConstant.lean#L228), with `eps_num` at line 9, `epsilon_bound_M_constant` at line 33, `epsFacts` at line 46, `restTMEps_of` at line 89 and `restTMEps_proved` at line 224. `RestTM` is in [BlockBoundUniformiser.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockBoundUniformiser.lean#L134), `RestTMEps` in [ExponentMatrixFirstDepthEq.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ExponentMatrixFirstDepthEq.lean#L19), and the model constants $\varepsilon_i$ (`InstM.eps`) in [FlipOneThree.lean](lean:Formalism/SharpRestriction/GrowthBounds/FlipOneThree.lean#L389).

Odd points:

- The datum $D$ is bound as `_D` and does not occur in the conclusion. The proof passes it to `alternative_mean_value_theorem`, whose statement `ModelLatticeRank` also ignores it.
- The constant is $C_M = 1$, fixed by `restTM_exists`, because its proof `restTM_of` works only at $C_M = 1$.
- The bound $30 + C_M$ is loose: the proof gives $17$. The hypothesis $C_M \ge 1$ of `epsilon_bound_M_constant` is more than its proof needs.
