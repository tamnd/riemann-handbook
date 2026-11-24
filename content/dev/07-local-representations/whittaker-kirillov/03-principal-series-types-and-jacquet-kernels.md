---
title: Principal series types and Jacquet kernels
decls:
  - GlobalTheory.T.eq_zero_of_mem_twistedJacquetKernel_upperUnitriangular
  - GlobalTheory.PsType.eq_zero_of_mem_twKer_unipB
  - GlobalTheory.PsType.subquotient_prinSeries_of_hasVec
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Principal series types and Jacquet kernels

This section proves that an irreducible smooth representation of $\mathrm{GL}_n(F)$ that contains a vector of a given principal series type is a subquotient of a principal series. The type is a character $\theta_\psi$ of a compact open subgroup $J_\psi \subset \mathrm{GL}_n(\mathcal{O})$, built from $n$ characters $\psi_1, \dots, \psi_n$ of $F^\times$. The main step says that a $\theta_\psi$-eigenvector never lies in the kernel of the Jacquet module for the Borel subgroup. The result is used in [Theorem](/entry/toral-of-lower/), where the inertia eigenvalues of a local component are read off from its type. For the background, see [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module), [unramified representations](/learn/representations/#unramified-representations) and [depth-zero representations and types](/learn/representations/#depth-zero-representations-and-types).

### Ordered families of characters

Let $F$ be a non-archimedean [[local field|J85FZEQG38]] with ring of integers $\mathcal{O}$ and absolute value $|\cdot|$. Let $G = \mathrm{GL}_n(F)$ and $K = \mathrm{GL}_n(\mathcal{O})$. A character $\chi \colon F^\times \to \mathbb{C}^\times$ is *smooth* if its kernel is open.

**Definition 4.3.1 (Triviality to a depth).** Let $\chi$ be a character of $F^\times$ and $x \in F$. We say that $\chi$ is *trivial to depth* $x$ if $\chi(u) = 1$ for every unit $u \in \mathcal{O}^\times$ with $|u - 1| \leq |x|$.

So $\chi$ is trivial to depth $1$ if and only if $\chi$ is trivial on $\mathcal{O}^\times$, and $\chi$ is trivial to depth $0$ for every $\chi$. A smooth character is trivial to depth $x$ for all $x$ with $|x|$ small enough.

**Definition 4.3.2 (Ordered family).** A family $\psi = (\psi_1, \dots, \psi_n)$ of characters of $F^\times$ is *ordered* if, for all $i \leq a \leq b \leq j$ and all $x \in F$, the character $\psi_i/\psi_j$ trivial to depth $x$ implies $\psi_a/\psi_b$ trivial to depth $x$.

In words, the conductor of $\psi_a/\psi_b$ is at most the conductor of $\psi_i/\psi_j$ when the interval $[a, b]$ lies inside $[i, j]$. For example, a family of unramified characters is ordered, and so is a constant family.

**Definition 4.3.3 (Principal series type).** Let $\psi$ be a family of characters of $F^\times$. Put
$$J_\psi = \{ g \in K : \psi_i/\psi_j \text{ is trivial to depth } g_{ij} \text{ for all } i < j \}.$$
For a character $\chi$ and $x \in F$, put $e_\chi(x) = \chi(x)$ if $|x| = 1$ and $e_\chi(x) = 1$ otherwise. Put $\psi_{n+1} = 1$. For $g \in G$ and $1 \leq m \leq n$, let $\Delta_m(g)$ be the determinant of the upper left $m \times m$ block of $g$. Define
$$\theta_\psi(g) = \prod_{m=1}^{n} e_{\psi_m/\psi_{m+1}}\big(\Delta_m(g)\big).$$

For a diagonal matrix $t$ with unit entries, $\Delta_m(t) = t_1 \cdots t_m$, and the product telescopes to $\theta_\psi(t) = \psi_1(t_1) \cdots \psi_n(t_n)$. So $\theta_\psi$ extends the character $\psi_1 \otimes \cdots \otimes \psi_n$ of the torus $T(\mathcal{O})$. When all $\psi_i$ are unramified, $J_\psi = K$ and $\theta_\psi = 1$. Then a $\theta_\psi$-eigenvector is a spherical vector.

**Definition 4.3.4 (Eigenvector of type $\psi$).** Let $(\pi, V)$ be a representation of $G$. A vector $v \in V$ is a $\theta_\psi$-*eigenvector* if $\pi(g)v = \theta_\psi(g) v$ for all $g \in J_\psi$. The representation *contains the type* $\psi$ if it has a nonzero $\theta_\psi$-eigenvector.

**Definition 4.3.5 (Agreement on units).** Two families $\psi$ and $\omega$ *agree on units* if $\psi_i(u) = \omega_i(u)$ for all $i$ and all $u \in \mathcal{O}^\times$.

**Definition 4.3.6 (Cut).** Let $0 < r < n$. The family $\psi$ is *cut at* $r$ if $\psi_i/\psi_j$ is nontrivial on $\mathcal{O}^\times$ for all $i \leq r < j$.

For an ordered family, one of two things holds: either all the $\psi_i$ agree on units with one smooth character $\chi$, or the family is cut at some $r$ with $0 < r < n$. Indeed, if $\psi_1/\psi_n$ is trivial on units, the ordering makes every $\psi_a/\psi_b$ trivial on units. Otherwise, take $r$ to be the last index with $\psi_1/\psi_r$ trivial on units; the ordering then gives the cut.

### Jacquet kernels

Let $B$ be the upper triangular Borel subgroup, $N$ its unipotent radical and $T$ the diagonal torus. For a subgroup $U$ of $G$ and a representation $(\pi, V)$, the *Jacquet kernel* $V(U)$ is the span of the vectors $\pi(u)w - w$ with $u \in U$ and $w \in V$. The quotient $V_U = V/V(U)$ is the *Jacquet module*.

**Theorem 4.3.7 (Eigenvectors leave the Jacquet kernel).** Let $(\pi, V)$ be a smooth representation of $G$. Let $\psi$ be an ordered family of smooth characters of $F^\times$. If $v \in V(N)$ is a $\theta_\psi$-eigenvector, then $v = 0$.

Lean: `GlobalTheory.PsType.eq_zero_of_mem_twKer_unipB` (also `GlobalTheory.T.eq_zero_of_mem_twistedJacquetKernel_upperUnitriangular`).

No irreducibility and no admissibility are assumed.

*Proof.* We argue by strong induction on $n$. By the dichotomy above there are two cases.

Constant case. The family agrees on units with one smooth character $\chi$. The group $J_\psi$ and the character $\theta_\psi$ depend only on the restrictions of the $\psi_i$ to $\mathcal{O}^\times$, so we may take $\psi_i = \chi$ for all $i$. Then $J_\psi = K$ and $\theta_\psi(g) = \chi(\det g)$ on $K$. Twist: put $\pi'(g) = \chi(\det g)^{-1}\pi(g)$. This is smooth, and $\pi' = \pi$ on $N$ since $\det u = 1$ there, so $v$ lies in the Jacquet kernel of $\pi'$. Now $v$ is fixed by $K$ under $\pi'$. A $K$-fixed vector of a smooth representation never lies in the Jacquet kernel $V(N)$ unless it is zero. So $v = 0$.

Cut case. The family is cut at $r$, with $0 < r < n$. Put $t = n - r$. Let $P = MU$ be the standard parabolic subgroup with Levi $M = \mathrm{GL}_r \times \mathrm{GL}_t$ and unipotent radical $U$. Let $\rho$ be the representation of $M$ on the Jacquet module $V_U$. Write $\psi' = (\psi_1, \dots, \psi_r)$ and $\psi'' = (\psi_{r+1}, \dots, \psi_n)$. Both are ordered. The cut gives three facts. First, $J_\psi \cap M = J_{\psi'} \times J_{\psi''}$. Second, $\theta_\psi(a, b) = \theta_{\psi'}(a)\,\theta_{\psi''}(b)$ on this group. Third, $\theta_{\psi'}$ and $\theta_{\psi''}$ equal $1$ at the identity.

The group $N$ is the product of $U$ with the group $N_r \times N_t$ of the Levi. So the Jacquet kernel of $N$ maps into the sum of the Jacquet kernels of $\rho$ for $N_r \times 1$ and for $1 \times N_t$. The image $\bar v$ of $v$ in $V_U$ is an eigenvector of $\rho$ for $J_{\psi'} \times 1$ with character $\theta_{\psi'}$, and for $1 \times J_{\psi''}$ with character $\theta_{\psi''}$, by the two product formulas. The induction hypothesis holds for $\mathrm{GL}_r$ and $\mathrm{GL}_t$ and for every smooth representation of these groups. A vector of a representation of $G_1 \times G_2$ that is an eigenvector for both factors and lies in the sum of the two kernels is then zero: restrict to one factor at a time. So $\bar v = 0$, and $v$ lies in the Jacquet kernel $V(U)$.

It remains to show that a $\theta_\psi$-eigenvector in $V(U)$ is zero when $\psi$ is cut at $r$. Fix a uniformizer $\varpi$, and let $z$ be the diagonal matrix with entries $\varpi$ in the first $r$ places and $1$ in the others. For $m \geq 0$ let $U_m$ be the set of $u \in U$ whose block entries $x = u_{ij}$, with $i \leq r < j$, satisfy $|\varpi^m x| \leq 1$ and $\psi_i/\psi_j$ trivial to depth $\varpi^m x$. These sets are compact open subgroups. They increase with $m$, and their union is $U$, because each $\psi_i/\psi_j$ is smooth. A vector of $V(U)$ is then in the span of the vectors $\pi(u)w - w$ with $u \in U_m$, for some finite $m$. Conjugation by $z$ moves $U_{m+1}$ into $U_m$, and $U_0 \subset J_\psi$ with $\theta_\psi = 1$ on $U_0$. The cut gives two facts. An element of $K$ outside $J_\psi$ does not intertwine $\theta_\psi$. And every $j \in J_\psi z J_\psi$ can be cleared in its upper right block by an element of $U_0$. With these facts, an eigenvector in the span for $U_m$ is in the span for $U_{m-1}$, and so on down to $U_0$, where $\pi(u)w - w$ is killed by the projection onto the $\theta_\psi$-isotypic part. So $v = 0$. $\square$

### The principal series

For a family $\omega = (\omega_1, \dots, \omega_n)$ of smooth characters of $F^\times$, let $\mathrm{Ind}(\omega)$ be the representation of $G$ induced from the character $\omega_1 \otimes \cdots \otimes \omega_n$ of $T$, extended to $B$ trivially on $N$, with the normalization by $\delta_B^{1/2}$. A representation $\pi$ is a *subquotient* of $\mathrm{Ind}(\omega)$ if there are subrepresentations $W' \subset W$ of $\mathrm{Ind}(\omega)$ with $W/W' \cong \pi$.

We take the following results of Bernstein and Zelevinsky as given.

**Theorem 4.3.8 (Bernstein-Zelevinsky finiteness).** Let $F$ be a non-archimedean local field. Then: every irreducible smooth representation of $\mathrm{GL}_n(F)$ is admissible; the Jacquet module of a smooth representation of finite length, for any standard parabolic subgroup, has finite length; parabolic induction from a standard Levi subgroup preserves finite length; and the contragredient of a parabolically induced representation is the induced representation of the contragredient, through the pairing $\langle f', f \rangle = \int_{K} f'(x)(f(x))\,dx$.

This is Bernstein-Zelevinsky, Ann. Sci. ENS 10 (1977), §2, and Russian Math. Surveys 31 (1976), §3.

**Theorem 4.3.9 (Subquotients of principal series).** Assume Bernstein-Zelevinsky finiteness. Let $\pi$ be an irreducible smooth representation of $G$. Let $\psi$ be an ordered family of smooth characters of $F^\times$, and assume that $\pi$ contains the type $\psi$. Then there is a family $\omega$ of smooth characters of $F^\times$ that agrees with $\psi$ on units such that $\pi$ is a subquotient of $\mathrm{Ind}(\omega)$.

Lean: `GlobalTheory.PsType.subquotient_prinSeries_of_hasVec`.

*Proof.* Let $v \neq 0$ be a $\theta_\psi$-eigenvector. Let $\pi_N$ be the normalized Jacquet module of $\pi$, a representation of $T$. Since $\pi$ is irreducible, it has finite length, so $\pi_N$ has finite length by Bernstein-Zelevinsky finiteness. The image $\bar v$ of $v$ in $\pi_N$ is nonzero by [Theorem 4.3.7](/entry/eq-zero-of-mem-twisted-jacquet-kernel-upper-unitriangular/). For $t \in T(\mathcal{O})$, the matrix $t$ lies in $J_\psi$, since its off-diagonal entries are $0$ and every character is trivial to depth $0$. So $\pi(t)v = \theta_\psi(t)v = \psi_1(t_1)\cdots\psi_n(t_n)\,v$. The modulus character $\delta_B^{1/2}$ is $1$ on $T(\mathcal{O})$. Hence $T(\mathcal{O})$ acts on $\bar v$ by the character $\psi_1 \otimes \cdots \otimes \psi_n$. A smooth representation of $T$ of finite length with such a vector has a nonzero linear form $l$ and a family $\omega$ of characters with $l(\pi_N(t)y) = \omega_1(t_1)\cdots\omega_n(t_n)\,l(y)$ for all $t \in T$, where $\omega_i = \psi_i$ on $\mathcal{O}^\times$. To see this, note that $T/T(\mathcal{O}) \cong \mathbb{Z}^n$ acts on the $\psi$-isotypic part for $T(\mathcal{O})$, which is a nonzero direct summand of finite length; a simple quotient of it is a character of $\mathbb{Z}^n$. Each $\omega_i$ is smooth because it agrees with the smooth $\psi_i$ on the open subgroup $\mathcal{O}^\times$. By [[Frobenius reciprocity|PAP76H0ND9]] for the Jacquet module, the nonzero $T$-map $l \colon \pi_N \to \omega$ gives a nonzero map $\pi \to \mathrm{Ind}(\omega)$, which is injective since $\pi$ is irreducible. So $\pi$ is a subquotient of $\mathrm{Ind}(\omega)$. $\square$

In the classical form, this says that the irreducible representations with a principal series type are exactly the irreducible subquotients of the principal series in the corresponding Bernstein component. For unramified $\psi$ it is the theorem of Borel and Casselman that a representation with a vector fixed by $\mathrm{GL}_n(\mathcal{O})$ is a subquotient of an unramified principal series.

**Remark 4.3.10 (Formalization).** The finiteness theorem of Bernstein and Zelevinsky is taken as a hypothesis of the second theorem, a conjunction of four statements in [HasFiniteLengthOfIsIrreducible.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/HasFiniteLengthOfIsIrreducible.lean#L49); only the clause on Jacquet modules is used. The first theorem has a wrapper whose file name is truncated: `EqZeroOfMemTwistedJacquetKernelUpperUnitriangulaStatement.lean`; the wrapper is proved by `first | exact` at line 7, under `maxHeartbeats 1000000`. The two-stage reduction to a maximal parabolic is proved in full; the last step, the chain argument through the strips $U_m$, is `eigenvector_eq_zero_of_mem_twistedSpan_chain`, which we read only as a statement. The constant case uses `spherical_vector_not_in_borel_jacquet_kernel`, and the torus step uses `TorusEigenform.main`; both were read only as statements. The definitions of $J_\psi$ and $\theta_\psi$ are in `OrderedConst.lean`, lines 38 to 51.
