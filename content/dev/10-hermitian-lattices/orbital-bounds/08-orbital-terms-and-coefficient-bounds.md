---
title: Orbital terms, residue unfoldings and coefficient bounds
decls:
  - terms_at_point_finite
  - support_oneCoset
  - gg_matrix_bound
  - TwistedEisensteinNonvanishing
  - kappa_off_diagonal_dim_form_C
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orbital terms, residue unfoldings and coefficient bounds

This section proves five statements that bound or locate the terms of the orbital expansion. The first says that only finitely many terms sit at a given point. The second locates the support of a partial Fourier transform over a finite field in a single double coset, and shows that it is not zero. The third bounds a Gram matrix built from the Gelfand-Graev functions of finite general linear groups, given two standard facts about generic representations. The fourth shows that the nonvanishing of a twisted Eisenstein coefficient depends only on a double coset. The fifth bounds a mass of lattices times a dimension by the dimension of a space of forms. The results are used in the steps that need [nonempty hypotheses](/step/nonempty-hyps/) and in the step on [theta local matching](/step/theta-local-matching/), and also in the [residue field unfolding](/entry/residue-field-unfolding-claims-hold/), and in the theorems on the Gelfand-Graev matrix bound and on the nonvanishing on a double coset. For the background see [matrices](/learn/algebra/#matrices) and [representations of a group](/learn/representations/#representations-of-a-group).

### Finitely many terms at a point

We use the setting of the orbital expansion. It has a CM field $E$, a Hermitian space $V$ over $E$, a rank $r$, words $u$ and $u'$, a flag $F_0$ of rank $r$ attached to $u$, and lattices $\Lambda \subseteq V$ that are *row lattices* for $F_0$. For a row lattice $\Lambda$, the *terms* for $(u', F_0, \Lambda)$ are the classes of lifted flags $F'$ attached to $u'$ that are admissible for $\Lambda$ and $F_0$, under the relation $F_2 = n\, m\, F_1$ with $n$ and $m$ in the stabilizer groups of $\Lambda$ and the two flags. Each lifted flag $F'$ has a value $G(F_0, F') \in E$ and a cell in the space of points of rank $r + 1$. A term *sits at* a point $w$ if it has a representative $F'$ with $G(F_0, F') \neq 0$ whose cell contains $w$.

**Theorem 4.8.1 (Finitely many terms at a point).** Assume that the space $V$ has the signature of the setting. Then for every flag $F_0$, every row lattice $\Lambda$ for $F_0$ and every point $w$, only finitely many terms for $(u', F_0, \Lambda)$ sit at $w$.

Lean: `terms_at_point_finite`.

*Proof.* This is a reduction lemma applied to two proved inputs. The first is a frame statement: there is an integer $b > 0$ such that, for every row lattice $\Lambda$ and every upper unitriangular integral matrix $B$ of size $r + 1$ whose entries above the diagonal are divisible by $b$, some element $n$ of the stabilizer group of $\Lambda$ and $F_0$ acts on the frame of $F_0$ by $B$. The second is a finiteness of vectors of given norm: if $\Lambda$ is a lattice and $P$ is a subspace on which the form is positive at every complex embedding, then for every $c \in E$ only finitely many $x \in \Lambda \cap P$ have $h(x, x) = c$. We did not unfold how the reduction lemma combines them. $\square$

### The residue field unfolding

Let $k$ be a finite field, let $\psi_0$ be an additive character of $k$, and let $\chi_0, \chi_1, \dots$ be multiplicative characters of $k^\times$, extended by $0$ at $0$. Fix integers $k_0 \geq 1$, an even $m \geq 4$, $t$, and $1 \leq j \leq m - 2$, and put $c = m - 1 - j$. Let $n'$ and $n$ satisfy
$$n' + c + 1 = k_0 + m - 1 + (j - 1) t, \qquad n + c = k_0 + m - 1 + j t.$$
Let $R_1$ be the group of invertible maps $\rho$ of $k^{n + c}$ that, together with $\rho^{-1}$, preserve the flag of the spans $U_i$ of the first $n + i$ basis vectors, fix $e_n$, and move each $e_{n + i}$ only by an element of $U_i$.

The data define a function $\Phi_S$ on $(n + c) \times (n' + c + 1)$ matrices. In a fixed reordering of the indices, $\Phi_S(x)$ is zero unless the first $k_0 + m - 1$ diagonal entries are $1$ and every nonzero entry off the diagonal is in an allowed position. When this holds, $\Phi_S(x)$ is $\psi_0$ of the sum of the first superdiagonal entries, times characters $\chi_i$ of the determinants of $t \times t$ diagonal blocks, divided by $\chi_{j-1}$ of a leading principal minor. A matrix $\kappa$ is in the set $J_S$ if it satisfies the same diagonal and position conditions.

For a function $\Phi$ on $(n + c) \times (n' + c + 1)$ matrices, its *partial transform* $E_1 \Phi$ is the function on $n \times n'$ matrices $x$ given by
$$E_1 \Phi(x) = \sum_{t} \Phi(x_1(x, t))\, \psi_0\big(-\operatorname{ch}(x_1(x, t))\big),$$
where $t$ runs over the values of the free entries, $x_1(x, t)$ is the matrix with block $x$, these free entries and a fixed identity part, and $\operatorname{ch}$ is a sum of $c$ entries next to that part. For an invertible $h$ write $h \cdot \Phi$ for the function $x \mapsto \Phi(h^{-1} x)$.

**Theorem 4.8.2 (Support in one coset).** For all such data:

1. If $E_1(h \cdot \Phi_S)$ is not identically zero, then $h = \rho\, \kappa$ with $\rho \in R_1$ and $\kappa \in J_S$.
2. $E_1 \Phi_S$ is not identically zero.

Lean: `support_oneCoset`.

*Proof.* This is a reduction lemma applied to five proved inputs: a closure property of the pattern of allowed positions, a vanishing statement for the off-pattern terms, a lemma on the elements of $R_1$ that fix the first block, a step that removes one entry at a time, and a second claim on the support. We did not unfold the reduction lemma or its inputs. $\square$

So the support of the transform in $h$ is the single set $R_1 J_S$, and $\Phi_S$ itself gives a nonzero transform. This is the finite field form of the statement that the unfolded period is supported on one double coset.

### The Gelfand-Graev matrix bound

Let $k$ be a finite field with $q$ elements, let $\psi_0 \neq 1$ be an additive character, and let $U \subseteq \mathrm{GL}_r(k)$ be the upper unitriangular group. Put $\psi_U(u) = \psi_0\big(\sum_i u_{i, i+1}\big)$ on $U$, and extend it by $0$ off $U$. Put
$$\gamma(x) = \frac{1}{\# U} \sum_{y \in \mathrm{GL}_r(k)} \psi_U(y x y^{-1}).$$
A representation $\pi$ of $\mathrm{GL}_r(k)$ is *generic* if there is a nonzero linear form $\ell$ with $\ell(\pi(u) v) = \psi_U(u)\, \ell(v)$ for all $u \in U$.

**Definition 4.8.3 (Gelfand-Graev multiplicity one).** For every finite field, every $r$, every $\psi_0 \neq 1$ and every irreducible finite-dimensional $\pi$, any two such forms $\ell_1, \ell_2$ with $\ell_1 \neq 0$ satisfy $\ell_2 = c\, \ell_1$ for some $c \in \mathbb{C}$.

**Definition 4.8.4 (Mirabolic bound).** For every finite field, every $r$, every $\psi_0 \neq 1$ and every irreducible generic $\pi$,
$$\prod_{i=1}^{r-1} (q^i - 1) \leq \dim \pi.$$

Now let $v$ run over a finite set, with a finite field $k_v$ of order $q_v \geq 3$ and a character $\psi_v \neq 1$ at each $v$. Put $G = \prod_v \mathrm{GL}_r(k_v)$ and $\gamma(x) = \prod_v \gamma_v(x_v)$. Let $G$ act freely on the right on a finite set $X$, and let $d(i, j) \in G$ satisfy $j \cdot d(i, j) = i$ whenever $i$ and $j$ are in the same orbit. Let $A$ be the $X \times X$ matrix with entry $\gamma(d(i, j))$ when $i$ and $j$ are in the same orbit, and $0$ otherwise.

**Theorem 4.8.5 (Gelfand-Graev matrix bound).** Assume Gelfand-Graev multiplicity one and the mirabolic bound. Then $A$ is positive semidefinite, and so is
$$\prod_v \Big(1 + \frac{3}{q_v}\Big) \operatorname{Re} \gamma(1) \cdot I - \bar A.$$

Lean: `gg_matrix_bound`.

*Proof.* This is a reduction lemma applied to proved inputs. They are an equation for matrix coefficients, a statement on totally Hermitian forms, an eigenvalue bound, the positive semidefiniteness of a spectrum, and three statements on finite general linear groups. The eigenvalue bound is built from a bound at each place, the existence of a joint eigenvector, and a product formula. The three statements on $\mathrm{GL}_r(k)$ are these. First, under multiplicity one, $\gamma(1)^{-1} \sum_x \gamma(x) \pi(x)$ is $(\# U / \dim \pi) \cdot 1$ for generic irreducible $\pi$ and $0$ otherwise. Second, under the mirabolic bound and the formula $\# U = q^{r(r-1)/2}$, the ratio $\# U / \dim \pi$ is at most $\prod_{i=1}^{r-1} (1 - q^{-i})^{-1}$ for generic irreducible $\pi$. Third, $\# U = q^{r(r-1)/2}$. $\square$

The theorem is used in the theorem on the Gelfand-Graev matrix bound of the closed volume statements. The constant $1 + 3/q$ comes from the bound $\prod_{i=1}^{r-1} (1 - q^{-i})^{-1} \leq 1 + 3/q$ for $q \geq 3$. For $r = 2$ the product is $q/(q-1)$, and $q/(q-1) \leq 1 + 3/q$ since $q^2 \leq q^2 + 2q - 3$.

### Nonvanishing on a double coset

We use the setting of the twisted Eisenstein coefficients. It has a number field $E$, a field $K$, a prime $P$ of $E$ with prime absolute norm $q$ and $q \notin P^2$, a function $\psi : E \to K$, nonzero scalars $s$ and $c_q$, and a character $\xi$ of $(\mathcal{O}_E / P)^\times$. The ranks are integers $k, m, t$ with $k$ and $m$ even, $t$ odd, $m + 3 \leq k$, $k + m + 4 \leq t$, $3m < t$, and a further order bound; put $N_j = k + j(t + 1)$ and $c_j = m - 1 - j$. For each $i$ and each pair of automorphisms $h_i$ of $E^{N_i + c_i}$ and $h$ of $E^{N_{i+1} + c_{i+1}}$, the *twisted Eisenstein coefficient* $C_{A, B}(h_i, h)$ is the partial transform $E_1$, with $\psi$ in place of $\psi_0$, of a test function $\Phi_Q$ translated by $h_i$ and $h$ and weighted by a character built from $\xi$ and $c_q$. Here the free entries run over the numbers $a / q^A$ with $0 \leq a < q^{A + B}$, and each free entry carries the weight $q^{-B}$. The coefficient is *eventually nonzero* if there are $A_0$ and $B_0$ with $C_{A, B}(h_i, h) \neq 0$ for all $A \geq A_0$ and $B \geq B_0$.

Let $\Lambda_j$ be the standard lattice of $E^{N_j + c_j}$ localized at $P$. An automorphism $h$ of $E^{N_j + c_j}$ is *bounded* if $h \Lambda_j \subseteq q^{-j} \Lambda_j$ and $h^{-1} \Lambda_j \subseteq \Lambda_j$. Two automorphisms are in the same *double coset* if $h' = \rho\, h\, \kappa$ with $\rho$ in the group $R_1$ of the previous subsection and $\kappa$ in the stabilizer of both $\Lambda_j$ and a scaled lattice of parahoric type.

**Theorem 4.8.6 (Nonvanishing on a double coset).** Let $\psi$ be additive on $q^{-2m} \mathcal{O}_P$, equal to $1$ on $\mathcal{O}_P$, and equal to $1$ off $q^{-2m} \mathcal{O}_P$. Let $i + 3 \leq m$, let $h_i$, $h$ and $h'$ be bounded, and let $h$ and $h'$ be in the same double coset. If the coefficient at $(h_i, h)$ is eventually nonzero, then so is the coefficient at $(h_i, h')$.

Lean: `TwistedEisensteinNonvanishing`.

*Proof.* This is a reduction lemma applied to three proved inputs: a support statement for the test function, a periodicity of the test function, and a bound on the entries of bounded matrices. We did not unfold the reduction lemma. $\square$

### A lower bound for a space of forms

We use the setting of the theta lift with a full family $Y$ of lattices. For a word $u$ there are a constant $\Gamma_1$, a mass $\operatorname{mass}(u) = \sum_\Lambda 1/\#\operatorname{Aut}(\Lambda)$ over the lattices of $Y$ for $u$, a representation space $V_\pi(u)$, and a space $C_u$ of forms. A tie condition links the setting and the family.

**Theorem 4.8.7 (Dimension bound).** For every setting, every full family $Y$ that satisfies the tie condition and every word $u$,
$$0 \leq \Gamma_1 \qquad \text{and} \qquad \Gamma_1 \cdot \operatorname{mass}(u) \cdot \dim V_\pi(u) \leq \dim C_u.$$

Lean: `kappa_off_diagonal_dim_form_C`.

*Proof.* This is a reduction lemma applied to three proved inputs. The first transports lattices: each rational element of the group of the word moves the lattice of a point by an element of the flag stabilizer. The second bounds stabilizers: the elements that link two points over $\Lambda$ lie in a set with at most $\#\operatorname{Aut}(\Lambda)$ elements. The third bounds an index: over each $\Lambda$ there are at least $\Gamma_1$ points in distinct cosets. The reduction lemma adds two more proved inputs, an orbit count and a stabilizer statement. $\square$

**Remark 4.8.8 (Formalization).** The Gelfand-Graev theorem is an implication: multiplicity one and the mirabolic bound are hypotheses, and they are not proved here; see [GGMirabolic.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GGMirabolic.lean#L120). In the nonvanishing theorem the function $\psi$ is asked to be $1$ outside $q^{-2m} \mathcal{O}_P$, so it is a truncation and not a character of $E$; see [TwistedEisensteinNonvanishing.lean](lean:Formalism/PeriodIntegrals/TwistedEisensteinNonvanishing.lean#L355). The theorem there has the same name as the statement it proves. In the dimension bound the name of the theorem does not describe its statement. The constant $\Gamma_1$ in the statement and the count of the third input are given by two different expressions, and we did not check that they agree. The constants and spaces $\Gamma_1$, $V_\pi(u)$, $C_u$, the tie condition, the row lattices, the admissible lifts, the cells, the pattern of allowed positions and the test function $\Phi_Q$ were not unfolded beyond what is said above. The statements are in [TermDef.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermDef.lean#L192), [OneCosetSharp.lean](lean:Formalism/PeriodIntegrals/OneCosetSharp.lean#L181), [TwistedEisensteinNonvanishing.lean](lean:Formalism/PeriodIntegrals/TwistedEisensteinNonvanishing.lean#L361) and [DimFormC.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DimFormC.lean#L80). The theorems are in [TermsAtPtFinite.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/TermsAtPtFinite.lean#L8), [OneCosetSharp.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/OneCosetSharp.lean#L6), [GGMatBound.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/GGMatBound.lean#L15), [TwistedEisensteinNonvanishing.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/TwistedEisensteinNonvanishing.lean#L4) and [UnitaryDimensionFormula.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UnitaryDimensionFormula.lean#L6).
