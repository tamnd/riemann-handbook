---
id: lemma-model
title: The energy limit in the model setting
kind: theorem
decl: Formalism.FourierDecayAlt.P.lemma_model
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.IsAdmissibleSplittingCharPairMulTwist
covers: 1378
status: drafted
drafted_by: writer@claude
---
This theorem proves `LemmaEModel`: in the abstract model setting, a cutoff energy form has a limit as the cutoff parameter goes to $0$. It is an assembly. It fixes the two constants and gives the abstract energy lemma `LE.LemmaE` the model data. The abstract lemma has the real analytic content. The main user is [the carrier bound](/entry/carrier-p/), through `carrierP_of_compact_model`. [Each place of a built setting is a model place](/entry/model-place-built-holds/) shows that the real places satisfy the model conditions.

## Statement

Fix a parameter record $P$ with integers $k$ and $r$, an index $l$, level data $L$, a family $j$ of functions indexed by the types $\pi$, real numbers $\lambda_s$ for $s$ in a set of size $k + 2r + 1$, an interval $[\alpha, \beta]$, a cutoff $c$ and a length $N \ge r + 1$. For a list $w$ of pairs $(b, Y)$ with $b$ a Boolean and $Y$ real, let $E_\varepsilon(w)$ be `cutoffEnergyForm P l j c ε w`. This is the real part of an inner product of the cut function `chiJ P j c ε` with its image under a product of operators `C0` at the points $Y$ of $w$. We have not unfolded `chiJ`, `C0`, the action `actA` or the inner product `ipA`. Let $P_\lambda(Y) = \prod_s (Y + \lambda_s)$.

**Theorem.** There are constants $C_2 > 0$ and $C_6 > 0$ with this property. Suppose that the model conditions `HidaSetting`, `JDecay` and `JAdj` (both with order $2N + 2$) and `JEigen` hold, and that

$$C_6 \bigl(k N (r+1)^2 + N^2 (r+1)^2\bigr) \le \beta - \alpha.$$

Let $w$ have length at most $N$, with each point $Y$ in $[\alpha, \beta]$ and any two points more than $2$ apart. Then, as $\varepsilon \to 0^+$,

$$E_\varepsilon(w) \to \Bigl(\prod_{(b, Y) \in w} |P_\lambda(Y)|\Bigr) \int \sum_\pi |j_\pi(q)|^2 \, d\mu_0(q).$$

## Proof

The proof applies `lemma_model_of_parts` to nine proved facts. The main one is `le_E_proof`, which is `lemmaE_closed`, the proof of `LE.LemmaE`. The others are `constants_choice`, `induction_imports`, `family_imports`, `roots_outside`, `first_identity`, `jacobi_square_integrable`, `theorem_P` and `jacobi_norm`.

`lemma_model_of_parts` does the bookkeeping.

1. It takes $C_R$, $C_d$, $C_P$ from the step imports and puts $C_2 = 64(1 + 2e\sqrt{C_7})$, with $C_7$ built from these three, and $C_6 = 6 C_2$.
2. It sets the level bound $L_b = C_2 N (r+1)^2$. Then it checks $N \le L_b$ and $2 < L_b$, and it gets the two other interval conditions from `Constants`. So the full hypothesis `Hyps` holds.
3. It applies `LE.LemmaE` to the system `sysQ`. The result is the limit `EnergyLimit`, with the factor `jn` in place of the integral.
4. `jacobi_norm` rewrites `jn` as $\int \sum_\pi |j_\pi|^2 \, d\mu_0$.

## In the Lean code

The theorem is in [IsAdmissibleSplittingCharPairMulTwist.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/IsAdmissibleSplittingCharPairMulTwist.lean#L17977). `LemmaEModel` is in [StatementMA.lean](lean:Formalism/HermitianCurvature/StatementMA.lean#L771), `lemma_model_of_parts` in [SquareIntegrableGammaZetabarInv.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SquareIntegrableGammaZetabarInv.lean#L1043) and `LE.LemmaE` in [StatementLE.lean](lean:Formalism/HermitianCurvature/StatementLE.lean#L577).

The file name has no relation to the theorem. The file has 17,981 lines and `lemma_model` is at the end.

In `sysQ`, the field `principalHermitianLattice` holds `cutoffEnergyForm` ([StatementMA.lean](lean:Formalism/HermitianCurvature/StatementMA.lean#L486)). The field name does not describe its value.

The hypotheses can be met. `hypotheses_nonvacuous` ([SquareIntegrableGammaZetabarInv.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SquareIntegrableGammaZetabarInv.lean#L1076)) gives, for each $N \ge 1$ and $L_b \ge N$ with $L_b > 2$ and each bound $B$, data that satisfy `Hyps` with $j \neq 0$ and $\beta - \alpha \ge B$.
