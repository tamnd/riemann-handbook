---
id: theorem-a-closed-form-holds
title: The averaged bad-share bound for large constants
kind: theorem
decl: Formalism.MainNotions.G.GramWindowAlt.theorem_A_closed_form_holds
module: Formalism.SharpRestriction.GrowthBounds.FockGramWindow
covers: 3015
status: drafted
drafted_by: writer@claude
---
This theorem proves `IntegralityFromMetricForLargeConstants D` for each datum $D$ and fills the field `p13A` of `Loc8All` and `Loc8`. Both children of the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/) reach it. It supplies three lattice statements to [`closed_of_minimal_vector`](/entry/closed-of-minimal-vector/), and the chain of reductions below that entry does the rest.

## Statement

An *instance* $X$ (`Inst`) has local data $L$ (`Loc`, not unfolded here) with a prime $p$ and a rank $r \ge 1$, two discrete valuation rings in an `UnramifiedQuadraticSetting`, a segment index and reals $m, x_a, x_b$. From $L$ and constants $C_0, C_{E1}, C_{E2}$ the code builds segment data with a length $s$ and a number $t$ of ties, and the window $A = \{a, \dots, \lfloor a + a/(kY) + x_a \rfloor\}$.

For a lattice $\Lambda$ over $O$ with a pairing $\beta$ and a depth $D'$, the *bad share* is

$$ \mathrm{bad}(\Lambda, D') = \frac{\operatorname{rk}\Lambda - \max \operatorname{rk}\Lambda_1}{\operatorname{rk}\Lambda}, $$

where $\Lambda_1$ runs over saturated sublattices (`SatIn`) whose primitive vectors $u$ have partners $u' \in \Lambda$ with $\beta(u,u')$ of depth at most $D'$ (`vLE`; neither unfolded here). The code takes the segment lattice $\Lambda(a_{\mathrm{top}}, a_+)$ (`segLat`), the form `segForm` (a weighted sum of a pairing `fock`) and the depth

$$ D' = C\,Y^2 N_1^2 (r+1)^2 \lambda + 4 N_t (r+1) \log_p a, \qquad \lambda = \log_p(8a+r) + 1. $$

**Theorem.** For each datum $D$ the following holds. For each $C_c \ge 0$ there is $T_0 > 0$; for each $C_0 \ge T_0$ there is $T_1 > 0$; for all $C_{E1}, C_{E2} \ge T_1$ there is $T_2 > 0$; for all $C_{Yb}, C_{de}, C_k, C_D, C_b \ge T_2$ and all $C_\kappa, C_s$ there is $C > 0$ such that each instance $X$ with `admitted` and with the window hypotheses `HI` satisfies

$$ \frac{1}{|A|^{s+1}} \sum_{a_{\mathrm{top}} \in A^s} \sum_{a_+ \in A} \mathrm{bad}\bigl(\Lambda(a_{\mathrm{top}}, a_+), D'\bigr) \le \frac{C (t+1) N_1}{Y}. $$

`HI` bounds the parameters of $L$ (`WindowHypotheses`, `CBound`, and bounds on $x_a, x_b, m$). `admitted` has eleven conjuncts: projectors on chain polynomials that are integral after multiplication by $p^{\lceil r^2\lambda \rceil}$ (two), highest weight lattices (one), Borel-equivariant functions on $\mathrm{GL}_{r+1}$ (four), a span of polynomials `Psi` (one), and bounds on dimensions and ranks of segment blocks (three).

## Proof

The proof is `closed_of_minimal_vector D PI.exists_minimalNormVector diagonal_rank_bound (restWinE_proved D)`.

1. **Minimal vector** (`OrthMin`). For $p$ odd, a lattice with a symmetric pairing $B \ne 0$ has $x$ with $B(x,x) \ne 0$ and $B(u,x) \in \mathbb{Z}_p B(x,x)$ for all $u$. Take generators $a, b$ with $|B(a,b)|_p$ maximal; as $|2|_p = 1$, one of $a$, $b$, $a+b$ works.
2. **Diagonal rank** (`GoodLeSmallMat`). If $U \operatorname{diag}(c) V^{T} = p^{e} I_n$ with $U, V$ integral, then $n \le \#\{a : c_a \ne 0,\ v_p(c_a) \le e\}$. The proof reduces to $U \operatorname{diag}(s) V^T = I - pN$, whose determinant is $1$ modulo $p$.
3. **Window count** (`restWinE_proved`, the statement `RestWinE D`). From `HI`, `restWin_of_lvl` combines the shift bound `winLvl` with `restWinNum_proved`. It bounds the sum over $a_+ \in A$ of the bad counts of an orthogonal family of size $n_1$ by $5|A| n_1/Y$.

We have not followed the chain past [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/).

## In the Lean code

The theorem is in [FockGramWindow.lean](lean:Formalism/SharpRestriction/GrowthBounds/FockGramWindow.lean#L24), with `restWinE_proved` at line 12. The statement is in [FlipOneThree.lean](lean:Formalism/SharpRestriction/GrowthBounds/FlipOneThree.lean#L321).

Odd points:

- The datum $D$ is never used: `Conclusion1` and all conjuncts of `admitted` take it as `_D`.
- Four conjuncts of `admitted` (`ArchimedeanSignatureMatching`, `adm5`, `adm6`, `adm7`) do not mention $X$ or the constants. If one is false, no instance is admitted and the theorem is vacuous. We have not checked them.
- `restWinE_proved` drops its hypothesis `AdmNoK` (line 15).
