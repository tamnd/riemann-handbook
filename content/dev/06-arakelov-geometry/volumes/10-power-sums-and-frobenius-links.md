---
title: Power sums and Frobenius links
decls:
  - GlobalTheory.CompanionTheory.Ar.Num.power_sum_height_model_change
  - GlobalTheory.T.power_sum_height_change_model
  - GlobalTheory.CompanionTheory.Ar.Num.power_sum_term_linked_tower
  - GlobalTheory.T.linked_tower_power_sum
  - GlobalTheory.CompanionTheory.Ar.Top.Link.link_step
  - GlobalTheory.CompanionTheory.Ar.Top.Link.goodOrigin_linked
  - GlobalTheory.T.good_tower_global_conditions
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Power sums and Frobenius links

Proposition 6 of [the tower conditions](/entry/full-intersection-tower-i8-identity/) is the power sum formula: the top intersection number of $p_k^\tau Q$ at a level $B_0$ equals the number at a higher level $B$ plus the volume times a sum over the good primes in $(B_0, B]$ of explicit terms $\delta_p$. This section proves it for good towers. The proof goes in three steps. First, when a root model is changed at a finite set of primes by a vertical change that is isometric at infinity and compatible with Frobenius at these primes, the arithmetic numbers of $p_k^\tau Q$ change by a sum of local terms $\log p$ times a geometric number. Second, a tower whose levels are linked by such changes satisfies Proposition 6. Third, the levels of a good tower are linked, with Frobenius labels of the right shape. The result is used in [the volume theorem](/entry/volume-theorem-x-of-inputs/).

We keep the notation of [the tower conditions](/entry/full-intersection-tower-i8-identity/): $R = \mathbb{R}[x_{\tau, i}]$, the power sums $p_k^\tau = \sum_i x_{\tau, i}^k$, the dimension $d$ of the flag variety, and for a root model $M$ the arithmetic functional $\mathrm{ar}_M(t)$ at the twisted lines of parameter $t$, the geometric functional $\mathrm{geo}_M$ and the limit $\mathrm{PP}_M$ of $\mathrm{ar}_M(t)$ as $t \to 0$. For $j$ and a label $\ell \in \Psi \sqcup \Psi$ the Lie power sums are

$$
\begin{aligned}
p^{\mathrm{Lie}}_m(\tau_{\mathrm{left}}) &= \sum_{i < j} x_{\tau, i}^m, \\
p^{\mathrm{Lie}}_m(\tau_{\mathrm{right}}) &= \sum_{i \ge j} (-x_{\tau, i})^m.
\end{aligned}
$$

For a permutation $\varphi$ of $\Psi \sqcup \Psi$, a prime $p$, $k \ge 1$ and $\tau \in \Psi$, the bracket is

$$
[\varphi]_{p, k, \tau} = k \sum_{\tau' \in \Psi \sqcup \Psi} c_{\varphi, p, k}(\tau, \tau')\, p^{\mathrm{Lie}}_{k-1}(\tau'),
$$

a homogeneous polynomial of degree $k - 1$, with coefficients $c_{\varphi, p, k}$ from the chapter on heights.

**Definition 9.10.1 (Second roots, change, local at places).** Let $M$ be a root model. A system of second roots on $M$ gives new coordinate degrees $\deg x'_{\tau, i}$, new smooth conjugation invariant twisted lines $x'_t(\tau, i)$, and integral polynomials $f_{\tau, i}$, $g_{\tau, i}$. Replacing the root data of $M$ by these gives a second root model $M'$. Let $S$ be a finite set of primes.

1. The second roots are a change at $S$ if the pairs $(f, g)$ are vertical off $S$, and for every $t > 0$ the pairs are isometric between $x_t$ and $x'_t$.
2. The second roots are local at the places of $S$ for $j$ and labels $\varphi_p$ if there is a Dedekind domain $A$, finite over $\mathbb{Z}$, inside the field of $M$ and containing the constants, such that for every $p \in S$ and every discrete valuation ring $O$ at a prime of $A$ over $p$, the flag Chern comparison holds at $O$ for $p$, $j$ and $\varphi_p$, and the power sums in the new degrees vanish at $O$.

**Definition 9.10.2 (Linked tower).** A root tower $T$ is linked for $\mathrm{II}$ and labels $\varphi$ if for all levels $2 \le B_0 \le B$ and every component $c$ there are a root model $M$, second roots on $M$ and a set $S$ of primes such that $S$ is the set of primes in $(B_0, B]$ outside the bad primes, $M$ and $M'$ converge, $\mathrm{PP}_M = \mathrm{PP}_{B_0, c}$, $\mathrm{PP}_{M'} = \mathrm{PP}_{B, c}$, $\mathrm{geo}_M = \mathrm{geo}_{M_{B_0, c}}$, and the second roots are a change at $S$ that is local at the places of $S$ for the index $j$ of $T$ and the labels $\varphi$.

So the model at level $B$ is obtained from the model at level $B_0$ by changing the root lines only at the new primes, and the change at each new prime is controlled by Frobenius.

**Theorem 9.10.3 (Change of model at finitely many primes).** Let $\mathrm{II}$ be an intersection system, let $M$ be a root model with second roots that are a change at $S$, local at the places of $S$ for $j$ and labels $\varphi$. Then for every $t > 0$, every $\tau$, every $1 \le k \le N$ and every $Q$ homogeneous of degree $d + 1 - k$,

$$
\mathrm{ar}_M(t)(p_k^\tau Q) = \mathrm{ar}_{M'}(t)(p_k^\tau Q) + \sum_{p \in S} \log p \cdot \mathrm{geo}_M\big([\varphi_p]_{p, k, \tau}\, Q\big).
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Num.power_sum_height_model_change` (also `GlobalTheory.T.power_sum_height_change_model`, a second name)

*Proof.* The difference of the two arithmetic numbers is the arithmetic number of the mixed difference of $p_k^\tau Q$ in the joined family of lines, by linearity and symmetry of arithmetic numbers. Since the pairs are isometric at infinity and vertical off $S$, this number is a sum over $p \in S$ of local numbers at $p$: the archimedean contributions cancel and only the fibres over $S$ remain.

Fix $p \in S$. Over $\mathbb{Z}_p$ the model is a discrete valuation model of the arithmetic variety. The flag Chern comparison at the places over $p$ gives the $p$-adic form of the third flag comparison, and the vanishing of the power sums at these places gives that the new roots satisfy the power sum relations there. The power sum term over a discrete valuation ring then computes the local number as a cycle number of the uniformizer divisor applied to $[\varphi_p]_{p, k, \tau} Q$, which has degree $d$. This cycle number is $\log p$ times the generic number of $[\varphi_p]_{p, k, \tau} Q$ over $\mathbb{Q}$, and the generic number of a root model is $\delta_M$ times the geometric functional. Dividing by $\delta_M > 0$ gives the formula. $\square$

**Theorem 9.10.4 (Linked towers satisfy the power sum formula).** Let $\mathrm{II}$ be an intersection system, let $T$ be a proportional root tower, and let $T$ be linked for $\mathrm{II}$ and labels $\varphi$. Then $T$ satisfies Proposition 6 for the label map

$$
\mathrm{frob}_p(\tau, n) = \varphi_p^{\,n+1}(\tau_{\mathrm{left}}).
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Num.power_sum_term_linked_tower` (also `GlobalTheory.T.linked_tower_power_sum`, a second name)

*Proof.* Let $2 \le B_0 \le B$, a component $c$, $\tau$, $k$ and $Q$ be given, and take $M$, the second roots and $S$ from the link. By the change of model theorem, for every $t > 0$ the difference $\mathrm{ar}_M(t)(p_k^\tau Q) - \mathrm{ar}_{M'}(t)(p_k^\tau Q)$ is the constant

$$
\sum_{p \in S} \log p \cdot \mathrm{geo}_M\big([\varphi_p]_{p, k, \tau}\, Q\big).
$$

A difference that is constant in $t$ passes to the limit $t \to 0$, since both models converge. With $\mathrm{PP}_M = \mathrm{PP}_{B_0, c}$ and $\mathrm{PP}_{M'} = \mathrm{PP}_{B, c}$ this gives $\mathrm{PP}_{B_0, c}(p_k^\tau Q) = \mathrm{PP}_{B, c}(p_k^\tau Q) + \sum_{p \in S} \log p \cdot \mathrm{geo}_M([\varphi_p]_{p, k, \tau} Q)$.

The set $S$ is the set of good primes in $(B_0, B]$. Since $\mathrm{geo}_M = \mathrm{geo}_{M_{B_0, c}}$ and the tower is proportional, $\mathrm{geo}_M(F) = \operatorname{vol}(c) \deg_{\mathrm{Fl}}(F)$. It remains to identify each term: for $p \ge 2$ an identity of the chapter on heights gives

$$
\log p \cdot \deg_{\mathrm{Fl}}\big([\varphi]_{p, k, \tau}\, Q\big) = \delta_p(\tau, k, Q)
$$

for the labels $\mathrm{frob}_p(\tau, n) = \varphi^{n+1}(\tau_{\mathrm{left}})$, where $\delta_p$ is the term of Proposition 6. $\square$

**Theorem 9.10.5 (Link step).** Assume the numerical Segre statement, the Hodge lattice flag bound and the trivial flag statement on Hodge components. Let $S_0 \subseteq S$ be finite sets of primes, with $S_0$ containing the primes dividing the discriminant of $E$, and let $o_0$, $o_1$ be root origins of root models $M_0$ over $S_0$ and $M_1$ over $S$, and $o_R$ a reference root origin over the empty set, all in the same analytic system. Assume that the Hodge components of $o_0$ and $o_1$ are Hodge-Tate free, that they have the same lattices at the primes of $S_0$, that the flag degree of $o_R$ is $1$, that all three realisations are on the full coordinate ideal, that $M_0$ and $M_1$ converge, that $2 \notin S \setminus S_0$, and that $\varphi_p$ is a Frobenius label permutation at every $p \in S \setminus S_0$. Then there are a root model $M$ and second roots on $M$ such that $M$ and $M'$ converge, $\mathrm{PP}_M = \mathrm{PP}_{M_0}$, $\mathrm{PP}_{M'} = \mathrm{PP}_{M_1}$, $\mathrm{geo}_M = \mathrm{geo}_{M_0}$, and the second roots are a change at $S \setminus S_0$ that is local at its places for $j = p$ and the labels $\varphi$.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.Link.link_step`

*Proof.* A comparison of root origins for nested prime sets puts the three origins into common coordinates $y$ with one Hodge component and one flag. The coordinates are birational and form an arithmetic variety of dimension $d + 1$. The model $M$ is the pullback of $M_0$ to the common coordinates; it has the same numbers as $M_0$ and the same geometric functional. The flag height bound for arithmetic varieties gives polynomials $f$ and $g$ whose pairs are vertical off $S \setminus S_0$. Isometric hermitian lines on the common coordinates give the twisted lines of the second roots, and the comparisons of heights of root origins, with the numerical Segre statement, show that the second root model has the numbers of $M_1$. At the primes of $S \setminus S_0$ the Frobenius labels, the Hodge lattice flag bound and the trivial flag statement give the flag Chern comparison and the vanishing of the power sums. $\square$

A permutation $\varphi$ of $\Psi \sqcup \Psi$ is a Frobenius label permutation at $p$ for the coefficient field if, at every prime ideal over $p$ of the ring of integers of the coefficient field, the label embedding of $\varphi(s)$ is congruent to the $p$-th power of the label embedding of $s$. A label map has Frobenius shape if, for every $p$ and $n$, $\mathrm{frob}_p(\tau, n)$ is a left label for one $\tau$ exactly when it is a left label for every $\tau$.

**Theorem 9.10.6 (Good towers are linked).** Assume the comparison input, the positivity of agreement, the Hodge lattice flag bound, the trivial flag statement on Hodge components and the top level inputs. Let $E$ be a CM field, abelian over $\mathbb{Q}$, let $Y$ be an integral model of $X_o(l)$, let $T$ be a root tower of type $(\Psi, p + q)$ with a good origin $o$, and let $\mathrm{II}$ be an intersection system. Assume that $Y$ is global, that the origin satisfies the extra conditions, that $\mathrm{II}$ is full and that $p, q \ge 1$. Then there are labels $\varphi$ such that the label map $\varphi_p^{\,n+1}(\tau_{\mathrm{left}})$ has Frobenius shape and $T$ is linked for $\mathrm{II}$ and $\varphi$.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.Link.goodOrigin_linked` (also `GlobalTheory.T.good_tower_global_conditions`, a second name)

*Proof.* Since $E$ is abelian over $\mathbb{Q}$, its Galois group is commutative, and the existence of Frobenius labels gives permutations $\varphi_p$ that are Frobenius label permutations at every prime and whose label map has Frobenius shape.

Let $2 \le B_0 \le B$ and a component $a$ be given. By the convergence part of the [statement on real towers](/entry/volume-theorem-x-of-inputs/), with the positivity of agreement and the inputs of the proof theory, the models $M_{B_0, a}$ and $M_{B, a}$ converge. The set $S_B$ of the origin consists of the primes $p \le B$ and the bad primes, so $S_{B_0} \subseteq S_B$, and $S_{B_0}$ contains the primes dividing the discriminant since these are bad. The extra conditions say that the Hodge lattices of the origin at a prime of $S_{B_0}$ do not depend on the level, so the Hodge components at $B_0$ and at $B$ have the same lattices there. The prime $2$ is bad, so $2 \notin S_B \setminus S_{B_0}$.

The link step, applied to the origins at $(B_0, a)$, $(B, a)$ and the reference origin of $a$, gives $M$ and second roots with the required numbers. The set $S_B \setminus S_{B_0}$ is the set of primes in $(B_0, B]$ outside the bad primes, and the index of the tower is $p$. So $T$ is linked. $\square$

The labels $\varphi_p^{\,n+1}(\tau_{\mathrm{left}})$ record the action of the $(n+1)$-st power of Frobenius on the CM types: the left or right label says whether the image lies on the $p$ side or the $q$ side of the Hodge decomposition. Frobenius shape says that this side does not depend on $\tau$; it is the input that lets the chain of tower estimates compare the shift terms of different CM types.

**Remark 9.10.7 (Formalization).** In the theorem on good towers the comparison input, the hypothesis that $Y$ is global, and $p, q \ge 1$ are not used; the extra conditions are used for the equality of the Hodge lattices, and the fullness of $\mathrm{II}$ for convergence ([GoodTowerGlobalConditions.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerGlobalConditions.lean#L197)). The numerical Segre statement and the inputs of the proof theory are taken from the top level inputs by position, as the fourth and tenth parts. The link step is stated with $j = p$ written directly as the first signature number ([GoodTowerGlobalConditions.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerGlobalConditions.lean#L69)). Primes are of two types in these statements: the linked tower uses a finite set of primes as a set of natural numbers with a primality condition, while second roots use the subtype of primes, and the proofs convert between them. We have not unfolded the coefficients $c_{\varphi, p, k}$, the flag Chern comparison, the vertical and isometric conditions on pairs, the local numbers, or the statements the proofs of the change of model and the link step call; the descriptions of these proofs list the steps, not their content.
