---
title: The inductive step of Angehrn and Siu
decls:
  - GlobalTheory.PairStep.exists_global_step
  - GlobalTheory.T.exists_global_section_angehrnSiu_inductive_step
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The inductive step of Angehrn and Siu

This section proves the inductive step of the theorem of Angehrn and Siu on a projective variety. A pair $(X, \Delta + D)$ has a non-klt centre $Z$ of dimension $k$ through a finite set $P$ of points. If the ample divisor $A$ is large on $Z$, in the sense $|P|\, k^k < h^k (A^k \cdot Z)$, we find a section $f_0$ of $lA$ that does not vanish identically on $Z$, such that the boundary $\Delta + (1-\delta)D + \frac{h}{l}\operatorname{div}(f_0)$ is not klt at any point of $P$. Since $f_0$ does not vanish on $Z$, the new non-klt locus meets $Z$ in a smaller set, and an induction on $k$ cuts the centre down to the points of $P$. The local work was done in Section 8. Here we count sections and pass from the scheme to its local rings.

For the background see [ample, nef and big line bundles](/learn/positivity-resolution/#ample-nef-and-big-line-bundles), [the theorem of Angehrn and Siu](/learn/positivity-resolution/#the-angehrn-siu-theorem) and [schemes and varieties](/learn/geometry/#schemes-and-varieties).

Let $X$ be an integral, locally noetherian, normal scheme, projective over $\mathbb{C}$, of dimension $n$. A $\mathbb{Q}$-divisor is a function $\Delta$ from the points of $X$ to $\mathbb{Q}$, read through its values at the generic points of prime divisors. We use the following notions.

**Definition 10.9.1 (Klt at a point and non-klt centre).** Let $\Delta$ be a $\mathbb{Q}$-divisor and $x \in X$. A *log equation* of $\Delta$ at $x$ is a nonzero rational $n$-form $\eta$, an integer $m > 0$ and a nonzero $g$ in the function field with $m(\operatorname{ord}_E \eta + \Delta_E) = \operatorname{ord}_E g$ for each prime divisor $E$ of $X$ through $x$, where $\Delta_E$ is the coefficient of $E$. So $g$ is a local equation of $m(K_X + \Delta)$ near $x$, with $K_X = \operatorname{div}(\eta)$. Then the discrepancy of a divisor $E$ over $X$ is $\operatorname{ord}_E \eta - \operatorname{ord}_E(g)/m$. The pair is *klt at* $x$ if there is a log equation at $x$ such that each divisor $E$ over $X$ whose centre passes through $x$ has discrepancy $> -1$. A point $z$ is a *non-klt centre* of $\Delta$ if there are a log equation at $z$ and a divisor $E$ over $X$ with centre the closure of $z$ and discrepancy $\le -1$.

So klt at $x$ is the condition of Section 6 for the local ring at $x$, written with a global form. A *log canonical multiple* is a Cartier divisor $G$ with $G \sim m(K_X + \Delta)$, given by one form $\eta$ and the local equations of $G$.

For a Cartier divisor $A$ and $l \ge 1$, a section of $lA$ is a rational function $f$ with $\operatorname{div}(f) + lA \ge 0$. It *generates at* $z$ if $f a^l$ is a unit at $z$ for a local equation $a$ of $A$, and it *vanishes at* $z$ if $f a^l$ lies in the maximal ideal at $z$. For the closure $Z$ of $z$, a section generates at $z$ if and only if it does not vanish identically on $Z$. We write $(A^k \cdot Z)$ for the intersection number of $A$ on $Z$, given by the Euler characteristics of the twists of $\mathcal{O}_Z$.

**Theorem 10.9.2 (Inductive step of Angehrn and Siu).** Assume principalisation. Let $X$ be as above, $\Delta$ an effective $\mathbb{Q}$-divisor with $(X,\Delta)$ klt at each point, $G$ a log canonical multiple of $\Delta$ with $m > 0$, $A$ an ample Cartier divisor and $D$ a $\mathbb{Q}$-Cartier $\mathbb{Q}$-divisor. Let $z \in X$ with closure $Z$ of dimension $k \ge 1$, and let $P$ be a finite set of closed points of $Z$. Suppose that $z$ is the generic point of $X$ or a non-klt centre of $\Delta + D$. Let $h \in \mathbb{Q}$, $h > 0$, with
$$|P|\, k^k < h^k\, (A^k \cdot Z).$$
Then for each $l_0$ there are $l \ge l_0$ with $l > h$, a section $f_0$ of $lA$ that generates at $z$, and $\delta_0 \in \mathbb{Q}$ with $0 < \delta_0 \le 1$, such that the following holds. For each section $u$ of $lA$ that vanishes at $z$, with $g = f_0 + u \neq 0$, each $\delta \in [0, \delta_0]$ and each $x \in P$, the pair
$$\Delta + (1-\delta) D + \frac{h}{l}\bigl(\operatorname{div}(g) + lA\bigr)$$
is not klt at $x$.

Lean: `GlobalTheory.PairStep.exists_global_step` (also `GlobalTheory.T.exists_global_section_angehrnSiu_inductive_step`, a second name).

The divisor $\operatorname{div}(g) + lA$ is the effective divisor of the section $g$, and $\frac{h}{l}$ of it is $\mathbb{Q}$-linearly equivalent to $hA$. The freedom in $u$ says that only the restriction of $f_0$ to $Z$ matters. In the standard form of the theorem the numerical condition reads $(A^k \cdot Z) > |P|\,(k/h)^k$; compare Lazarsfeld, *Positivity II*, §10.4.

*Proof.* We use five facts, each of which we read as a statement.

- (a) *A count.* For natural numbers $c$, $k \ge 1$ and rational $h > 0$, $d$ with $c\, k^k < h^k d$, there is $q < d$ such that for each $l_0$ there are $l \ge l_0$ and $M \ge 1$ with $kl < hM$, $h < l$ and
$$c \binom{M+k-1}{k} < \frac{q\, l^k}{k!}.$$
The reason is that $\binom{M+k-1}{k} \sim M^k / k!$, and we may take $M$ just above $kl/h$, so the left side is about $c\, k^k l^k / (h^k k!)$.
- (b) *Growth of sections on $Z$.* For $q < (A^k \cdot Z)$ there is $l_1$ with $h^0(Z, lA|_Z) \ge q\, l^k/k!$ for $l \ge l_1$. This is the asymptotic Riemann-Roch theorem on $Z$.
- (c) *Sections that restrict to a basis.* There is $l_2$ such that for $l \ge l_2$ there are sections $f_1, \dots, f_r$ of $lA$ on $X$ with $r = h^0(Z, lA|_Z)$ such that each nonzero combination $\sum_j a_j f_j$ with $a \in \mathbb{C}^r$ generates at $z$. For $l$ large the restriction $H^0(X, lA) \to H^0(Z, lA|_Z)$ is onto, by Serre vanishing, and the $f_j$ lift a basis.
- (d) *The residue map of $Z$.* There are a field $\kappa$ of transcendence degree $k$ over $\mathbb{C}$ and a surjective map $\pi_0$ over $\mathbb{C}$ from the local ring at $z$ onto $\kappa$ with kernel the functions that vanish at $z$. For each point $x$ of $Z$, the image of the local ring at $x$ is a local model of $\kappa$, and each element of $\kappa$ is a quotient of two elements of it; for a closed point $x$ the image has rational residues. So $\kappa$ is the function field of $Z$ and the image is the local ring of $Z$ at $x$.
- (e) *From local rings to the scheme.* Let $x \in P$, and suppose that the local ring $R_x$ has the property of the conclusion of the theorem of Section 8 for the combination $\sum_j a_j f_j a_x^l$, with $t = h/l$. Suppose that $z$ is the generic point and $kl < hM$, or that there is a divisor $E$ over $X$ with centre $Z$, with discrepancy $\le -1$ for a log equation of $\Delta + D$ at $z$, and with $k + M\delta \operatorname{ord}_E(D) \le \frac{h}{l} M$, where $\operatorname{ord}_E(D)$ is the order along $E$ of $D$ at $x$. Then the pair of the theorem is not klt at $x$ for each $u$, $g$ as in the theorem.

The fact (e) is proved in the same file as the theorem. It takes a transcendence basis $\xi$ in $R_x$, writes the form $\eta$ of $G$ as $F_0\, d\xi$, and turns the log equation of $\Delta + (1-\delta)D + \frac{h}{l}(\operatorname{div}(g) + lA)$ at $x$ into a formal sum $\varphi + t[s]$ over $R_x$ with $s = g a_x^l$, so that klt at $x$ becomes klt over $R_x$ in the sense of Section 6. In case $E$ exists, the discrepancy of $E$ for $\Delta + (1-\delta)D$ is at most $-1 + \delta\operatorname{ord}_E(D)$, since $D \ge 0$ along $E$ near $x$. So the condition of (e) gives condition (B) of Section 8.

Now the proof. Let $c = |P|$, and apply (a) with $d = (A^k \cdot Z)$. It gives $q$. Let $l_1$ be as in (b) for $q$, and $l_2$ as in (c). By (a) with the bound $\max(l_0, l_1, l_2)$ there are $l$ and $M \ge 1$ with $l \ge \max(l_0, l_1, l_2)$, $kl < hM$, $h < l$ and $c\binom{M+k-1}{k} < q l^k/k!$. Let $f_1, \dots, f_r$ be as in (c). By (b),
$$c \binom{M+k-1}{k} < \frac{q\,l^k}{k!} \le h^0(Z, lA|_Z) = r.$$

Number the points of $P$ as $x_1, \dots, x_c$. Each $x_i$ is a specialisation of $z$, so the local ring $R_i$ at $x_i$ lies in the local ring at $z$, and $\pi_i$, the restriction of $\pi_0$ of (d), maps $R_i$ to $\kappa$. Choose a local equation $a_i$ of $A$ at $x_i$ and a local equation $a_z$ at $z$. Put
$$w_{ij} = f_j a_i^l \in R_i, \qquad \lambda_i = \pi_0\bigl(a_i^l / a_z^l\bigr), \qquad \bar w_j = \pi_0\bigl(f_j a_z^l\bigr).$$
Since $a_i$ is also a local equation at $z$, the ratio $a_i^l/a_z^l$ is a unit at $z$, so $\lambda_i \neq 0$, and $\pi_i(w_{ij}) = \lambda_i \bar w_j$. The ring $R_i$ is an integrally closed local model of the function field, since $X$ is normal, and it has rational residues, since $x_i$ is a closed point of a projective variety over $\mathbb{C}$. The other hypotheses of the theorem of Section 8 ([Theorem 10.8.1](/entry/not-klt-at-points/)) hold by (d) and by the count above. It gives $a \in \mathbb{C}^r$, $a \neq 0$. Put
$$f_0 = \sum_{j=1}^r a_j f_j.$$
It is a section of $lA$, and it generates at $z$ by (c). Also $\sum_j a_j w_{ij} = f_0 a_i^l$.

It remains to choose $\delta_0$ and to check (e) at each $x \in P$.

*The generic case.* If $z$ is the generic point of $X$, put $\delta_0 = 1$. Then $kl < hM$, and (e) applies at each $x \in P$ for each $\delta \in [0, 1]$.

*The centre case.* Otherwise let $E$ be a divisor over $X$ with centre $Z$ and discrepancy $\le -1$ for $\Delta + D$. For $x \in P$ let $D = \frac{1}{m_x}\operatorname{div}(f_x)$ near $x$ with $f_x$ regular at $x$. Then $\operatorname{ord}_E(D)_x = \operatorname{ord}_E(f_x)/m_x \ge 0$, since the centre of $E$ passes through $x$. Put
$$B = \sum_{x \in P} \frac{\operatorname{ord}_E f_x}{m_x} \ge 0, \qquad \delta_0 = \min\Bigl(1, \frac{hM/l - k}{M(B+1)}\Bigr).$$
Since $kl < hM$, we have $hM/l - k > 0$, so $0 < \delta_0 \le 1$. For $\delta \in [0, \delta_0]$ and $x \in P$,
$$M \delta\, \frac{\operatorname{ord}_E f_x}{m_x} \le M\delta (B+1) \le \frac{h}{l}M - k.$$
So $k + M\delta \operatorname{ord}_E(D)_x \le \frac{h}{l} M$, and (e) applies.

In both cases (e) gives that the pair is not klt at $x$, for each $u$, $g$, $\delta$ and $x$ as in the theorem. $\square$

The perturbation by $\delta$ costs at most $M\delta\operatorname{ord}_E(D)_x$ in condition (B) of Section 8, because the discrepancy of $E$ for $\Delta + (1-\delta)D$ is at most $-1 + \delta\operatorname{ord}_E(D)_x$. The gap $hM/l - k > 0$ from the count (a) pays for it. So a user of the theorem can lower the coefficient of $D$ a little, and the new pair is still not klt at the points of $P$.

**Remark 10.9.3 (Formalization).** The theorem is in ExistsGlobalSectionAngehrnSiuInductiveStep.lean, line 237. Klt at a point is `KltAt` (PublishedTheorems/Divisors₂/IsLogCanonicalMultipleCanonical.lean, line 315), the non-klt centre is `IsNkltCentre` (Definitions/Divisors/CentreAtOfIsAt.lean, line 33), and the intersection number is `interNumRed`, the Snapper number of the reduced closure. The facts (a) to (e) are `exists_lt_binomial_bound_of_mul_pow_lt`, `h0_lower_bound_of_isAmple_cartierDiv`, `exists_sections_restrict_basis`, `exists_residueMap_closure_point` and `not_kltAt_of_local`. We read their statements, not their proofs, and the reasons given for (a), (b) and (c) are the standard ones. The hypothesis that $(X, \Delta)$ is klt at each point is bound as `_` on line 248 and not used. The conclusion does not say that $f_0$ vanishes to high order at the points of $P$. It says only that $f_0$ generates at $z$ and that the new pair is not klt. The users of the theorem are `AmpleStep.exists_divisor` and `PairStep.exists_step_divisor`.

## Notes and references

The chapter feeds the step [EveryCharacter from the literature](/step/every-character-of-literature/) of [the literature part of the proof](/proof/literature/) in two places. The estimate of [Hörmander](/entry/hormander/) and the $L^2$ extension from a finite set of Section 5 prove [the $L^2$ extension theorem for log canonical bundles](/entry/l2-extension-log-canonical-of-literature/), which the step uses in its published form. The [inductive step of Angehrn and Siu](/entry/exists-global-section-angehrn-siu-inductive-step/) is used in the construction of divisors with an isolated non-klt centre at given points, through the lemmas on ample and pair steps that call it. Together with the vanishing theorem of Nadel these give sections of adjoint bundles that separate points.

- L. Hörmander, *$L^2$ estimates and existence theorems for the $\bar\partial$ operator*, Acta Math. 113 (1965), 89 to 152, for the estimate of Section 1.
- L. Hörmander, *An Introduction to Complex Analysis in Several Variables*, Chapter IV, for the $L^2$ method on pseudoconvex domains and Stein manifolds.
- J.-P. Demailly, *Complex Analytic and Differential Geometry*, Chapter VIII, for $L^2$ estimates on weakly pseudoconvex Kähler manifolds and the twisted estimates.
- T. Ohsawa and K. Takegoshi, *On the extension of $L^2$ holomorphic functions*, Math. Z. 195 (1987), for the extension theorem of Sections 4 and 5.
- L. Manivel, *Un théorème de prolongement $L^2$ de sections holomorphes d'un fibré hermitien*, Math. Z. 212 (1993), for the extension of sections of line bundles from the common zeros of sections.
- J.-P. Demailly, *On the Ohsawa-Takegoshi-Manivel $L^2$ extension theorem* (2000), for the form with a twist of the weight by a function of $\psi$.
- U. Angehrn and Y.-T. Siu, *Effective freeness and point separation for adjoint bundles*, Invent. Math. 122 (1995), for Sections 8 and 9.
- R. Lazarsfeld, *Positivity in Algebraic Geometry II*, Chapter 9, for multiplier ideals and klt pairs, and §10.4, for the theorem of Angehrn and Siu.
- J. Kollár and S. Mori, *Birational Geometry of Algebraic Varieties*, Chapter 2, for discrepancies and klt pairs, and Theorem 5.50, for inversion of adjunction in Section 6.
- J. Kollár, *Singularities of pairs*, Proc. Sympos. Pure Math. 62 (1997), for non-klt centres and the method of cutting them down.
- J. Kollár, *Lectures on Resolution of Singularities*, Chapter 3, for principalisation of ideals.
- H. Hironaka, *Resolution of singularities of an algebraic variety over a field of characteristic zero*, Ann. of Math. 79 (1964), for resolution and principalisation in characteristic zero.
