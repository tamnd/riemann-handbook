---
id: pair-count-bound-of-siegel-mass
title: The weighted count of pairs of relevant terms, from the mass formulas
kind: theorem
decl: GlobalTheory.TypeAsm.pair_count_bound_of_siegel_mass
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TermPairCountBoundOfSiegelMassRatios
covers: 1178
status: drafted
drafted_by: writer@claude
---
This theorem proves the pair count `PairsP` from two mass formulas for Hermitian lattices over CM fields. Its statement form is [`termPairCountBound_of_siegelMassRatios`](/entry/term-pair-count-bound-of-siegel-mass-ratios/), and [`typeBound_of_gap`](/entry/type-bound-of-gap/) uses it for the type bound.

## Statement

Let $K$ be a number field with an involution $\ast$. `IsCMUnram K` says: $K$ is totally complex, each embedding $K \to \mathbb{C}$ takes $\ast$ to complex conjugation, and for each maximal ideal $P$ there is $\theta \in \mathcal{O}_K$ with $\theta - \theta^\ast \notin P$. For a Hermitian form $h$ and an $\mathcal{O}_K$-lattice $L$, the mass is $\mathrm{mass}(h, L) = \sum_M 1/\lvert\mathrm{Aut}(M)\rvert$ over a set of class representatives $M$ of the genus of $L$ (and $0$ if there is none).

- **`MaxMass`.** Let $K$ satisfy `IsCMUnram` and $n \geq 1$. There is $c$ such that for each positive definite Hermitian space $(V, h)$ of dimension $n$ and each maximal integral lattice $M$, $\mathrm{mass}(h, M) = c \prod_{P} \frac{q_P^{\,n} - (-1)^n}{q_P + 1}$, over the primes $P$ where $M$ is not unimodular, with $q_P = \lfloor \sqrt{N P} \rfloor$.
- **`SiegelMassRatio`.** Let $K$ satisfy `IsCMUnram`, $f$ the number of its infinite places, $v = \lvert d_K \rvert^{1/(2f)}/2$, and $M \geq 3$. If $L$ and $L'$ have orthonormal bases of sizes $M$ and $M - 1$, then
$$\frac{\mathrm{mass}(h, L)}{\mathrm{mass}(h', L')} = \frac{\bigl((M-1)! \, (v/\pi)^M\bigr)^f}{\sqrt{(2v)^f}} \prod_{P} \varepsilon_P(M),$$
where $\varepsilon_P(M) = (1 - (-1)^M N P^{-M/2})^{-1}$ if $P^\ast = P$ and $(1 - N P^{-M})^{-1/2}$ otherwise.

**Theorem.** `MaxMass` and `SiegelMassRatio` imply `PairsP`, as stated in [the entry for `typeBound_of_gap`](/entry/type-bound-of-gap/).

## Proof

Fix the constants and $C_H \geq 0$. Let $C_a = \max(1, 2(C_H + 1), C_T)$. The arithmetic lemma `sum_pairBd_mul_datBd_le` at $C_a$ gives $C_h \geq 0$ and $C'_l$. The proof takes $C_p = 16$, the threshold $1$ for $C'$ and $\max(1, C'_l)$ for $C_l$. Fix a datum and a set $P$ of pairs. If $P$ is empty, the bound holds by nonnegativity. Else:

1. `unitaryHostFieldArithmeticConditions` gives facts on the field $E$ of $D$, such as: $f$ is its number of infinite places. `parameter_size_constraints` gives the size relations between $k, r, m, b$ and $f$.
2. `relevantTerm_norms_ge_one_and_bounded` gives $1 \leq \Delta \leq H_b(2(C_H + 1)) \sigma_H^2$ for each relevant term, and a similar bound for a second norm $\Delta_b$. Since $2(C_H + 1) \leq C_a$, these hold with $C_a$.
3. With these bounds, `sum_pairBd_mul_datBd_le` gives $\sum_{x \leq \Delta'} \sum_{x' \leq \Delta''} B(x, x') \, d(x) d(x') \leq e(j', \delta') e(j'', \delta'')$, for the explicit functions `pairBd` $B$ and `datBd` $d$, which we have not unfolded.
4. `definite_quotient_model_exists` gives a positive definite Hermitian subspace $W$ of dimension $k$ with an embedding.
5. `genusMean_embeddedPairs_le_mass_mul_pairBound` uses `MaxMass` and `SiegelMassRatio`. It bounds the orbit sum over the genus of each row lattice of the number of embedded triples by the mass times $B(x, x')$. `weightedTermPairs_sum_le_via_rows_genusMeans` turns this into $\sum_P w w \, \omega \omega \leq \mathrm{mass}(Y, u) \sum_{x, x'} B(x, x') \, d(x) d(x')$, in $[0, \infty]$.
6. The private lemma `le_mul_sum_sum_of_ofReal_le_ennreal_sum` moves this to $\mathbb{R}$. Step 3 ends the proof.

## In the Lean code

The theorem is in [TermPairCountBoundOfSiegelMassRatios.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermPairCountBoundOfSiegelMassRatios.lean#L70). `MaxMass` is in [MaxMass.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/DiscreteSeriesUnitary₂/MaxMass.lean#L10), `SiegelMassRatio` and `mass` in [StatementMass.lean](lean:Formalism/HermitianLattices/StatementMass.lean#L67).

The two mass hypotheses are used only in step 5. The hypothesis `ConcTie X Y` of `PairsP` is introduced as `_` and not used. The other inputs are proved theorems: `termsOverRow_compatible`, `termPairs_rowLattice_counted_via_embeddings`, `rowsMeanC_holds`, `isometricEmbeddedDatumPairs_encard_isometry_smul`, `base_lattice_construction_holds`, and the three normal form lemmas passed to step 2. We have not unfolded `omT`, `pairBd`, `datBd` or the set `Trip` of embedded triples. We have not compared the two mass statements with the literature.
