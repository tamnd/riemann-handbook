---
title: The integral Witt theorem
decls:
  - GlobalTheory.Hk3.IntWittMod.witt_mod_pow
  - GlobalTheory.T.integralWittTheorem_mod_uniformizerPow
  - GlobalTheory.Hk3.HoweG.exists_intUnitary_of_gramClass
  - GlobalTheory.T.exists_intUnitary_of_gramClass_alt
---
## The integral Witt theorem

This section proves a form of Witt's theorem for Hermitian lattices over an unramified quadratic extension of local fields: two families of integral vectors that are independent modulo the uniformizer and have congruent [[Gram matrices|00SPJSDT3Z]] are moved into each other, up to the given congruences, by an integral unitary matrix. The second theorem turns this into a statement on matrices: two matrices $x, y$ with the same lattice data differ, modulo integral matrices, by an integral unitary matrix on the left. The second theorem is the orbit step of the proof of unramified Howe duality in the next two sections: it shows that every term of maximal lattice index in a certain finite sum lies in one orbit of the integral unitary group. The background is the [local classification of Hermitian lattices](/learn/hermitian-lattices/#local-classification) and [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms).

### The local setting

Let $L$ be a field with a valuation $v$ with values in $\mathbb{Z} \cup \{\infty\}$, written multiplicatively in the code, and suppose $L$ is complete. Let $\mathcal{O} = \{a : v(a) \geq 0\}$ be its [[valuation ring|QSX12D8RQM]]. For $a, b \in L$ and $k \geq 0$ write $a \equiv b \pmod{\varpi^k}$ if $a - b = \varpi^k c$ with $c \in \mathcal{O}$.

**Definition 2.1.1.** Let $\varpi \in L$, let $\sigma$ be a ring endomorphism of $L$, and let $q$ be a natural number. The triple $(\varpi, \sigma, q)$ is an *unramified involution* if $\sigma^2 = 1$, $\sigma$ preserves $v$, $\sigma(\varpi) = \varpi$, $\varpi$ has valuation $1$, there is $x \in \mathcal{O}$ with $\sigma(x) - x$ a unit, $q \geq 2$, and the residue field $\mathcal{O}/\mathfrak{m}$ has $q^2$ elements.

So $\sigma$ is the Galois involution of an unramified quadratic extension $L / L^{\sigma}$, the uniformizer $\varpi$ is fixed, and $\sigma$ acts on the residue field $\mathbb{F}_{q^2}$ as the Frobenius of $\mathbb{F}_{q^2}/\mathbb{F}_q$. For a matrix $g$ write $g^* = \sigma(g)^{\mathsf{T}}$. A matrix $J \in GL_n(L)$ is Hermitian if $\sigma(J_{ij}) = J_{ji}$ for all $i, j$. It defines the [[Hermitian form|8NJ7XY6F1S]]
$$h_J(x, y) = \sum_{i, j} \sigma(x_i) J_{ij} y_j$$
and the [[unitary group|0R9R0Y1HDK]] $U(J) = \{g \in GL_n(L) : g^* J g = J\}$. A matrix is *integral* if it lies in the image of $GL_n(\mathcal{O})$. A family $(z_i)_{i \in I}$ of vectors in $\mathcal{O}^n$, with $I$ finite, is *independent modulo $\varpi$* if $\sum_i d_i z_i \equiv 0 \pmod{\varpi}$ with all $d_i \in \mathcal{O}$ forces $d_i \equiv 0 \pmod{\varpi}$ for all $i$.

### Witt's theorem modulo powers of the uniformizer

**Theorem 2.1.2 (Integral Witt theorem).** Let $(\varpi, \sigma, q)$ be an unramified involution on $L$ with $q$ odd, and let $J \in GL_{n}(\mathcal{O})$ be Hermitian. Let $I$ be a finite set, let $a : I \to \mathbb{N}$ with $a_i \geq 1$ for all $i$, and let $(z_i)$ and $(z'_i)$ be families in $\mathcal{O}^{n}$, both independent modulo $\varpi$, with
$$h_J(z'_i, z'_j) \equiv h_J(z_i, z_j) \pmod{\varpi^{\min(a_i, a_j)}}$$
for all $i, j \in I$. Then there is an integral $h \in U(J)$ with $h z_i \equiv z'_i \pmod{\varpi^{a_i}}$ for all $i$, coordinate by coordinate.

Lean: `GlobalTheory.Hk3.IntWittMod.witt_mod_pow` (also `GlobalTheory.T.integralWittTheorem_mod_uniformizerPow`, a second name)

*Proof.* We show by induction on $k \geq 1$ that there is an integral $h \in U(J)$ with $h z_i \equiv z'_i$ modulo $\varpi^{\min(a_i, k)}$ for all $i$. Taking $k = \max_i a_i$ gives the theorem.

For $k = 1$ the hypothesis gives the congruences of Gram matrices modulo $\varpi$, and the case of one power of $\varpi$ is a separate lemma: modulo $\varpi$ the forms live over the residue field $\mathbb{F}_{q^2}$, where Witt's theorem for nondegenerate Hermitian forms gives an integral matrix $g$ with $g^* J g \equiv J$ and $g z_i \equiv z'_i$ modulo $\varpi$. A Newton iteration (here $q$ odd is used) corrects $g$ step by step without changing it modulo $\varpi$, and since $L$ is complete the corrections converge to an integral matrix in $U(J)$.

For the step from $k$ to $k + 1$, suppose $h z_i \equiv z'_i \pmod{\varpi^{\min(a_i, k)}}$. The indices with $a_i \leq k$ are finished. For the others the family $(h z_i)$ is again independent modulo $\varpi$ and has the same Gram matrix as $(z_i)$, so the hypothesis gives
$$h_J(z'_i, z'_j) \equiv h_J(h z_i, h z_j) \pmod{\varpi^{k+1}}.$$
The Hensel step for families gives an integral $g \in U(J)$ with $g \equiv 1 \pmod{\varpi^k}$ and $g h z_i \equiv z'_i \pmod{\varpi^{k+1}}$ for these indices. Since $g \equiv 1 \pmod{\varpi^k}$, the congruences for the finished indices survive. So $gh$ works for $k + 1$. This is the usual [[Hensel's lemma|010QVB71T2]] argument: the error of the Gram matrix at level $k + 1$ is a Hermitian matrix over the residue field, and one solves a linear equation for a correction $1 + \varpi^k X$ with $X$ in the Lie algebra; the factor $\tfrac12$ needed for this is a unit because $q$ is odd. $\square$

The classical Witt theorem says that an isometry between subspaces of a nondegenerate Hermitian space extends to the whole space; see O. T. O'Meara, *Introduction to Quadratic Forms*, §42 for quadratic forms. The theorem above is its integral form for unimodular Hermitian lattices over an unramified extension, with congruences in place of equalities.

### Matrices with the same lattice data

Now fix Hermitian $J_S \in GL_n(\mathcal{O})$ and $J_T \in GL_{n'}(\mathcal{O})$. For $x \in M_{n' \times n}(L)$ let $x^{\dagger} = J_S^{-1} x^* J_T$ be its adjoint.

**Definition 2.1.3.** Let $x, y \in M_{n' \times n}(L)$.

1. $y$ is *dominated* by $x$ if for every $u \in \mathcal{O}^n$ with $x u \in \mathcal{O}^{n'}$ also $y u \in \mathcal{O}^{n'}$, and $y x^{\dagger} w \in \mathcal{O}^{n'}$ for every $w \in \mathcal{O}^{n'}$.
2. $x$ and $y$ have *the same Gram class* if for all $m, m' \in \mathcal{O}^n$ and $c \in \mathcal{O}$ with $x(c m)$ and $x(c m')$ integral,
$$c \bigl(h_{J_T}(y m, y m') - h_{J_T}(x m, x m')\bigr) \in \mathcal{O}.$$
3. The *lattice index* $\operatorname{idx}(x)$ is the number of elements of the image of $u \mapsto x u$ from $\mathcal{O}^n$ to $L^{n'}/\mathcal{O}^{n'}$, that is, the index of $\mathcal{O}^{n'}$ in $x \mathcal{O}^n + \mathcal{O}^{n'}$.

**Theorem 2.1.4 (Integral unitary from a Gram class).** Let $(\varpi, \sigma, q)$ be an unramified involution on $L$ with $q$ odd, and let $J_S \in GL_n(\mathcal{O})$ and $J_T \in GL_{n'}(\mathcal{O})$ be Hermitian. Let $x, y \in M_{n' \times n}(L)$ with $x J_S^{-1} x^*$ integral. If $y$ is dominated by $x$, $x$ and $y$ have the same Gram class, and $\operatorname{idx}(y) = \operatorname{idx}(x)$, then there is an integral $h \in U(J_T)$ such that $y - h x$ has entries in $\mathcal{O}$.

Lean: `GlobalTheory.Hk3.HoweG.exists_intUnitary_of_gramClass` (also `GlobalTheory.T.exists_intUnitary_of_gramClass_alt`, a second name)

*Proof.* By elementary divisors over the [[discrete valuation ring|MGM3CNJW9V]] $\mathcal{O}$ (a form of the [[Smith normal form|MV28Z5N9XX]]) there are $V \in GL_n(\mathcal{O})$ and exponents $a_1, \dots, a_n \geq 0$ such that for every $c \in \mathcal{O}^n$, the vector $x V c$ is integral exactly when $\varpi^{a_j}$ divides $c_j$ for all $j$. The first half of domination says that the lattice $\{u : x u \in \mathcal{O}^{n'}\}$ is contained in $\{u : y u \in \mathcal{O}^{n'}\}$; the two lattice indices are equal, so the two lattices are equal, and the same description holds for $y$ with the same $V$ and $a_j$.

Let $I = \{j : a_j > 0\}$ and put $z_j = x V(\varpi^{a_j} e_j)$ and $z'_j = y V(\varpi^{a_j} e_j)$ for $j \in I$. These are integral. Each family is independent modulo $\varpi$: an integral relation $\sum d_j z_j \equiv 0 \pmod \varpi$ means that $x V c$ is integral for $c_j = \varpi^{a_j - 1} d_j$, so $\varpi^{a_j}$ divides $\varpi^{a_j - 1} d_j$. The Gram class condition, applied with $m = V \varpi^{a_i} e_i$, $m' = V \varpi^{a_j} e_j$ and suitable $c$, gives
$$h_{J_T}(z'_i, z'_j) \equiv h_{J_T}(z_i, z_j) \pmod{\varpi^{\min(a_i, a_j)}}.$$
The integral Witt theorem gives an integral $h \in U(J_T)$ with $h z_j \equiv z'_j \pmod{\varpi^{a_j}}$ for $j \in I$. Then $(y - h x) V e_j$ is integral for every $j$: for $j \in I$ divide the congruence by $\varpi^{a_j}$, and for $a_j = 0$ both $x V e_j$ and $y V e_j$ are integral. Since $V$ is invertible over $\mathcal{O}$, $y - h x$ is integral. $\square$

**Remark 2.1.5 (Formalization).** The first theorem is at [IntegralWittTheoremModUniformizerPow.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/IntegralWittTheoremModUniformizerPow.lean#L105) and the second at [ExistsIntUnitaryOfGramClass.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsIntUnitaryOfGramClass.lean#L17). The names in the namespace `GlobalTheory.T` are restatements whose proofs only apply the first names ([IntegralWittTheoremModUniformizerPowStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/IntegralWittTheoremModUniformizerPowStatement.lean#L8), [ExistsIntUnitaryOfGramClassStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsIntUnitaryOfGramClassStatement.lean#L8)). The base case is `witt_mod_base` and the Hensel step is `hensel_step`. In the second theorem the hypothesis that $x J_S^{-1} x^*$ is integral is named `_hG` and is not used ([L27](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsIntUnitaryOfGramClass.lean#L27)), and the hypotheses that $J_S$ is integral and Hermitian are also not used; the theorem holds without them. The valuation is a `Valued` instance with values in `WithZero (Multiplicative ℤ)`, so "valuation $1$" for $\varpi$ is written `ofAdd (-1)`, and the lattice index is a `Nat.card`.
