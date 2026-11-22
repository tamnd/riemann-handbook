---
id: theorem-i-of-pairing-gl
title: The base-level projection bound from a GL-invariant pairing
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_pairing_GL
module: Formalism.SharpRestriction.GrowthBounds.HermitianTensor.ModelIdentificationHolds
covers: 1259
status: drafted
drafted_by: writer@claude
---
This theorem reduces `SecondPartClosed D` to the pairing statement `QPh`. Its only caller is [the base-level projection bound for large constants](/entry/theorem-i-closed-form-holds/), which proves `QPh` and states `SecondPartClosed D` in full. The proof is a chain of reductions. It takes one tool, `CartanOnto`, out of the hypothesis and passes it on with `QPh`.

## Statement

Let $(W, Q, O, K, \iota, \sigma, w)$ be an `UnramifiedQuadraticSetting` for $p$ and $n'$ (the record `RS`). For a weight $\nu \in \mathbb{N}^r$, let $S_\nu \subset K[X_{ij}]_{1 \le i,j \le r}$ be the polynomials of column weight $\nu$ that are invariant under the column operations $X_{\cdot j} \mapsto X_{\cdot j} + c X_{\cdot l}$ for $l < j$ (`dualWeyl`), and let $S_\nu^O$ be the image of the same space over $O$ (`intO`). The group $\mathrm{GL}_r(K)$ acts on the rows (`rowAct`). Write $f \otimes f'$ for the product of $f$ in one set of variables and $f'$ in a second set (`blockEmb`).

`QPh` says: for $r \ge 1$, natural numbers $a, c, N$, and a decreasing $\alpha \in \mathbb{N}^r$ with $\alpha_i \le N$, $\alpha_i \le \alpha_j + c$ and $c \le 8a$, put $\alpha^\vee_i = N - \alpha_{r+1-i}$. Then there is a $K$-linear form $\Lambda$ on polynomials in the two sets of variables such that:

1. $\Lambda(gf \otimes gf') = \det(g)^N \Lambda(f \otimes f')$ for $g \in \mathrm{GL}_r(K)$, $f \in S_\alpha$, $f' \in S_{\alpha^\vee}$;
2. $\Lambda(f \otimes f') \in O$ for $f \in S_\alpha^O$, $f' \in S_{\alpha^\vee}^O$;
3. there are $n_b$ elements $u_b \in S_\alpha^O$ and $u'_b \in S_{\alpha^\vee}^O$, with $n_b$ the Weyl dimension of $\alpha$, and exponents $k_b \le \lceil \kappa_1(p, a, r+1) \rceil$ (`kappaOneExponent`), with $\Lambda(u_b \otimes u'_{b'}) = p^{k_b}$ if $b = b'$ and $0$ otherwise.

**Theorem.** For each datum $D$, if `QPh` holds, then `SecondPartClosed D` holds.

## Proof

Assume `AdmBE D`. Specialize it at $C_c = 0$ and at the smallest allowed constants. This gives `AdmB D`. Its fifth conjunct is `AdmT D`, the seventh tool of `AdmT D` is `GradedLatticeStable D`, and its second half is `CartanOnto`.

1. `contraction_of_pairing_GL` turns `QPh` and `CartanOnto` into `ContractionStandardLattice`. Let $\lambda \in \mathbb{Z}^{m+2}$ be decreasing with $\lambda_1 = P + c$, $\lambda_{m+2} = -(Q + c)$ and $|\lambda_i| \le c$ in between, put $\omega_{P,Q} = (P, 0, \dots, 0, -Q)$ and $\mu^*_i = -\mu_{m+3-i}$, and index $S$ by weights shifted to end in $0$ (`nuOf`). The statement gives a $\mathrm{GL}$-equivariant map from $S_\lambda \otimes S_{(\lambda - \omega_{P,Q})^*}$ into $S_{\omega_{P+2c,Q+2c}}$, integral on the lattices, and families $s_b, s'_b$ with $F s_b \otimes s'_{b'} \mapsto \delta_{bb'} p^{k_b} h F$ for $F \in S_{\omega_{P,Q}}$ and a fixed polynomial $h$ (`hw`). It calls `contraction_of_pairing_lemmas` with fourteen further lemmas.
2. `theorem_I_of_contraction` applies `theorem_I_of_two_letter_clauses_contraction` with `explicit_map_injective`, `explicit_map_onto_two_letter_space` and `two_letter_lattice_gauss_inverse`. That theorem takes three tools from `AdmBE D` again and builds `TiePsi` (by `tiePsi_of`) and `RestCloudMaps` (by `cloud_maps_of_contraction`).
3. These go to `theorem_I_of_explicit_minor_map`. A chain of five reductions in [TheoremIOfLatticeFunctorComparison.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TheoremIOfLatticeFunctorComparison.lean#L70) ends in `theorem_I_of_intermediate_bounds`.

We have not followed the chain past `theorem_I_of_intermediate_bounds`.

## In the Lean code

The theorem is in [ModelIdentificationHolds.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/ModelIdentificationHolds.lean#L25). `QPh` is in [CoeffSumMonomialLinear.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/CoeffSumMonomialLinear.lean#L77), and `ContractionStandardLattice` in [CloudADef.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/CloudADef.lean#L17).

Odd points:

- `CartanOnto` comes from the hypothesis `AdmBE D`, but it is also proved outright as `cartanOnto_proved` in [Cartan.lean](lean:Formalism/LocalToGlobal/GroupLattices/FockModels/Cartan.lean#L263). The theorem could take it from there.
- The name says "GL". The only GL in the statement is the equivariance of $\Lambda$ in `QPh`.
- The specialization at $C_c = 0$ differs from `tools_of_admitted_statements`, which uses $C_c = 4$. Both are allowed, as `AdmBE` asks $C_c \ge 0$.
