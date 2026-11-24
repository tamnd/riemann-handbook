---
title: Families of Hermitian lattices and Theorem B
decls:
  - Formalism.MainNotions.tCV_of_ties
  - Formalism.MainNotions.slopeLineT_holds
  - Formalism.MainNotions.StandardLattice.HarishChandraReduction.tuSize_min
  - Formalism.MainNotions.LatticeGluingRadicals.lattice_theorem_B
  - Formalism.MainNotions.LatticeGluingRadicals.theorem_B_section
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Families of Hermitian lattices and Theorem B

This section collects four results on the Hermitian lattices that a family of global data carries. The first two give, for large members of a family, a column valuation datum and the slope of the ramified line. They feed [Theorem 3.6.8 of Volume 15](/entry/shape-closed-link-n-of-green/) and the local matching step [Theta local matching](/step/theta-local-matching/). The third bounds the size of the auxiliary prime $T_u$; it feeds [Theorem 8.11.3 of Volume 15](/entry/row-h-tu-c-tmin-alt/). The fourth is Theorem B, an inequality between the norms of two flags in a unimodular Hermitian lattice; it feeds [Theorem 4.6.3](/entry/small-term-of-corank-one-pair/).

Throughout, $E$ is the CM host field of a global datum $\mathcal{D}$, with complex embeddings $\tau$, and $f$ is the degree attached to the ranks of $\mathcal{D}$. A family $\mathcal{F}$ assigns to each large $x$ a finite set of global data $\mathcal{D}_{x,i}$. For each word $u$ the datum gives a prime $T_u$, Hermitian spaces over $E$, and lattices with Hermitian forms at each level. Background on these objects is in [Hermitian lattices](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

### Column valuations

**Definition 8.6.1 (Column valuation datum).** Let $u$ be a word of $\mathcal{D}$. A column valuation datum for $u$ consists of the following, for each class $c$ at level $0$ (there is at least one class) and each embedding $\tau$ of the field $L$ of definition:

1. a ring map $\rho_\tau \colon E \to L$ and a good Hermitian lattice $Q_{c,\tau}$ over $L$ of rank $N_0$;
2. an additive map $b_{c,\tau}$ from the level-$0$ space to $Q_{c,\tau}$ with $b_{c,\tau}(a y) = \rho_\tau(a) b_{c,\tau}(y)$, such that the lattice of $Q_{c,\tau}$ is spanned by the image of the class lattice of $c$, and such that $b_{c,\tau}$ carries the Hermitian norm of $y$ to the norm at each infinite place;
3. a lattice condition on each class lattice relative to $T_u^{2f}$;
4. an injective linear map $\operatorname{co}$ from the level-$0$ space of $u$ to tuples of polynomials, whose image is the set of tuples with each entry in the span of the highest-weight vectors of weight $\lambda_0$;
5. a local description: at each finite place $w$, for each choice of local bases $\gamma_{c,\tau}$ of the $Q_{c,\tau}$, a vector $x$ lies in the local lattice at $w$ if and only if $\gamma^{-1}$ carries $\operatorname{co}(x)_c$ into the integral span at $w$, for each $c$;
6. an archimedean description: at each infinite place $v$, the norm of $x$ is the sum over $c$ of the norms of $\operatorname{co}(x)_c$, computed with the inverse Gram matrices of the $Q_{c,\tau}$ at $v$.

Lean: `Formalism.MainNotions.flipTwoThree.ColVal`

So a column valuation datum identifies the level-$0$ lattice of $u$, both locally and at infinity, with a sum of explicit lattices built from the class lattices.

**Theorem 8.6.2 (Column valuations from ties).** Let $\mathcal{F}$ be a family. Assume that there is $x_0$ such that, for each $x \geq x_0$ and each $i$, the datum $\mathcal{D}_{x,i}$ has a tied symmetric system of column forms and the stabilizer of each class at level $0$ has at most one element. Then there is $x_0'$ such that, for each $x \geq x_0'$, each $i$ and each word $u$ of $\mathcal{D}_{x,i}$, there is a column valuation datum for $u$.

Lean: `Formalism.MainNotions.tCV_of_ties`

*Proof.* We take the following as proved: each global datum with a tied symmetric system of column forms and trivial stabilizers at level $0$ has a column valuation datum for each word. Apply it to $\mathcal{D}_{x,i}$ for $x \geq x_0$, with $x_0' = x_0$. $\square$

### The ramified line

For a word $u$ of $\mathcal{D}$ let $\mu_0$ be the slope of the level-$0$ lattice and $\mu_{\mathrm{ram}}$ the slope of its ramified sublattice. The Hida setting for $u$ asks three things: $2 f N_m + 1 < T_u$; $4 a_{\max} < T_u$ and the alcove condition $2(w_a - w_b + N_j) < T_u$ for the weights of $\lambda_j$ at all levels $j \leq m$; and the top shifts $b_\tau$ are non-negative at the top embeddings. The concrete forms at level zero are a tied symmetric system of forms whose level-$0$ character $\chi$ has finite order $n > 0$ with values in $L$, together with the condition that the stabilizers of the classes at level $0$ are trivial.

**Theorem 8.6.3 (Slope of the ramified line).** Let $u$ be a word of $\mathcal{D}$. Assume the Hida setting for $u$ and the concrete forms at level zero. Then
$$\mu_{\mathrm{ram}} = \mu_0 - \frac{f \log(T_u - 1)}{T_u - 2}.$$

Lean: `Formalism.MainNotions.slopeLineT_holds`

*Proof.* The tied system of forms restricts to a system of forms at level $0$, and the character $\chi$ keeps its finite order and its values in $L$. The slope formula for a tied system at level $0$ in the Hida setting then gives the equation. $\square$

### The size of the auxiliary prime

The following statement on binary Hermitian forms is an input. It is a case of the Hasse principle for Hermitian forms over a CM field (Landherr's theorem): a positive definite form of rank at least $2$ represents each totally positive element that it represents locally, and locally such a form represents every nonzero element.

**Theorem 8.6.4 (Binary Hermitian representation).** Let $K$ be an unramified CM field with complex conjugation $s \mapsto \bar{s}$. Let $a$, $b$, $n$ be totally positive elements of the totally real subfield. Then there are $s, t \in K$ with $a s \bar{s} + b t \bar{t} = n$.

Lean: `Formalism.HermitianLattices.Ext.L3.HermRepUnram`

Let $C_{\mathrm{YL}}$ and $C_{\mathrm{Tu}}$ be the two constants of the family, and put $c_{\min}(y) = \max(11, 16 + 3\max(5, y + 1))$. The size condition on $T_u$ says: there is $x_0$ such that, for each $x \geq x_0$ and each $i$, the lower size condition on $T_u$ holds for $\mathcal{D}_{x,i}$ and $\log T_u \leq C_{\mathrm{Tu}}\, m\, L$ for each word $u$, where $m$ is the number of levels and $L$ the log size of the family member.

**Theorem 8.6.5 (Size of the auxiliary prime).** Assume the binary Hermitian representation theorem. Let $\mathcal{F}$ be a family with $c_{\min}(C_{\mathrm{YL}}) \leq C_{\mathrm{Tu}}$. Assume that for large $x$ each member $\mathcal{D}_{x,i}$ has base volume equal to its mass, and satisfies the two-sided bound for the degrees $d_\sigma(\rho)$ of the discrete series: for $e^{-r} \leq \epsilon_0 < 1/2$ and each $\rho$ with a gap at least the spectral gap bound,
$$(1 - \epsilon_0) \dim V_{\lambda(\rho)} \leq d_\sigma(\rho) \leq 4 d_\tau\, (3 p_Y q_Y |\lambda(\rho)|)^{p_Y q_Y}.$$
Then the size condition on $T_u$ holds.

Lean: `Formalism.MainNotions.StandardLattice.HarishChandraReduction.tuSize_min`

*Proof (outline).* The Siegel mass ratio for the family, the base volume and the degree bound give the explicit form of the Vandermonde count, with both constants equal to $\max(5, C_{\mathrm{YL}} + 1)$. The bound on the rows gives the second input with the same constant. Together they give the fifth part of the family bounds for large $x$. The general size theorem for $T_u$ then gives the size condition with the constant $c_{\min}(C_{\mathrm{YL}})$, and so with each larger constant $C_{\mathrm{Tu}}$. $\square$

### Theorem B

Let $V$ be a Hermitian space over $E$ with form $h$, and let $\Lambda$ be a lattice in $V$. For $T \in E$, a flag of norm $T$ is a tuple $(e_1, \dots, e_r, z)$ with the $e_a$ linearly independent and isotropic, $h(e_a, z) = 0$ and $h(z, z) = -T$. Let $X = \operatorname{span}(e_a)$. For two flags $F$ and $F'$, with frames $(f_1, \dots, f_{r+1})$ and $(f'_1, \dots, f'_{r+1})$, let $\hat Z(F,F')$ be the matrix $(h(f_a, f'_b))_{a,b}$, let $D_r$ be its leading minor of size $r$ and $D_{r+1}$ its determinant. For $T, T'$ rational and an embedding $\tau$ put
$$\operatorname{ch}_\tau(F,F') = \frac{|\tau(D_{r+1}/D_r)|}{\sqrt{T T'}}, \qquad \operatorname{sh}_\tau = \sqrt{\operatorname{ch}_\tau^2 - 1}.$$
Put $\operatorname{cs}_\tau = \operatorname{ch}_\tau/\operatorname{sh}_\tau$ and $\operatorname{is}_\tau = 1/\operatorname{sh}_\tau$ if $D_r \neq 0$, and $\operatorname{cs}_\tau = 1$, $\operatorname{is}_\tau = 0$ if $D_r = 0$.

The hypotheses of Theorem B are these. The space is the level-$0$ space $V$ of $\mathcal{D}$, of rank $k$, and $g = g_0 g_1$ is the product of the two type primes.

1. $\Lambda$ is a unimodular lattice, the vector $z$ of $F$ lies in $\Lambda$, and $X \cap \Lambda$ is locally spanned by multiples $c_a e_a$ at each prime, with $c_a = 1$ at the primes over $g$; also each $c z$ in the lattice $L$ attached to $F$ has $c$ integral.
2. $T_u$ and $T'$ are primes at least $3$ that split completely in $E$, as do $g_0$ and $g_1$; $g$ is prime to $T_u T'$; $T_u \equiv T' \pmod g$; and the only root of unity $\zeta$ in $E$ with $\zeta \equiv 1 \pmod{T_u}$ is $1$.
3. $F'$ and $F''$ are terms over $F$: they are lifts, admissible modulo $g$, and their Gram invariant with $F$ is nonzero.
4. $(F', F'')$ is a pair: an isometry $\beta$ of $V$ with $\beta\Lambda = \Lambda$ carries the flag of $F'$ to that of $F''$, with a compatibility modulo $g$.
5. The corank $s_0 = k - \dim \Theta$ of the space $\Theta$ of matched pairs is $1$, and $F'$ and $F''$ are generic over $F$.

**Theorem 8.6.6 (Theorem B).** Assume hypotheses 1 to 5 for a word $u$, a prime $T'$, a lattice $\Lambda$, flags $F$ of norm $T_u$ and $F', F''$ of norm $T'$, and an isometry $\beta$. Then either the pair is scalar, or
$$\Big(\frac{T_u T'}{g^2}\Big)^{f/2} \leq \Big(\prod_\tau \big(\operatorname{cs}_\tau(F,F')\operatorname{is}_\tau(F,F'') + \operatorname{is}_\tau(F,F')\operatorname{cs}_\tau(F,F'')\big)\Big)^{1/2}.$$

Lean: `Formalism.MainNotions.LatticeGluingRadicals.lattice_theorem_B` (also `Formalism.MainNotions.LatticeGluingRadicals.theorem_B_section`, a second name)

Here the pair is scalar if the following holds for all lifts $y_1, y_2$ of the first kind (for $F'$ and $F''$), all lifts $y'_1, y''_2$ of the second kind with $y_1 - y_2 \in X$ and $y''_2 - \beta y'_1 \in X''$, and all $\alpha, \alpha' \in E$: $y_1 - y'_1 \in \alpha z + \alpha' z' + X + X'$ if and only if $y_2 - y''_2 \in \alpha z + \alpha' z'' + X + X''$.

*Proof (outline).* Let $H'$ be the orthogonal complement of the span of $X$, $z$, $X'$ and $z'$, and define $H''$ in the same way with $F''$. Since the corank is $1$, $H'$ is the space $\Theta$ of matched pairs and $H''$ is the space of second members of the matched pairs (the definite rank-one property). It gives normal vectors for the two hyperplanes. Lemma 2 of the gluing argument holds for $(F, F')$ and for $(F, F'')$. From its two cases and the normal vectors we get elements $a, b, c, d$ with a first relation. The first two steps of the argument, which use the unimodular gluing of the lattice, give two more relations. The three relations and $g > 0$ give the inequality, or show that the pair is scalar. $\square$

**Remark 8.6.7 (Formalization).** The first theorem is the general column valuation theorem, proved in [FlipTwoThree.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/FlipTwoThree.lean#L403) and [LinkGLOBAL7Tied4.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/LinkGLOBAL7Tied4.lean#L18), applied for large $x$. The proof of the slope theorem drops the stabilizer condition, so that hypothesis is not used ([LinkTied.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/LinkTied.lean#L42)). The size theorem takes the binary representation theorem as a global instance ([TheoremThreeFamilyOfFormalDegreeInput.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/TheoremThreeFamilyOfFormalDegreeInput.lean#L95), [MassLandSt.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/MassLandSt.lean#L17)). In $c_{\min}$ the maximum with $11$ is redundant, since $16 + 3\max(5, y+1) \geq 31$. The second name of Theorem B is a one-line alias ([LatticeGluingRadicals.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/LatticeGluingRadicals.lean#L6762)). The target is the fourth conclusion of the gluing chapter; a different statement with the same short name is defined in ProductZerothFirstParts.lean. Not unfolded here: the goodness of the lattices $Q_{c,\tau}$, the lattice condition, the lower size condition on $T_u$, the Gram invariant, admissibility and genericity, the lifts of the two kinds, the unramified condition on $K$, the general slope formula, and the steps of the proof of Theorem B.
