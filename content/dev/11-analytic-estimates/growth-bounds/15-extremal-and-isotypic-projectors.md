---
title: Extremal and isotypic projectors
decls:
  - Formalism.MainNotions.G.ExtremalProjector.raising_operators_kill_image
  - Formalism.MainNotions.G.ExtremalProjector.extremal_projector_statement
  - Formalism.MainNotions.G.GLWeightTheory.isotypicProjectorTheoremField_of_linfty_bound
  - Formalism.MainNotions.G.GLWeightTheory.isotypic_projector_theorem_field
  - Formalism.MainNotions.G.GLWeightTheory.counting_statement_of_block_form
  - Formalism.MainNotions.G.GLWeightTheory.part_one_of_extremal_projector
  - Formalism.MainNotions.G.GLWeightTheory.problem_holds
  - Formalism.MainNotions.G.tool_statements_hold
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Extremal and isotypic projectors

This section proves the representation theory that the bounds of the chapter rest on: the extremal projector of $\mathfrak{gl}_n$, the bound on the denominators of isotypic projectors on lattices, and the package of projection lemmas built from them. The package and the seven statements on path polynomials are the tool statements used by [the hypotheses of the base level bound](/entry/first-theorem-admitted-closed/), below the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). The main result is that the five admitted facts of representation theory hold for every datum, with no open hypothesis left.

### Representations and lattices

Let $K$ be a field of characteristic $0$. A *representation of $\mathfrak{gl}_n$* on a $K$-vector space $V$ is a family of operators $E_{ab}$, $1 \leq a, b \leq n$, with
$$[E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{da}E_{cb},$$
such that every vector lies in a finite-dimensional subspace stable under all $E_{ab}$, and $V$ is the sum of the weight spaces $V_\mu = \{x : E_{aa}x = \mu_ax \text{ for all } a\}$, $\mu \in \mathbb{Z}^n$. A weight is *dominant* if $\mu_1 \geq \dots \geq \mu_n$. A *highest weight vector* of weight $\lambda$ is a nonzero $v \in V_\lambda$ with $E_{ab}v = 0$ for $a < b$. The *isotypic subspace* $V[\lambda]$ is spanned by the images of the highest weight vectors of weight $\lambda$ under products of the $E_{ab}$. An *isotypic projector* for $\lambda$ is an operator $e_\lambda$ that is the identity on $V[\lambda]$ and zero on $V[\mu]$ for $\mu \neq \lambda$; for $\lambda = 0$ it is an *invariant projector*. A *weight projector* $\pi_\mu$ is the identity on $V_\mu$ and zero on the other weight spaces.

The *divided powers* are $E_{ab}^{(k)} = E_{ab}^k/k!$, and the *binomials* are $\binom{E_{aa}}{k} = \frac{1}{k!}\prod_{j < k}(E_{aa} - j)$. Products of these operators form the *Kostant monoid* $U_{\mathbb{Z}}$.

Let $\mathcal{O}$ be a complete discrete valuation ring with fraction field $K$ and a fixed uniformizer, with $p$ in the maximal ideal and $p \neq 0$. It is *admissible* for $n'$ if $p \geq 5$ is prime, $n' \geq 2$ is even and the residue field contains a subfield with $p^{n'}$ elements. A *$U_{\mathbb{Z}}$-lattice* is a finitely generated $\mathcal{O}$-submodule $M \subseteq V$ stable under the divided powers and the binomials; it is *full* if it spans $V$ over $K$. We use three numbers:
$$N_0 = \frac{n(n-1)}{2}, \qquad d_p(n, k) = \lfloor\log_p(k + n - 1)\rfloor, \qquad \ell(\lambda) = \lambda_1 - \lambda_n,$$
and $\ell(V)$, the largest $k$ such that two weights of $V$ differ by $k(\varepsilon_a - \varepsilon_b)$ for some $a \neq b$.

### The extremal projector

**Definition 5.15.1 (Extremal projector).** A *normal order* is a list of all pairs $(a, b)$ with $a < b$, each once, such that for $a < b < c$ the pair $(a, c)$ lies between $(a, b)$ and $(b, c)$. For a weight $\mu$ and $a < b$ put $h_{ab} = \mu_a - \mu_b + b - a$. For $T \in \mathbb{N}$ put
$$p_{ab} = \sum_{k=0}^{T}\frac{(-1)^k}{\binom{h_{ab} + k}{k}}\,E_{ba}^{(k)}E_{ab}^{(k)},$$
and let $p_\mu$ be the product of the $p_{ab}$ in a normal order.

Since $E_{ba}^{(k)}E_{ab}^{(k)} = E_{ba}^kE_{ab}^k/(k!)^2$ and $\binom{h + k}{k}^{-1} = k!/((h + 1)\cdots(h + k))$, the factor $p_{ab}$ is $\sum_k \frac{(-1)^k}{k!\,(h_{ab} + 1)\cdots(h_{ab} + k)}E_{ba}^kE_{ab}^k$, cut at $k = T$. Each term maps every weight space into itself, so $p_\mu$ preserves $V_\mu$.

**Lemma 5.15.2 (Raising operators kill the image).** Let $V$ be a finite-dimensional representation of $\mathfrak{gl}_n$ over $K$ and $\mu$ a weight with $h_{ab} \geq 1$ for all $a < b$. Let $T \geq \dim V$. Then for every normal order, every $x \in V_\mu$ and every $a < n$,
$$E_{a,a+1}\,p_\mu x = 0.$$

Lean: `Formalism.MainNotions.G.ExtremalProjector.raising_operators_kill_image`.

*Proof.* The argument has four inputs. First, two factors $p_{ab}$ and $p_{cd}$ with $\{a, b\} \cap \{c, d\} = \emptyset$ commute. Second, for $a < b < c$, the braid relation
$$p_{ab}\,p_{ac}\,p_{bc} = p_{bc}\,p_{ac}\,p_{ab}$$
holds on $V_\mu$; here $h_{ac} = h_{ab} + h_{bc}$, since $\mu_a - \mu_c + c - a$ is the sum of the two other values. Third, every normal order can be carried by swaps of adjacent commuting pairs and by braid moves to a list that begins with $(a, a+1)$. Fourth, $E_{a,a+1}p_{a,a+1}y = 0$ for $y \in V_\mu$ when $h_{a,a+1} = \mu_a - \mu_{a+1} + 1$ and $T \geq \dim V$.

Fix $x \in V_\mu$ and $a$. Each factor maps $V_\mu$ into itself, so by the first two inputs each move of the third input does not change the value of the product at $x$. Hence $p_\mu x = p_{a,a+1}y$, with $y \in V_\mu$ the product of the remaining factors at $x$. The fourth input gives $E_{a,a+1}p_{a,a+1}y = 0$. $\square$

**Theorem 5.15.3 (Extremal projector).** For every datum the following holds. Let $V$ be a finite-dimensional representation of $\mathfrak{gl}_n$ over $K$, $\mu$ a weight with $h_{ab} \geq 1$ for all $a < b$, a normal order, and $T \geq \dim V$. Then:

1. $p_\mu$ maps $V_\mu$ into $V_\mu$;
2. $p_\mu x = 0$ for $x \in V_\mu \cap \sum_{b < a}E_{ab}V$;
3. $p_\mu x = x$ for every $x \in V_\mu$ with $E_{ab}x = 0$ for all $a < b$.

Lean: `Formalism.MainNotions.G.ExtremalProjector.extremal_projector_statement`.

*Proof.* The first claim holds factor by factor. For the third, if $E_{ab}x = 0$ for all $a < b$, then every term with $k \geq 1$ of each factor kills $x$, and the term $k = 0$ is the identity; so each factor fixes $x$, and so does the product. The second claim is derived from the Lemma (Raising operators kill the image): the image of $V_\mu$ under $p_\mu$ consists of vectors killed by the simple raising operators $E_{a,a+1}$, hence by all $E_{ab}$ with $a < b$, which are their iterated commutators. The derivation of the second claim from this is not unfolded here. $\square$

This is the extremal projector of Asherova, Smirnov and Tolstoy, read on the weight space $V_\mu$. For $\mu = 0$ all $h_{ab} = b - a$ are at least $1$, so $p_0$ is defined on the zero weight space of every representation.

### Isotypic projectors on lattices

**Definition 5.15.4 (Invariant denominator bound).** For a finite-dimensional $V$ let $\ell_\infty(V)$ be the largest $|\nu_a|$ over the weights $\nu$ of $V$ with $\sum_a\nu_a = 0$. The *invariant denominator bound* says: for every admissible $\mathcal{O}$, every finite-dimensional representation $V$ over $K$, every full $U_{\mathbb{Z}}$-lattice $M$ and every invariant projector $e_0$,
$$p^{N_0\,d_p(n, \ell_\infty(V))}\,e_0(M) \subseteq M.$$

The bound is proved from the complete reducibility of finite-dimensional representations in characteristic $0$.

**Theorem 5.15.5 (Isotypic projectors with the invariant bound).** Assume complete reducibility and the invariant denominator bound. Let $\mathcal{O}$ be admissible, $V$ a finite-dimensional representation over $K$ with $n \geq 1$, $M$ a full $U_{\mathbb{Z}}$-lattice, $S$ a finite set of dominant weights and $e_\lambda$ an isotypic projector for each $\lambda \in S$. Then for $x \in M$,
$$p^{\,c}\sum_{\lambda \in S}e_\lambda x \in M, \qquad c = \max_{\lambda \in S}N_0\,d_p\big(n, \ell(V) + \ell(\lambda)\big).$$

Lean: `Formalism.MainNotions.G.GLWeightTheory.isotypicProjectorTheoremField_of_linfty_bound`.

*Proof.* It suffices to prove $p^{N_0d_p(n, \ell(V) + \ell(\lambda))}e_\lambda x \in M$ for one $\lambda$, since a larger power of $p$ keeps an element of $M$ in $M$ and $M$ is closed under sums.

If $V$ has no highest weight vector of weight $\lambda$, then $V[\lambda] = 0$. By complete reducibility $V$ is the sum of its isotypic subspaces, and $e_\lambda$ kills each of them, so $e_\lambda x = 0$.

Otherwise take a highest weight vector $v_0$ of weight $\lambda$ and the subrepresentation $L$ it generates. There is a basis $b_1, \dots, b_d$ of $L$ with $b_i \in M$ whose coordinate functions $b_i^*$ take values in $\mathcal{O}$ on $L \cap M$. The space $H = \operatorname{Hom}_K(L, V)$ is a representation, and the homomorphisms that map $L \cap M$ into $M$ form a full $U_{\mathbb{Z}}$-lattice $H_M$ of it. Let $P$ be an invariant projector of $H$. The map $b_i^* \otimes x \colon y \mapsto b_i^*(y)\,x$ lies in $H_M$, so the invariant denominator bound for $H$ gives
$$p^{N_0d_p(n, \ell_\infty(H))}\,P(b_i^* \otimes x)(b_i) \in M.$$
A weight of $H$ is a difference $\nu - \nu'$ of a weight $\nu$ of $V$ and a weight $\nu'$ of $L$, which gives $\ell_\infty(H) \leq \ell(V) + \ell(\lambda)$, and $d_p(n, \cdot)$ is monotone. Finally, a trace formula, proved from complete reducibility and Schur's lemma, gives
$$e_\lambda x = d\sum_{i=1}^{d}P(b_i^* \otimes x)(b_i).$$
So $p^{N_0d_p(n, \ell(V) + \ell(\lambda))}e_\lambda x \in M$. $\square$

**Corollary 5.15.6 (Isotypic projector theorem).** For every datum the conclusion of the Theorem (Isotypic projectors with the invariant bound) holds without hypotheses.

Lean: `Formalism.MainNotions.G.GLWeightTheory.isotypic_projector_theorem_field`.

*Proof.* Complete reducibility holds: every invariant subspace of a finite-dimensional representation in characteristic $0$ has an invariant complement. The invariant denominator bound is proved from it. Apply the theorem. $\square$

### The projection package

**Definition 5.15.7 (Projection package).** For a datum, the *projection package* is the conjunction of five groups of statements:

1. the *projection theorems*: for an invariant projector $e_0$ on $V$ with a full $U_{\mathbb{Z}}$-lattice $M$, $e_0 = p_0\pi_0$ for every normal order and $T \geq \dim V$, and $p^{N_0d_p(n, \ell(V))}e_0(M) \subseteq M$; the comparison $\Delta(v) \subseteq M \subseteq \nabla(v)$ and $p^{N_0d_p(n, \ell(\lambda))}\nabla(v) \subseteq \Delta(v)$ for an irreducible $V$ with highest weight vector $v$ of weight $\lambda$ and a full lattice $M$ with $M \cap V_\lambda = \mathcal{O}v$, where $\Delta(v)$ is the $\mathcal{O}$-span of $U_{\mathbb{Z}}v$ and $\nabla(v)$ is the set of $x$ such that each $ux$, $u \in U_{\mathbb{Z}}$, has its $V_\lambda$-component in $\mathcal{O}v$; the Corollary (Isotypic projector theorem); and two corollaries for translates and for filtered products of isotypic projectors on polynomial rings;
2. the *valuation lemmas*: the lowest and highest weight coordinates of a polynomial are additive on products and are read off from the weights of the $U_{\mathbb{Z}}$-module it generates, or from its isotypic components;
3. a *determinant divisibility statement*: a polynomial whose lowest weight coordinate exceeds its degree in the other vector letters by $m$ is divisible by the $m$-th power of a minor of the plane variables;
4. the *unit product lemmas*: expansions of the unit parts of factorials $(\rho + p^{t+1}e)!$ in binomials $\binom{e}{j}$ with coefficients of valuation at least $j/4$, and a degree truncation bound;
5. the *derivative lemmas*: valuation bounds for a monomial times a divided derivative, a $p$-adic digit expansion of $\prod_k\binom{\rho_k + p^te_k}{M_k}$ modulo $p^c$, and stability of digit classes under derivatives.

**Theorem 5.15.8 (Projection package from the product formula).** For every datum, if every invariant projector $e_0$ on a representation with a full $U_{\mathbb{Z}}$-lattice over an admissible $\mathcal{O}$ satisfies $e_0 = p_0\pi_0$ for every weight projector $\pi_0$, every normal order and $T \geq \dim V$, then the projection package holds.

Lean: `Formalism.MainNotions.G.GLWeightTheory.counting_statement_of_block_form`.

*Proof.* The product formula is the first half of the first projection theorem, and the bound $p^{N_0d_p(n, \ell(V))}e_0(M) \subseteq M$ is proved from complete reducibility. The comparison of $\Delta(v)$ and $\nabla(v)$ follows from complete reducibility and the invariant denominator bound. The isotypic projector theorem is the corollary above. The corollary for translates follows from the comparison, and the corollary for filtered products from the isotypic projector theorem. The other four groups are proved directly: the valuation lemmas from the additivity of the two coordinates and complete reducibility, the divisibility statement from a height bound on weights, and the unit product and derivative lemmas by computations with binomial coefficients. $\square$

**Theorem 5.15.9 (Projection package from the extremal projector).** For every datum, if the conclusion of the Theorem (Extremal projector) holds, then the projection package holds.

Lean: `Formalism.MainNotions.G.GLWeightTheory.part_one_of_extremal_projector`.

*Proof.* Let $e_0$ be an invariant projector and $\pi_0$ a weight projector. An invariant vector has weight $0$ and is killed by all $E_{ab}$, so $p_0\pi_0$ fixes it by the third property of $p_0$. A vector of weight $0$ in an irreducible summand with highest weight $\lambda \neq 0$ lies in $\sum_{b < a}E_{ab}V$, so $p_0$ kills it by the second property. With complete reducibility this gives $e_0 = p_0\pi_0$, and the Theorem (Projection package from the product formula) applies. $\square$

**Theorem 5.15.10 (Integrality from the admitted facts).** For every datum, if the datum is admitted, the projection package holds.

Lean: `Formalism.MainNotions.G.GLWeightTheory.problem_holds`.

*Proof.* Admitted means five facts: the Pieri rule for alternants, complete reducibility, Kummer's theorem on $v_p\binom{m}{k}$, Gauss's lemma for polynomials over a factorial domain, and the conclusion of the Theorem (Extremal projector). The fifth gives the package. $\square$

**Theorem 5.15.11 (Tool statements).** Assume that the conclusion of the Theorem (Extremal projector) holds for every datum. Then for every datum, the projection package holds, [the seven statements on path polynomials](/entry/splitting-package-holds/) hold, and the polynomials $\Psi(\mu, I)$ for paths $\mu$ of dominant weights and standard tableaux $I$ over a discrete valuation ring are linearly independent and span the polynomials of their multidegree.

Lean: `Formalism.MainNotions.G.tool_statements_hold`.

*Proof.* The Pieri rule, complete reducibility, Kummer's theorem and Gauss's lemma are proved, and the hypothesis gives the fifth admitted fact, so the datum is admitted. The Theorem (Integrality from the admitted facts) gives the package. The other two statements are proved in the chapter on path polynomials and do not use the hypothesis. $\square$

The Theorem (Extremal projector) holds for every datum, so the hypothesis of the Theorem (Tool statements) holds and its three conclusions hold unconditionally.

**Remark 5.15.12 (Formalization).** The four inputs of the lemma are `restComm`, `restYB`, `restConn` and `restKill`, combined in `raising_kill_of_interface` (TruncatedChains/RaisingKillOfInterface.lean:165); the braid relation `restYB` (TruncatedChains.lean:13) is the only one that receives the datum, through `ybat_base`. The step from the lemma to `adm5` is `sizes_bound_of_log_estimates` (RootWeights/FiltrationAdjointStable.lean:207), whose name does not describe it; a different theorem with the same name is at PlaneCountTheoremWithConstants.lean:1366. The proofs of `restConn`, `restKill`, `ybat_base`, `linf_lemma_without_projector`, `invariant_projection_extremal_formula`, `lattice_adapted_basis_exists` and `hom_lattice_dividedPower_stable` were not unfolded. The trace formula is `isotypic_projector_trace_formula` (RootWeights/IsotypicProjectorTraceFormula.lean:21), with $d$ the cardinality of the index type of the basis. The record `ExtremalProjectorTools` (PlaneCountTheoremWithConstants.lean:1005) is a hypothesis of `tool_statements_hold`, although `extremal_projector_statement` (TruncatedChains.lean:19) proves its only field. `problem_holds` (GLWeightTheory.lean:150) reads only the fifth part of `admitted`, so the four proofs built at PlaneCountTheoremWithConstants.lean:1010 are not used. The fourth admitted fact is named `ArchimedeanSignatureMatching` (CovariantDegrees.lean:38), although it is Gauss's lemma. All parts of `Conclusion1` take the datum as an unused `_D` (CovariantDegrees.lean:53 to 261). The name `counting_statement_of_block_form` is also used at LatticeSystems.lean:2382 and CountingStatementReduction.lean:2445, and `problem_holds` at LatticeSystems.lean:4447, for other statements.
