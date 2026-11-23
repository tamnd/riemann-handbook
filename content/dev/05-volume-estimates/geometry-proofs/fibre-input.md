---
id: fibre-input
title: Heights of root lines as graded degrees of a Lie algebra flag
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.TopFibre.fibreInput
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.RootModelFlagHeight
covers: 518
status: drafted
drafted_by: writer@claude
---
This theorem proves the condition `Ht.FibreInput` for a root model $R$ that carries a Hodge component with a flag and root lines. At each algebraic point, it writes the heights of the lines of $R$ as the graded degrees of a flag in the Lie algebra of a semi-abelian scheme, up to a constant, and it bounds the maximal slope of that Lie algebra. Its one user is the renaming [`T.root_model_flag_height`](/entry/root-model-flag-height/). Through it the result feeds the bound `I5` in [`tower_good_of_sandwich_split`](/entry/tower-good-of-sandwich-split/).

## Statement

Let $R$ be a root model (`Top.RootModel`) for a CM type $\Psi$ and $N = p + q$. It has coordinates $y$, a variety $P$, and hermitian lines $x_{\tau, r}$ for $\tau \in \Psi$ and $r < N$. For a number field $L$ and an $L$-point $w$, write $h_{x}(w)$ for the height of $w$ for the line $x$ (`lineHt`). For a hermitian bundle $\mathcal{E}$ over $\mathcal{O}_{L'}$ and a saturated flag $0 = F_0 \subset \cdots \subset F_r$, write $\operatorname{gr}_i = \widehat{\deg}_n F_{i+1} - \widehat{\deg}_n F_i$, and $\mu_{\max}(\mathcal{E})$ for the maximal slope.

`FibreInput R` says: there is $C \geq 0$ such that for each number field $L$ and each $w \in P(L)$ there are a finite extension $L'$, a hermitian bundle $\mathcal{E}$ over $\mathcal{O}_{L'}$ and, for each $\tau$, saturated flags $W_\tau$ of length $p$ and $S_\tau$ of length $q$, with:

1. the tops of all the $W_\tau$ and $S_\tau$ are pairwise orthogonal, and $\#\Psi \cdot (p+q) = \operatorname{rank} \mathcal{E}$ (`IsOrthFull`);
2. $|h_{x_{\tau,i}}(w) - \operatorname{gr}_i(W_\tau)| \leq C$ for $i < p$;
3. $|h_{x_{\tau,p+i}}(w) + \operatorname{gr}_{q-1-i}(S_\tau)| \leq C$ for $i < q$;
4. $\mu_{\max}(\mathcal{E}) \leq C \log\bigl(2 + C + \max(-\widehat{\deg}_n \mathcal{E}, 0)\bigr) + C$.

**Theorem.** Assume `N1ab`, `PartI`, `ResKStatement`, `SemiAbelianHomExtension` and `SlopeBoundSt`. Let $\mathfrak{M}$ be a Hodge component over the coordinates of $R$, with a flag $\mathrm{Fl}$ whose graded pieces have the degrees of the lines of $R$ (`Fl.RootLines`), and let $N \geq 1$. Then `FibreInput R` holds.

## Proof

1. `exists_orthogonal_lie_metric` gives a metric $h$ on the Lie model of $\mathfrak{M}$, orthogonal for the action `𝔐.t.act` (the Lean `h.Orth`).
2. `hodge_cpt_lie_metric_bound` uses the five hypotheses. It gives $C_1 \geq 0$ such that at each integral point, after a finite extension, each hermitian bundle that is the Lie algebra with the metric $h$ satisfies clause 4 with $C_1$.
3. `flag_line_degree_formula` uses the root lines. It gives $C_2$ such that clauses 2 and 3 hold with $C_2$ for each flag pair whose pieces are the fibres of the flag $\mathrm{Fl}$.
4. Fix $L$ and $w$. `number_field_point_integral_model` extends $w$ to an $\mathcal{O}_L$-point $z_0$. Step 2 gives $L'$. `lie_metric_hermitian_bundle` gives the Lie algebra $\mathcal{E}$ at the point over $\mathcal{O}_{L'}$, with the metric $h$. `orthogonal_metric_flag_degree` gives a flag pair in $\mathcal{E}$ that satisfies clause 1 and matches $\mathrm{Fl}$.
5. Heights do not change under the extension $L'/L$ (`line_height_invariant_scaling`). Take $C = \max(C_1, C_2)$; the bound of clause 4 grows with $C$ (`logBound_mono`).

The rest is bookkeeping.

## In the Lean code

The theorem is in [RootModelFlagHeight.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/RootModelFlagHeight.lean#L78). `FibreInput` is in [ArchBetween.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ArchBetween.lean#L80). The lemmas, each in a file `<Name>Statement.lean` of the same folder:

- `T.exists_orthogonal_lie_metric` and `T.orthogonal_metric_flag_degree`;
- `T.hodge_cpt_lie_metric_bound`, the only use of the five hypotheses;
- `T.flag_line_degree_formula`;
- `T.number_field_point_integral_model`, `T.lie_metric_hermitian_bundle` and `T.line_height_invariant_scaling`.

The file also proves `coordsAt_comp` and `valAt_comp`, which move point coordinates along a field map. The set of primes $S$ of $\mathfrak{M}$ is arbitrary, and [the user](/entry/tower-good-of-sandwich-split/) takes $S = \emptyset$. We have not unfolded the proofs of the seven lemmas.
