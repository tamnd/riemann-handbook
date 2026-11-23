---
title: The maximal slope of the level-zero lattice
decls:
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.classMapT_of
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.class_map_archimedean
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slopeMaxGiven_free
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slope_inequality_constant_four
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slope_inequality_family_four
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.muMax_le_mon
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.muMax_le_class
  - Formalism.MainNotions.flipTwoThree.hookBound_holds
  - Formalism.MainNotions.flipTwoThree.shortDual_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The maximal slope of the level-zero lattice

This section proves an upper bound for the maximal slope of the level-zero lattice $A_0$ at every word that has a column valuation. The bound is a sum over the indices $\tau$ of three terms: the size of the weight times $4 \log(k\, \mathrm{rd}_E / 2)$, a term $k^2 \log(\delta_\tau + k)$ from the spread of the weight, and the last entry of the weight times $\log T_u$. The proof maps each class part of the lattice into a lattice of polynomial coefficients by the slope inequality of Section 1, using short vectors in the dual of the class lattice to change variables. The bound is [Theorem 1.7.8](/entry/slope-inequality-constant-four/), and the form for families is used in [the connectedness statement from Green](/entry/shape-closed-link-n-of-green/).

We keep the setting of Section 6 at a word $u$ and write $k$ for the rank $N$ of the level-zero columns, which is also the rank of $X_0$ over $E$. For each $\tau$ the level-zero weight is a sequence of rational numbers $\lambda_{\tau,0} \geq \lambda_{\tau,1} \geq \dots \geq \lambda_{\tau,k-1}$, with integer differences, and we put
$$
\begin{aligned}
P_\tau &= \sum_{i=0}^{k-1} (\lambda_{\tau,i} - \lambda_{\tau,k-1}), &\qquad \delta_\tau &= \lambda_{\tau,0} - \lambda_{\tau,k-1}, \\
\nu_\tau &= (\lambda_{\tau,i} - \lambda_{\tau,k-1})_{0 \leq i < k}, &\qquad d_\tau &= \lambda_{\tau,k-1}.
\end{aligned}
$$
So $\nu_\tau$ is a decreasing sequence of natural numbers with sum $P_\tau$, the polynomials in $\Delta(\lambda_\tau)$ are homogeneous of degree $P_\tau$, and $d_\tau$ is the determinant shift of Section 6. The *root discriminant* of $E$ is $\mathrm{rd}_E = |d_E|^{1/[E:\mathbb{Q}]}$, and $[E : \mathbb{Q}] = 2f$.

### Two inputs

For a decreasing sequence $\nu \in \mathbb{N}^k$ let $\xi_\nu$ be the extremal vector of the Weyl module of highest weight $\nu$, and put
$$
c(\nu) = \frac{\langle \xi_\nu, \xi_\nu \rangle_{\mathrm{F}}}{\prod_{l} \nu_l!} .
$$

**Theorem 1.7.1 (Hook bound).** For every $k \geq 1$ and every decreasing $\nu \in \mathbb{N}^k$,
$$
1 \leq c(\nu) \leq (\nu_0 + k)^{k(k-1)/2} .
$$

Lean: `Formalism.MainNotions.flipTwoThree.hookBound_holds`

*Proof.* The bound is derived from the Capelli determinant identity; the proof lies outside this chapter. $\square$

**Theorem 1.7.2 (Short vectors in the dual lattice).** Let $\Lambda \subseteq X_0$ be an $\mathcal{O}_E$-lattice with $\Lambda \subseteq \Lambda^\vee$. Then there are vectors $y_1, \dots, y_k \in \Lambda^\vee$, linearly independent over $E$, with
$$
\operatorname{tr}_{E/\mathbb{Q}} h(y_a, y_a) \leq [E:\mathbb{Q}]\, k^2\, \mathrm{rd}_E^2 \qquad (1 \leq a \leq k).
$$

Lean: `Formalism.MainNotions.flipTwoThree.shortDual_holds` (also `Formalism.MainNotions.flipTwoThree.exists_short_basis_dual`).

*Proof.* The bilinear form $\operatorname{tr}_{E/\mathbb{Q}} h(x, y)$ makes $X_0$ a Euclidean space of dimension $2fk$ over $\mathbb{R}$ after extension of scalars, since $h$ is positive definite at every embedding. The proof applies the transference theorem for successive minima, $\lambda_i(M)\, \lambda_{n+1-i}(M^*) \leq n$ for a full lattice $M$ in a Euclidean space of dimension $n$ and its dual $M^*$, to Euclidean lattices built from $\Lambda$. The discriminant of $E$ enters when the Euclidean dual is compared with $\Lambda^\vee$. We did not unfold this part of the proof. $\square$

We say that $y = (y_a)$ is a family of *short dual vectors* for the class $c$ if $y_a \in \Lambda_c^\vee$, the $y_a$ are linearly independent over $E$, and $\operatorname{tr}_{E/\mathbb{Q}} h(y_a, y_a) / (2f) \leq k^2 \mathrm{rd}_E^2$ for every $a$. Since a column valuation makes every class lattice $T^{2f}$-modular, and in particular contained in its dual, the theorem gives short dual vectors for every class.

### Lattices of coefficients

Let $\mathcal{M}$ be a finite set with weights $w(m) > 0$. We give $K^{\mathcal{M}}$ the standard basis and the metric with $\| a \|_v^2 = \sum_m w(m) |\sigma_v(a_m)|^2$ at every infinite place $v$.

**Proposition 1.7.3 (Maximal slope through coefficients).** Let $K$ be totally complex, $(V, b, X)$ with invertible frames, and $N \subseteq V$ a finitely generated $\mathcal{O}_K$-submodule. Let $\varphi : V \to K^{\mathcal{M}}$ be $K$-linear, injective on $N$, with $\varphi(N) \neq 0$. Let $I$ be a nonzero fractional ideal with $\varphi(x)_m \in I$ for every $x \in N$ and every $m$, and let $B_v > 0$ satisfy $\|\varphi x\|_v^2 \leq B_v \|x\|_v^2$ for all $v$ and $x$. If $c_0 > 0$ and $w(m) \geq c_0$ for all $m$, then
$$
\mu_{\max}(N) \leq -\log c_0 - \frac{2 \log \mathrm{N}(I)}{[K:\mathbb{Q}]} + \frac{1}{n_\infty} \sum_{v \in S_\infty} \log B_v .
$$

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.muMax_le_mon`

*Proof.* Let $L_0 = \mathcal{O}_K^{\mathcal{M}}$ be the sum of the lines $\mathcal{O}_K e_m$. The lines are orthogonal at every place, and the basis vector $e_m$ has $\|e_m\|_v^2 = w(m) \geq c_0$, so each line has maximal slope at most $-\log c_0$. By the orthogonal sum theorem of Section 2, $\mu_{\max}(L_0) \leq -\log c_0$. Multiplying a lattice by the fractional ideal $I$ lowers the maximal slope by $2 \log \mathrm{N}(I) / [K:\mathbb{Q}]$, so $\mu_{\max}(I L_0) \leq -\log c_0 - 2\log\mathrm{N}(I)/[K:\mathbb{Q}]$. By hypothesis $\varphi(N) \subseteq I L_0$. The norm bound gives $\|\varphi\|_v^2 \leq B_v$, so $h(\varphi) \leq \frac{1}{n_\infty} \sum_v \log B_v$, and the slope inequality of Section 1 for the map $\varphi$, injective on $N$, gives the claim. $\square$

For the lattice $A_0$ the set $\mathcal{M}$ is the set of monomials $m$ in the variables $(Z_\tau)_{ij}$ that occur in $\mathcal{P}_\lambda$, with the weight $w(m) = m! / \prod_\tau \langle \xi_\tau, \xi_\tau \rangle_{\mathrm{F}}$, where $m!$ is the product of the factorials of the exponents. This is the normalized Fock norm of the monomial. Put
$$
c_\lambda = \Big( k^{\sum_\tau P_\tau} \prod_\tau c(\nu_\tau) \Big)^{-1}, \qquad\text{so that}\qquad -\log c_\lambda = \sum_\tau \big( P_\tau \log k + \log c(\nu_\tau) \big).
$$
A multinomial estimate shows $w(m) \geq c_\lambda$ for every $m \in \mathcal{M}$.

### The bound class by class

Let a column valuation at $u$ be given. Since $\kappa$ is injective, every $x \in V$ is the sum over the classes of the elements $x_c$ with $\kappa(x_c)$ equal to $\kappa(x)$ at $c$ and zero elsewhere, and $x_c \in L$ when $x \in L$. Let $N_c \subseteq L$ be the image of $L$ under $x \mapsto x_c$.

**Lemma 1.7.4 (Reduction to one class).** There is a class $c$ with $\mu_{\max}(A_0) \leq \mu_{\max}(A_0[N_c])$.

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.muMax_le_class`

*Proof.* The $N_c$ are nonzero and orthogonal at every infinite place, by the infinite condition of the column valuation. Each has rank $\dim_K \mathcal{P}_\lambda$, their sum is $L$, and the rank of $L$ is the number of classes times $\dim_K \mathcal{P}_\lambda$. The classes are nonempty. Now apply the orthogonal sum theorem of Section 2. $\square$

**Theorem 1.7.5 (Class map).** Let a column valuation at $u$ be given, let $c$ be a class, and let $y_1, \dots, y_k \in \Lambda_c^\vee$ be linearly independent over $E$. For $v \in S_\infty$ and each $\tau$ put $G_{v,\tau} = \sum_a \operatorname{Re} \sigma_v \rho_\tau h(y_a, y_a)$. Then there are a $K$-linear map $\varphi : V \to K^{\mathcal{M}}$, a nonzero fractional ideal $I$ and numbers $D_v > 0$ such that $\varphi$ is injective on $N_c$, $\varphi(x)_m \in I$ for $x \in N_c$, and
$$
\begin{aligned}
\|\varphi x\|_v^2 &\leq \Big( \prod_\tau G_{v,\tau}^{P_\tau} \Big) D_v\, \|x\|_v^2 \qquad (v \in S_\infty,\ x \in V), \\
-\frac{2\log \mathrm{N}(I)}{[K:\mathbb{Q}]} + \frac{1}{n_\infty} \sum_v \log D_v &\leq -\sum_\tau \lambda_{\tau,k-1} \log T_u .
\end{aligned}
$$

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.class_map_archimedean` (also `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.classMapT_of`, `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.q_frame_degree`).

*Proof.* Let $g_\tau$ be the inverse of the $k \times k$ matrix whose $(a, i)$ entry is the pairing of $y_a$ with the $i$th basis vector of $Q_{c,\tau}$ through $\beta_{c,\tau}$, and let $\varphi(x)$ be the family of coefficients of the polynomial $g \cdot \kappa(x)_c$. It is injective on $N_c$ because $\kappa$ is injective and the twisted action is invertible. Let $M_\tau \subseteq K^k$ be the lattice of coordinate vectors of $L_{Q_{c,\tau}}$, and let $I$ be the *twisted ideal* of the family $M = (M_\tau)$: the elements $a \in K$ such that $a \prod_\tau \det(\gamma_\tau)^{-d_\tau}$ is integral at $w$ for every finite place $w$ and every family $\gamma$ of local bases of the $M_\tau$ at $w$. The finite condition of the column valuation, together with $y_a \in \Lambda_c^\vee$, puts the coefficients in $I$. Put $D_v = \prod_\tau |\det X_v(Q_{c,\tau})|^{2 d_\tau}$. The norm bound comes from the infinite condition: after the change of variables by $g$, the Fock norm of each monomial is bounded by the product of the $G_{v,\tau}$ raised to the degrees $P_\tau$.

For the second inequality we prove equality. The norm of the twisted ideal is
$$
-\frac{2\log\mathrm{N}(I)}{[K:\mathbb{Q}]} = \sum_\tau d_\tau\, k\, \mu(M_\tau),
$$
where $M_\tau$ has the standard metric. By the frame formula of Section 1, applied to $Q_{c,\tau}$ with its own basis and to $M_\tau$,
$$
k\, \mu(Q_{c,\tau}) = k\, \mu(M_\tau) + \frac{1}{n_\infty} \sum_v \log |\det X_v(Q_{c,\tau})|^2 .
$$
Since $\Lambda_c$ is $T_u^{2f}$-modular and $\beta_{c,\tau}$ is an isometry onto $Q_{c,\tau}$, $\mu(Q_{c,\tau}) = -\log T_u / k$. With $d_\tau = \lambda_{\tau,k-1}$ the left side becomes $\sum_\tau \lambda_{\tau,k-1} \cdot (-\log T_u)$. $\square$

**Lemma 1.7.6 (Mean of short vectors).** If $y$ is a family of short dual vectors for $c$, then $\frac{1}{n_\infty} \sum_v \log G_{v,\tau} \leq \log(k^3 \mathrm{rd}_E^2)$ for every $\tau$.

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.shortAt_mean_log`

*Proof.* As $v$ runs over the infinite places of $K$, the composite $\sigma_v \circ \rho_\tau$ runs over the places of $E$, each equally often, so the mean over $v$ equals the mean over the $f$ places of $E$. Each $h(y_a, y_a)$ is totally positive, so the mean of $\sigma(h(y_a, y_a))$ over the places of $E$ is $\operatorname{tr}_{E/\mathbb{Q}} h(y_a,y_a) / (2f) \leq k^2 \mathrm{rd}_E^2$. By concavity of the logarithm the mean of $\log G$ is at most the logarithm of the mean of $G$, which is at most $k \cdot k^2 \mathrm{rd}_E^2$. $\square$

### The bound

**Theorem 1.7.7 (Maximal slope given short vectors).** Let a column valuation at $u$ be given, and suppose that every class has a family of short dual vectors. Then
$$
\mu_{\max}(A_0) \leq \sum_\tau \Big( P_\tau \log\big(k^4 \mathrm{rd}_E^2\big) + \log c(\nu_\tau) - \lambda_{\tau,k-1} \log T_u \Big).
$$

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slopeMaxGiven_free` (also `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slopeMaxGiven_of_class`, `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slopeMaxClass_of_map`, `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.class_map_of_archimedean`).

*Proof.* Choose $c$ by the reduction lemma, and apply the class map theorem to the short dual vectors of $c$. Put $B_v = \prod_\tau G_{v,\tau}^{P_\tau} D_v$. By the lemma on short vectors,
$$
\frac{1}{n_\infty}\sum_v \log B_v \leq \sum_\tau P_\tau \log(k^3\mathrm{rd}_E^2) + \frac{1}{n_\infty}\sum_v \log D_v .
$$
The proposition on coefficients with $c_0 = c_\lambda$ bounds $\mu_{\max}(A_0[N_c])$ by $-\log c_\lambda$ plus the ideal and archimedean terms, which by the class map theorem are at most $\sum_\tau P_\tau \log(k^3 \mathrm{rd}_E^2) - \sum_\tau \lambda_{\tau,k-1}\log T_u$. Adding $-\log c_\lambda = \sum_\tau (P_\tau \log k + \log c(\nu_\tau))$ gives the bound. $\square$

**Theorem 1.7.8 (Maximal slope bound with constant 4).** At every word $u$ with a column valuation,
$$
\mu_{\max}(A_0) \leq \sum_\tau \Big( 4 P_\tau \log\frac{k\, \mathrm{rd}_E}{2} + k^2 \log(\delta_\tau + k) + |\lambda_{\tau,k-1}| \log T_u \Big).
$$

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slope_inequality_constant_four` (also `Formalism.MainNotions.flipTwoThree.slope_bound_of_max_slope`, `Formalism.MainNotions.flipTwoThree.slopeMaxOpen_of_hook_two_le_v`, `Formalism.MainNotions.flipTwoThree.two_le_half_rootDiscr`).

*Proof.* The class lattices are contained in their duals, so short dual vectors exist for every class by the theorem on short vectors, divided by $[E:\mathbb{Q}] = 2f$. The previous theorem applies. We compare the three terms. The data force $\mathrm{rd}_E \geq 4$, so $(\mathrm{rd}_E/2)^2 \geq 4$ and
$$
k^4 \mathrm{rd}_E^2 = 4 k^4 (\mathrm{rd}_E/2)^2 \leq (k\,\mathrm{rd}_E/2)^4 ;
$$
since $P_\tau \geq 0$, the first term is at most $4 P_\tau \log(k\,\mathrm{rd}_E/2)$. By the hook bound, $\log c(\nu_\tau) \leq \frac{k(k-1)}{2}\log(\delta_\tau + k) \leq k^2 \log(\delta_\tau + k)$, because $\nu_{\tau,0} = \delta_\tau$ and $\delta_\tau + k \geq 1$. Finally $-\lambda_{\tau,k-1}\log T_u \leq |\lambda_{\tau,k-1}| \log T_u$ since $\log T_u \geq 0$. $\square$

The constant $4$ is the exponent in $k^4 \mathrm{rd}_E^2 \leq (k\,\mathrm{rd}_E/2)^4$: three powers of $k$ come from the short vectors, one from the multinomial estimate, and the factor $4$ inside the logarithm is absorbed by $\mathrm{rd}_E \geq 4$.

A *family* of data is indexed by a real parameter $x > x_1$ and, for each $x$, a set of indices $i$; it carries a datum $D(x, i)$ of the kind used here for each pair. A property holds *for the family* if there is an $x_0$ such that it holds for all $D(x, i)$ with $x \geq x_0$ and $x > x_1$.

**Corollary 1.7.9 (Maximal slope bound for families).** For every family, the bound with constant 4 holds for the family.

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.slope_inequality_family_four`

*Proof.* Take $x_0 = 0$ and apply [Theorem 1.7.8](/entry/slope-inequality-constant-four/) to each $D(x, i)$. $\square$

**Remark 1.7.10 (Formalization).** The statement that the class map exists with an inequality is proved as an equality ([PacketOfFrameDegree.lean](lean:Formalism/LocalToGlobal/GlobalTheory/GL4/PacketOfFrameDegree.lean#L102)). The class map theorem uses only that the $y_a$ lie in the dual and are independent, and discards the trace bound ([PacketOfFrameDegree.lean](lean:Formalism/LocalToGlobal/GlobalTheory/GL4/PacketOfFrameDegree.lean#L74)). The short vector theorem uses only $\Lambda \subseteq \Lambda^\vee$ and not the index $T^{2f}$. The inequality $\mathrm{rd}_E \geq 4$ is derived from the standing bounds on the ranks and a lower bound for the root discriminant carried by the data ([SlopeMaxOpenOfHookTwoLeV.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/SlopeMaxOpenOfHookTwoLeV.lean#L171)). The corollary for families ignores the family: it holds for every datum, with threshold $0$ ([PStmtFree.lean](lean:Formalism/LocalToGlobal/GlobalTheory/GL4/PStmtFree.lean#L17)). We did not unfold the norm bound of the class map, the multinomial estimate, or the comparison of duals in the short vector theorem; the descriptions above follow the statements of the lemmas used.
