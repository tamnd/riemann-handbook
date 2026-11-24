---
title: Finite constants and p-adic eigen lines
decls:
  - GlobalTheory.T.finite_constant_all_holds
  - GlobalTheory.CompanionTheory.Ar.Flat.FinAll.finConstAll
  - GlobalTheory.T.eigen_line_p_adic_frame
  - GlobalTheory.CompanionTheory.Ar.Flat.CPoint.value_at_point
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Finite constants and p-adic eigen lines

A flat line function has a constant archimedean norm on each component by its definition. This section proves that it also has a constant $p$-adic norm at integral points of each component, at every prime $p$. So each flat line function has a finite norm in the sense of the section on the flat degree, and the degree of its log norms is defined. The constant is computed from the order of vanishing of the eigen line of the Hodge lattice along the special fibre. The result is used, together with the Hodge freeness of the last section, in the [covolume statement](/entry/top-covol-slim2-use-alt-alt/).

Let $E$ be a CM field with host $H$, a datum $D$ with $N = p + q$, a level, a moduli space $X_o$ and a coefficient datum with number field $F$. Let $O$ be a discrete valuation ring with an injective map $\beta: O \to F$, let $Y$ be a model of $X_o$ over $O$, let $U$ be an unfolding, and let $Z$ be a component of $Y$ over $U$ with generic point $\xi_0$, field $\Omega$ and Lie model with fibre $V$. Let $\tau$ be an embedding of $E$ with $\tau(\sqrt{-d}) = r_0$, and let $\varphi$ be a frame function.

In this section the letter $\ell$ is the prime, to keep $p$ for the signature. Let $\kappa: F \to \mathbb{C}_\ell$ be an embedding whose unit ball is $\beta(O)$.

### The finite constant statement

**Definition 8.22.1 (Finite norm).** $\varphi$ has the finite norm $t$ at $\ell$ and $\kappa$ if for every discrete valuation ring $V'$ with fraction field $K$, every embedding $j: K \to \mathbb{C}_\ell$ over $\kappa$, every integral point $y$ of $Z$ over $V'$, and all integral frames $v$ and $w$ of the $\tau$ and $\bar\tau$ eigenspaces at $y$ that are framed,
$$
\log \bigl| j \varphi(y, v, w) \bigr| = t .
$$

**Definition 8.22.2 (Finite constant statement).** The finite constant statement for $H$ says: for all data as above, if $Y$ has split fibres and the condition N3, $Z$ is geometric, $\varphi$ is a line function, and $\varphi$ is flat on the model, then there is $t$ such that $\varphi$ has the finite norm $t$ at $\ell$ and $\kappa$.

Flat on the model means that $\varphi$ is a line function and that there are $a \ne 0$ and $b \ne 0$ such that $\varphi$ represents the pair of top wedges $a \wedge v$ and $b \wedge w$ of bases of the two eigenspaces at the generic point of $Z$.

**Theorem 8.22.3 (Finite constants for all hosts).** The finite constant statement holds for every CM field $E$ and every host $H$.

Lean: `GlobalTheory.T.finite_constant_all_holds` (also `GlobalTheory.CompanionTheory.Ar.Flat.FinAll.finConstAll`, a second name).

The proof is at the end of the section. It uses the next theorem, which computes the constant from a Hodge lattice.

### Eigen lines at a point

Let $\mathcal{H}$ be a Hodge lattice of rank $p + q$ on the Lie model of $Z$: a lattice in $V \times V^\vee$ with the Hodge action, free and a vector bundle near each point of $Z$. Let $\sigma: E \to \Omega$ be the embedding of $\tau$. A basis $u$ of $\mathcal{H}$ is adapted to $v$ and $w$ if it is a basis of the Hodge lattice that restricts to the eigen bases $v$ and $w$ on the two eigen parts of the quotient.

Let $\varpi$ be a uniformizer of $O$. We say that $\alpha/\kappa'$ has order $a/M$ along $\varpi$ on the determinant of the eigen quotient of $\mathcal{H}$ if, at every point $x$, the $M$th power of the ratio of $\alpha/\kappa'$ to the determinant of $u$ is $\varpi^a$ times a unit.

**Theorem 8.22.4 (Value at an integral point).** Let $v$ and $w$ be bases of the $\sigma$ and $\bar\sigma$ eigenspaces of $V$, let $u$ be a basis of $\mathcal{H}$ adapted to $v$ and $w$, let $M > 0$ and $a \in \mathbb{Z}$, and let $\alpha, \kappa' \in \Omega$ with $\kappa' \ne 0$, such that $\alpha/\kappa'$ has order $a/M$ along $\varpi$ on the determinant of the eigen quotient. Assume that $\varphi$ is a line function that represents the pair $\alpha \wedge v$ and $\kappa' \wedge w$. Then there is a constant $\gamma$ with $|\gamma| \ne 0$, depending only on the CM type and $\kappa$, such that $\varphi$ has the finite norm
$$
t = \frac{a}{M} \log \bigl| \kappa(\beta \varpi) \bigr| + \log |\gamma|
$$
at $\ell$ and $\kappa$.

Lean: `GlobalTheory.T.eigen_line_p_adic_frame` (also `GlobalTheory.CompanionTheory.Ar.Flat.CPoint.value_at_point`, a second name).

*Proof.* Each embedding of $E$ into $\mathbb{C}_\ell$ factors through a complex embedding and $\kappa$. The valuation of the eigen decomposition of $\mathcal{O}_E \otimes \mathcal{O}_{\mathbb{C}_\ell}$ along the CM type gives a constant $\gamma \ne 0$: it is the norm of the generator that compares the eigen lattices of $\mathcal{O}_E \otimes \mathcal{O}_{\mathbb{C}_\ell}$ with the product of the eigen lines. We take $t$ as stated.

Let $y$ be an integral point over $V'$ with integral frames $v'$ and $w'$. The reduction of $y$ is a point of $Z$, and the eigen frames at $y$ reduce to eigen frames at this point. Near the point, the Hodge lattice is free and a vector bundle, so it has a basis, and its Hodge decomposition is local: the eigen parts of the quotient are lattices, and the frames $v'$ and $w'$ are bases of them, by the definition of an integral frame. The coordinates of $u$ in the frame $(v', w')$ reduce to the residue field, and the adapted basis at the residue field is a basis of the reduced lattice.

So the value of $\varphi$ at $(y, v', w')$ is the value of $\alpha/\kappa'$ divided by the determinant of $u$ in the eigen frames, times the comparison constant of the eigen decomposition. The order condition says that the $M$th power of the first factor is $\varpi^a$ times a unit $\mu$ with $|\mu| = 1$. The comparison of orders and valuations gives, for $x^M = \varpi^a \mu$ with $|\mu| = 1$,
$$
\log |x| = \frac{a}{M} \log |\varpi| .
$$
The second factor has the norm $|\gamma|$. This gives $\log |j \varphi(y, v', w')| = t$. $\square$

The constant $\gamma$ depends on the CM type and on $\kappa$ only, not on the point. So the theorem says that the $\ell$-adic norm of a flat frame function is constant along each component, with the value read from the order of the eigen line along the special fibre.

### Proof of the finite constant statement

Let the data of the statement be given. We first make the order condition hold.

The proper normal compactification of the component gives the two eigenspaces of dimensions $p$ and $q$ and bases $v$ and $w$. The flatness on the model gives $a \ne 0$ and $b \ne 0$ in $\Omega$ such that $\varphi$ represents $a \wedge v$ and $b \wedge w$. Since the model has split fibres and the condition N3, the eigen line bound at $\ell$ gives a Hodge lattice $\mathcal{H}$ whose eigen quotients have a degree condition at $\varpi$. The hermitian signature basis gives a basis $u$ of $\mathcal{H}$ adapted to $v$ and $w$.

Now $O$ is a discrete valuation ring, so every element of $\Omega$ is in $O$ or has its inverse in $O$, and every element of the fraction field is a power of $\varpi$ times a unit. The constants are closed on a geometric component, so $a/b$ times the determinant of $u$ is a constant of the component, and it is a fraction of elements of $\beta(O)$. The valuations of the Hodge lattice agree at all points of the component, so there are $M > 0$ and $k$ with the order condition for $a/b$ along $\varpi$. The theorem on the value at an integral point then gives $t$. $\square$

**Remark 8.22.5 (Formalization).** The Lean proof calls the prime `p`, the same letter as the signature $p$ of the datum; we call it $\ell$. In `finConstAll` the flatness hypothesis contains a second copy of the line function condition, which is dropped by `obtain ⟨-, a, b, ⟨ha0, hb0, hco⟩, hrep⟩ := hflat` (FiniteConstantAllHolds.lean:173); the proof uses the separate hypothesis `hline` instead (line 195). The finite constant statement `FinConstFor` (FinConstFor.lean:17) is asked for all $E$ and $H$ in `FinConstAll` (line 27), but the statement `FinConst` that the chapter uses asks it only for hosts in the range with $2$, $q_1$ and $d$ prime, and it follows at once. In `value_at_point` (EigenLinePAdicFrame.lean:72) the hypotheses `hτ` ($\tau(\sqrt{-d}) = r_0$) and `hκ'` ($\kappa' \ne 0$) are introduced at line 73 and not used after, and the theorem needs `maxHeartbeats 4000000` (line 70). The rule on $x^M = \varpi^a \mu$ is `log_end` (line 55). We do not unfold the Hodge lattice, the representation of a frame function or the condition N3.
