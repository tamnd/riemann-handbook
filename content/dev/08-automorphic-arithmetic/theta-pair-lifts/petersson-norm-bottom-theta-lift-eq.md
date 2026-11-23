---
id: petersson-norm-bottom-theta-lift-eq
title: The norm of a bottom pair from the Rallis inner product formula
kind: theorem
decl: GlobalTheory.NormRatio.petersson_norm_bottom_theta_lift_eq
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.ThetaLiftPeterssonNormEqRallisIntegral
covers: 367
status: drafted
drafted_by: writer@claude
---
This theorem computes the norm of the large member of one bottom pair: an explicit constant times a product of values of a Hecke L-function. Two lemmas use it, one for the nonvanishing of the norm and one for the ratio of norms at two points. Both go into [the proof of `NormBig`](/entry/norm-big-alt/). The main input is an inner product formula for theta lifts between two anisotropic Hermitian spaces.

## Statement

Notation is as in [the entry above](/entry/norm-big-alt/): $(P, P')$ is a bottom pair at $t$ for the stage $(i, j)$, $\|P\|$ is the norm of $P$, and $e_0, h_0$ are fixed by the ranks of the stage. $P$ has ranks $a \le d$ and a weight vector $n$.

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), `Inp D`, and `Rec L` for size data $L$ of $D$. Let $G$ be a grid over a level character with base point $\mu$. Let $(P, P')$ be a bottom pair at $t$ for the ideal `modT G t`, and let $\Lambda$ be an L-function of $\nu_H(t, i, j)$: an entire function equal to $\prod_v (1 - \nu_H(v) Nv^{-s})^{-1}$ for $\operatorname{Re} s > 1$, the product over unramified $v$. Then

$$\|P\| = N(\delta, t_0, a, d, n) \prod_{s = 1 - e_0}^{h_0} \Lambda(s),$$

$$N(\delta, t_0, a, d, n) = \frac{c(a, n)\, m(d)\, m(a)\, F(a, d, n)\, v(\delta, t_0, a, d)}{\Delta(a, d; \tfrac{d-a}{2})}.$$

Here $m(d) = \sum_h |\Gamma_h|^{-1}$ is the mass of the classes at the maximal integral level (`mass`), and $c$, $F$, $v$ and $\Delta$ are `normConst`, `fockSum`, `vacNorm` and the normalizing factor `dSfun` with an empty set of places. We have not unfolded these four.

## Proof

1. `goodMod_modT` shows that `modT G t` is a good modulus.
2. `exact_dictionary` gives a theta datum $X$ with Hermitian spaces $A$ of rank $a$ and $B$ of rank $d$. It writes $\|P\|$ as $c(a, n)$ times an index $[K : J]$ times $\sum_T \langle \theta(\varphi_T), \theta(\varphi_T) \rangle$, a sum of Petersson norms of theta lifts to $B$.
3. `heckeCharEq_of_finitePart_power_inverse` identifies the character of $B$ with $\nu_H(t, i, j)$. Then `squareNu_unramified_off_pair_partial_L_primitive` makes the values of $\Lambda$ the values of the partial L-function of $\chi_B^{-1}$.
4. `theta_lift_petersson_norm_eq_rallis_integral` (the same file, line 38) computes each Petersson norm: $m(d)\, m(a)$ times $\prod_{k < a} \Lambda(\tfrac{d}{2} - k)$ over a partial normalizing factor, times local terms. It calls `rallis_inner_product_bottom_norm_eq` with Witt index 0 for $A$ and $B$, and `volQ_eq_mass` for the volumes.
5. Since $d = 2h_0$ and $a$ is the rank `botBig`, the values $\tfrac{d}{2} - k$ for $k < a$ run over the integers from $1 - e_0$ to $h_0$.
6. `localIndex_localNorm_normalizingFactor_eq_partial` links the index, the local norm and the two normalizing factors. The lemma `collect` does the rest of the algebra.

Step 4 has the shape of the Rallis inner product formula (S. Rallis, Compositio Math. 52, 1984): the norm of a theta lift is L-values times local integrals. We have not compared the Lean proof with that source.

## In the Lean code

The theorem is at [ThetaLiftPeterssonNormEqRallisIntegral.lean line 74](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftPeterssonNormEqRallisIntegral.lean#L74). `normFactor` is in [HeckeLFunctionBottomPair.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeLFunctionBottomPair.lean#L367). Its users are `big_theta_petersson_norm_ratio_eq` (line 115) and `big_theta_petersson_norm_ne_zero` in [BigThetaLiftNeZeroOfPeterssonNorm.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BigThetaLiftNeZeroOfPeterssonNorm.lean#L12).

Odd points:

- `norm_bottom` in [HeckeLFunctionBottomPair.lean line 378](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeLFunctionBottomPair.lean#L378) has the same statement and almost the same proof, with the hypothesis `Hypotheses₂` in place of `ThetaLocalInputs`.
- The name speaks of a Petersson norm. The left side is `Pair.norm`, a weighted sum over classes. It is a Petersson norm only through step 2.
