---
id: match-principal-congruence-inert
title: Matching of principal congruence indicators at an inert place
kind: theorem
decl: GlobalTheory.CongMatch.match_principal_congruence_inert
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CongruenceSubgroupIndicatorWeight
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem gives an explicit pair of matching test functions at an inert place of a CM field. On the unitary group $U(n)$ it takes the indicator of a principal congruence subgroup of level $k$. On $\mathrm{GL}_a \times \mathrm{GL}_b$ it takes a scaled indicator of the elements whose norms lie in the same kind of subgroup. It says that the stable twisted orbital integrals of the second function equal the $\kappa$-orbital integrals of the first, with the transfer factor. The result goes to the step [every character](/step/every-character/) through the statement `congruence_subgroup_indicator_weight` and the matching statement `M2` of the Hecke blocks.

## Statement

Let $E$ be a CM field in which every place is unramified over the maximal totally real subfield. Let $w$ be a finite place of $E$ that is not split over that subfield, with completion $E_w$, ring of integers $\mathcal{O}_w$, residue field of size $q_w$, and conjugation $c$. Let $n = a + b$ and $k \geq 1$.

For $m \geq 1$ let $K_m(k) \subset \mathrm{GL}_m(\mathcal{O}_w)$ be the principal congruence subgroup of level $k$: the $g$ with $g \equiv 1 \bmod \varpi^k$. Let $U(n) = \{g \in \mathrm{GL}_n(E_w) : {}^t\bar g\, g = 1\}$, and let $N(y) = y\, \theta(y)$ be the norm map on $\mathrm{GL}_m(E_w)$ for the twist $\theta$ built from $c$. Put
$$f = \mathbf{1}_{U(n) \cap K_n(k)}, \qquad \varphi(y_1, y_2) = \bigl(-\sqrt{q_w}\bigr)^{-kab} \prod_{i=1}^{2} \mathbf{1}\bigl[y_i \in \mathrm{GL}(\mathcal{O}_w),\ N(y_i) \in K(k)\bigr].$$

**Theorem.** Let $Q_1, Q_2$ be monic polynomials over $E_w$ of degrees $a$ and $b$, with $Q_1 Q_2$ separable and each $Q_i$ conjugate self-reciprocal. Then
$$\mathrm{SO}^{\theta}_{Q_1, Q_2}(\varphi) = (-1)^{v(R)}\, |R|_w^{1/2}\, \mathrm{O}^{\kappa}_{Q_1 Q_2}(f),$$
where $R = \operatorname{Res}(Q_1, Q_2)$ and $v$ is its valuation. The left side sums twisted orbital integrals over the classes with $\operatorname{char} N(y_i) = Q_i$. The right side is the signed sum of orbital integrals over $\gamma \in U(n)$ with characteristic polynomial $Q_1 Q_2$. In Lean this is `Match n a b w 1 f φ`.

## Proof

1. `exists_uq` puts $E_w$ into the form of an unramified quadratic datum $K$ with residue field of size $q^2$, so $\sqrt{q_w} = q$. `exists_small_conjFixed_of_valuation` gives a $c$-fixed $t$ of valuation $k$.
2. For each $Q_i$, `exists_involutiveAlgebra_adjoinRoot_selfReciprocal` gives a commutative algebra $B_i$ of rank $\deg Q_i$ over $E_w$, with an involution $\sigma$ over $c$ and an element $g_i$. The element $x_i = 1 + t g_i$ generates $B_i$, is a root of $Q_i$, and satisfies $x_i \sigma(x_i) = 1$. `val_resultant_charpoly_shifted_unit_adjoinRoot` says that the characteristic polynomials $P_i$ of $g_i$ have separable product and $v(\operatorname{Res}(P_1, P_2)) = v(R) - kab$.
3. `twistedOrbitalIntegral_levelFunction_inert_eq_latticeCount` and `kappaOrbitalIntegral_congruence_inert_latticeCount` rewrite both sides as counts of self-dual lattices stable under $g_i$, summed over classes. The lemma `stableTwistedOrbitalIntegral_integralNormCongruence_product` splits the left side as a product.
4. The two counts satisfy the unit identity $(-q)^{-v(\operatorname{Res}(P_1, P_2))} \cdot \kappa\text{-count} = \text{count}_1 \cdot \text{count}_2$ (`InvAlg.Identity`). The proof gets it from `invAlg_identity_of_principal_congruence`, applied to the Lie algebra unit lemma `unitLemma_lieAlgebra_unitaryGroup_of_jacquetRallis`, which in turn takes `jacquetRallisUnitMatch_all_ranks`. We have not unfolded these three statements.
5. The private lemma `unit_product_rescale_disjoint_finsets` checks that the powers of $-q$ agree. The rest is bookkeeping.

## In the Lean code

The theorem is at [CongruenceSubgroupIndicatorWeight.lean#L41](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CongruenceSubgroupIndicatorWeight.lean#L41). `Match`, `stTw2`, `kapOrb`, `delta` and `nrmL` are in [SimpleTwistedTraceFormulaStable.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SimpleTwistedTraceFormulaStable.lean#L264). `InvAlg`, the lattice counts `stSum`, `kapSum` and `Identity` are in [UnitLemmaGroup.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnitLemmaGroup.lean#L148).

The "weight" in the file name is the constant $(-\sqrt{q_w})^{-kab}$ in $\varphi$. The level bound uses `WithZero.exp (-k)`, which is the condition $g \equiv 1 \bmod \varpi^k$ in the multiplicative valuation.
