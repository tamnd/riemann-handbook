---
title: Pure periods and adapted determinants
decls:
  - GlobalTheory.T.pure_period_local_basis_exists
  - GlobalTheory.CompanionTheory.Ar.Fl.DSplit.exists_split_period
  - GlobalTheory.T.cm_type_valuation_embedding
  - GlobalTheory.CompanionTheory.Ar.Flat.det_adapted_eq_unit_mul_const
  - GlobalTheory.CompanionTheory.Ar.Flat.ExG.targetO
  - GlobalTheory.T.valuation_lattice_matrix_reduction
  - GlobalTheory.CompanionTheory.Ar.Flat.ExG.Core.det_adapted_core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pure periods and adapted determinants

This section has two results on lattices with an action of a CM field $E$. The first one moves a period map to one of pure type and finds a basis of the lattice, prime to a given prime $\ell$, that splits into a positive and a negative part. It is used for the [frames of CM points](/entry/exists-cm-point-loc-basis-frames/). The second one computes the determinant of an adapted basis of the de Rham lattice up to a unit and a constant that depends only on $E$, the embeddings and the ranks. It is used for the [values at points](/entry/value-at-point/). For CM fields see [the section on kinds of number fields](/learn/number-fields/#kinds-of-number-fields), and for hermitian forms see [the section on hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms).

### Pure periods with a split local basis

Let $E$ be a CM field with a host $H$, and let $D$ be a datum over $H$: a projective module $\Lambda$ over the integers $O_E$ with an alternating unimodular form $e$ that is adjoint for complex conjugation, and a signature $(D_p, D_q)$. The form gives an $E$-valued sesquilinear form $\langle x, y \rangle$ on $\Lambda$. The host fixes a square root $r$ in $E$ and a square root $r_0$ in $\mathbb{C}$ of the same negative integer. For a family $x$ of vectors, $\mathrm{Gram}(x)$ is the matrix of the $\langle x_m, x_n \rangle$.

**Definition 5.10.1 (Local basis).** Let $\ell$ be a prime. A family $x_i$ in $\Lambda$ is a local basis at $\ell$ if it is linearly independent over $O_E$ and there is an integer $n$ prime to $\ell$ with $n y$ in the span of the $x_i$ for every $y \in \Lambda$.

Lean: `GlobalTheory.CompanionTheory.Ar.Fl.IsLocBasis`.

**Definition 5.10.2 (Pure family).** Let $P \colon \Lambda \to \mathbb{C}^g$ be a period map for a type $ty$. A family $x$ indexed by $\{1, \dots, p\} \sqcup \{1, \dots, q\}$ is pure for $P$ if the first $p$ vectors lie in the pure lattice of $P$ for the sign $+r_0$ and the last $q$ vectors lie in the pure lattice for $-r_0$.

Lean: `GlobalTheory.CompanionTheory.Ar.Fl.IsPure`.

We do not unfold the host, the datum, the period condition, the type condition or the pure lattices.

**Theorem 5.10.3 (Pure periods with a local basis).** Let $P_0$ be a period map for $D$ of type $ty$, where $ty$ is a type function of signature $(p, q)$ with $p + q = D_p + D_q$. Let $\ell$ be a prime. Then there are a period map $P$ of type $ty$ and a family $x$ indexed by $\{1, \dots, p\} \sqcup \{1, \dots, q\}$ that is a local basis at $\ell$ and is pure for $P$.

Lean: `GlobalTheory.CompanionTheory.Ar.Fl.DSplit.exists_split_period` (also `GlobalTheory.T.pure_period_local_basis_exists`, a second name).

*Proof.* Start with a local basis $x$ at $\ell$ whose Gram determinant $\delta$ is nonzero and has bounded $\ell$-adic norm. Let $\Psi$ be the set of embeddings $\tau \colon E \to \mathbb{C}$ with $\tau(r) = r_0$. For $\tau \in \Psi$ the matrix $M_\tau = i\, \tau(\mathrm{Gram}(x))$ is hermitian of signature $(p, q)$, so there is a $p \times (p + q)$ matrix $C_\tau$ with $C_\tau M_\tau C_\tau^*$ positive definite. A perturbation lemma gives an integral matrix $Y$ such that
$$X = \begin{pmatrix} 1 & 0 \end{pmatrix} + \ell\, Y$$
makes $X M_\tau X^*$ positive definite for all $\tau \in \Psi$. Put $x'_a = \sum_m X_{a m} x_m$. Then $x'_a = x_a + \ell w_a$, and the ultrametric stability of determinants shows that the Gram determinant of $x'$ has the same $\ell$-adic norm as that of the first $p$ vectors of $x$. So $x'$ extends to a local basis $x_2$ at $\ell$ whose first $p$ vectors are $x'$ and whose last $q$ vectors are orthogonal to them. On the first block $i\,\tau(\mathrm{Gram})$ is positive definite for $\tau \in \Psi$, and the signature forces it to be negative definite on the orthogonal block. A splitting lemma for Gram matrices of this signature gives a period map $P$ for which $x_2$ is pure. $\square$

### Determinants of adapted bases

Now let $C$ be a field of characteristic $0$ with a valuation $\nu$, and $V$ its valuation ring. Assume there is $\ell \in C$ with $0 < \nu(\ell) < 1$, that every embedding $s \colon E \to C$ sends $O_E$ into $V$, and that there are $[E : \mathbb{Q}]$ such embeddings. Let $c$ be an involution of $O_E$ and let $\sigma, \sigma'$ be embeddings with $\sigma'(a) = \sigma(c(a))$.

For an action $\rho$ of $O_E$ on a space $W$ over $C$, let $W_s$ be the eigenspace where $a$ acts by $s(a)$, and $\pi_s$ the projection onto it. Let $\rho_H$ be an action on $W \times W^\vee$ that is $\rho$ on the first factor and $\varphi \mapsto \varphi \circ \rho(c(a))$ on the second.

**Definition 5.10.4 (Adapted family).** Let $v_1, \dots, v_p$ and $w_1, \dots, w_q$ be vectors of $W$. A family $u_1, \dots, u_{p+q}$ in $W \times W^\vee$ is adapted to $(v, w)$ for $\sigma$ if each $u_k$ lies in the $\sigma$-eigenspace of $\rho_H$, the first component of $u_i$ is $v_i$ for $i \le p$, and for $j \le q$ the vector $u_{p+j}$ is $(0, \varphi_j)$ with $\varphi_j(w_{j'}) = 1$ if $j = j'$ and $0$ otherwise.

Lean: `GlobalTheory.CompanionTheory.Ar.Flat.IsAdapted`.

**Theorem 5.10.5 (Adapted determinants).** There is a nonzero $\gamma \in C$ with the following property. Let $W$ be a finite dimensional space over $C$ with actions $\rho$ and $\rho_H$ as above, and let $H \subseteq W \times W^\vee$ and $\mathrm{Lie} \subseteq W$ be $V$-lattices such that:
1. the image of $H$ in $W$ is $\mathrm{Lie}$, and $(0, \varphi) \in H$ if and only if $\varphi(\mathrm{Lie}) \subseteq V$;
2. $H$ is free over $O_E$ on vectors $x_1, \dots, x_{p+q}$, and $\dim W_s = rk(s)$ for every $s$;
3. the $v_i$ are a basis of $\mathrm{Lie} \cap W_\sigma$, and the $w_j$ are a basis of $\mathrm{Lie} \cap W_{\sigma'}$;
4. $u$ is adapted to $(v, w)$ for $\sigma$, and the vectors $\sum_j A_{ij} u_j$ are a basis of the lattice $\pi_\sigma(H)$.

Then $\det A = \varepsilon \gamma$ for a unit $\varepsilon$ of $V$.

Lean: `GlobalTheory.CompanionTheory.Ar.Flat.det_adapted_eq_unit_mul_const` (also `GlobalTheory.T.cm_type_valuation_embedding`, a second name).

*Proof.* This is the theorem on the target below for the valuation subring of $\nu$, which is $V$ up to the identification of the two rings. $\square$

**Theorem 5.10.6 (The target).** The theorem on adapted determinants holds with $V$ the valuation subring of $\nu$.

Lean: `GlobalTheory.CompanionTheory.Ar.Flat.ExG.targetO`.

*Proof.* Let $S$ be the set of embeddings $s$ such that $s(a) - \sigma(a)$ is not a unit for any $a \in O_E$. A lemma on monogenic blocks gives $\pi \in O_E$ with distinct values $s(\pi)$ on $S$, such that the functions on $S$ that are polynomials in $s(\pi)$ over $V$ are the span of the functions $s \mapsto s(a)$. We take
$$\gamma = \frac{Q}{P^{p+q}}, \qquad P = \prod_{s \neq \sigma} (\sigma(\pi) - s(\pi)), \qquad Q = \prod_{s \neq \sigma} (\sigma(\pi) - s(\pi))^{r_s},$$
with products over $S$ and ranks $r_s$ defined below. Decompose $W \times W^\vee$ into the eigenspaces of $\rho_H$. For $s \in S$ let $g_s$ map $C^{p+q}$ to $W_s$ by the coordinates of the free basis $x$. A vanishing criterion for CM types shows that a sum $\sum_s g_s(f_s)$ vanishes only if each term vanishes, and $r_s$ is the dimension of the kernel of $g_s$. The rank of the kernel at $\sigma$ is $q$, by the duality between $W_\sigma$ and the dual of $W_{\sigma'}$. The vectors $v_i$ are the images of the first $p$ adapted vectors, and the last $q$ adapted vectors map to $0$ and form a basis of the $\sigma$-part of the kernel lattice. The lattice reduction theorem below then gives the unit $\varepsilon$ with $\det A \cdot P^{p+q} = \varepsilon\, Q$. $\square$

**Theorem 5.10.7 (Lattice reduction).** Let $w$ be a valuation on $C$ with valuation subring $\mathcal{O}$, and let $\ell \in C$ with $0 < w(\ell) < 1$. Let $S$ be finite, $a \colon S \to \mathcal{O}$ injective, $\tau \in S$, and $g_s \colon C^{p+q} \to W$ linear maps with:
1. $\sum_s g_s(f_s) = 0$ only if every $g_s(f_s) = 0$, and $\dim \ker g_s = r_s$ with $r_\tau = q$;
2. $v_1, \dots, v_p$ independent, with $y$ in their $\mathcal{O}$-span if and only if $y$ is in the image of $g_\tau$ and $y = \sum_s g_s(f_s)$ for some $f$ in the free lattice, the families $f_s = F(a_s)$ with $F$ a vector of polynomials over $\mathcal{O}$;
3. vectors $U_1, \dots, U_{p+q}$ with $g_\tau(U_i) = v_i$ for $i \le p$ and $g_\tau(U_{p+j}) = 0$, such that the $U_{p+j}$ are a basis of the $\tau$-part of the kernel lattice, the $f$ in the free lattice with $g_s(f_s) = 0$ for all $s$;
4. the vectors $\sum_j A_{ij} U_j$ are a basis of the $\tau$-part of the free lattice.

Here the $\tau$-part of a lattice of families $f$ is its image under $f \mapsto f_\tau$.

Then there is a unit $\varepsilon$ of $\mathcal{O}$ with
$$\det A \prod_{s \neq \tau} (a_\tau - a_s)^{p+q} = \varepsilon \prod_{s \neq \tau} (a_\tau - a_s)^{r_s}.$$

Lean: `GlobalTheory.CompanionTheory.Ar.Flat.ExG.Core.det_adapted_core` (also `GlobalTheory.T.valuation_lattice_matrix_reduction`, a second name).

*Proof.* The kernel lattice gives a filtration of the free lattice. The images of the $v_i$ in the quotient by the kernel are a lattice basis there. A determinant formula for appended bases gives $c$ with
$$\det(U) = c \cdot \det\Bigl(\sum_j A_{ij} U_j\Bigr), \qquad w(c) = \prod_{s \neq \tau} w(a_\tau - a_s)^{p + q - r_s}.$$
Since $\det(\sum_j A_{ij} U_j) = \det A \det U$ and $\det U \neq 0$, we get $c \det A = 1$. So both sides of the claim have the same value. They are nonzero, because $a$ is injective, so their quotient is a unit. $\square$

**Remark 5.10.8 (Formalization).** The theorem on the target cites a lemma on monogenic blocks under the name `T.statement_unavailable_one` ([CmTypeValuationEmbedding.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/CmTypeValuationEmbedding.lean#L32)), a placeholder name. The theorem on adapted determinants is proved by passing the theorem on the target to a theorem named for a rank bound of conjugate embeddings, which takes it as a hypothesis (line 302). The theorem on pure periods is declared with its full name after the end of its namespace ([PurePeriodLocalBasisExists.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/PurePeriodLocalBasisExists.lean#L202)). The second names call the first with `first | exact @…`. We did not open the proofs of the perturbation, orthogonal basis and splitting lemmas, the vanishing criterion, or the determinant formula for appended bases.
