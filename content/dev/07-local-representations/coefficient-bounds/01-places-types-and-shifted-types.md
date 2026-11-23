---
title: Places, types and shifted types
decls:
  - GlobalTheory.WigSh.exists_shifted_types_lower_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Places, types and shifted types

This chapter bounds a matrix coefficient of a discrete series representation of a real unitary group at each point of a big cell, by its $L^2$ norm times an explicit power of the distance to a boundary hypersurface. This first section fixes the setting: the group, the compact subgroup that acts on the types, the local terms and the form of the bound. It also proves one result on finite-dimensional representations, the bound for shifted types. That result says that a vector of a type is seen by one of two Wigner maps into types whose parameter is moved by $n_0$. It is used by the step [the hypotheses are not empty](/step/nonempty-hyps/) of the proof.

### The group and its types

Fix integers $k \ge 1$ and $r \ge 0$, and put $n = 2r + k + 1$. Let $H = H_{k,r}$ be the hermitian form on $\mathbb{C}^n$ of the chapter on Bessel models, and write $H(x, y)$ for its value on $x, y \in \mathbb{C}^n$. Let $G = \mathrm{U}(H)$ be its unitary group; see [unitary groups](/learn/groups/#unitary-groups). Let $W_0 \subset \mathbb{C}^n$ be the subspace of vectors $\omega$ with $\omega_i = 0$ for $i < r$ and for $i > r + k$ (we number coordinates from $0$). For $z \in W_0$ put $T_z = -\mathrm{Re}\, H(z, z)$.

**Definition 5.1.1 (Stabilizer of a vector).** Let $z \in W_0$. The group $U_W(z)$ is the set of $g \in G$ that fix the first $r$ basis vectors $e_a$, their $r$ partner vectors $e_a^*$, and the vector $z$.

The group $U_W(z)$ acts on the part of $W_0$ orthogonal to $z$. Its irreducible finite-dimensional representations are described by highest weights; see [highest weights and branching](/learn/representations/#highest-weights-and-branching). In this chapter a representation is described instead by the eigenvalues of a Capelli element.

**Definition 5.1.2 (Type).** Let $z \in W_0$ and let $u : \mathbb{N} \to \mathbb{R}$. A *type of $U_W(z)$ with parameter $u$* is a nonzero finite-dimensional Hilbert space $V$ with a map $\pi : U_W(z) \to \mathrm{End}(V)$ such that:

1. $\pi$ is a continuous representation of $U_W(z)$ and each $\pi(h)$ is an isometry;
2. $\pi$ is irreducible: the only subspaces of $V$ stable under all $\pi(h)$ are $0$ and $V$;
3. for each frame $B$ of $z$ and each $w \in \mathbb{C}$, the Capelli operator of $B$ at $w$ acts on $V$ by the scalar $\prod_{i=1}^{k} \bigl(w - \tfrac{k-1}{2} + u_i\bigr)$.

We have not unfolded the Capelli operator of a frame. Condition 3 is the way a parameter is attached to a type in this chapter. The parameter is regular and integral when $u_i - u_{i+1} - 1 \in \mathbb{N}$ for $1 \le i \le k - 1$. Then $u_1 > u_2 > \dots > u_k$ with integer gaps.

**Definition 5.1.3 (Wigner map).** Let $(V_1, \pi_1)$ and $(V_2, \pi_2)$ be types of $U_W(z)$, and let $d \in \mathbb{N}$. A *Wigner map of degree $d$ from $\pi_2$ to $\pi_1$* is a map $A : \mathbb{C}^n \to \mathrm{Hom}(V_2, V_1)$ with these properties:

1. there are polynomials $q_1, \dots, q_t$ in $\omega$ and $\bar\omega$ of total degree at most $d$ and maps $L_1, \dots, L_t$ with $A(\omega) = \sum_i q_i(\omega, \bar\omega) L_i$;
2. $A(h\omega)\,\pi_2(h) = \pi_1(h)\, A(\omega)$ for $h \in U_W(z)$ and $\omega \in \mathbb{C}^n$;
3. $A(t\omega) = t^d A(\omega)$ for real $t$;
4. $\|A(\omega)\|^2 \le \mathrm{Re}\, H(\omega, \omega)^d$ for $\omega \in W_0$ with $H(\omega, z) = 0$.

A Wigner map is an equivariant polynomial map, as in the classical construction of intertwiners from harmonic polynomials. Condition 4 normalizes its size.

### Shifted types

**Theorem 5.1.4 (Shifted types).** Let $z \in W_0$ with $T_z > 0$, and let $(V, \pi)$ be a type of $U_W(z)$ with parameter $u$. Let $l, n_0 \in \mathbb{N}$ and $b \in \mathbb{R}$. Assume:

1. $u_i - u_{i+1} - 1 \in \mathbb{N}$ for $1 \le i \le k - 1$;
2. $1 \le l < k$ and $2n_0 + 1 \le u_l - u_{l+1}$;
3. $|u_i| \le b$ for $1 \le i \le k$, $n_0 \le b$ and $1 \le b$.

Let $u^+$ be $u$ with $u_{l+1}$ replaced by $u_{l+1} + n_0$, and let $u^-$ be $u$ with $u_l$ replaced by $u_l - n_0$. Then there are types $(V_+, \pi_+)$ with parameter $u^+$ and $(V_-, \pi_-)$ with parameter $u^-$, and Wigner maps $A_+$ from $\pi_+$ to $\pi$ and $A_-$ from $\pi_-$ to $\pi$, both of degree $n_0$, such that for each $\omega \in W_0$ with $H(\omega, z) = 0$ and each $v \in V$,
$$\mathrm{Re}\, H(\omega, \omega)^{n_0}\, \|v\|^2 \le (3b)^{2n_0} \bigl( \|A_+(\omega)^* v\|^2 + \|A_-(\omega)^* v\|^2 \bigr).$$

Lean: `GlobalTheory.WigSh.exists_shifted_types_lower_bound` (also `GlobalTheory.T.exists_shifted_types_lower_bound_alt`, a second name).

The gap $u_l - u_{l+1} \ge 2n_0 + 1$ leaves room to move the two parameters toward each other by $n_0$ each.

*Proof.* Write $k = m + 1$. Since the gaps of $u$ are integers, there are a real shift $\beta$ and a decreasing sequence of integers $L_1 \ge \dots \ge L_k$ that describe $u$; the integer gaps of $L$ are those of $u$. So the gap hypothesis gives $L_{l+1} + 2n_0 + 1 \le L_l$, and the bound $|u_i| \le b$ gives $L_1 - L_k \le 2b$. Choose a frame $B$ of $z$; it exists since $z \in W_0$ and $T_z > 0$.

A chain of Wigner contractions that raises the coordinate $l + 1$ by $n_0$ gives the type $\pi_+$ and the map $A_+$. A chain that lowers the coordinate $l$ by $n_0$ gives $\pi_-$ and $A_-$. Each chain needs that the coordinates it moves stay below (or above) their neighbours, which follows from the gap and from the monotonicity of $L$.

To bound $v$, use branching to the subgroup of the frame. The space $V$ is the sum of the joint eigenspaces of the Capelli elements of this subgroup, indexed by the integer sequences $M$ that interlace $L$; see [highest weights and branching](/learn/representations/#highest-weights-and-branching). On the eigenspace of $M$, the two chains act by explicit scalars. A lower bound on these scalars, which uses the gap at $l$, $1 \le b$, $n_0 \le b$ and $L_1 - L_k \le 2b$, gives
$$(3b)^{-2n_0} \|v\|^2 \le \|A_+(\omega_0)^* v\|^2 + \|A_-(\omega_0)^* v\|^2$$
for $v$ in that eigenspace, at the last vector $\omega_0$ of the frame. A general lemma on joint eigenspaces that span $V$ turns these bounds into the bound for all $v \in V$; it uses how $A_\pm$ act on the eigenspaces. Finally, the equivariance and the homogeneity of $A_\pm$ move the bound from $\omega_0$ to each $\omega \in W_0$ with $H(\omega, z) = 0$, with the factor $\mathrm{Re}\, H(\omega, \omega)^{n_0}$. $\square$

### Local terms and the pointwise bound

The rest of the chapter works at one real place, with the place data of the chapter on Bessel models. A place datum $p$ has a parameter $P = (k, r, u, u', T, T')$, two vectors $z, z' \in W_0$ with $T_z, T_{z'} > 0$, two types $\pi, \pi'$ of $U_W(z)$ and $U_W(z')$ on spaces $W_p$ and $W_q$ with parameters $u$ and $u'$, a level $l_0$ and a family of differential operators indexed by words. A *coefficient* is a function $F : G \to \mathrm{Hom}(W_q, W_p)$.

The place defines a function $G_f$ on $G$, a polynomial in the matrix entries built from two leading minors, and its zero set is the boundary hypersurface. A *local point of size $r+1$* is a point $\gamma$ at which the place evaluates coefficients; $G_p(\gamma)$ is the value of the boundary function at $\gamma$. For $c \in \mathbb{C}^{r+1}$ the *big-cell point* $\gamma(c)$ is the local point with $r+1$ blocks of size one and entries $c_0, \dots, c_r$. For a word $w$ in the letters of the place and a local point $\gamma$, the *local term* $E_w(F)(\gamma) \in \mathbb{R}$ is built from the derivatives of $F$ along $w$ at $\gamma$, with weights in $\gamma$. We write $E(F) = E_{\emptyset}(F)$ for the empty word. We have not unfolded the local terms, the local points or $G_p$.

**Definition 5.1.5 (Norm on the big cell).** For a coefficient $F$ put
$$\|F\|^2 = \int_{\mathbb{C}^{r+1}} E(F)(\gamma(c))\, dc \in [0, \infty],$$
where the integral is of the positive part of $E(F)$, against Lebesgue measure.

**Definition 5.1.6 (Pointwise bound).** Let $b, C_4 \in \mathbb{R}$ and $n_0, p_0 \in \mathbb{N}$. A coefficient $f$ satisfies the *pointwise bound with constants $(b, C_4, n_0, p_0)$* if for each local point $\gamma$ of size $r+1$ with $G_p(\gamma) > 0$,
$$E(f)(\gamma) \le b^{C_4 (2r+2)^4}\, G_p(\gamma)^{-(2p_0 + n_0)}\, \|f\|^2 .$$
Both sides are read in $[0, \infty]$, and the left side means the positive part.

The exponent of $b$ grows like the fourth power of the rank. The exponent of $G_p(\gamma)$ measures how fast the bound can blow up at the boundary.

**Definition 5.1.7 (Regularity on the big cell).** Let $b, C_3 \in \mathbb{R}$ and $a_1 \in \mathbb{N}$. For $c \in \mathbb{C}^{r+1}$ let $\Delta(c)$ be the determinant of the matrix of size $r+1$ attached to $\gamma(c)$. A coefficient $f$ is *regular on the big cell with constants $(b, C_3, a_1)$* if for each $a \le a_1$,
$$\int_{\mathbb{C}^{r+1}} |\Delta(c)|^{2a}\, E(f)(\gamma(c))\, dc \le b^{2 C_3 (2r+2)^2 a}\, \|f\|^2 .$$

Regularity is an $L^2$ statement with weights. The pointwise bound is the $L^\infty$ statement that the chapter derives from it.

**Remark 5.1.8 (Formalization).** The types are `IsType`, the Wigner maps are `WigMap` in [WigMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/WigMap.lean#L12), and the pointwise bound and regularity are `ThmBpAt` and `RegularityBoundBigCell` in [StatementTBB.lean](lean:Formalism/HermitianCurvature/StatementTBB.lean#L127). The norm is `jN2` and the local term is `Ew` with weight $1$. The proof of the shifted types theorem is in [ExistsShiftedTypesLowerBound.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/ExistsShiftedTypesLowerBound.lean#L19); its second name carries the suffix `_alt` although it states the same thing. We have not opened the chain lemmas, so the description of the two chains and of the eigenvalue bound follows their statements as they are used, not their proofs.
