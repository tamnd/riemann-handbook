---
title: Vanishing fibre integrals
decls:
  - GlobalTheory.CompanionTheory.BZPsiPG.FibKer.mem_twKer_of_fibInt_eq_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Vanishing fibre integrals

This section proves that a function in the product $\tau \times_0 \sigma$ of the previous section whose fibre integrals all vanish lies in the kernel of the untwisted coinvariants along the unipotent part $U$. The result is used in the computation of $\Psi(\tau \times \sigma)$, [Lemma 7.5.3](/entry/ker-le-tw-ker/), where it shows that the kernel of the map given by fibre integrals is no larger than the kernel of the coinvariants. The idea is to cut a function on the unipotent part into finitely many fibre functions on $k^t$, and to move a vanishing integral of a fibre function back to the function itself.

We keep the notation of the two previous sections: $G_n$, $P_n$, $U_n$, the vectors $u(y)$, the embedding $\iota$, the ring of integers $\mathcal{O}$, the group $H_{n,t}$ and the product $\tau \times_0 \sigma$.

### Fibre functions

Now let $n \geq 1$ and $t \geq 0$, let $\tau$ be a smooth representation of $P_n$ on $V$ and $\sigma$ a smooth representation of $G_t$ on $W$. Put $N = n + t$. A vector $y \in k^{N-1}$ splits as $y = (y', y'')$ with $y' \in k^{n-1}$ and $y'' \in k^t$, and for $v \in k^t$ we write $(0, v)$ for the vector with $y' = 0$ and $y'' = v$. Let $q : V \to V_{U_n,1}$ be the quotient map of the untwisted coinvariants of $\tau$ along $U_n$.

**Definition 1.7.1 (Fibre functions and fibre integrals).** For $f \in \tau \mathbin{\times_0} \sigma$ and $g \in G_{N-1}$, the *fibre function* is $\varphi_{f,g}(v) = f\big(u(0,v)\,\iota(g)\big)$ for $v \in k^t$, with values in $V \otimes W$. Given a Haar measure $\mu$ on $k^t$, the *fibre integral* is
$$I_\mu(f)(g) = (q \otimes 1)\int_{k^t} \varphi_{f,g}\,d\mu.$$

The fibre functions are locally constant with compact support (taken as given below), so the integral is a finite sum: $\int \varphi\,d\mu = \sum_z \mu(\varphi^{-1}(z))\,z$ over the nonzero values $z$ of $\varphi$.

**Theorem 1.7.2 (Vanishing fibre integrals).** Let $f \in \tau \mathbin{\times_0} \sigma$. If $I_\mu(f)(g) = 0$ for every $g \in G_{N-1}$, then $f$ lies in the span of the $u \cdot f' - f'$ with $u \in U_N$ and $f' \in \tau \mathbin{\times_0} \sigma$.

Lean: `GlobalTheory.CompanionTheory.BZPsiPG.FibKer.mem_twKer_of_fibInt_eq_zero`.

The conclusion says that $f$ maps to $0$ in $\Psi^-(\tau \mathbin{\times_0} \sigma)$. To prove it we let $U_N \cong k^{N-1}$ act on functions on $k^t$. Let $\rho_0(x) = \tau(u(x)) \otimes 1$ on $Z = V \otimes W$ for $x \in k^{n-1}$, and let $F$ be the space of locally constant functions $k^t \to Z$ with compact support, with
$$(y \cdot \varphi)(v) = \rho_0(y')\,\varphi(v + y''), \qquad y \in k^{N-1}.$$
For $c \in k^\times$ let $L_c = \{v \in k^t : cv_j \in \mathcal{O} \text{ for all } j\}$, a compact open subgroup, and write $1_{a + L_c}z$ for the function equal to $z$ on $a + L_c$ and $0$ elsewhere. Let $K_0 = \mathrm{GL}_{N-1}(\mathcal{O})$. For a group $A$ acting on a space $X$, write $X(A)$ for the span of the $a x - x$.

We take the following facts as given; they are proved elsewhere in the development.

**Theorem 1.7.3 (Facts on fibre functions).**
- (i) Each $\varphi_{f,g}$ lies in $F$, and the representations $\rho_0$ of $k^{n-1}$ and $F$ of $k^{N-1}$ are smooth.
- (ii) For $\kappa \in G_{N-1}$ and $y \in k^{N-1}$, $\varphi_{u(y)f,\kappa} = (\kappa y)\cdot\varphi_{f,\kappa}$.
- (iii) The set $\{\varphi_{f,\kappa} : \kappa \in K_0\}$ is finite.
- (iv) If $\varphi_{f,\kappa} = 0$ for all $\kappa \in K_0$, then $f = 0$.
- (v) If $(q \otimes 1)z = 0$, then $z \in Z(k^{n-1})$.
- (vi) Every $\varphi \in F$ is $L_c$-periodic for some $c$, and is then $\sum_{a \in A} 1_{a + L_c}\varphi(a)$ for a finite set $A$. For such a sum, $\int \sum_a 1_{a+L_c}z_a\,d\mu = \mu(L_c)\sum_a z_a$, and $\mu(L_c) \neq 0$.
- (vii) $1_{a + L_c}z - 1_{L_c}z \in F(k^{N-1})$, and $z \in Z(k^{n-1})$ implies $1_{L_c}z \in F(k^{N-1})$.
- (viii) If $\varphi \in F(L)$ for the lattice $L = \{y \in k^{N-1} : cy_j \in \mathcal{O}\}$ and $\kappa \in K_0$, then $\varphi$ also lies in the span of the $(\kappa y)\cdot\varphi' - \varphi'$ with $y \in L$. If finitely many vectors lie in $F(k^{N-1})$, they all lie in $F(L)$ for one such $L$.
- (ix) Let $L$ be a compact group acting smoothly on $X$, $x \in X(L)$, $K \leq L$ an open subgroup fixing $x$, and $R$ a set of representatives of $L/K$. Then $\sum_{r \in R} r\,x = 0$.

Property (ii) comes from $\iota(\kappa)u(y) = u(\kappa y)\iota(\kappa)$ and $u(\kappa y) = u((\kappa y)', 0)\,u(0, (\kappa y)'')$, where $u((\kappa y)',0)$ lies in $H_{n,t}$ and projects to $(u((\kappa y)'), 1)$. Property (ix) is the averaging over $L$ of a coinvariant relation.

**Lemma 1.7.4 (From the integral to the function).** If $\varphi \in F$ and $\int \varphi\,d\mu \in Z(k^{n-1})$, then $\varphi \in F(k^{N-1})$.

*Proof.* By (vi), $\varphi = \sum_{a \in A} 1_{a + L_c}\varphi(a)$ and $\int \varphi\,d\mu = \mu(L_c)\sum_a \varphi(a)$, so $z = \sum_a \varphi(a)$ lies in $Z(k^{n-1})$. Then
$$\varphi = \sum_{a \in A}\big(1_{a + L_c}\varphi(a) - 1_{L_c}\varphi(a)\big) + 1_{L_c}z,$$
and each term lies in $F(k^{N-1})$ by (vii). $\square$

**Lemma 1.7.5 (A finite sum).** Let $X$ be a smooth representation of $k^{N-1}$ and $x \in X$ a vector with these properties: for $\kappa \in K_0$ there are linear maps $F_\kappa : X \to F$ with $F_\kappa(yx') = (\kappa y)\cdot F_\kappa(x')$ for all $x'$; $x' = 0$ when all $F_\kappa(x') = 0$; each $F_\kappa(x)$ lies in $F(k^{N-1})$; and only finitely many $F_\kappa(x)$ occur. Then there is a finite nonempty set $R \subset k^{N-1}$ with $\sum_{y \in R} y\,x = 0$.

*Proof.* By (viii) there is a lattice $L$ with every $F_\kappa(x)$ in $F(L)$, and then in the span of the $(\kappa y)\cdot\varphi' - \varphi'$ with $y \in L$. The lattice $L$ is compact. Let $K \leq L$ be the stabilizer of $x$, which is open since $X$ is smooth, and so of finite index. Let $R$ be a set of representatives of $L/K$. For each $\kappa$, the group $L$ acting through $y \mapsto \kappa y$ fixes $F_\kappa(x)$ on $K$, because $F_\kappa(yx) = (\kappa y)\cdot F_\kappa(x)$. By (ix), $F_\kappa\big(\sum_{y \in R} y\,x\big) = \sum_{y \in R} (\kappa y)\cdot F_\kappa(x) = 0$ for all $\kappa \in K_0$, so $\sum_{y \in R} y\,x = 0$. $\square$

*Proof of the theorem.* Take $X = \tau \mathbin{\times_0} \sigma$ with $y$ acting by $u(y)$, which is smooth, and $F_\kappa(f') = \varphi_{f',\kappa}$. The maps intertwine by (ii), and they detect zero by (iv). For $\kappa \in K_0$ the hypothesis gives $(q \otimes 1)\int \varphi_{f,\kappa}\,d\mu = 0$, so by (v) and the first lemma, $\varphi_{f,\kappa} \in F(k^{N-1})$. By (iii) only finitely many fibre functions occur. The second lemma gives a finite nonempty $R$ with $\sum_{y \in R} u(y)f = 0$. Then
$$|R|\, f = \sum_{y \in R}\big(f - u(y)f\big),$$
and each term lies in the span of the $u \cdot f' - f'$. Dividing by $|R|$ proves the theorem. $\square$

Only the $g \in K_0$ were used, so the hypothesis could be weakened to $I_\mu(f)(\kappa) = 0$ for $\kappa \in K_0$.

**Remark 1.7.6 (Formalization).** The fibre theorem is in [MemTwKerOfFibIntEqZero.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MemTwKerOfFibIntEqZero.lean#L176), under `maxHeartbeats 1000000`; the first lemma is `mem_twKer_fibAct` (L121), the second is `exists_sum_eq_zero_abs` (L81) with representatives from `exists_reps` (L55), and the last step is `mem_twKer_of_sum` (L38). Fibre functions and fibre integrals are `fibV` and `fibInt` in [ExistsUMOfMem.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsUMOfMem.lean#L88), the space $F$ with its action, $\rho_0$, $L_c$ and the cosets are `fibM`, `fibAct`, `topRep`, `Lc` and `cosetSet` in [IsCompactCosetSet.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsCompactCosetSet.lean#L40), and the integral is the finite sum `smInt` in [OpenFns.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/OpenFns.lean#L77). The facts (i) to (ix) are the inputs `fibre_function_locally_constant_compact`, `smooth_top_representation`, `smooth_fibre_action`, `fibre_function_unipotent_action`, `finite_fibre_functions_compact`, `induced_vanishing_on_compact`, `closure_kernel_mem_jacquet_kernel`, `exists_lattice_periodicity`, `locally_constant_coset_indicator_sum`, `integral_coset_indicator_sum`, `haar_measure_coset_ne_zero`, `coset_function_translate_jacquet_kernel`, `coset_function_jacquet_kernel`, `jacquet_kernel_lattice_conj_compact`, `finite_jacquet_kernel_common_lattice` and `sum_over_compact_cosets_jacquet_kernel`; we read their statements only. The Lean hypothesis asks for vanishing at every $g \in G_{N-1}$, though the proof only uses $g \in K_0$.
