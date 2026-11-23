---
id: half-of-printed-hida
title: No two Frobenius eigenvalues differ by a factor of square root p
kind: theorem
decl: UpperTheory.V.Z.Sym.Unl.half_of_printed_hida
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.THalfOf
covers: 642
status: drafted
drafted_by: writer@claude
---
This theorem proves `HalfOf` from the hypotheses $\mathrm{HypothesesH'}$. `HalfOf` says that the two-dimensional ordinary Galois representation of an eigenform has no pair of Frobenius eigenvalues whose absolute values differ by a factor $\sqrt p$. The private lemma [`core`](/entry/eg-core/) takes an eigenform $g$ whose eigenvalues are congruent to those of an Eisenstein series, and builds a twist $\rho$ of its Galois representation with four properties. `NoHalf ι ρ` is the fourth: `core` applies `twOk` to the output of this theorem. `core` feeds [`prop_eg_complex_of_printed_hida`](/entry/prop-eg-complex-of-printed-hida/).

## Statement

Let $\ell$ be a prime, $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ an isomorphism, $k \ge 3$ and $N \ge 1$. Let $\chi$ be a primitive Dirichlet character modulo $N$ and $g$ a normalized eigenform of weight $k$, level $\Gamma_1(N)$ and character $\chi$, with Hecke eigenvalues $a_p$. Suppose that each conjugate $\sigma(g)$, $\sigma \in \operatorname{Aut}(\mathbb{C})$, is a cusp form of character $\sigma \circ \chi$ (the condition `Cj`). Let $\pi$ be a cuspidal representation of $\mathrm{GL}_2$ over $\mathbb{Q}$ and $r \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ an ordinary representation attached to $\pi$ with $\det r = \bar\varepsilon^{1-k} \xi$ for a finite order character $\xi$ (the structure `OrdForm`). Suppose:

- at each prime $p$, the local component $\pi_p$ has a nonzero vector of level $p^{v_p(N)}$ on which $U_p$ acts by $a_p$;
- at each $p \nmid N$, $\pi_p$ has Satake parameters whose normalized Hecke polynomial is $X^2 - a_p X + \chi(p) p^{k-1}$.

**Theorem.** Under $\mathrm{HypothesesH'}$: for each prime $p \ne \ell$, each Frobenius element $s$ at $p$ and all eigenvalues $\alpha, \beta$ of $r(s)$, we have $|\iota\alpha|^2 \ne p\, |\iota\beta|^2$. This is `NoHalf ι r`.

## Proof

Suppose $|\iota x|^2 = p |\iota y|^2$ for two eigenvalues of $r(s)$. Then $x^{-1}$ and $y^{-1}$ are eigenvalues of $r(s^{-1})$.

1. **Case $p \mid N$.** `badAbs` gives $|a_p|^2 = p^{k-1}$. `tieU_a_alt` gives one eigenvalue of $r(s^{-1})$ of absolute value $|a_p|$. The determinant of $r(s^{-1})$ has absolute value $p^{k-1}$, since $\xi$ has finite order. So both eigenvalues have absolute value $|a_p|$, and $|x| = |y|$. This contradicts $p > 1$.
2. **Case $p \nmid N$.** `tieS_a_alt` says that the characteristic polynomial of $r(s^{-1})$ is $X^2 - a_p X + \chi(p) p^{k-1}$. If $x = y$, we get $p = 1$ again. Otherwise $\alpha = y^{-1}$ and $\beta = x^{-1}$ are its two roots with $|\alpha|^2 = p |\beta|^2$, and `goodHalf` excludes this.

The rest is bookkeeping.

## In the Lean code

The theorem is in [THalfOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/THalfOf.lean#L54). `HalfOf` and `NoHalf` are in [UnitFormC.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/UnlinkedHalfIntegral/UnitFormC.lean#L107). The lemmas it calls:

- `tieU_a_alt` and `tieS_a_alt` in [OrdWinA.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/OrdWinA.lean#L155). These are the only places where $\mathrm{HypothesesH'}$ is used. Both get the attached Galois representation from `exRS_alt` applied to the classical part of $\mathrm{HypothesesH'}$.
- `badAbs`, and `goodHalf` in [GoodHalf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/UnlinkedHalfIntegral/UnlinkedHeckeRoots/GoodHalf.lean#L12). `goodHalf` takes $\sigma \in \operatorname{Aut}(\mathbb{C})$ with $\sigma(\sqrt p) = -\sqrt p$, the conjugate eigenform, and the relation $\overline{a_p} \chi(p) = a_p$ for both forms, then applies `halfAlg`. We have not opened `halfAlg`, `selfAdj` or `conjEig`.
- Private helper lemmas in the same file: `quad_pair`, `charpoly_quad`, `inv_charpoly_root`, `norm_xi`, `det_inv`.

The proof is a line-for-line copy of `halfOf` in [HalfOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/UnlinkedHalfIntegral/UnlinkedHeckeRoots/HalfOf.lean#L59). The copy takes $\mathrm{HypothesesH'}$ in place of `HypothesesH` and calls `tieU_a_alt`, `tieS_a_alt` in place of `tieU`, `tieS`. The private helpers are copied too.
