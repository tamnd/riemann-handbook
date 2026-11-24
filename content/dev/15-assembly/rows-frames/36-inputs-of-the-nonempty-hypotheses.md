---
title: Inputs of the nonempty hypotheses
decls:
  - GlobalTheory.LeviCut.exCut
  - GlobalTheory.FunObj.gridChoice_nonempty_of
  - GlobalTheory.T.realisation_extends_by_newTuples_keeping_laws
  - GlobalTheory.TupExt.extend_tuples
  - GlobalTheory.T.exists_routeDatum_finite_pureTensors_vacuum
  - GlobalTheory.SmallDatum.exists_datum_pure_linBar
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Inputs of the nonempty hypotheses

The statement that [the hypotheses of the definite side are nonempty](/step/nonempty-hyps/) has many inputs. This section proves four of them: a cut inequality for the exponents that compare Weyl lattices with dual Weyl lattices, the existence of grid choices, the extension of a real datum by new tuples, and a pure tensor form for the data of the small route. They have little in common beyond their user, and we treat them one after the other.

### Weyl lattices and the exact exponent

Let $R$ be a commutative ring, $r \geq n$ and $\nu = (\nu_0 \geq \dots \geq \nu_{n-1})$ a dominant weight. On the polynomial ring $R[x_{a b}]$ with $a < r$ and $b < n$:

1. the *dual Weyl lattice* $\nabla_R(\nu)$ is the set of polynomials that are homogeneous of degree $\nu_b$ in each column $b$ and invariant under the column operations $x_{\cdot j} \mapsto x_{\cdot j} + c\, x_{\cdot l}$ for $l < j$; over a field of characteristic zero it is the irreducible representation of $\mathrm{GL}_r$ of highest weight $\nu$, and over $\mathbb{Z}$ it is the induced module;
2. the *Weyl lattice* $\Delta_R(\nu)$ is the span of the images of the highest weight vector under words in the divided powers of the row operators; it is the Weyl module.

Over $\mathbb{Z}$ we have $\Delta_{\mathbb{Z}}(\nu) \subseteq \nabla_{\mathbb{Z}}(\nu)$ with finite index. For a prime $\ell$, the *exact exponent* $e_\ell(\nu)$ is the least $e$ for which there is $m$ prime to $\ell$ with $m \ell^e \nabla_{\mathbb{Z}}(\nu) \subseteq \Delta_{\mathbb{Z}}(\nu)$. For a weight $\lambda$ of length $N$ we write $\lambda_{<a}$ for its first $a$ entries and $\lambda_{\geq a}$ for the others, and $u_a = \lambda_a + N - 1 - a$ for the shifted entries.

**Theorem 7.36.1 (Cut inequality for exact exponents).** Let $\lambda$ be a dominant weight of length $N$, $\ell$ a prime, and assume that all $u_a$ lie in an interval $[\mathrm{lo}, \mathrm{lo} + w]$. Then for each $a \leq N$,
$$\begin{aligned} e_\ell(\lambda) &\leq e_\ell(\lambda_{<a}) + e_\ell(\lambda_{\geq a}) + a (N - a) \lfloor \log_\ell w \rfloor. \end{aligned}$$

Lean: `GlobalTheory.LeviCut.exCut`.

*Proof.* We follow the Lean proof. Write $b = N - a$.

1. For the two blocks there are $m_1$ and $m_2$ prime to $\ell$ with $m_1 \ell^{e_\ell(\lambda_{<a})} \nabla \subseteq \Delta$ for $\lambda_{<a}$, and $m_2 \ell^{e_\ell(\lambda_{\geq a})} \nabla \subseteq \Delta$ for $\lambda_{\geq a}$. Call these constants $c_1$ and $c_2$.
2. There is $m$ prime to $\ell$ such that $\Lambda = m\, \ell^{\lfloor \log_\ell w \rfloor}$ satisfies $(j + k + 1)! \mid \Lambda\, j!\, k!$ whenever $j + k + 1 \leq w$. This is the bound for the denominators of the beta integrals: the $\ell$-adic valuation of a binomial coefficient $\binom{j + k + 1}{j}$ is at most $\lfloor \log_\ell (j + k + 1) \rfloor$.
3. From the interval condition, $\lambda_i - \lambda_j \leq w + 1 - N$ for all $i$ and $j$.
4. Under these conditions, $c_1 c_2 \Lambda^{a b}\, \nabla_{\mathbb{Z}}(\lambda) \subseteq \Delta_{\mathbb{Z}}(\lambda)$. The proof builds a projector from the Levi projection of the two blocks and the grid of adjoint actions of the matrix units. It commutes with the action of the Lie algebra, so by Schur's lemma it is a scalar on $\nabla_{\mathbb{Q}}(\lambda)$. Its value on the highest weight vector shows that $z$ times it is the identity, where
$$z = \prod_{i < a \leq j} (\lambda_i - \lambda_j + j - i).$$
The integrality of the grid, with denominators bounded by $\Lambda^{a b}$, then gives the inclusion.
5. Since $m_1 m_2 m^{a b}$ is prime to $\ell$, the exponent of $\ell$ in $c_1 c_2 \Lambda^{a b}$ bounds $e_\ell(\lambda)$, and it is the right side of the inequality.

This proves the theorem. $\square$

### Grid choices

Let $L$ be a family of level characters with base $\mu_0$, indexed by $T$, and $G$ a grid for $L$ with a Weil datum. For $U \subseteq T$ a *grid choice* for $U$ consists of:

1. frames of all grid lattices, and frames $\beta'_j$ of the top lattices;
2. at each local place $w$ of each $t \in U$, decompositions of the row lattices as sum frames of $\beta'_j$, with signs and, for $j = 0$, powers of a uniformizer, and a decomposition of the last top lattice;
3. a standard datum $N$ for $U$ and a normal form for $N$;
4. a finite set of places that controls the ideals $\mathfrak{A}$ and $\bar{\mathfrak{A}}$ of the host.

**Theorem 7.36.2 (Grid choices exist).** Let $U \subseteq T$ be finite. Assume that $p_{de}$ and $p'_{de}$ are prime to $Q_S\, q$, and that for $t \in U$ and every prime $P$ of the level set of $t$, the norm of the class conductor $\mathfrak{c}_K$ does not lie in $P$. Then there is a grid choice for $U$.

Lean: `GlobalTheory.FunObj.gridChoice_nonempty_of`.

*Proof.* Standard data for the finite set $U$ exist, and so do normal forms for them. The union of the local places of the $t \in U$ is finite. At each such place $w$, the integer $\mathrm{bad}(D)$ does not lie in $w$, by the two coprimality conditions and the condition on $\mathfrak{c}_K$, and so $\mathfrak{A}$ and $\bar{\mathfrak{A}}$ have valuation $0$ at $w$. It remains to build the frames.

1. Each top lattice is a finitely generated full lattice, so it has an adelic frame.
2. For the rows, choose finite ideles $y_p$ with valuation $-\operatorname{ord}_Q(\mathfrak{r}_{j,p})$ at every place $Q$, where $\mathfrak{r}_{j,p}$ are the row ideals, and with the prescribed sign and uniformizer power at the finitely many local places. This is possible by approximation, because the prescribed values have the right valuations there, which is where the vanishing of the valuations of $\mathfrak{A}$ is used.
3. A frame of the top lattice and such ideles give a sum frame of the row lattice.

The last decomposition and the set of places are built in the same way. $\square$

### Extension by new tuples

Let $R$ be a real datum with index set $T_0$, with face $F$, weights $\kappa$, vectors $v_0$, model data $O$, phases and a base $B$ at the step $j$, satisfying the *laws* of the conjugate twist: the core laws, finiteness, the face, the lowest types, the guard, the pins, the phase tie and the base.

**Theorem 7.36.3 (Extension by new tuples).** Assume rapid decay of cusp forms, global Artin reciprocity, the existence of ray class fields, the covering by discrete series and the theorem of Casselman and Wallach. Let $(R, F, \dots)$ satisfy the laws, and let $N$ be a finite type with, for each $n \in N$, a Hecke character $\chi_n$, a unitary idele class character $\xi_n$, a finite set $Q_n$ of places and local characters, satisfying the twist level conditions. Assume that $n \mapsto \chi_n$ is injective, that no $\chi_n$ is a character of $R$, and that for $p \in \{p_{de}, p'_{de}\}$ all primes over $p$ in the level sets of $R$ and in the $Q_n$ lie over a single prime of $K$. Then there is a real datum $R'$, with face, vectors and model data, that satisfies the laws, extends $R$, and has for each $n$ an index $t'$ with character $\xi_n$ and level set $Q_n$.

Lean: `GlobalTheory.T.realisation_extends_by_newTuples_keeping_laws` (also `GlobalTheory.TupExt.extend_tuples`).

*Proof.* The index set of $R'$ is $T_0 \sqcup N$.

1. The level characters of $R$ together with the new tuples form a family of level characters with the same base $\mu_0$. This uses the injectivity of $\chi$, the distinctness from the characters of $R$, and the condition on the primes over $p_{de}$ and $p'_{de}$.
2. A family stage gives a new family and a real stage for it, from the real side at more levels.
3. The core extends: from the covering by discrete series, the Harish-Chandra modules of the indefinite unitary group, rapid decay, the theorem of Casselman and Wallach and the chain parameters of the node gap, there is an extended real datum $Y$ with the core laws and the pins.
4. The guard extends by the half and the guard conditions of the new tuples, and the face, lowest types, pins, phase tie and base extend to $Y$ unchanged.
5. The new tuple $n$ is the index $n$ in the second summand.

This gives $R'$. $\square$

### Pure tensors for the small route

Let $G$ be a grid with a Weil datum and frames $B$, $t$ an index and $i, j$ steps. A *triple* consists of a base $(\psi, v_1, \tau_1)$ at a place $v_1$ of $F$, a geometry $\Gamma$ with hermitian spaces $V, V', W$ and a model $M'$, characters, and Weil representations $\omega, \omega'$ of the two pairs, attached to a volume $M$ at $t$ and a numerator $e$.

**Theorem 7.36.4 (Pure tensor data for the small route).** Let $\Theta$ and $\Theta'$ be matched totals for the big and the small route at $t, i, j$, and let a triple be given, with no local place of $t$ over $v_1$. Then there is a datum $\Phi_B$ for the small route with
$$\Phi_B = \sum_{k = 1}^{m} f_k \otimes \bigotimes_v \varphi_{k, v},$$
where each $\varphi_{k, v}$ is a Schwartz-Bruhat function, $\varphi_{k, v}$ is the vacuum of $M'$ for almost all $v$, and $\varphi_{k, v_1} = \varphi_0$ for all $k$. There are also a partial Fourier model $\iota$ of $M'$ at $(\psi, \tau_1)$, a matrix $P \in \mathrm{GL}(F_{v_1})$, a lattice $\Lambda$ and a constant $c$ with
$$\iota(\varphi_0)(Y) = c \cdot \mathbf{1}_{M(\Lambda)}(P\, Y) \qquad \text{for all } Y.$$

Lean: `GlobalTheory.T.exists_routeDatum_finite_pureTensors_vacuum` (also `GlobalTheory.SmallDatum.exists_datum_pure_linBar`).

*Proof.* The datum of the grid gives $\Phi_B$ as a finite sum of pure tensors with Schwartz-Bruhat factors that are vacua almost everywhere, and with a common factor $\varphi_0$ at $v_1$. The factor $\varphi_0$ is a lattice vacuum: it is fixed by the stabilizer of two lattices $L_1, L_2$ and a character $\theta$, it is nonzero, and it is unique with these properties up to scalars. A lattice vacuum at a split place is, in the partial Fourier model, a multiple of the indicator of a translated matrix lattice. $\square$

**Remark 7.36.5 (Formalization).** The theorem `exCut` is at line 154 of [WeylLatticeExactExponentBlockCut.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/WeylLatticeExactExponentBlockCut.lean#L154). It applies `ExCut₂` (line 109) to nine statements proved elsewhere, and `ExCut₂` uses `cut_incl` (line 36) for step 4 and `exact_z_specialization` for step 1. `ExCut` is at line 25 of [StatementE.lean](lean:Formalism/PieriBlockIdeals/StatementE.lean#L25), and `InclZ` and `exZ` are at lines 18 and 41 of [StatementLA.lean](lean:Formalism/PieriBlockIdeals/StatementLA.lean#L41). The reason given in step 2, the valuation of binomial coefficients, is the classical argument; the Lean proof cites `beta_integral_denominator_bound`. The theorem `gridChoice_nonempty_of` is at line 588 of [AuxiliaryVectorDecompositionEqZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AuxiliaryVectorDecompositionEqZero.lean#L588), with `gridChoice_nonempty` at line 418 under `maxHeartbeats 4000000` and `count_AA_AAbar` at line 564; `GridChoice` is at line 185 of [InvVolConjLevelOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/InvVolConjLevelOne.lean#L185). The relay for the extension is at line 12 of [RealisationExtendsByNewTuplesKeepingLawsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RealisationExtendsByNewTuplesKeepingLawsStatement.lean#L12), under `maxHeartbeats 1000000`, and the target `extend_tuples` is at line 46 of [RealisationExtendsByNewTuplesKeepingLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RealisationExtendsByNewTuplesKeepingLaws.lean#L46), under `maxHeartbeats 2000000`. Its hypotheses `GlobalArtinReciprocity` and `RayClassFieldSt` are not used (`intro h1 _ _ h4 h5`, line 63). Its proof destructures with the local macro `obt` (lines 64, 67 and 68), and the helper `ext_ext` at line 37 closes a goal with `with_unfolding_all exact`. The relay for the small route is at line 21 of [ExistsRouteDatumFinitePureTensorsVacuumStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRouteDatumFinitePureTensorsVacuumStatement.lean#L21), under `maxHeartbeats 1000000`, and its target `exists_datum_pure_linBar` is at line 23 of [ExistsRouteDatumFinitePureTensorsVacuum.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRouteDatumFinitePureTensorsVacuum.lean#L23). It is the composition of the cited lemmas `exists_gridDatum_pureTensor_vacuaAE` and `latticeVacuum_eq_smul_indicator_splitPlace`, and the argument $g_1$ is only passed on to the first of them. The proofs of these lemmas, and of `exists_std` and `normal_nonempty` in the grid choice, were not opened.
