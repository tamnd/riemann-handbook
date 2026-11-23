---
title: The Iwahori factorization for unitary groups
decls:
  - GlobalTheory.T.IwahoriStatement
  - GlobalTheory.CompanionTheory.Iwahori.stIwahori
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Iwahori factorization for unitary groups

This section proves the Iwahori factorization of a principal congruence subgroup of a $p$-adic unitary group. Every element congruent to $1$ is a product of an upper and a lower unipotent element, both congruent to $1$, and conjugation by a dominant torus element keeps the two factors congruent to $1$. This is the second condition of a Cartan structure in [Theorem 2.6.4](/entry/st-cartan-u/), which gives the uniform admissibility of unitary representations behind the tensor product theorem. The proof is block Gauss elimination, followed by a uniqueness argument that makes the two factors isometries. For background see [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups).

### Setting

Let $L$ be a nontrivially normed field of characteristic $0$, ultrametric, with compact closed balls. Let $s$ be a ring endomorphism of $L$ with $s \circ s = \mathrm{id}$, $|s(x)| = |x|$ and $s \neq \mathrm{id}$. Let $\delta \in L$ satisfy three conditions: $\delta \neq 0$; for $a \in L$, $|ax + s(ax)| \leq 1$ for all $|x| \leq 1$ if and only if $|a| \leq |\delta|$; and $c\delta + s(c\delta) = 1$ for some $|c| \leq 1$. Let $V$ be a finite-dimensional $L$-vector space and $h : V \times V \to L$ additive and $L$-linear in the second variable, with $h(y, x) = s(h(x, y))$ and $h(x, \cdot) = 0$ only for $x = 0$. An *isometry* is an $L$-linear automorphism $g$ with $h(gx, gy) = h(x, y)$.

**Definition 1.23.1 (Frame, lattice, congruence).** A *frame* is a family $e_1, \dots, e_l, f_1, \dots, f_l$ and a subspace $W$ with $h(e_i, e_j) = h(f_i, f_j) = 0$, $h(e_i, f_j) = \delta$ if $i = j$ and $0$ otherwise, $W$ orthogonal to all $e_i$ and $f_i$, $h(w, w) \neq 0$ for $w \in W \setminus 0$, and $V = \sum L e_i + \sum L f_i + W$. A *lattice* is a subgroup $\Lambda$ that is the set of vectors with all coordinates of norm at most $1$ in some basis. It is *adapted* to the frame if $\sum a_ie_i + \sum b_if_i + w \in \Lambda$ exactly when all $|a_i| \leq 1$, all $|b_i| \leq 1$ and $|h(w, w)| \leq 1$. For $\pi \in L$, an automorphism $g$ is *congruent to $1$ modulo $\pi$* if for every $x \in \Lambda$ there is $y \in \Lambda$ with $gx - x = \pi y$.

**Theorem 1.23.2 (Iwahori factorization).** Let $(e, f, W)$ be a frame, $\Lambda$ a lattice adapted to it, $|\pi| < 1$, and $k$ an isometry congruent to $1$ modulo $\pi$. Then there are isometries $a$ and $b$ with $k = ab$ and the following property. Let $u \in L^l$ with all $u_i \neq 0$ and $|u_1| \leq \dots \leq |u_l| \leq 1$. Let $t$ be an automorphism with $te_i = u_ie_i$, $tf_i = s(u_i)^{-1}f_i$ and $t = \mathrm{id}$ on $W$. Then $tat^{-1}$ and $t^{-1}bt$ are congruent to $1$ modulo $\pi$.

Lean: `GlobalTheory.T.IwahoriStatement` (also `GlobalTheory.CompanionTheory.Iwahori.stIwahori`).

With $u_i = 1$ we get $t = 1$, so $a$ and $b$ are themselves congruent to $1$.

Order the pieces $Le_1, \dots, Le_l, W, Lf_l, \dots, Lf_1$ with weights $1, \dots, 2l+1$, and let $P_i$ be the projections of $V = \bigoplus_i(\text{piece } i)$. An element $a$ of a ring with such pieces is *upper* if $P_iaP_j = 0$ whenever the weight of $j$ is less than that of $i$. It is *lower unipotent* if $P_iaP_j = 0$ whenever the weight of $i$ is less than that of $j$, and $P_iaP_i = P_i$.

**Theorem 1.23.3 (Inputs on lattices).**
1. (Adjoint.) Each $L$-linear $g$ has an adjoint $g^\ast$ with $h(gx, y) = h(x, g^\ast y)$.
2. (Inverse.) If $g\Lambda \subseteq \pi\Lambda$ and $|\pi| < 1$, then $1 + g$ has an inverse $1 + g'$ with $g'\Lambda \subseteq \pi\Lambda$.
3. (Block Gauss elimination.) Let $J$ be an additive subgroup of a ring with pieces, closed under products and under multiplication by each $P_i$ on both sides, such that $1 + J$ consists of units with inverses in $1 + J$. Then every $k \in 1 + J$ is $ab$ with $a, b \in 1 + J$, $a$ upper and $b$ lower unipotent.
4. (Triangular inverses.) The inverse of an invertible upper endomorphism is upper.
5. (Unitary factors.) Let $\ast$ be an anti-automorphism that maps $P_i$ to the piece of opposite weight. If $a$ is invertible and upper, $b$ is invertible and lower unipotent, and $(ab)^\ast$ is a two-sided inverse of $ab$, then $a^\ast a = 1$ and $b^\ast b = 1$.
6. (Torus conjugation.) Let $J$ be as in item 3 and stable under scalars of norm at most $1$. Let $T$ act on piece $i$ by $\tau_i \neq 0$, with $|\tau_i| \leq |\tau_j|$ when the weight of $i$ is at most that of $j$. If $a, b \in 1 + J$, $a$ upper and $b$ lower, then $TaT^{-1}$ and $T^{-1}bT$ lie in $1 + J$.

Iwahori and Matsumoto (1965), Section 2, give the factorization for Chevalley groups. Casselman's notes, Section 1.4, give it for reductive $p$-adic groups. Items 1, 2 and 4 are linear algebra, and item 2 is a Neumann series in the complete field $L$.

Lean: `GlobalTheory.T.hermitian_adjoint_exists` (also `GlobalTheory.T.congruence_endomorphism_inverse_exists`, `GlobalTheory.T.iwahori_upper_lower_factorization`, `GlobalTheory.T.upper_triangular_inverse_is_upper`, `GlobalTheory.T.unitary_factors_of_unitary_upper_mul_lowerUni`, `GlobalTheory.T.torus_conjugation_preserves_congruence`).

*Proof.* Let $J$ be the set of endomorphisms $g$ with $g\Lambda \subseteq \pi\Lambda$. It is closed under products. Since $\Lambda$ is adapted, $P_i\Lambda \subseteq \Lambda$, so $J$ is stable under the $P_i$ on both sides. Input 2 gives the inverses. So $J$ satisfies the conditions of input 3, and $k - 1 \in J$ since $k$ is congruent to $1$. Input 3 gives $k = ab$ with $a$ upper, $b$ lower unipotent and $a - 1, b - 1 \in J$.

The adjoint of input 1 is an anti-automorphism. Since $h(e_i, f_i) = \delta$ and $W$ is orthogonal to the $e_i$ and $f_i$, it maps the projection on $Le_i$ to the projection on $Lf_i$ and fixes the projection on $W$. As $k$ is an isometry, $k^\ast k = kk^\ast = 1$. Input 5, with input 4 for upper inverses and, by reversing the weights, for lower inverses, gives $a^\ast a = b^\ast b = 1$. In outline, $k = (k^\ast)^{-1}$ gives $a^{-1}(a^{-1})^\ast = bb^\ast$. The left side is upper and the right side is lower unipotent, so both are $1$. Hence $a$ and $b$ are isometries.

For $u$ and $t$ as in the theorem, $t$ acts on the pieces by $u_1, \dots, u_l, 1, s(u_l)^{-1}, \dots, s(u_1)^{-1}$. Since $|s(u_i)| = |u_i|$, these norms increase with the weight. Input 6 with $T = t$ then gives the claim. $\square$

**Classical form.** Let $K_\pi$ be the principal congruence subgroup of the unitary group $U(V, h)$ for $\Lambda$, $B$ the stabilizer of the isotropic flag $Le_1 \subseteq Le_1 + Le_2 \subseteq \dots$, and $\bar N$ the unipotent radical of the opposite group. The theorem says $K_\pi = (K_\pi \cap B)(K_\pi \cap \bar N)$, and that $t(K_\pi \cap B)t^{-1} \subseteq K_\pi$ and $t^{-1}(K_\pi \cap \bar N)t \subseteq K_\pi$ for dominant $t$.

**Remark 1.23.4 (Formalization).** The statement `CompanionTheory.Rg.FlB.StIwahori` is defined in [StSandwich.lean](lean:CompanionTheory/RealGroups/UnitaryAdmissibility/ArchimedeanUnitaryDual/StSandwich.lean#L102), in a folder named for the archimedean unitary dual, although the statement is $p$-adic. The proof is in [IwahoriStatement.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/IwahoriStatement.lean#L53). It uses only $\delta \neq 0$ from the three conditions on $\delta$. The input `unitary_factors_of_unitary_upper_mul_lowerUni` sits in a module named `AntiInvolutionSwapsUpperLowerStatement`. The pieces, weights and the set $J$ are `piece`, `wt` and `congJ`, defined in `IsCongIdealTwoTorsion`, next to an unrelated `twoTorsion` (L30), the $2$-torsion of $(\mathbb{Z}/4)^2$. The wrapper `GlobalTheory.T.IwahoriStatement` runs under `maxHeartbeats 1000000` and closes the goal with `first | exact`. We read the statements of the inputs, not their proofs.

## Notes and references

The chapter collects local inputs of the base change argument of Volume 8 and of the classification of the unitary dual of $\mathrm{GL}_n$. Sections 1 to 4, 17 and 18 feed the archimedean and cuspidal parts of base change. Sections 5 to 9, 14, 16 and 21 develop the theory of Bernstein and Zelevinsky for the unitary dual of $\mathrm{GL}_n$, and with it the step [EveryCharacter](/step/every-character/). Sections 10 to 12 and 15 put the parameters of unramified representations in a fixed order for the extremal embedding. Section 13 is the torus input of the twisted trace formula, and Section 19 gives local inputs of the theta argument for the discrete series. Section 20 belongs to the step [EveryCharacterOfLiterature](/step/every-character-of-literature/). Section 22 feeds the decay of matrix coefficients for discrete series, and Section 23 the Cartan structure of $p$-adic unitary groups behind the tensor product theorem.

- J. Arthur, *A trace formula for reductive groups I. Terms associated to classes in G(Q)*, Duke Math. J. 45 (1978), 911 to 952.
- I. N. Bernstein, *All reductive p-adic groups are tame*, Funct. Anal. Appl. 8 (1974), 91 to 93.
- I. N. Bernstein, *P-invariant distributions on GL(N) and the classification of unitary representations of GL(N) (non-archimedean case)*, Lecture Notes in Math. 1041 (1984), 50 to 102.
- I. N. Bernstein and A. V. Zelevinsky, *Representations of the group GL(n, F) where F is a non-archimedean local field*, Russian Math. Surveys 31:3 (1976), 1 to 68.
- I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. École Norm. Sup. 10 (1977), 441 to 472.
- A. Borel and Harish-Chandra, *Arithmetic subgroups of algebraic groups*, Ann. of Math. 75 (1962), 485 to 535.
- P. Cartier, *Representations of p-adic groups: a survey*, Proc. Sympos. Pure Math. 33, Part 1 (1979), 111 to 155.
- W. Casselman, *Introduction to the theory of admissible representations of p-adic reductive groups*, unpublished notes (1974), Section 1.4.
- W. Casselman, *The unramified principal series of p-adic groups I. The spherical function*, Compositio Math. 40 (1980), 387 to 406.
- W. Casselman and D. Miličić, *Asymptotic behavior of matrix coefficients of admissible representations*, Duke Math. J. 49 (1982), 869 to 930.
- W. Casselman and M. S. Osborne, *The n-cohomology of representations with an infinitesimal character*, Compositio Math. 31 (1975), 219 to 227.
- R. Godement, *Domaines fondamentaux des groupes arithmétiques*, Séminaire Bourbaki 15 (1962/63), Exposé 257.
- R. Godement, *The spectral decomposition of cusp-forms*, Proc. Sympos. Pure Math. 9 (1966), 225 to 234.
- R. Godement and H. Jacquet, *Zeta Functions of Simple Algebras*, Lecture Notes in Math. 260 (1972), Sections 3 and 6.
- D. R. Grayson, *Reduction theory using semistability*, Comment. Math. Helv. 59 (1984), 600 to 634.
- A. Grothendieck, *Éléments de géométrie algébrique IV, troisième partie*, Publ. Math. IHÉS 28 (1966), 5 to 255.
- Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62 (1968), Chapter I.
- R. Howe and T. Umeda, *The Capelli identity, the double commutant theorem, and multiplicity-free actions*, Math. Ann. 290 (1991), 565 to 619.
- N. Iwahori and H. Matsumoto, *On some Bruhat decomposition and the structure of the Hecke rings of p-adic Chevalley groups*, Publ. Math. IHÉS 25 (1965), 5 to 48.
- A. W. Knapp, *Representation Theory of Semisimple Groups*, Princeton University Press (1986), Chapters V and VIII.
- S. Lang, *Algebra*, Springer (2002), Chapter XIV, Section 2.
- H. Matsumura, *Commutative Ring Theory*, Cambridge University Press (1986), Section 23.
- A. Mínguez, *Correspondance de Howe explicite: paires duales de type II*, Ann. Sci. École Norm. Sup. 41 (2008), 717 to 741.
- D. Mumford, *Abelian Varieties*, Oxford University Press (1970), Sections 6, 8, 10 and 13.
- K. R. Parthasarathy, R. Ranga Rao and V. S. Varadarajan, *Representations of complex semi-simple Lie groups and Lie algebras*, Ann. of Math. 85 (1967), 383 to 429.
- I. Satake, *Theory of spherical functions on reductive algebraic groups over p-adic fields*, Publ. Math. IHÉS 18 (1963), 5 to 69.
- U. Stuhler, *Eine Bemerkung zur Reduktionstheorie quadratischer Formen*, Arch. Math. 27 (1976), 604 to 610.
- A. V. Zelevinsky, *Induced representations of reductive p-adic groups II. On irreducible representations of GL(n)*, Ann. Sci. École Norm. Sup. 13 (1980), 165 to 210.

