---
id: one-char-unram-u
title: The bound for one character, with unramified coefficients
kind: theorem
decl: oneChar_unramU
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.FOneCharU
covers: 437
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound of [the bound for one character](/entry/one-char-u-of-kato-two-w-rig-adm-i-automorphy/) when the coefficient ring $\mathcal{O}$ has ramification index $e_{\mathcal{O}} = 1$. That theorem reduces the general case to this one. Here the work is done: a deformation ring is built from the character, its length is compared with the Selmer type length $V$, and its points give the representations in the set $X$.

## Statement

We use the notation of [the parent entry](/entry/one-char-u-of-kato-two-w-rig-adm-i-automorphy/): $K$, $\ell$, $\mathcal{O}$, $N$, $e$, $\psi$, $\Psi = \chi_{\mathrm{cyc}}^e \psi$, $\mathrm{GD}$, $V$, $V_n$, $t$ and admissible $\rho$.

**Theorem.** Assume $\mathrm{CohInp}$, $\mathrm{LemmaM}$, $\mathrm{LemmaM'}$, $\mathrm{LemmaP}$, $\mathrm{KatoTwoW}$, the two rigidity statements, $\mathrm{AdmI}$ and $\mathrm{AutomorphyUnramifiedCoefficientsAlt}$. Let the data satisfy $\mathrm{GD}$ and $e_{\mathcal{O}} = 1$. Let $\sigma \in G_K$ and suppose that $\operatorname{tr}\rho(\sigma) \ne t$ for each admissible $\rho$. Then $V < \infty$, and there is a finite set $X$ of pairwise non-isomorphic admissible $\rho$ with $V_n \le 2 \sum_{\rho \in X} v_\ell(\operatorname{tr}\rho(\sigma) - t)$.

## Proof

1. **Data.** `U3.exists_dat` builds a datum $D$ from $\mathrm{GD}$: the quadratic character $\eta$ of $G_{\mathbb{Q}}$ with kernel $G_K$, a complex conjugation, a decomposition group at $\ell$, and the local properties of $\Psi$. The hypothesis $\mathrm{AutomorphyUnramifiedCoefficientsAlt}$ applies since $e_{\mathcal{O}} = 1$. It gives a marked element $g_1$, a finiteness statement and two automorphy statements.
2. **The ring.** `exists_uLoc`, `exists_ring` and `exists_model` build an $\mathcal{O}$-algebra $R$ with a universal representation $r$ of $G_{\mathbb{Q}}$ with multiplier $\eta$. `exists_model` uses $\mathrm{LemmaP}$. Each point $f \colon R \to \overline{\mathbb{Q}}_\ell$ gives a representation $\rho_f$ of $G_K$, and `trace_reducible_three_dim` writes $\operatorname{tr}\rho_f(\sigma) - t$ as the image under $f$ of one element of $R$. Here $\eta(\sigma) = 1$ since $\sigma \in G_K$.
3. **Points are admissible.** By `twoPt_shape`, a point with the property `TwoPt` is of type I or type II. Type I points are admissible by $\mathrm{AdmI}$. Type II points are admissible by `adm2B_rhoK_of_typeII_of_modular_extensions`. So the trace hypothesis says that the trace difference is nonzero at each such point.
4. **Upper bound for $R$.** `U3.model_upper` takes $\mathrm{LemmaM}$, the finiteness, the point hypothesis and the nonzero trace differences. It gives that the length $L$ of a module of $R$ is finite, a finite set of points, and $L_n \le 2\sum v_\ell(\operatorname{tr}\rho_f(\sigma) - t)$ over that set. The point hypothesis comes from `ptHyp_of_autB_of_lemW_of_isBase`, which uses $\mathrm{CohInp}$, $\mathrm{KatoTwoW}$ and the two rigidity statements.
5. **Comparison.** `U3.vlen_le` uses $\mathrm{CohInp}$ and $\mathrm{LemmaM'}$ to give $V \le L$. So $V < \infty$, and `Chr.nrm_mono` gives $V_n \le L_n$.
6. **Distinct points.** `twoPt_shape` shows that distinct points of the set give non-isomorphic $\rho_f$. So $X = \{\rho_f\}$ is a set of pairwise non-isomorphic admissible representations.

## In the Lean code

The theorem is a private lemma in [FOneCharU.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean#L19), in the root namespace. The main lemmas:

- `U3.exists_dat` in [ExistsDat.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/ExistsDat.lean#L134).
- `U3.model_upper` in [ModelUpper.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/ModelUpper.lean#L103).
- `U3.vlen_le` in [VlenLe.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/VlenLe.lean#L52).
- `ptHyp_of_autB_of_lemW_of_isBase` in [FPtHypU.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FPtHypU.lean#L15).

We have not unfolded the ring of `exists_ring`, the properties `TwoPt` and `PtHyp`, or the proof of `model_upper`. $\mathrm{LemmaM}$ and $\mathrm{LemmaM'}$ are statements of commutative algebra that bound a length by $2\sum v(\xi(a))$, in [OrbitVanishingLocal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/OrbitVanishingLocal.lean#L111). Each hypothesis is used. A private lemma with the same name `oneChar_unramU` and older hypotheses is in [OneCharU.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/WeightInfinitesimalCharacters/OneCharU.lean#L12), and `oneChar_unram` in [OneCharOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/OneCharOf.lean#L102) has the same shape.
