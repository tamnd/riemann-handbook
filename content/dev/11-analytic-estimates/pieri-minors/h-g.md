---
id: h-g
title: The graded Lemma D from the Pieri inputs over the rationals
kind: theorem
decl: Formalism.CohomologicalDescent.Down.hG
module: Formalism.PieriBlockIdeals.PieriColumnMinors.CorollaryOfParamsLinkage
covers: 593
status: drafted
drafted_by: writer@claude
---
This theorem proves the graded Lemma D: a bound on the power of $l$ that moves a weight space of a dual Weyl module into the Weyl module, for block weights. It only combines three lemmas. [The lattice inclusion at the short weight bound](/entry/down-inclusion-w-real-holds/) gives it as the hypothesis of `ShortWeightBounds.inclusion_w_real_holds`.

## Statement

Let $r \ge 1$ and $\nu \in \mathbb{N}^r$. Let $\nabla(\nu) \subset \mathbb{Z}[x_{ab}]$ be the polynomials in an $r \times r$ matrix of column weight $\nu$ that are invariant under adding $t$ times column $s$ to column $j$ for $s < j$, with $t$ an indeterminate (`dualWeyl`). Let $\Delta(\nu)$ be the span of the images of the product of leading principal minors (`hw`) under the divided row operators (`weyl`). For a row weight $\mu$ and $e \in \mathbb{N}$, say $E_l(\nu, \mu, e)$ (`ExpLe`) if for each $x$ of row weight $\mu$ in $\nabla(\nu)$ there is $m \in \mathbb{Z}$ prime to $l$ with $m\, l^e x \in \Delta(\nu)$.

Fix $p, q, w$ and a partition $\lambda_2 = (\lambda_2(1) \ge \dots \ge \lambda_2(q))$ with all parts at most $w$. Let $\nu = (w, \dots, w, \lambda_2) \in \mathbb{N}^{p+q}$, with $p$ entries $w$ (`blockWt`). For $\xi \in \mathbb{Z}^{p+q}$ put $d_\xi(\mu) = \sum_a \xi_a (\nu_a - \mu_a)$ (`depth2`). For $i \in \mathbb{N}$ let $D_i$ be the integer $\prod_c (w - c)^{m_i(c)}$ (`Dn`). Here $c$ runs from $-q$ to $w + i - 1$, and $m_i(c)$ is the largest number of boxes of content $c$ in a skew diagram $\tau / \lambda_2$ with $i$ boxes, at most $p$ boxes in each column and no box of content $w$ (`mu`, `shapes`).

**Theorem.** Let $l$ be prime and $\xi$ nonincreasing. Let $i' \in \mathbb{Z}$ and $e_L \in \mathbb{N}$. Suppose that $E_l(\lambda_2, \mu_2, e_L)$ holds in $\nabla(\lambda_2)$ for $\mathrm{GL}_q$ for each $\mu_2$ with $d_\xi(w, \dots, w, \mu_2) \le i'$. Then $E_l(\nu, \mu, e_L + v_l(D_i))$ holds for each $\mu$ and $i$ with $\mu_1 + \dots + \mu_p + i = pw$ and $d_\xi(\mu) \le i'$.

## Proof

The proof term is

```
LR.real_of_pieri LPR.pieri_real_form (ColumnMinorsFromPieri.columns_real_of_pieri_real LPR.pieri_real_form)
```

Let $V = \nabla_{\mathbb{Q}}(\nu)$, with the polarization operators $E_{ab} = \sum_j x_{aj}\, \partial / \partial x_{bj}$ (`EV`). Let $W_0 \subseteq V$ be the subspace killed by $E_{\alpha a}$ for $\alpha$ in the first block and $a$ in the second, and on which $E_{\alpha\beta}$ acts as $w\,\delta_{\alpha\beta}$ (`W0`). The operators $E_{bb'}$ of the second block act on $W_0$.

1. `pieri_real_form` proves `PieriReal`: for each $n$, the path spaces of all shapes $\tau$ span the $n$-fold tensor space built on $W_0$. It applies `pieri_generated` with `real_form_modular` and `real_form_generation`.
2. `columns_real_of_pieri_real` turns `PieriReal` into `ColumnsReal`: symmetrization (`toSym`) kills the path space of each $\tau$ for which $\tau / \lambda_2$ has a column of more than $p$ boxes. It is `LC.columns_from_pieri`.
3. `real_of_pieri` turns these two facts into the theorem. It is `real_of_skeleton coefficient_word lower_triangular_integral`. The real content is in `real_of_skeleton`, which applies `depth_skeleton_third_form_holds` to $W_0$ with the normalized Fock pairing `formB`.

We have not unfolded the path spaces (`PathSpace`) or `depth_skeleton_third_form_holds`.

## In the Lean code

The theorem is in [CorollaryOfParamsLinkage.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/CorollaryOfParamsLinkage.lean#L9). It calls:

- `LR.real_of_pieri`, in [RealOfSkeleton.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/RealOfSkeleton.lean#L82);
- `LPR.pieri_real_form`, in [IrreducibleGeneration.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/IrreducibleGeneration.lean#L244);
- `ColumnMinorsFromPieri.columns_real_of_pieri_real`, in [ColumnsPieriSkeleton.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/ColumnsPieriSkeleton.lean#L24).

`LemmaDGraded` is in [StatementLD.lean](lean:Formalism/PieriBlockIdeals/StatementLD.lean#L63). The file of `hG` also derives `hLG`, `hL` and `hD`, the other forms of Lemma D, from it.

`real_of_skeleton` does not use its hypothesis `LowerTriIntegral` (the binder is `_hL`). So `lower_triangular_integral` is passed but plays no part. The name `hG` reads like a local hypothesis.
