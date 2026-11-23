---
title: The closed form from the window condition
decls:
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_finite
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_coefficient_function
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_windows
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_dims
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_lattice
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_basis
  - Formalism.MainNotions.G.SymmetricFormBlocks.integralityFromMetric_of_orthBasisLat
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_splitting
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_splitting_matrix
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_minimal_vector
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The closed form from the window condition

This section finishes the reduction of the closed form of Theorem A. After Section 7 the remaining hypotheses are the orthogonal family, window and level dimension conditions and the base change property. We prove all of them except the window condition, and we derive the orthogonal family condition from the lattice results of Section 1. The final theorem says: if the two lattice inputs of Section 1 (the minimal vector and the diagonal count) hold, and the window condition holds for large constants, then the closed form holds. This is the form used by [Theorem 5.18](/entry/theorem-a-closed-form-holds/).

We keep the notation of Sections 6 and 7: $\Lambda_\ell$ is a level lattice of a block with $a_+ = 0$, $\beta^{\Phi}_\ell$ its tie pairing, $\beta^{a_+}_\ell$ the pairing at $a_+$, and $D_1 = D_1(C_M)$. Each proposition below has the shape: if the listed conditions hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants. We list only the conditions.

**Definition 7.8.1 (Further conditions).** Let $X$ be an instance. At each class $\delta$, box point $a_{\mathrm{top}} \in \operatorname{box}(\delta)$ and index $(b, \ell) \in I(\delta, a_{\mathrm{top}})$, consider:

1. (Symmetry.) $\beta^{\Phi}_\ell(u, v) = \beta^{\Phi}_\ell(v, u)$ for all $u, v \in \Lambda_\ell$.
2. (Finiteness.) $\Lambda_\ell$ is a finitely generated $\mathbb{Z}_p$-module, contained in a finite-dimensional $\mathbb{Q}_p$-subspace of the polynomial ring.

**Definition 7.8.2 (Coefficient maps).** Let $O$ be a domain with fraction field $K$ and $\iota : \mathbb{Q}_p \to K$ a ring map. A *coefficient map* is an additive map $f : K \to \mathbb{Q}_p$ with $f(\iota(a) x) = a f(x)$ for $a \in \mathbb{Q}_p$ and $x \in K$. It acts on polynomials over $K$ coefficient by coefficient. The *coefficient property* says: for every such $O$, $\iota$ and $f$, every word $L$ and all thresholds $J, M$, the coefficient map sends the highest weight space $Y(L, J, M)$ over $K$ into the highest weight space $Y(L, J, M)$ over $\mathbb{Q}_p$.

The coefficient property holds because the conditions that define $Y(L, J, M)$ are linear with rational coefficients in the coefficients of a polynomial, and $f$ is $\mathbb{Q}_p$-linear for the structure given by $\iota$; it also preserves the support of a polynomial in the letters.

**Proposition 7.8.3 (Orthogonal families from symmetry).** Assume the base change property and the Theorem (Orthogonal family) of Section 1 for all lattice settings. Conditions: symmetry, finiteness, window, level dimension.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_finite`.

*Proof.* The window hypotheses force $p \geq 3$, so $p \neq 2$. By finiteness and symmetry, $\Lambda_\ell$ with the pairing $\beta^{\Phi}_\ell$ is a lattice setting. The pairing is linear in its first variable, being a Fock pairing composed with linear operators. The Theorem (Orthogonal family) at depth $\lfloor D_1 \rfloor$ gives exactly the orthogonal family condition. Then the [Proposition (Levels from base change)](/entry/integrality-from-metric-of-orthogonality-window/) applies. $\square$

**Proposition 7.8.4 (Base change from coefficient maps).** Assume the coefficient property and the Theorem (Orthogonal family). Conditions: symmetry, finiteness, window, level dimension.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_coefficient_function`.

*Proof.* We show that the coefficient property implies the base change property. Let $y$ be an integral highest weight polynomial over $O$. Its coefficients span a finite-dimensional $\iota(\mathbb{Q}_p)$-subspace of $K$; choose a basis $x_1, \dots, x_k$ of it and coefficient maps $f_1, \dots, f_k$ with $f_a(x_b) = \delta_{ab}$, extended to $K$ through a complement. Then $y = \sum_a x_a\, \iota(f_a(y))$, and each $f_a(y)$ lies in $Y$ over $\mathbb{Q}_p$ by the coefficient property. Multiply each $f_a(y)$ by a power of $p$ to make it integral, and move the power into $x_a$. So $y$ lies in the $K$-span of $\iota(Y_{\mathbb{Z}})$. The previous proposition applies. $\square$

**Proposition 7.8.5 (Finiteness).** Assume the coefficient property and the Theorem (Orthogonal family). Conditions: symmetry, window, level dimension.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_windows`.

*Proof.* The finiteness condition holds for every instance: $\Lambda_\ell$ is generated by finitely many polynomials of one multidegree, so it lies in the finite-dimensional space of polynomials of that multidegree. Apply the [Proposition (Base change from coefficient maps)](/entry/closed-of-coefficient-function/). $\square$

**Proposition 7.8.6 (Level dimension).** Assume the coefficient property and the Theorem (Orthogonal family). Conditions: symmetry, window.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_dims`.

*Proof.* The level dimension condition holds for every instance. The generators of the standard lattice at level $\ell$ include the products of a basis of the highest weight space $Y_\ell$ with the $d_r(B - j_+)$ monomials of degree $B - j_+$ in the $r$ variables of the last letter. These products are linearly independent, because the highest weight polynomials do not involve those variables. So $\dim \operatorname{span} \Gamma_\ell(G) \geq \dim Y_\ell \cdot d_r(B - j_+) = r_L$. Apply the [Proposition (Finiteness)](/entry/closed-of-symmetric-windows/). $\square$

**Proposition 7.8.7 (Orthogonal family input).** Assume the Theorem (Orthogonal family). Conditions: symmetry, window.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_lattice` (also `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_basis`, with the orthogonal basis and the good count lemma in place of the Theorem (Orthogonal family)).

*Proof.* The coefficient property holds, by the remark after its definition, so the [Proposition (Level dimension)](/entry/closed-of-symmetric-dims/) applies. For the second form, the Proposition (Orthogonal basis) and the Lemma (Good count and an orthogonal basis) of Section 1 give the Theorem (Orthogonal family), as in its proof. $\square$

**Proposition 7.8.8 (Window condition alone).** Assume the Proposition (Orthogonal basis) and the Lemma (Good count and an orthogonal basis) of Section 1. Condition: window.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.integralityFromMetric_of_orthBasisLat`.

*Proof.* The symmetry condition holds for every instance. The pairing $\beta^{\Phi}_\ell$ is the Fock pairing with tie operators applied to one side; on the level lattice the operators are self-adjoint for the Fock pairing and commute, because the tie operators at distinct ties act on disjoint pairs of letters and $\Phi_{o,n,z}$ is a polynomial in $EF$, which is self-adjoint (Section 2). So $\beta^{\Phi}_\ell$ is symmetric on $\Lambda_\ell$. Apply the [Proposition (Orthogonal family input)](/entry/closed-of-orthogonal-basis/) in its second form. $\square$

**Theorem 7.8.9 (Closed form from the window condition).** Assume the Theorem (Minimal vector) and the Lemma (Diagonal count) of Section 1. If for large constants, for all $C_\kappa, C_s$, all $C_M \geq 1$ and all admitted instances $X$ satisfying the window hypotheses, the window condition holds at every class, box point and index, then the closed form of Theorem A holds for large constants.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_minimal_vector` (also `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_splitting_matrix` and `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_orthogonal_splitting`, which assume the splitting step in place of the minimal vector, and the second of which assumes the good count lemma in place of the diagonal count).

*Proof.* The minimal vector theorem gives the splitting step $L = \mathbb{Z}_p x \oplus L'$ of the proof of the Proposition (Orthogonal basis). The splitting step and the freeness of lattices give the Proposition (Orthogonal basis). The diagonal count gives the Lemma (Good count and an orthogonal basis). Then the [Proposition (Window condition alone)](/entry/integrality-from-metric-of-orth-basis-lat/) applies. $\square$

So the closed form rests on the window condition and on two facts about lattices over $\mathbb{Z}_p$ for odd $p$. The window condition is where the size of $Y$ enters: on average over $a_+ \in A$, an orthogonal family of $\beta^{\Phi}_\ell$ stays good for $\beta^{a_+}_\ell$ at depth $\lfloor Y D_1 \rfloor$, except on a share $5/Y$ of its vectors.

**Remark 7.8.10 (Formalization).** All ten theorems are compositions of one step each, in the order of the propositions, from `closed_of_minimal_vector` ([ClosedOfMinimalVector.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfMinimalVector.lean#L8)) down to `closed_of_symmetric_finite`. The step names do not match what they add: `symmetric_dims_of_windows` ([IntegralityFromMetricOfOrthBasisLat.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/IntegralityFromMetricOfOrthBasisLat.lean#L15)) adds the symmetry condition `symmCondition`, `windows_of_symmetric_dims` adds the level dimension condition `lvlDimCondition`, and `symmetric_finite_of_windows` adds finiteness `restLjjFin_proved`. The window condition `RestWinE` is stated for admitted instances (`AdmNoK`) with the window hypotheses `HI`. The prime is odd by `p25` inside `orthogonal_of_symmetric_finite`. The coefficient property is `RestFunY`, proved by `restFunY_proved`; the passage to the base change property `RestYbc` is `restYbc_of_funY` with `restDecomp_proved` and `restClear_proved`, and the proofs of the symmetry and level dimension conditions (`restSymm_of commCondition`, `lvlDimCondition`) were not opened; the proofs above are our arguments for what they state.
