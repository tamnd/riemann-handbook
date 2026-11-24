---
title: Masses of self-dual Hermitian lattices
decls:
  - GlobalTheory.PrimScale.cont_prim_scale
  - GlobalTheory.HL.Unfold.mass_bounds
  - GlobalTheory.T.selfDual_hermitianLattice_mass_bounds
  - GlobalTheory.HL.FrameMass.mass_trace
  - GlobalTheory.T.selfDualHermitianLattice_mass_of_trace
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Masses of self-dual Hermitian lattices

The local bounds of the last section contain a mass: a weighted count of the self-dual lattices whose intersection with a fixed subspace is a given lattice. This section shows that this mass is, up to a factor $2$, a constant times a power of an index. The proof has three steps. First we compare the content of a set of primitive tuples with the content of a set of Hermitian matrices. Then we write the mass as a sum of such contents and get two-sided bounds in terms of a matrix $A$. Last, we put the bounds in the form of the frames of the setting, where the power is $[M_h : M(p)]^{-(k-1)}$. The two users of the last result are the bounds on the total mass and on the shares in the local analysis of [the amplitude](/entry/amp-le-mass/).

Throughout, $F$ is a nonarchimedean local field with uniformizer $\varpi$ and residue field of size $q$, and $E/F$ is a quadratic extension with conjugation $c$. Let $v_E$ be the valuation of $E$. Let $H \in M_n(E)$ be a nondegenerate Hermitian matrix, and write $h(x, y)$ for the form it defines on $E^n$.

**Definition 2.21.1 (Content).** Let $W$ be an abelian group with a subgroup $W_0$. A set $S \subseteq W$ is a *finite union of cosets* of $W_0$ if $S$ is a finite union of sets $w + W_0$. For such $S$ the *content* of $S$ is
$$\operatorname{cont}(S) = \#(S / W_0) \cdot \operatorname{vol}(W_0),$$
the number of cosets in $S$ times the fixed relative volume of $W_0$. If $S$ is not a finite union of cosets, put $\operatorname{cont}(S) = 0$.

For a tuple $x = (x_1, \dots, x_m)$ of vectors in $E^n$ let $G(x)$ be its Gram matrix, with entries $h(x_a, x_b)$. For $i \ge 0$ let $K_i$ be the congruence subgroup of matrices in $GL_m(\mathcal{O}_E)$ that are $1$ modulo $\varpi^i$, and let
$$H_i(x) = \{\, c(K)^{T}\, G(x)\, K : K \in K_i \,\}$$
be the orbit of $G(x)$ under $K_i$. For a matrix $A \in GL_m(E)$ put $v_A = v_E(\det A \cdot c(\det A))$.

**Definition 2.21.2 (Primitive tuple).** Let $\Lambda$ be an $\mathcal{O}_E$-lattice in $E^n$. A tuple $(x_1, \dots, x_m)$ is *primitive* in $\Lambda$ if every $x_a$ lies in $\Lambda$ and there are $y_1, \dots, y_m \in \Lambda$ with $h(x_a, y_b) = \delta_{ab}$ for all $a, b$.

**Proposition 2.21.3 (Content of primitive tuples).** Let $\Lambda_s$ be a self-dual lattice for $H$, let $x$ be an $m$-tuple with $\det G(x) \ne 0$, and assume $2m + 3 \le n$. Let $A \in GL_m(E)$ have a unit determinant, and assume that $G(x A^{-1})$ has integral entries. For $i \ge 0$ let
$$S_i = \{\, z : z A^{-1} \text{ primitive in } \Lambda_s,\ G(z) \in H_i(x) \,\}.$$
Then there is $i_0$ such that for all $i \ge i_0$
$$\begin{aligned} q^{-v_A(n-m)} \operatorname{cont}(H_i(x)) &\le 2 \operatorname{cont}(S_i), \\ \operatorname{cont}(S_i) &\le 2\, q^{-v_A(n-m)} \operatorname{cont}(H_i(x)). \end{aligned}$$

Lean: `GlobalTheory.PrimScale.cont_prim_scale`.

*Proof.* There is $i_0$ such that $A K A^{-1}$ has integral entries for every $K \in K_i$ and every $i \ge i_0$, because $K - 1$ is divisible by $\varpi^i$. Fix $i \ge i_0$ and let
$$B = c(A^{-1})^{T}\, H_i(x)\, A^{-1}.$$
This set is again a finite union of cosets, and the change of variables formula for Hermitian matrices gives
$$\operatorname{cont}(B) = q^{v_A m} \operatorname{cont}(H_i(x)).$$
Every element of $B$ is $c(K')^T G(x A^{-1}) K'$ with $K' = A K A^{-1}$ integral, so $B$ is a set of integral Hermitian matrices.

Substitute $y = z A^{-1}$. Then $z \in S_i$ if and only if $y$ is primitive in $\Lambda_s$ and $G(y) \in B$. Since $n \ge 2m + 3$, the count of primitive tuples with Gram matrix in an integral finite union of cosets $B$ gives
$$\operatorname{cont}(B) \le 2 \operatorname{cont}(P_B), \qquad \operatorname{cont}(P_B) \le 2 \operatorname{cont}(B),$$
where $P_B$ is the set of primitive tuples $y$ with $G(y) \in B$. Right multiplication by $A$ is a bijection from $P_B$ to $S_i$, and it multiplies the content of a set of tuples by $q^{-v_A n}$. So $\operatorname{cont}(S_i) = q^{-v_A n} \operatorname{cont}(P_B)$. Combine the three relations. The exponents add to $-v_A n + v_A m = -v_A(n - m)$, and this gives the two inequalities. $\square$

The hypothesis $n \ge 2m + 3$ is used only in the count of primitive tuples. It makes the local densities of the representation of $B$ close to $1$.

### The mass of a trace

Let $Y \subseteq E^n$ be a subspace and $M$ an $\mathcal{O}_E$-lattice in $Y$. Let $U$ be the unitary group of $H$, let $U_Y$ be its subgroup that fixes $Y$ pointwise, and let $\Lambda_0$ be a lattice. The group $U_Y$ acts on the self-dual lattices $\Lambda$ with $\Lambda \cap Y = M$.

**Definition 2.21.4 (Mass of a trace).** The *mass* of $M$ with respect to $\Lambda_0$ is
$$\sigma(Y, \Lambda_0, M) = \sum_{[\Lambda]} \operatorname{iv}(\Lambda),$$
where $[\Lambda]$ runs over the $U_Y$-orbits of self-dual lattices with $\Lambda \cap Y = M$, and $\operatorname{iv}(\Lambda)$ is the relative inverse volume of $U_Y \cap \operatorname{Stab}(\Lambda)$ with respect to $U_Y \cap \operatorname{Stab}(\Lambda_0)$.

We call $\Lambda \cap Y$ the *trace* of $\Lambda$ on $Y$. The mass counts self-dual lattices with a given trace, each with the inverse volume of its stabilizer.

**Theorem 2.21.5 (Mass bounds).** Let $\Lambda_s$ be a self-dual lattice for $H$, let $x$ be an $m$-tuple with $\det G(x) \ne 0$, assume $2m + 3 \le n$, and let $\Lambda_0$ be a lattice. Put $Y = \operatorname{span}_E(x)$. Then there is $\kappa > 0$ with this property: for every $A \in GL_m(E)$ with a unit determinant such that $G(x A^{-1})$ is integral, the lattice $M_A = \operatorname{span}_{\mathcal{O}_E}(x A^{-1})$ satisfies
$$\begin{aligned} \tfrac{\kappa}{2}\, q^{-v_A(n-m)} &\le \sigma(Y, \Lambda_0, M_A), \\ \sigma(Y, \Lambda_0, M_A) &\le 2 \kappa\, q^{-v_A(n-m)}. \end{aligned}$$

Lean: `GlobalTheory.HL.Unfold.mass_bounds` (also `GlobalTheory.T.selfDual_hermitianLattice_mass_bounds`, a second name).

*Proof.* We unfold the mass into a content of tuples.

1. The group $U$ acts transitively on the self-dual lattices, so every self-dual $\Lambda$ is $g \Lambda_s$ for some $g \in U$. Its trace is $M_A$ when the tuple $g^{-1} x A^{-1}$ is primitive in $\Lambda_s$ and spans $g^{-1} \Lambda \cap g^{-1} Y$. So the mass is a constant times the content of a set of tuples $z$ with $z A^{-1}$ primitive in $\Lambda_s$ and $G(z)$ close to $G(x)$.
2. Fix $i$ large. The self-dual lattices with trace $M_A$ fall into finitely many $U_Y$-orbits, and we choose a finite set $s$ of elements $g$ with $g \Lambda_s \cap Y = M_A$, one for each orbit. The mass is the sum over $g \in s$ of the inverse volumes.
3. For each $g \in s$, the image of the stabilizer under $u \mapsto u^{-1} x$ is a thick orbit: a finite union of cosets whose content is the inverse volume times a constant that does not depend on $A$. The content of tuples changes by the Jacobian of right multiplication by $A$.
4. The sets for distinct $g \in s$ are disjoint, so the content of their union is the sum of their contents. The union is the set $S_i$ of the [Proposition 2.21.3](/entry/cont-prim-scale/) above.
5. That Proposition bounds $\operatorname{cont}(S_i)$ above and below by $2^{\pm 1} q^{-v_A(n - m)} \operatorname{cont}(H_i(x))$.
6. The group $K_i$ is open, so $\operatorname{cont}(H_i(x)) > 0$. Divide by it and by the constant of step 3.

The constant $\kappa$ collects $\operatorname{cont}(H_i(x))$, the relative volumes and the constant of step 1. It does not depend on $A$. $\square$

### The form in the frames of the setting

Now let the data be a frames record of the setting, as in the [local analysis](/entry/amp-le-mass/). It gives a nonarchimedean local field, an extension $E$, the lattice $M_E$ spanned by the frame vectors and their dual vectors, and the Hermitian form of size $n = k + 2r + 1$. A frame class $C$ is an orbit of frames, and each frame $p \in C$ defines a lattice $M(p) \subseteq M_E$ of rank $2r + 2$. The mass of a lattice $M_h$ is $\sigma_h(M_h) = \sigma(Y, \mathcal{O}_E^n, M_h)$, where $Y$ is the span of $M_E$.

**Theorem 2.21.6 (Mass of a trace in the frames of the setting).** Let $S$ be a frames record with $2r + 6 \le k$, and assume that a self-dual lattice exists. Then there is $\kappa > 0$ with this property. Let $C$ be a frame class, $p \in C$, and $M_h$ a lattice with $M(p) \subseteq M_h \subseteq M_E$ on which $h$ is integral. Then
$$\begin{aligned} \tfrac{\kappa}{2}\, [M_h : M(p)]^{-(k-1)} &\le \sigma_h(M_h), \\ \sigma_h(M_h) &\le 2\kappa\, [M_h : M(p)]^{-(k-1)}. \end{aligned}$$

Lean: `GlobalTheory.HL.FrameMass.mass_trace` (also `GlobalTheory.T.selfDualHermitianLattice_mass_of_trace`, a second name).

*Proof.* There is a tuple $x$ of $2r + 2$ vectors that spans $M_E$ over $\mathcal{O}_E$, with $\det G(x) \ne 0$. For each frame $p$ there is $B$ with $\det B \cdot c(\det B) = 1$ such that $M(p) = \operatorname{span}(x B)$. The subgroup of $U$ that fixes the span of $M_E$ is $U_Y$, and the mass $\sigma_h$ is the mass of the [Theorem 2.21.5](/entry/mass-bounds/) above with $\Lambda_0 = \mathcal{O}_E^n$.

Apply that Theorem with $m = 2r + 2$ and $n = k + 2r + 1$. The condition $n \ge 2m + 3$ is $k + 2r + 1 \ge 4r + 7$, that is, $k \ge 2r + 6$. This gives $\kappa$, which depends only on $S$.

Now let $C$, $p$ and $M_h$ be given, and put $y = x B$. Since $M(p) \subseteq M_h$ and both lattices have rank $2r + 2$, there is $A$ with $M_h = \operatorname{span}(y A^{-1})$. The index of the overlattice is
$$[M_h : M(p)] = q^{v_A}.$$
Apply the bounds to the matrix $A B^{-1}$, for which $x (A B^{-1})^{-1} = y A^{-1}$. Since $\det B \cdot c(\det B) = 1$, the exponent of this matrix is $v_A$. The Gram matrix $G(y A^{-1})$ is integral because $h$ is integral on $M_h$. Last, $n - m = k - 1$, so $q^{-v_A(n - m)} = [M_h : M(p)]^{-(k-1)}$. $\square$

The two users of this theorem, the bound on the total mass and the bound on the shares, ask $k \ge 4r + 7$. This is more than the condition $k \ge 2r + 6$ used here.

**Remark 2.21.7 (Formalization).** The content `cont` ([HermLat.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/HermLat.lean#L20)) is $0$ on sets that are not finite unions of cosets, so each use of a content bound must also prove this property. The mass `sigMass` ([HermLat.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/HermLat.lean#L68)) is a `tsum` over the orbits, and each orbit enters through its chosen representative `o.out`. The Proposition is `cont_prim_scale` in [ExistsConjInt.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsConjInt.lean#L126), and the integrality of $A K A^{-1}$ is the lemma `exists_conj_int` in the same file. In the mass bounds ([SelfDualHermitianLatticeMassBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SelfDualHermitianLatticeMassBounds.lean#L113)) the constant $\kappa$ is chosen after $\Lambda_0$, $\Lambda_s$ and $x$, and $A$ need not be integral. The name of the last theorem speaks of a trace, but its statement has no trace map: the trace is the intersection $\Lambda \cap Y$ ([SelfDualHermitianLatticeMassOfTrace.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SelfDualHermitianLatticeMassOfTrace.lean#L84)). The description of the unfolding in steps 1 to 3 follows the names of the lemmas used in the proof, and the lemmas themselves are not unfolded here.
