---
title: Weyl and dual Weyl lattices
decls:
  - Formalism.InvariantFactorPaths.INST.Top.sandwichLocal
  - Formalism.InvariantFactorPaths.ColumnFamilies.highest_weight_corollary_two
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weyl and dual Weyl lattices

This section compares two integral forms of an irreducible representation of $\mathrm{GL}_r$. The first is the Weyl lattice, spanned by divided powers of lowering operators applied to a highest weight vector. The second is the dual Weyl lattice, the integral polynomials that are invariant under a unipotent group. The Weyl lattice is contained in the dual Weyl lattice, and a power of $p$ that depends only on $r$ and on the size of the weight multiplies the dual lattice into the Weyl lattice. The second theorem identifies the lattice spanned by bideterminants with the largest lattice on which all divided powers have integral highest weight coordinates. Both results feed the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/), where lattices of polynomials on matrices must be compared up to a controlled power of $p$. The background is in [polynomials on matrices](/learn/combinatorics/#polynomials-on-matrices), [minors](/learn/combinatorics/#minors-and-determinant-identities) and [[highest weight|C5W8BE1DRY]] theory ([highest weights and branching](/learn/representations/#highest-weights-and-branching)).

Throughout, $r \geq 1$ and $n \leq r$. Let $R$ be a commutative ring and let $R[x]$ be the polynomial ring in the variables $x_{a t}$ with $a < r$ (rows) and $t < n$ (columns).

**Definition 8.1.1 (Dual Weyl lattice).** Let $\nu = (\nu_0 \geq \nu_1 \geq \dots \geq \nu_{n-1})$ be a non-increasing sequence of natural numbers. For $l < j < n$ let $\theta_{lj}$ be the substitution $x_{a j} \mapsto x_{a j} + s\, x_{a l}$ (for all $a$) in $R[s][x]$, with $s$ a new variable. The *dual Weyl lattice* $\nabla_R(\nu)$ is the set of $f \in R[x]$ that are homogeneous of degree $\nu_t$ in the variables of column $t$, for each $t$, and that satisfy $\theta_{lj}(f) = f$ for all $l < j$.

Lean: `Formalism.GradedWeylDivisibility.dualWeyl`.

In words, $\nabla_R(\nu)$ is the space of functions on $r \times n$ matrices of column degree $\nu$ that are invariant under the upper unipotent group acting on the columns. The group $\mathrm{GL}_r$ acts on the rows. Over a field of characteristic $0$ this is the irreducible representation of highest weight $\nu$, and over $\mathbb{Z}$ it is the module of global sections of a line bundle on the flag variety (Jantzen, Part II, Chapter 2).

**Definition 8.1.2 (Weyl lattice).** For $a \neq b$ and $k \geq 0$ let $\rho^{(k)}_{ab}(f)$ be the coefficient of $s^k$ in $f(x_{b t} \mapsto x_{b t} + s\, x_{a t})$. Over $\mathbb{Q}$ this is $\frac{1}{k!} E_{ab}^k f$ with $E_{ab} = \sum_t x_{a t}\, \partial/\partial x_{b t}$, so $\rho^{(k)}_{ab}$ is a divided power, and it is defined over every ring. Let $\Delta_s$ be the leading principal $s \times s$ minor of $(x_{a t})$ and put
$$h_\nu = \prod_{s < n} \Delta_{s+1}^{\,\nu_s - \nu_{s+1}}, \qquad \nu_n = 0.$$
The *Weyl lattice* $W_R(\nu)$ is the $R$-span of all words $\rho^{(k_1)}_{a_1 b_1} \cdots \rho^{(k_m)}_{a_m b_m}(h_\nu)$.

Lean: `Formalism.GradedWeylDivisibility.weyl`.

The polynomial $h_\nu$ is the highest weight vector: it is a product of initial minors, so it is invariant under $\theta_{lj}$, and its column degrees are $\nu$. Since the row operations $\rho^{(k)}_{ab}$ commute with the column substitutions $\theta_{lj}$, $W_R(\nu) \subseteq \nabla_R(\nu)$ over any ring.

For a prime $p$ and a natural number $l$ put
$$e(p, r, l) = \frac{r(r-1)}{2}\, \lfloor \log_p (l + r - 1) \rfloor.$$
We say that $\nu$ is *bounded by $l$* if $\nu_t \leq l$ for all $t$, or if $n = r$ and $\nu_s \leq \nu_t + l$ for all $s, t$. The second case allows large weights as long as the spread $\nu_0 - \nu_{r-1}$ is at most $l$.

**Theorem 8.1.3 (Sandwich over a local domain).** Let $p$ be a prime, $n \leq r$, $\nu$ non-increasing and bounded by $l$. Let $O$ be a local integral domain in which $p$ is not a unit. Then
$$p^{e(p, r, l)}\, \nabla_O(\nu) \subseteq W_O(\nu) \subseteq \nabla_O(\nu).$$

Lean: `Formalism.InvariantFactorPaths.INST.Top.sandwichLocal` (also `Formalism.InvariantFactorPaths.INST.sandwichLocal`).

*Proof (outline).* The second inclusion was shown above. For the first we pass through four rings.

1. Every integer $c$ prime to $p$ is a unit in $O$. Indeed $c$ and $p$ are coprime, so $up + vc = 1$ with $u, v \in \mathbb{Z}$. In a local ring, if $p$ is not a unit then $p$ is in the maximal ideal, so $vc = 1 - up$ is a unit, and so is $c$.
2. Over $\mathbb{Z}_p$ the inclusion $p^{e}\nabla \subseteq W$ holds. The two cases of the bound on $\nu$ are first brought to one common form (the case $\nu_t \leq l$ for all $t$ and the square case $n = r$ are treated by two separate reductions). In the common form, the proof compares the two lattices with the operators $\rho^{(1)}_{ab}$ and $\rho^{(k)}_{ab}$ for one pair of rows $a < b$ at a time, that is, inside a copy of $\mathrm{GL}_2$. The exponent $e(p, r, l)$ has one factor $\lfloor \log_p(l + r - 1)\rfloor$ for each of the $r(r-1)/2$ pairs of rows: by Kummer's theorem, a binomial coefficient $\binom{m}{k}$ with $m \leq l + r - 1$ has $p$-adic valuation at most $\lfloor \log_p(l + r - 1)\rfloor$, and such coefficients are the denominators that the divided powers create.
3. Descent to $\mathbb{Z}$. For $f \in \nabla_{\mathbb{Z}}(\nu)$ there is an integer $c$ prime to $p$ with $c\, p^{e} f \in W_{\mathbb{Z}}(\nu)$. This follows from step 2, since $\mathbb{Z}_p$ is the completion of the localization $\mathbb{Z}_{(p)}$ and both lattices are spanned by polynomials with integer coefficients.
4. Ascent to $O$. If every integer prime to $p$ is a unit in the domain $O$, the factor $c$ of step 3 can be inverted, and base change from $\mathbb{Z}$ to $O$ gives $p^{e}\nabla_O(\nu) \subseteq W_O(\nu)$.

Step 1 shows that step 4 applies to $O$. $\square$

The second result describes the bideterminant lattice by a duality. Let $n \geq 1$ and let $\mu = (\mu_1 \geq \dots \geq \mu_n)$ be a dominant weight in $\mathbb{Z}^n$. Now take $n \times n$ variables $x_{ij}$ and let $X$ be the generic matrix. For an integer $c$ let $h(c) = \#\{m : c \leq \mu_m\}$ be the height of column $c$ of the diagram of $\mu$, for $\mu_n < c \leq \mu_1$.

**Definition 8.1.4 (Bideterminants of shape $\mu$).** A *column choice* $I$ gives, for each $c$ with $\mu_n < c \leq \mu_1$, a set $I_c \subseteq \{1, \dots, n\}$ of size $h(c)$. Put
$$b_\mu(I) = \det(X)^{\max(\mu_n, 0)} \prod_{\mu_n < c \leq \mu_1} \det X[\{1, \dots, h(c)\}, I_c],$$
the product of the minors with the first $h(c)$ rows and the columns $I_c$. The *canonical* choice $I^0$ has $I^0_c = \{1, \dots, h(c)\}$.

Lean: `Formalism.InvariantFactorPaths.ColumnFamilies.brkPol` (also `Formalism.InvariantFactorPaths.ColumnFamilies.canT`).

Let $\mathfrak{gl}_n$ act on $\mathbb{Q}[x]$ through the columns, $E_{ab} = \sum_i x_{ia}\, \partial/\partial x_{ib}$. The *Kostant monoid* $U_{\mathbb{Z}}$ is the monoid of operators generated by the divided powers $E_{ab}^k/k!$ for $a \neq b$ and by the binomials $\binom{E_{aa}}{k} = \frac{1}{k!}\prod_{j < k}(E_{aa} - j)$. The polynomial $v = b_\mu(I^0)$ has weight $\lambda$ with $\lambda_a = \mu_a + \max(-\mu_n, 0)$: column $a$ occurs in the minors with $c \leq \mu_a$ and in the power of the determinant.

**Definition 8.1.5 (Maximal lattice).** Let $V$ be a $\mathbb{Q}$-representation of $\mathfrak{gl}_n$, $\lambda$ a weight and $v \in V$ of weight $\lambda$. Then $\nabla_{\mathbb{Z}}(v)$ is the set of $x \in V$ such that for every $u \in U_{\mathbb{Z}}$ there is $c \in \mathbb{Z}$ with $u x - c v$ in the sum of the weight spaces of weights $\neq \lambda$.

Lean: `Formalism.InvariantFactorPaths.ColumnFamilies.Nabla` (also `Formalism.InvariantFactorPaths.ColumnFamilies.UZmon`).

So $x \in \nabla_{\mathbb{Z}}(v)$ when every Kostant word sends $x$ to a vector whose $\lambda$-component is an integer multiple of $v$. In an irreducible module of highest weight $\lambda$, this is the largest lattice that is stable under $U_{\mathbb{Z}}$ and meets the line $\mathbb{Q}v$ in $\mathbb{Z}v$.

**Theorem 8.1.6 (Bideterminant lattice).** Let $n \geq 1$ and $\mu$ dominant. Let $B_{\mathbb{Q}}$ be the $\mathbb{Q}$-span of the polynomials $b_\mu(I)$ over all column choices $I$. Then the $\mathbb{Z}$-span of the $b_\mu(I)$ is
$$\{ x \in B_{\mathbb{Q}} : x \in \nabla_{\mathbb{Z}}(b_\mu(I^0)) \},$$
for the action of $\mathfrak{gl}_n$ on the columns and the weight $\lambda$ above.

Lean: `Formalism.InvariantFactorPaths.ColumnFamilies.highest_weight_corollary_two`.

*Proof (outline).* Each $b_\mu(I)$ lies in $\nabla_{\mathbb{Z}}(v)$: a divided power $E_{ab}^k/k!$ sends a product of minors with integral coefficients to a sum of such products with integer coefficients, because it is the coefficient of $s^k$ in a column substitution. The $\lambda$-component of such a sum is an integer multiple of $v$, since $v$ spans the $\lambda$-weight space of $B_{\mathbb{Q}}$. For the converse let $x \in B_{\mathbb{Q}} \cap \nabla_{\mathbb{Z}}(v)$. The dual Weyl lattice over $\mathbb{Z}$ is spanned by the bideterminants of standard bitableaux (the standard basis theorem of De Concini, Eisenbud and Procesi), and these are among the $b_\mu(I)$ up to the power of the determinant. Pairing $x$ with the divided powers and evaluating at the identity matrix, where $b_\mu(I^0)(1) = 1$, shows that the coordinates of $x$ in this basis are integers. $\square$

**Remark 8.1.7 (Formalization).** The sandwich theorem is `SandwichLocal` in [StatementW.lean](lean:Formalism/ThetaLogCoordinates/SandwichModelDomains/StatementW.lean#L1), proved in [FinalW.lean](lean:Formalism/ThetaLogCoordinates/SandwichModelDomains/FinalW.lean#L50) through the forms over $\mathbb{Z}_p$, over $\mathbb{Z}$ and over a domain in which integers prime to $p$ are units. The proof over $\mathbb{Z}_p$ uses the lemmas `rowGlOne`, `rowGlDiv`, `swpWt`, `swpPol` and `swpInt`; we have not opened their proofs, and the outline of step 2 gives only the shape of the argument. The weight $\nu$ takes values in $\mathbb{N}$. The bideterminant theorem is `RationalBitableauLatticeStatement` in [StatementH.lean](lean:Formalism/ThetaLogCoordinates/DualWeylCoordinates/StatementH.lean#L15); its proof uses `bracket_mem_dualWeyl`, `dualWeyl_le_span_bracket` (from the standard basis theorem `dualWeyl_eq_span_tableauBideterminant`) and `eval_id_bracket_canonical`, whose proofs we have not opened. The exponent $\max(\mu_n, 0)$ of the determinant goes with the shift $\max(-\mu_n, 0)$ of the weight, so the statement is consistent for negative $\mu_n$. We have not unfolded the weight spaces past their definition as eigenspaces of the $E_{aa}$.
