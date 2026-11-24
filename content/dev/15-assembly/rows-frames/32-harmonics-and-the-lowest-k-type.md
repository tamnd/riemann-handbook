---
title: Harmonics and the lowest K-type
decls:
  - GlobalTheory.T.howeDuality_compactPair_polynomialFock_allRealPlaces
  - GlobalTheory.HoweCompactAlg.mem_of_equivariant
  - GlobalTheory.T.unitary_basis_general_linear_series
  - GlobalTheory.LowestKType.lowestKType_irreducible
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Harmonics and the lowest K-type

This section proves the algebraic form of compact Howe duality that [the irreducibility theorem of Section 31](/entry/howe-irr/) uses. The statement is about polynomials only: a compact group acts on a polynomial ring through unitary matrices, a Lie algebra acts by differential operators, and the two actions commute. The proof follows the method of harmonic polynomials. A nonzero invariant space of maps contains a harmonic map, the harmonic maps of a given type form an irreducible module of the maximal compact subalgebra, and every map of the given type is obtained from harmonic maps by raising operators.

### The polynomial Fock model

Let $n$ and $m$ be integers, and let $\mathcal{P}$ be the polynomial ring over $\mathbb{C}$ in the variables $x_{\tau, a, b}$, with $\tau$ an archimedean index, $a < m$ and $b < n$. A *weight* $w$ gives an integer $0 \leq p_\tau \leq m$ for each $\tau$. Let $B$ be a basis, and let $\mathrm{GL}$ be the product over $\tau$ of the groups $\mathrm{GL}_n(\mathbb{C})$. The *Fock action* $\mathrm{Fock}(g)$ of $g \in \mathrm{GL}$ on $\mathcal{P}$ is the action by linear substitution in the indices $b$, read in the basis $B$ and twisted by the weight.

For $\tau$ and a complex $m \times m$ matrix $Z$, the operator $T_\tau(Z)$ on $\mathcal{P}$ is the Fock operator of $Z$ at $\tau$ with the signs $\varepsilon_a = +$ for $a < p_\tau$ and $\varepsilon_a = -$ otherwise. For the matrix unit $E_{a b}$ it is a multiplication operator, a derivation, or a mixed second order operator, according to the signs of $a$ and $b$. We distinguish:

1. the *lowering operators* $T_\tau(E_{a b})$ with $a \geq p_\tau > b$;
2. the *compact operators* $T_\tau(E_{a b})$ with $a < p_\tau$ if and only if $b < p_\tau$.

The compact operators span the action of the complexified Lie algebra of $U(p_\tau) \times U(m - p_\tau)$, the maximal compact subgroup of $U(p_\tau, m - p_\tau)$. A polynomial is *jointly harmonic* if every lowering operator at every $\tau$ kills it.

Let $K$ be a group with a homomorphism $r \colon K \to \mathrm{GL}$ such that $r(k)$ is unitary in the basis $B$ at every $\tau$, and $r$ maps onto the group of all such elements. Let $W$ be a finite-dimensional irreducible representation $\rho$ of $K$. A linear map $\psi \colon W \to \mathcal{P}$ is *equivariant* if $\psi(\rho(k) x) = \mathrm{Fock}(r(k))\, \psi(x)$ for all $k$ and $x$. It is *jointly harmonic* if each $\psi(x)$ is.

### The lowest K-type

**Theorem 7.32.1 (The lowest K-type is irreducible).** Let $n, m, w, B, K, r$ and $(W, \rho)$ be as above. Let $S$ be a nonzero space of linear maps $W \to \mathcal{P}$ such that every $\psi \in S$ is equivariant and jointly harmonic, and $S$ is stable under $\psi \mapsto T_\tau(E_{a b}) \circ \psi$ for every compact operator. Then $S$ contains every equivariant jointly harmonic map $\varphi \colon W \to \mathcal{P}$.

Lean: `GlobalTheory.T.unitary_basis_general_linear_series` (also `GlobalTheory.LowestKType.lowestKType_irreducible`).

*Proof.* Let $\varphi$ be equivariant and jointly harmonic. We may assume $\varphi \neq 0$.

1. A nonzero equivariant map is injective, since its kernel is a $K$-stable subspace of the irreducible $W$.
2. Take $s \in S$ with $s \neq 0$. The span of the values of $s$ and $\varphi$ under the compact operators is a finite-dimensional space: the compact operators preserve the total degree, and the degrees of $s$ and $\varphi$ are bounded by some $d$. So all the work takes place in the polynomials of total degree at most $d$.
3. The Fock inner product on $\mathcal{P}$ is positive definite, and for it the adjoint of $T_\tau(E_{a b})$ is $T_\tau(E_{b a})$ on the compact part. So the compact operators generate a semisimple action on the finite-dimensional space of step 2, and every stable subspace has a stable complement.
4. The values of $s$ contain a highest weight vector for the compact operators, of a highest weight $\lambda$, and there is a vector $w_0 \in W$ whose image is such a vector.
5. The highest weight theory gives a map from the $K$-type of $\lambda$ into the space of step 2, with image $U$ in $S$.
6. The jointly harmonic polynomials of highest weight $\lambda$ that carry the type $W$ under $K$ occur with multiplicity one. So $\varphi$, which is jointly harmonic of the same type, lies in $U$.

So $\varphi \in S \cap U = U \subseteq S$. $\square$

The multiplicity one of step 6 is the point of the theorem. It is the theorem of Kashiwara and Vergne on harmonic polynomials: under the compact pair $(K, U(p) \times U(m - p))$ the space of jointly harmonic polynomials is multiplicity free, and the $K$-type determines the type of the maximal compact subgroup. The Lean proof gives it as the lemma `jointHarmonic_highestWeight_multiplicity_one`; we have not opened that lemma.

### Membership from harmonics

**Theorem 7.32.2 (Howe duality in the polynomial Fock model).** Let $n, m, w, B, K, r$ and $(W, \rho)$ be as above. Let $M$ be a nonzero space of linear maps $W \to \mathcal{P}$ such that every $\psi \in M$ is equivariant, and $M$ is stable under $\psi \mapsto T_\tau(Z) \circ \psi$ for every $\tau$ and every complex matrix $Z$. Then $M$ contains every equivariant map $\varphi \colon W \to \mathcal{P}$.

Lean: `GlobalTheory.T.howeDuality_compactPair_polynomialFock_allRealPlaces` (also `GlobalTheory.HoweCompactAlg.mem_of_equivariant`).

*Proof.* We go down to harmonics and up again.

1. Since $M$ is nonzero and stable under the lowering operators, $M$ contains a nonzero jointly harmonic map $\psi$. Each lowering operator lowers a grading that is bounded below on the finite-dimensional space spanned by the values of a map, so a nonzero map can be lowered until all lowering operators kill it.
2. Let $S$ be the set of jointly harmonic maps in $M$. It is a subspace, and it contains $\psi$, so $S \neq 0$.
3. $S$ is stable under the compact operators. A compact operator maps $M$ to $M$ by hypothesis, and it maps jointly harmonic polynomials to jointly harmonic polynomials, because the compact part normalizes the span of the lowering operators.
4. By the theorem on the lowest K-type, applied to $S$, every equivariant jointly harmonic map lies in $S$, and so in $M$.
5. Every equivariant map $\varphi$ is a sum of compositions of raising operators with equivariant jointly harmonic maps. Since $M$ is stable under all $T_\tau(Z)$, and the raising operators are among them, step 4 gives $\varphi \in M$.

This proves the theorem. $\square$

Steps 1 and 5 are the decomposition $\mathcal{P} = \mathcal{H} \cdot \mathbb{C}[\mathfrak{p}^+]$ of the Fock space into harmonics times the image of the raising operators. Together with step 4 this is the statement that the isotypic component of type $W$ is irreducible under the Lie algebra, which is the form of Howe duality for compact dual pairs.

**Remark 7.32.3 (Formalization).** The relay `howeDuality_compactPair_polynomialFock_allRealPlaces` is at line 24 of [HoweDualityCompactPairPolynomialFockAllRealPlaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HoweDualityCompactPairPolynomialFockAllRealPlaceStatement.lean#L24), and its target `mem_of_equivariant` is at line 27 of [HoweDualityCompactPairPolynomialFockAllRealPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HoweDualityCompactPairPolynomialFockAllRealPlace.lean#L27). Its steps are the cited lemmas `exists_jointHarmonic_of_lowering_stable_submodule` (step 1), `fockTargetGlAction_compact_preserves_jointHarmonics` (step 3) and `mem_of_raisingOperators_jointHarmonics` (step 5). The relay `unitary_basis_general_linear_series` is at line 24 of [UnitaryBasisGeneralLinearSeriesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitaryBasisGeneralLinearSeriesStatement.lean#L24), under `maxHeartbeats 1000000`; its name does not describe the statement. The target `lowestKType_irreducible` is at line 34 of [UnitaryBasisGeneralLinearSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitaryBasisGeneralLinearSeries.lean#L34). Its steps use `exists_sourceHighestWeight_fock_stable_subspace` (step 4), `fockInnerProduct_posDef_compact_matrixUnit_adjoint` (step 3), `restrictTotalDegree` (step 2), `exists_highest_weight_K_type_map` (step 5) and `jointHarmonic_highestWeight_multiplicity_one` (step 6). The reasons given in steps 1 and 3 of the proof of membership, a bounded grading and the normalizing property of the compact part, are the classical arguments; the Lean proof cites the lemmas.
