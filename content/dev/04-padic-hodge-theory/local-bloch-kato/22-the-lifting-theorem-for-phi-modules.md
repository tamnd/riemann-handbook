---
title: The lifting theorem for phi-modules
decls:
  - GlobalTheory.T.liftingTheorem_phiModules_exact_triple
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The lifting theorem for $\varphi$-modules

Let $D_0 \xrightarrow{F} D_1 \xrightarrow{G} D_2$ be an exact triple of Breuil-Kisin data. This section proves that a vector of $D_2$ with monodromy class $0$, times an explicit power $\ell^k$, is the image under $G$ of a vector of $D_1$ with monodromy class $0$. The proof first lifts the vector with [the theorem on the cokernel](/entry/cokernel-lattice-map-killed-by-prime-pow-main/), and then corrects the lift by the image of a vector of $D_0$, so that its monodromy class becomes $0$. The theorem is Step 4 of the proof of [the theorem on lifting along surjections](/entry/lift-f-of-is-good/).

We keep the notation of [the section on lifting](/entry/lift-f-of-is-good/) and of [the previous section](/entry/kills-coker-l/). In particular $\ell$ is a prime, $e + 1 = \ell^a$, $L$ is a finite extension of $\mathbb{Q}_\ell$ with tame descent data, $E = X^e + \ell$, the numerical conditions and the period $r = r(\Sigma)$ are as before, and $\rho = 2(N - 1) r$. For a Breuil-Kisin datum $D$ of heights $(\eta, H)$ we use the lattices $M_\eta$, $M^\Delta$, $Y_\eta$ and $Y'_\eta = X^e Y_\eta$ of the previous section.

**Definition 7.22.1 (The quotient by the disc).** Let $D$ be a Breuil-Kisin datum. Let $V$ be the $L$-vector space of all vectors $v = (v_\tau)_{\tau \in \mathbb{Z}/a}$ with $v_\tau \in L[[X]]^\iota$. Put $\Pi = V / M_R$, with quotient map $v \mapsto [v]$, and $\Pi_\eta = \{ [v] : E^\eta v \in M_R \}$. The descent datum acts on $\Pi$, and we write $\Pi^\Delta$ for the fixed classes. Put
$$Z_\eta = \{ [y] : y \in M_\eta \} \cap \Pi^\Delta, \qquad Z_\eta[1/\ell] = \Pi_\eta \cap \Pi^\Delta.$$
So $Z_\eta$ is an $\mathcal{O}$-module and $Z_\eta[1/\ell]$ is an $L$-vector space that contains it. Since $E N(M_R) \subseteq M_R$, the operator $E N$ induces an $L$-linear map $\Lambda$ of $\Pi$, $\Lambda [v] = [E N v]$.

**Definition 7.22.2 (Monodromy class).** The *monodromy class* of a vector $y \in V$ is
$$\mathrm{Mon}(y) = [E N y - E \zeta(y)] \in \Pi,$$
where $\zeta(y) = -\sum_{j \ge 1} (\ell \varphi)^j N y$ is the correction term of [the section on lifting](/entry/lift-f-of-is-good/), the sum taken as a limit coefficient by coefficient. It is $L$-linear in $y$. A map of Breuil-Kisin data $F$ induces a map of the quotients, also written $F$, and $F(\mathrm{Mon}(y)) = \mathrm{Mon}(F y)$.

The monodromy class measures how far $y$ is from giving a crystalline cocycle: by [the theorem on Galois classes](/entry/galois-class-of-monodromy-eq-zero/), a vector with monodromy class $0$ has a Galois class. This is why the theorem below asks for monodromy class $0$ on both sides.

Let $D$ be a Breuil-Kisin datum, $U \subseteq \mathbb{Z}$ finite and $\eta \ge 1$. Put $U + [1, \eta] = \{ i + k : i \in U, 1 \le k \le \eta \}$ and
$$R_U(T) = \prod_{n \in (U + [1, \eta]) \setminus \{0\}} (T - n e \ell) \in \mathbb{Z}[T].$$
Let $\Lambda_Z$ be the restriction of $\Lambda$ to $Z_\eta[1/\ell]$; this space is stable under $\Lambda$. We say that $D$ satisfies the *image condition* for $U$ if (1) every $w$ in the image of $\Lambda_Z$ satisfies $R_U(\Lambda_Z) w = 0$ and $R_U(0)\, w = -\Lambda_Z\big(R_{U,1}(\Lambda_Z) w\big)$, where $T R_{U,1}(T) = R_U(T) - R_U(0)$, and (2) every subspace $W$ of $Z_\eta[1/\ell]$ with $\Lambda_Z W \subseteq W$ satisfies $\Lambda_Z(Z_\eta[1/\ell]) \cap W = \Lambda_Z(W)$. In words, $\Lambda_Z$ acts on its image through the eigenvalues $n e \ell$, and its image meets each stable subspace in the image of that subspace.

We take the following results as given. They are proved in other parts of the development, and we read their statements, not their proofs. In all of them $L$ is complete.

**Theorem 7.22.3 (Bounds for the period).** Let $\ell$ be prime, $a \ge 1$, $e + 1 = \ell^a$, and $\Sigma \subseteq \mathbb{Z}/e$ with $\ell \Sigma \subseteq \Sigma$, $0 \in \Sigma$, $|\Sigma| \le N$ and $N \ge 2$. Then $1 \le r(\Sigma)$, $4 r(\Sigma) \le N^2$, and every $c \in \Sigma$ has least period at most $r(\Sigma)$ under $x \mapsto \ell x$.

**Theorem 7.22.4 (Size of the prime).** Let $2 \le N$, $1 \le \eta < H$, $4 r \le N^2$ and $40(H N^2 + N^3) < \ell$. Then $10 H + 2 \le \ell$, $14 H + (N + 2)\eta < \ell$, $(r + 2) \eta < \ell + 1$, and three more inequalities hold.

**Theorem 7.22.5 (A power of $\ell$ makes the class integral).** Let $D$ be a Breuil-Kisin datum of heights $(\eta, H)$ with $1 \le \eta < H$, $14 H < \ell$, $10 H + 2 \le \ell$ and $\ell \ne 2$. Let $r \ge 1$ be such that every character of $D$ has least period at most $r$, and $(r + 2)\eta < \ell + 1$. Then for $y \in Y'_\eta$ and $m \in M^\Delta$,
$$\ell^{\eta(r + 1)} \mathrm{Mon}\big(y + \varphi(m)\big) \in Z_\eta.$$

**Theorem 7.22.6 (Exact triples on the quotient).** Let $D_0 \xrightarrow{F} D_1 \xrightarrow{G} D_2$ be an exact triple of Breuil-Kisin data of heights $(\eta, H)$. Then the jumps of $D_0$ are jumps of $D_1$, the characters of $D_0$ are characters of $D_1$, $F$ is injective on $\Pi$, and for every $n \ge 0$ the following holds: if $\ell^n$ kills the cokernel of $G$ from $M$ to $M$, then for every $w \in Z_\eta(D_1)$ with $G w = 0$ there is $w_0 \in Z_\eta(D_0)$ with $F w_0 = \ell^n w$.

**Theorem 7.22.7 (Invariant vectors).** Let $D$ be a Breuil-Kisin datum and let $y$ be a vector fixed by $\Delta$ with $\ell^n y \in Y_\eta$ for some $n$. Then $\mathrm{Mon}(y) = \Lambda w$ for some $w \in Z_\eta[1/\ell]$.

**Theorem 7.22.8 (Image condition).** Let $D$ be a Breuil-Kisin datum, $U$ finite and $N \ge 0$, with jumps of $D$ in $U$, $U \subseteq [-\eta, H]$, $|U| \le N + 1$ and $\eta < H$. Then $D$ satisfies the image condition for $U$.

**Theorem 7.22.9 (Lifting through $\Lambda$).** Let $F : D_0 \to D_1$ be a map of Breuil-Kisin data, and assume that $D_1$ satisfies the image condition for $U$. Let $\omega = \Lambda w_1$ with $w_1 \in Z_\eta[1/\ell](D_1)$, and assume that $F w_0 = \ell^c \omega$ for some $c \ge 0$ and $w_0 \in Z_\eta[1/\ell](D_0)$. Then $F(\Lambda w) = \omega$ for some $w \in Z_\eta[1/\ell](D_0)$.

**Theorem 7.22.10 (Integral representatives).** Let $D$, $U$ and $N$ be as in the image condition theorem, and assume also $H + \eta < \ell$ and $10 H + 2 \le \ell$. Let $c \ge 0$ and $w \in Z_\eta[1/\ell]$ with $\ell^c \Lambda w \in Z_\eta$. Then there is $y \in Y'_\eta$ with
$$\Lambda [y] = \ell^{c + \eta + (N + 1)\eta}\, \Lambda w.$$

**Theorem 7.22.11 (Monodromy of integral vectors).** Let $D$, $U$ and $N$ be as in the image condition theorem, and assume also $1 \le \eta$, $14 H + (N + 2)\eta < \ell$ and $10 H + 2 \le \ell$. Assume that $Y'_\eta$ is $\ell$-adically complete and that $Z_\eta$ is $\ell$-adically separated. Then for every $y \in Y'_\eta$ there is $y_0 \in Y'_\eta$ with $\mathrm{Mon}(y_0) = \Lambda [y]$.

**Theorem 7.22.12 (Completeness).** Let $L$ be complete. For every Breuil-Kisin datum $D$, the module $Z_\eta$ is free of finite rank over $\mathcal{O}$, the lattice $Y'_\eta$ is $\ell$-adically complete, and $Z_\eta$ is $\ell$-adically separated.

The last three statements are the analytic core of the argument. The polynomial $R_U$ has its roots at $n e \ell$ with $|n| < \ell$, so its constant term has $\ell$-adic valuation at most $(N + 1)\eta$. This is the source of the term $(N + 1)\eta$ in the exponent.

**Theorem 7.22.13 (Lifting theorem for $\varphi$-modules).** Let $L$ be complete. Let $D_0, D_1, D_2$ be Breuil-Kisin data of heights $(\eta, H)$, and $F : D_0 \to D_1$, $G : D_1 \to D_2$ maps of Breuil-Kisin data. Let $N \ge 0$, $\Sigma \subseteq \mathbb{Z}/e$ and $U \subseteq \mathbb{Z}$ be finite, and put $r = r(\Sigma)$. Assume that:

1. $(F, G)$ is an exact triple;
2. the numerical conditions hold for $(\ell, e, N, \eta, H, \Sigma, U)$;
3. $D_1$ is of type $(\Sigma, U)$;
4. the characters of $D_2$ lie in $\Sigma$.

Let $y_2' \in Y'_\eta(D_2)$ and $m_2 \in M^\Delta(D_2)$ with $\mathrm{Mon}(y_2' + \varphi(m_2)) = 0$. Put
$$k = \eta(r + 1) + 2\rho + \eta + (N + 1)\eta.$$
Then there are $y' \in Y'_\eta(D_1)$ and $m \in M^\Delta(D_1)$ with $\mathrm{Mon}(y' + \varphi(m)) = 0$ and
$$G\big(y' + \varphi(m)\big) = \ell^{k}\big(y_2' + \varphi(m_2)\big).$$

Lean: `GlobalTheory.T.liftingTheorem_phiModules_exact_triple`.

*Proof.* Put $c_1 = \eta(r + 1)$, $c_2 = c_1 + \rho$ and $n = c_2 + \eta + (N + 1)\eta$, so that $k = n + \rho$.

*Step 1: numbers.* By the theorem on the period, $r \ge 1$, $4 r \le N^2$, and every element of $\Sigma$ has period at most $r$. By the theorem on the size of the prime, $10 H + 2 \le \ell$, $14 H + (N + 2)\eta < \ell$ and $(r + 2)\eta < \ell + 1$; these also give $14 H < \ell$ and $H + \eta < \ell$. Since $N \ge 2$, we have $N^3 \ge 8$, so $\ell > 320$ and $\ell \ne 2$.

*Step 2: a first lift.* By [the theorem on the cokernel](/entry/cokernel-lattice-map-killed-by-prime-pow-main/), applied to $G$, the power $\ell^\rho$ kills the cokernel of $G$ from $M$ to $M$, from $M^\Delta$ to $M^\Delta$ and from $Y'_\eta$ to $Y'_\eta$. Its hypotheses hold: the cokernel of $G$ has finite length since the triple is exact, $D_1$ is of type $(\Sigma, U)$, and the characters of $D_2$ lie in $\Sigma$. So there are $y_1 \in Y'_\eta(D_1)$ with $G y_1 = \ell^\rho y_2'$ and $m_1 \in M^\Delta(D_1)$ with $G m_1 = \ell^\rho m_2$. Since $G$ commutes with $\varphi$,
$$G\big(y_1 + \varphi(m_1)\big) = \ell^\rho \big(y_2' + \varphi(m_2)\big).$$

*Step 3: the defect.* Put $\omega = \mathrm{Mon}(y_1 + \varphi(m_1))$. This is the defect that we must remove. By the theorem on integrality, applied to $D_1$ with the bounds of Step 1 and the periods of the characters of $D_1$, which lie in $\Sigma$, we get $\ell^{c_1} \omega \in Z_\eta(D_1)$. Also
$$G(\ell^{c_1} \omega) = \ell^{c_1} \mathrm{Mon}\big(G(y_1 + \varphi(m_1))\big) = \ell^{c_1 + \rho} \mathrm{Mon}\big(y_2' + \varphi(m_2)\big) = 0.$$

*Step 4: the defect comes from $D_0$.* By the theorem on exact triples, with $n = \rho$ and Step 2, there is $w_0 \in Z_\eta(D_0)$ with $F w_0 = \ell^{\rho} \ell^{c_1} \omega = \ell^{c_2} \omega$.

*Step 5: a rational preimage under $F \circ \Lambda$.* The vector $y_1 + \varphi(m_1)$ is fixed by $\Delta$, since $m_1$ is and $\Delta$ commutes with $\varphi$. It lies in $Y_\eta$: we have $y_1 \in Y'_\eta \subseteq Y_\eta$, and $E^\eta \varphi(m_1) \in M$ by the height bound $E^\eta \varphi^* M \subseteq M$. By the theorem on invariant vectors, $\omega = \Lambda w_1$ with $w_1 \in Z_\eta[1/\ell](D_1)$. The jumps of $D_1$ lie in $U$ since $D_1$ is of type $(\Sigma, U)$, so $D_1$ satisfies the image condition for $U$. Since $Z_\eta \subseteq Z_\eta[1/\ell]$, the theorem on lifting through $\Lambda$ applies with $c = c_2$ and gives $w' \in Z_\eta[1/\ell](D_0)$ with $F(\Lambda w') = \omega$.

*Step 6: integrality of $w'$.* We have $F(\ell^{c_2} \Lambda w') = \ell^{c_2} \omega = F w_0$. Since $F$ is injective on $\Pi$, $\ell^{c_2} \Lambda w' = w_0 \in Z_\eta(D_0)$.

*Step 7: an integral vector of $D_0$.* The jumps of $D_0$ are jumps of $D_1$, so they lie in $U$. By the theorem on integral representatives with $c = c_2$, there is $y \in Y'_\eta(D_0)$ with $\Lambda [y] = \ell^{n} \Lambda w'$. By the theorem on completeness, $Y'_\eta(D_0)$ is $\ell$-adically complete and $Z_\eta(D_0)$ is $\ell$-adically separated. By the theorem on the monodromy of integral vectors, there is $y_0 \in Y'_\eta(D_0)$ with $\mathrm{Mon}(y_0) = \Lambda [y]$. Hence
$$F\big(\mathrm{Mon}(y_0)\big) = \ell^n F(\Lambda w') = \ell^n \omega.$$

*Step 8: the correction.* Since $(F, G)$ is exact, $G F$ vanishes on $M(D_0)$, which contains a basis, so $G F = 0$ on all vectors. Put
$$y' = \ell^n y_1 - F(y_0), \qquad m = \ell^n m_1.$$
Then $y' \in Y'_\eta(D_1)$, since $F$ maps $Y'_\eta(D_0)$ into $Y'_\eta(D_1)$, and $m \in M^\Delta(D_1)$. We have $y' + \varphi(m) = \ell^n (y_1 + \varphi(m_1)) - F(y_0)$. So
$$\mathrm{Mon}\big(y' + \varphi(m)\big) = \ell^n \omega - F\big(\mathrm{Mon}(y_0)\big) = 0,$$
and
$$G\big(y' + \varphi(m)\big) = \ell^n G\big(y_1 + \varphi(m_1)\big) - G F(y_0) = \ell^{n + \rho}\big(y_2' + \varphi(m_2)\big).$$
Since $n + \rho = k$, this proves the theorem. $\square$

For $N = 2$, $\eta = 1$ and $r = 1$ we get $\rho = 2$, $c_1 = 2$, $c_2 = 4$, $n = 8$ and $k = 10$.

**Remark 7.22.14 (Formalization).** The theorem is a wrapper of `lifting_along_exact_triple`, which is not in the outline of the chapter ([LiftingTheoremPhiModulesExactTriple.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftingTheoremPhiModulesExactTriple.lean#L23)); the wrapper sets `maxHeartbeats` to 1000000. The conclusion is the proposition `Lifting` with exponent `kExp N η (maxPeriod l Sig)`. The inputs are `maxFrobeniusOrbitLengthDiff_bounds_zmod`, `numerical_conditions_theorem_T_large_prime`, `breuilKisinDescent_pow_smul_monodromy_add_phi_mem`, `breuilKisin_exactTriple_jumps_characters_lift`, `monodromy_mem_range_of_invariant_vector`, `breuilKisinDescent_monodromy_image_valuation`, `lift_image_eulerE_invariants_quotient`, `exists_mem_tameDescent_class_eq_of_pow_mem`, `exists_monodromy_eq_leadingCoeff_breuilKisinDescent`, `breuilKisinDescent_finite_free_invertPrime`, `isAdicComplete_twistedInvariantLattice` and `isHausdorff_invariants_quotient_of_finiteFree`. We read their statements, not their proofs. The theorem on invariant vectors has a first part (a solution $s$ of $\nabla_P s = \zeta(y)$ and a Frobenius relation), and the theorem on the image condition has two more parts; the proof discards them (lines 78 and 79). The numerical conditions are copied field by field into a second structure `Bounds` with the same ten fields (lines 43 to 45), as in [the section on lifting](/entry/lift-f-of-is-good/). The exponent $\rho$ appears twice, as `rho l Sig N` and as `eW N r`, and the proof checks that they agree (line 49).
