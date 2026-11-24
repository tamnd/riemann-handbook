---
title: The periods lie on one line
decls:
  - GlobalTheory.RowReal.realLine
  - GlobalTheory.T.rowTest_realPlaces_definitePeriods_onOneLine
  - GlobalTheory.RowReal.periodsOnLine_big
  - GlobalTheory.T.rowTest_definitePeriods_invariant_functional
  - GlobalTheory.RowReal.invLine_big
  - GlobalTheory.RowReal.invLine_of_iso
  - GlobalTheory.OneFunctional.oneLine
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The periods lie on one line

The flat dictionary of [the previous section](/entry/flat-at-big/) writes the unfolded theta integral as a finite sum of periods indexed by pairs of polynomial data. This section proves that these periods, as functions of the polynomial data, all lie on one line. The line does not depend on the type, the datum, the coset, the volume or the expansion. The proof writes each period as an invariant functional on a fixed representation of a product of compact unitary groups, and shows that the space of such functionals has dimension $1$ by a [branching law with interlacing](/learn/periods/#interlacing-and-the-branching-law-for-discrete-series). The result is used in [the unfolding of the twisted theta integral](/entry/twisted-theta-integral-unfolding/).

### Periods of a row test

Fix a choice $\mathrm{ch}$ as in the previous section. Let $Q = (Q_1, Q_2)$ be a pair of polynomial data, $Q_1$ on the column edges and $Q_2$ on the row edges. For a type $t$, an index $a$, a volume $M$, a pure datum $d$ and a point $y$, the *period* $\mathcal{P}_M(Q, d)$ is the integral over a fundamental domain of the lift of the column function $\varphi_a$ along the column, times the lift of the form $F_y$ along the row. The lifts use the Fock vectors of $Q$ and of the theta functions of $d$. For finite combinations $\sigma$ of pairs and $\tau$ of pure data, put

$$\mathcal{P}_M(\sigma, \tau) = \sum_{Q, d} \sigma_Q\, \tau_d\, \mathcal{P}_M(Q, d).$$

A tuple $(t, a, \beta, M, \tau)$ is *admissible* if the sum condition holds at $(t, \Phi_a)$, the coset family $\beta$ is in the support, $M$ is a volume of the term at $\beta$, and $\tau$ is an expansion of the term at $\beta$.

### The compact model

A *size* $S = (k, m, s, t_S)$ is a quadruple of positive integers with $k$ and $m$ even and $s$ and $t_S$ odd. Put

$$\begin{aligned}
n_R(j) &= k + m s + j (t_S + 1), \\
n_C(i) &= k + m - 1 + m t_S + i s.
\end{aligned}$$

Then $n_R$ and $n_C$ are strictly increasing and $n_R(m) = n_C(m) + 1$. An *entry* for $S$ is a family of numbers $a_l \in \mathbb{Q}$ for $l \le m$, $c_i, b_j, e_j \in \mathbb{Z}$ for $i, j < m$, and $v_i \in \mathbb{Z}$, $u_i \in \mathbb{Q}$ for $i < k - 1$. The entry is *good* if each $a_l$ and each $u_i$ lies in $\tfrac12 + \mathbb{Z}$, and the list

$$a_0,\ c_0^{(s)},\ a_1,\ \dots,\ v_0, u_0,\ \dots,\ -b_0,\ (-e_0)^{(t_S)},\ \dots$$

is strictly decreasing, where $x^{(n)}$ is a block of $n$ consecutive values that starts at $x$.

Let $\iota$ be a finite set and let $E = (E_x)_{x \in \iota}$ be good entries for $S$. Let $G$ be the product of the groups $U(n_R(j))^{\iota}$ for $j < m$ and $U(n_C(i))^{\iota}$ for $i \le m$, where $U(n)$ is the compact [unitary group](/learn/groups/#unitary-groups). The representation $\Omega(E)$ of $G$ is the tensor product of:

1. $m$ Fock spaces of polynomials between the consecutive row groups, twisted by characters read off from the $e_j$;
2. $m$ Fock spaces between the consecutive column groups, twisted by characters read off from the $c_i$;
3. a Weyl module of $U(n_R(0))^{\iota}$ with the highest weight read off from the first part of the entries;
4. the dual of a Weyl module of $U(n_C(0))^{\iota}$ with the highest weight read off from the last part of the entries.

Let $\mathrm{Hom}_G(\Omega(E), \mathbb{C})$ be the space of $G$ invariant linear functionals.

**Theorem 8.11.1 (Multiplicity one for the compact model).** For each finite set $\iota$, each size $S$ and each family $E$ of good entries, $\mathrm{Hom}_G(\Omega(E), \mathbb{C})$ has dimension $1$.

Lean: `GlobalTheory.OneFunctional.oneLine`.

*Proof.* For each $x \in \iota$ there are dominant weights $\lambda_{x,j}$ on the row groups and $\kappa_{x,i}$ on the column groups with these properties. The first are the weights of the Weyl module of item 3, the last are dual to the weights of item 4, and each Fock space contracts the irreducible representation of weight $\lambda_{x,j}$ to that of weight $\lambda_{x,j+1}$, and the same for $\kappa$. A chain of such contractions shows that the invariant functionals on the tensor product of the Fock spaces and the two end modules correspond to the invariant functionals on the tensor product of the two last irreducible representations. These are the representation of $U(n_R(m))^{\iota}$ of weight $\lambda_{x,m}$, restricted to $U(n_C(m))^{\iota}$, and the representation of $U(n_C(m))^{\iota}$ of weight $\kappa_{x,m}$. The space of invariant functionals on an outer tensor product over $\iota$ is the tensor product of the spaces for each $x$. For each $x$, the weight $\lambda_{x,m}$ interlaces the dual of $\kappa_{x,m}$, because the good entries are strictly decreasing. The branching law for $U(n) \subset U(n + 1)$ then gives dimension $1$ for each $x$. $\square$

**Theorem 8.11.2 (Periods as invariant functionals).** For all large choices there are a finite set $\iota$, a size $S$, good entries $E$ and a map $e$ from pairs of polynomial data to $\Omega(E)$ with this property. For each admissible tuple, each $d$ in the support of $\tau$ and each $y$, there is $\lambda \in \mathrm{Hom}_G(\Omega(E), \mathbb{C})$ with $\mathcal{P}_M(Q, d) = \lambda(e(Q))$ for all $Q$.

Lean: `GlobalTheory.T.rowTest_definitePeriods_invariant_functional` (also `GlobalTheory.RowReal.invLine_big`, the proof).

*Proof.* For all large choices, the generators of the column and row lifts are left invariant under the rational points, and the generic periods converge. The first Weyl module is isomorphic to the dual of the coefficient space of the column, and the dual of the second Weyl module is isomorphic to the dual of the coefficient space of the base. Both isomorphisms are equivariant through the real points of the grid. The next theorem gives the claim. $\square$

**Theorem 8.11.3 (Invariant functionals from isomorphisms).** Let $\mathrm{ch}$ be a choice with a level type $\mu_0$. Assume that the generators of the column and row lifts are left invariant under the rational points, and that the generic periods converge for each admissible tuple. Let $A$ be an isomorphism from the first Weyl module to the dual of the column coefficient space, and $B$ an isomorphism from the dual of the second Weyl module to the dual of the base coefficient space, both equivariant for the real points. Then the conclusion of the previous theorem holds, with $\iota$ the set of real places, the size and entries of the row, and

$$e(Q) = \bigotimes_j t_c(Q_{1,j}) \otimes \bigotimes_i t_r(Q_{2,i}) \otimes A^{-1}(\xi) \otimes B^{-1}(v),$$

where $t_c$ and $t_r$ are Fock transports, $\xi$ is the column vector of the choice and $v$ is the base vector.

Lean: `GlobalTheory.RowReal.invLine_of_iso`.

*Proof.* There are linear isomorphisms $t_c$ and $t_r$ from the polynomial Fock spaces of the grid to the Fock spaces of the compact model, compatible with the real points. The generic period is multilinear in the column and row polynomials and in the two coefficients. Pull it back along $t_c$, $t_r$, $A$ and $B$ to get a multilinear form $\Phi$ on the factors of $\Omega(E)$. A real point $g$ moves the generic period by the Weil action on the Fock factors and by the coefficient actions. The transports and the equivariance of $A$ and $B$ turn this into the action of $g$ on $\Omega(E)$. So $\Phi$ is invariant. An invariant multilinear form factors through an invariant functional $\lambda$ on the tensor product, and $\lambda(e(Q)) = \mathcal{P}_M(Q, d)$. $\square$

### One line

**Theorem 8.11.4 (The periods lie on one line).** For all large choices there is a function $\ell$ on pairs of polynomial data such that for each admissible tuple, each $d$ in the support of $\tau$ and each $y$, there is $\kappa \in \mathbb{C}$ with $\mathcal{P}_M(Q, d) = \kappa\, \ell(Q)$ for all $Q$.

Lean: `GlobalTheory.T.rowTest_realPlaces_definitePeriods_onOneLine` (also `GlobalTheory.RowReal.periodsOnLine_big`, the proof).

*Proof.* Take the data of the previous theorems. By multiplicity one, there is $L_0$ that spans $\mathrm{Hom}_G(\Omega(E), \mathbb{C})$. Put $\ell(Q) = L_0(e(Q))$. Each $\lambda$ is $c L_0$ for some $c$, and $\kappa = c$. $\square$

**Theorem 8.11.5 (A nonzero line).** For all large choices there is a nonzero function $\ell$ on pairs of polynomial data with these properties.

1. For each admissible tuple and each $y$ there is $K \in \mathbb{C}$ such that for all $\sigma$,

$$\mathcal{P}_M(\sigma, \tau) = \Bigl(\sum_Q \sigma_Q\, \ell(Q)\Bigr) K.$$

2. For each $z \in \mathbb{C}$ there is $\sigma$ with $\sum_Q \sigma_Q\, \ell(Q) = z$, and $\sigma = 0$ if $z = 0$.

Lean: `GlobalTheory.RowReal.realLine`.

*Proof.* Take $\ell_0$ from the previous theorem. If $\ell_0 \ne 0$, put $\ell = \ell_0$. If $\ell_0 = 0$, then all periods vanish, so put $\ell = 1$ and take each $\kappa_d = 0$. In both cases $K = \sum_d \tau_d \kappa_d$. For clause 2, choose $Q_0$ with $\ell(Q_0) \ne 0$ and put $\sigma = (z / \ell(Q_0))\, \delta_{Q_0}$. $\square$

**Remark 8.11.6 (Formalization).** The theorems are in [FinrankInvFunBranch.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FinrankInvFunBranch.lean#L248), [RowTestDefinitePeriodsInvariantFunctional.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RowTestDefinitePeriodsInvariantFunctional.lean#L34), [RowTestRealPlacesDefinitePeriodsOnOneLine.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RowTestRealPlacesDefinitePeriodsOnOneLine.lean#L8) and [RealLine.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RealLine.lean#L9). The compact model and the good entries are in [MinorOrderedEntries.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/MinorOrderedEntries.lean#L89). The name of the last theorem says "real", but $\ell$ is complex valued. Clause 2 follows from $\ell \ne 0$ alone. The names of the two middle theorems speak of real places and definite periods, but the statements do not. We have not unfolded the Weyl modules, the highest weights, the Fock spaces of the compact model, the generic periods, the contraction lemmas or the Fock transports, so their descriptions above are read from the names and from the way they are used.
