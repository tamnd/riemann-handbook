---
title: The Poincaré-Lelong formula without conjugation invariance
decls:
  - GlobalTheory.CompanionTheory.Ar.Tw.Main.poincareLelong_of_inv
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Poincaré-Lelong formula without conjugation invariance

The arithmetic intersection numbers of the next section are built from an integrated Poincaré-Lelong formula. The formula in the literature is stated for metrics that are invariant under complex conjugation, since the complex points of a variety over $\mathbb{Q}$ carry that involution. This section removes the invariance. We twist the variety by an imaginary quadratic field. The complex points of the twist are two copies of the old ones, swapped by conjugation, and on the twist any metric can be made invariant. Both sides of the formula double, and we divide by $2$.

### Arithmetic varieties in products of projective spaces

We use the words of the heights chapter, see [Poincaré-Lelong on leaves](/entry/poincare-lelong-of-leaves/). Let $K$ be a finite set of blocks with a finite set $\iota_k$ of coordinates for each $k \in K$, and let $R = \mathbb{Z}[x_{k,i}]$, graded by $\mathbb{Z}^K$. An arithmetic variety of dimension $d$ is a multihomogeneous relevant prime $P \subset R$ with $P \cap \mathbb{Z} = 0$ and $\dim R/P = d + \lvert K\rvert$. Its complex points $X(\mathbb{C})$ lie in $\prod_k \mathbb{P}^{\iota_k}(\mathbb{C})$. A hermitian line $A$ has a multidegree $a \in \mathbb{Z}^K$ and a metric $h_A$ on the cones. A section of $A$ on $P$ is a form $s \notin P$ of degree $a$, and $\log\lVert s\rVert_A$ is a function on $X(\mathbb{C})$. A prime $W \supseteq P + (s)$ is horizontal if $W \cap \mathbb{Z} = 0$. For smooth lines $L_1, \dots, L_n$ let $\omega_L$ be the product of their Chern forms $dd^c \log h_{L_j}$, and for a function $f$ write $\int_{X(\mathbb{C})} f \, dd^c\log h_B\, \omega_L$ for the integral against the mixed form.

**Definition 10.13.1.** The arithmetic Poincaré-Lelong formula holds for $(P, L, A, B, s)$ if
$$
\begin{aligned}
\int_{X(\mathbb{C})} \log\lVert s\rVert_A \, dd^c \log h_B\, \omega_L
&= \sum_{W} m_W \int_{W(\mathbb{C})} \log h_B \, \omega_L \\
&\quad - \int_{X(\mathbb{C})} \log h_B \, dd^c \log h_A\, \omega_L ,
\end{aligned}
$$
where $W$ runs over the horizontal minimal primes of $P + (s)$ and $m_W$ is the length of $R/(P + (s))$ at $W$.

Here $P$ has dimension $n + 2$, the lines $L_1, \dots, L_n$, $A$, $B$ are smooth, $B$ has degree $0$ so that $\log h_B$ is a function on $X(\mathbb{C})$, and $s$ is a section of $A$ on $P$. A line is conjugation invariant if $h(\bar z) = h(z)$.

### The twist

Let $p$ be a prime. Add a block with two coordinates $x, y$ and put $q_p = x^2 + p y^2$. For an ideal $W \subseteq R$ the twist is
$$
W^{(p)} = W R[x, y] + (q_p).
$$
We say that $p$ has no root on $W$ if $a^2 + p b^2 \in W$ implies $b \in W$. For a prime $W$ this says that $-p$ is not a square in the fraction field of $R/W$.

The conic $q_p = 0$ in $\mathbb{P}^1$ has the two complex points $v_\pm = (\pm i\sqrt p : 1)$, and conjugation swaps them. So $X^{(p)}(\mathbb{C}) = X(\mathbb{C}) \times \{v_+, v_-\}$, and conjugation maps the sheet at $v_+$ to the sheet at $v_-$. Let
$$
\chi(x, y) = \frac12 + \frac{p + 1}{2\sqrt p} \cdot \frac{\operatorname{Im}(x \bar y)}{\lvert x\rvert^2 + \lvert y\rvert^2}.
$$
This is a smooth function on $\mathbb{P}^1(\mathbb{C})$ with $\chi(v_+) = 1$ and $\chi(v_-) = 0$. For a hermitian line $A$ define the twisted line $A^{(p)}$ with the same degree, degree $0$ on the new block, and
$$
\log h_{A^{(p)}}(z, u) = \chi(u) \log h_A(z) + (1 - \chi(u)) \log h_A(\bar z).
$$

**Lemma 10.13.2 (Twist).** Let $p$ be a prime and $W$ a horizontal prime on which $p$ has no root.

1. If $W$ is an arithmetic variety of dimension $d$, so is $W^{(p)}$.
2. If $A$ is smooth, then $A^{(p)}$ is smooth and conjugation invariant.
3. For smooth lines $L_1, \dots, L_e$, a smooth line $A$ and a section $s$ of $A$ on $W$,
$$
\int_{W^{(p)}(\mathbb{C})} \log\lVert s\rVert_{A^{(p)}} \, \omega_{L^{(p)}} = 2 \int_{W(\mathbb{C})} \log\lVert s\rVert_A \, \omega_L .
$$

*Proof.* For part 1, the ring $R[x,y]/W^{(p)}$ is $(R/W)[x,y]/(x^2 + p y^2)$. Since $-p$ is not a square in the fraction field of $R/W$, the polynomial $x^2 + p y^2$ stays irreducible there, so the twist is prime. The new block adds two variables and one equation, so the dimension grows by one, which is the one new block. The twist meets $\mathbb{Z}$ in $0$. For part 2, $\chi$ is smooth, and conjugation sends $(z, v_\pm)$ to $(\bar z, v_\mp)$ and $\chi$ to $1 - \chi$ on the conic. For part 3, the integral over $X^{(p)}(\mathbb{C})$ is the sum of the integrals over the two sheets. On the sheet at $v_+$ the twisted metrics are the old ones. On the sheet at $v_-$ they are the old ones composed with conjugation, and conjugation preserves the integral. $\square$

Only finitely many primes have a root on a given horizontal prime $W$. Indeed, if $-p$ is a square in the fraction field $F$ of $R/W$, then $\sqrt{-p}$ lies in the algebraic closure of $\mathbb{Q}$ in $F$, which is a number field, and a number field contains $\sqrt{-p}$ for only finitely many $p$.

### The theorem

**Theorem 10.13.3 (Poincaré-Lelong without invariance).** Assume resolution of singularities in characteristic $0$. Assume that the arithmetic Poincaré-Lelong formula holds whenever $L_1, \dots, L_n$, $A$ and $B$ are conjugation invariant. Then it holds for all $(P, L, A, B, s)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Tw.Main.poincareLelong_of_inv`.

*Proof.* Step 1: integrability. Resolution of singularities makes the integrals over complex points finite and independent of the choice of charts. We use this in each application of the twist lemma.

Step 2: choose a prime. Let $H$ be the finite set of horizontal minimal primes of $P + (s)$. Each $W \in H$ is an arithmetic variety of dimension $n + 1$. By the remark above, there is a prime $p$ that has no root on $P$ and on every $W \in H$.

Step 3: the invariant formula on the twist. By the twist lemma, $P^{(p)}$ is an arithmetic variety of dimension $n + 2$, the lines $L_j^{(p)}$, $A^{(p)}$ and $B^{(p)}$ are smooth and conjugation invariant, $B^{(p)}$ has degree $0$, and $s$ is a section of $A^{(p)}$ on $P^{(p)}$. So the invariant formula holds for $(P^{(p)}, L^{(p)}, A^{(p)}, B^{(p)}, s)$.

Step 4: the left side doubles. Part 3 of the twist lemma, with the lines $B, L_1, \dots, L_n$, gives that the left side on the twist is twice the left side on $P$.

Step 5: the last term doubles. View $\log h_B$ as $\log\lVert 1\rVert$ for the constant section $1$ of the inverse line of $B$, which has degree $0$. Part 3 of the twist lemma with the lines $A, L_1, \dots, L_n$ gives that the last term on the twist is twice the last term on $P$.

Step 6: the divisor sum doubles. We have $P^{(p)} + (s) = (P + (s)) R[x,y] + (q_p)$. The horizontal minimal primes of this ideal are the twists $W^{(p)}$ for $W \in H$, and $W \mapsto W^{(p)}$ is injective. The length at $W^{(p)}$ equals the length $m_W$ at $W$, since $W^{(p)}$ is prime. Part 3 of the twist lemma on $W$, again with the inverse line of $B$ and the section $1$, gives that the integral over $W^{(p)}(\mathbb{C})$ is twice the integral over $W(\mathbb{C})$. So the sum on the twist is twice the sum on $P$.

Step 7: divide. By Steps 3 to 6, twice the left side on $P$ equals twice the right side on $P$. Divide by $2$. $\square$

The trick works since the twist changes no intersection theoretic data: the multiplicities, the horizontal components and the integrals all match up to the factor $2$, which is the degree of $\mathbb{Q}(\sqrt{-p})$ over $\mathbb{Q}$.

**Remark 10.13.4 (Formalization).** The theorem is at `Development/AutomorphicSpectrum/Proofs/MetricProofs/PoincareLelongOfInv.lean:262`. The invariant formula is the hypothesis `PoincareLelongInv` in `Development/AutomorphicSpectrum/PublishedTheorems/Metrics₂/PoincareLelongInv.lean:9`, and the conclusion is `ArithmeticPoincareLelongFormula` (`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterSt.lean:76`). The twist, the quadric $q_p$ and the condition "no root" are in `IsHorizontalTwist.lean` (lines 31 to 36), and $\chi$ is `chi` at line 91 of that file. The choice of the prime is `exists_prime_noRoot` (`PoincareLelongOfInv.lean:29`) and the doubling is `twist_double` (line 196). The new block has index `none` of `Option K`, and the twisted section is the image of $s$ under the renaming `inc`. The first hypothesis is resolution in the Hironaka form; it enters only through integrability and independence of charts (`ptsIntegrable_of_resK`, `ptsIndep_of`).
