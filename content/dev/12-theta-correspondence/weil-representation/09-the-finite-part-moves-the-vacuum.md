---
title: The finite part moves the vacuum
decls:
  - GlobalTheory.VacMoveFin.vacuum_move_reads
  - GlobalTheory.T.weil_datum_finite_part_moves_vacuum_as_theta_model
  - GlobalTheory.NormRatio.finite_data
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The finite part moves the vacuum

This section compares the adelic Weil representation with a classical model on functions of a complex variable. The first theorem says that when the adelic vacuum is moved by points of the two unitary groups that live at the finite places, the result is again a theta function, and its classical reading is the classical vacuum moved by the classical action, with no extra constant. The second theorem computes the finite data of the vacuum of a bottom pair: it is spherical off a finite set of places, its norm is a product of a local volume and a classical norm, and it is orthogonal to its translates by finite points outside the integral group. The first theorem is used in [the joined estimates for the top term of the square](/entry/square-top-term-joined-estimates/), and the second in [the identity of the Petersson norm of a theta lift with a Rallis integral](/entry/theta-lift-petersson-norm-eq-rallis-integral/).

### The setting

Let $F$ be a totally real number field, $E/F$ a CM extension, and $S$, $T$ Hermitian spaces over $E$ of ranks $a$ and $d$, both with Gram matrix $1$. Let $\psi$ be a standard additive character of $\mathbb{A}_F/F$ of sign $-1$, and fix an embedding $\tau$ of $E$ over each infinite place. Let $\omega$ be the adelic [Weil representation](/learn/theta/#the-weil-representation) of $\mathrm{U}(S)(\mathbb{A}_F) \times \mathrm{U}(T)(\mathbb{A}_F)$ on functions of $w \in \mathbb{W} = M_{d \times a}(\mathbb{A}_E)$, for a pair of [[Hecke characters|KPYFGB342X]] $\chi_S$, $\chi_T$. A *theta function* is a function on $\mathbb{W}$ in the space on which the global [[Heisenberg group|ZZYCV5EX9J]] acts by $\omega$.

Fix a scalar $\delta \in \mathbb{C}^\times$ and an element $r \in E^\times$. For $w \in \mathbb{W}$ the *classical coordinate* is the tuple
$$y(w) = \bigl(\delta\, \tau(r)\, w_\tau\bigr)_\tau \in V_{\mathbb{C}} = \prod_\tau M_{d \times a}(\mathbb{C}),$$
where $w_\tau$ is the component of $w$ at the place of $\tau$. Let $H$ be the positive definite Hermitian form on $V_{\mathbb{C}}$ given by the torus of $\delta$.

**Definition 1.9.1 (Reading).** A function $f$ on $\mathbb{W}$ *reads* a function $G$ on $V_{\mathbb{C}}$ if $f$ is a theta function and, for each $w$ with finite part $0$,
$$f(w) = e^{-\frac{\pi}{2} H(y,y)}\, G(y), \qquad y = y(w).$$

So the reading of $f$ is the function $G$ that remains when the Gaussian factor of the [Fock model](/learn/theta/#the-fock-model) is taken out of the archimedean part of $f$.

**Definition 1.9.2 (Finite point).** Let $x \in \mathrm{GL}_a(\mathbb{A}_{E,\mathrm f})$. An element $g \in \mathrm{U}(S)(\mathbb{A}_F)$ is a *finite point for $x$* if the archimedean component of $g$ is $1$ and the finite component of $g$ is $x$, entry by entry.

The classical model is a representation $(x, y) \mapsto \Omega(x, y)$ of $\mathrm{GL}_a(\mathbb{A}_{E,\mathrm f}) \times \mathrm{GL}_d(\mathbb{A}_{E,\mathrm f})$ on functions on $V_{\mathbb{C}}$, with a classical vacuum $e_0$. The adelic vacuum $f_0$ is a theta function that reads $e_0$.

### Moving the vacuum

**Theorem 1.9.3 (Finite points move the vacuum).** Let $f_0$ read $e_0$. Let $g$ be a finite point for $x$ in $\mathrm{U}(S)(\mathbb{A}_F)$ and $h$ a finite point for $y$ in $\mathrm{U}(T)(\mathbb{A}_F)$. Then $\omega(g, h) f_0$ reads $\Omega(x, y)\, e_0$.

Lean: `GlobalTheory.VacMoveFin.vacuum_move_reads` (also `GlobalTheory.T.weil_datum_finite_part_moves_vacuum_as_theta_model`, a second name).

*Proof.* For a pair $(x, y)$, say that $(x, y)$ is *exact* if for all finite points $g$, $h$ for $x$, $y$ the function $\omega(g,h)f_0$ reads $\Omega(x,y)e_0$. We show that each pair is exact in four steps.

First, for each pair $(x, y)$ and finite points $g$, $h$ there is a constant $c \in \mathbb{C}$ such that $\omega(g,h) f_0$ reads $c\, \Omega(x,y) e_0$. The reason is that $\omega(g,h)$ commutes with the archimedean Heisenberg operators, since $g$ and $h$ are trivial at infinity, so $\omega(g,h)f_0$ is killed by the same annihilation operators as $f_0$. The space of such readings is a line spanned by the moved classical vacuum.

Second, the constants are multiplicative. Suppose $\omega(g_1, h_1)f_0$ reads $c_1\Omega(x_1,y_1)e_0$ and $\omega(g_2, h_2)f_0$ reads $c_2\Omega(x_2,y_2)e_0$. Apply $\omega(g_1, h_1)$ to the second function. The moved theta function reads the classical action of $(x_1,y_1)$ on its reading, so $\omega(g_1g_2, h_1h_2) f_0$ reads
$$c_1 c_2\, \Omega(x_1x_2,\, y_1y_2)\, e_0.$$
So the set of exact pairs is closed under products.

Third, the constant is $1$ when $x$ and $y$ are supported at the places of $F$ that split in $E$. At a split place the unitary group is a general linear group, and the local Weil representation is the action by substitution on a Schrödinger model, which agrees with the classical action on the vacuum.

Fourth, the constant is $1$ when $x$ and $y$ are integral and supported at the places that are inert in $E$. At such a place an integral point fixes the local spherical vector, so it fixes the adelic vacuum, and it fixes the classical vacuum.

Each finite point is a product of points of the last two kinds, up to the products allowed by the second step. So each pair is exact. $\square$

### The finite data of a bottom vacuum

Let $\mathfrak{m}$ be a nonzero ideal of $\mathcal{O}_E$. It is a *good modulus* with finite set $S_{\mathrm f}$ of places of $F$ if $\mathfrak{m} + \bar{\mathfrak{m}} = \mathcal{O}_E$, $\mathfrak{m}$ is prime to a fixed bad integer of the data, and $S_{\mathrm f}$ is the set of places of $F$ below the primes that divide $\mathfrak{m}$. Let $K(\mathfrak m) \subset \mathrm{GL}_a(\widehat{\mathcal{O}}_E)$ be the principal congruence subgroup of level $\mathfrak{m}$.

For a lattice $L$ in a Hermitian space, a vector is *spherical off $S_{\mathrm f}$* for $L$ if it is fixed by the Heisenberg lattice of $L$ at each finite place outside $S_{\mathrm f}$. For a Haar measure $\nu$ on $\mathbb{W}$ and a fundamental domain $\mathcal{F}$ of the rational lattice with $\nu(\mathcal{F}) = 1$, write
$$\langle f_1, f_2 \rangle = \int_{\mathcal{F}} f_1\, \overline{f_2}\, d\nu.$$

The bottom pair gives an adelic vacuum $v$ of a standard form: there is a finite set $R \subset \mathrm{GL}_a(\widehat{\mathcal{O}}_E)$ of representatives of $\mathrm{GL}_a(\widehat{\mathcal{O}}_E)/K(\mathfrak m)$ such that the classical vacuum is
$$\textstyle \sum_{\rho \in R} \Omega(\rho, 1)\, e_{\mathfrak m, o},$$
where $e_{\mathfrak m,o}$ is the classical coset vector of level $o$.

**Theorem 1.9.4 (Finite data of the vacuum).** Let the bottom pair be exact, let $\mathfrak m$ be a good modulus with set $S_{\mathrm f}$, let the datum be standard of level $o$, and suppose $o + a \leq d$. Then:

1. there is a self-dual lattice $L_T$ in $T$ such that $v$ is spherical off $S_{\mathrm f}$ for the standard lattice of $S$ and $L_T$;
2. for each $\nu$ and $\mathcal F$ as above, $\langle v, v\rangle = N_{\mathrm{loc}}(\mathfrak m)\, N_{\mathrm{vac}}$;
3. for each finite point $g$ of $\mathrm{U}(S)$ that is not in the integral group and whose component at each place outside $S_{\mathrm f}$ stabilizes the standard lattice, $\langle \omega(g,1)v, v\rangle = 0$.

Here, with $a' = d - a$ and $e_w$ the exponent of the prime $w$ in $\mathfrak m$,
$$N_{\mathrm{loc}}(\mathfrak m) = \prod_{w \mid \mathfrak m} \mathrm{N}w^{-e_w a a'}\, \operatorname{vol}_a(\mathrm{N}w),$$
where $\operatorname{vol}_a(q)$ is the normalized volume of $\mathrm{GL}_a$ over a local field with residue field of size $q$, and $N_{\mathrm{vac}}$ is the square norm of the classical theta constant of the torus, raised to the power $[F:\mathbb{Q}]\, a\, d$.

Lean: `GlobalTheory.NormRatio.finite_data`.

*Proof.* Choose a theta function $\varphi$ that reads $e_{\mathfrak m,o}$ and a theta function $f_0$ that reads $e_0$. By the theorem on finite points, $\omega(\rho,1)\varphi$ reads $\Omega(\rho,1)e_{\mathfrak m,o}$ for each $\rho \in R$, so
$$\textstyle v = \sum_{\rho \in R} \omega(\rho, 1)\,\varphi.$$

For (1), there is a self-dual lattice $L_T$ for which the vacuum $f_0$ is spherical off $S_{\mathrm f}$, and then $\varphi$ is spherical off $S_{\mathrm f}$ too, since it differs from $f_0$ only at the places of $S_{\mathrm f}$. Each $\rho \in R$ stabilizes the standard lattice at the places outside $S_{\mathrm f}$, and the Weil representation of a lattice stabilizer keeps spherical vectors. So each term of the sum is spherical off $S_{\mathrm f}$, and so is $v$.

For (3), the translates $\omega(g\rho, 1)\varphi$ and $\omega(\rho', 1)\varphi$ have disjoint supports in the finite variable when $g\rho$ and $\rho'$ lie in different cosets of $K(\mathfrak m)$. If $g$ is not integral, then $g\rho$ is not in $\rho' K(\mathfrak m)$ for any $\rho, \rho' \in R$. The hypothesis $o + a \leq d$ makes the coset vector see the full congruence condition. So each term of $\langle \omega(g,1)v, v\rangle$ is $0$.

For (2), the same orthogonality gives
$$\langle v, v\rangle = |R|\, \langle \varphi, \varphi\rangle.$$
Three computations finish the proof. The norm of $\varphi$ is $\mathrm{N}\mathfrak{m}^{-ad}$ times the norm of the moved vacuum. The adelic norm of a theta function that reads a classical vector is the mean square of its reading over the torus, which for the vacuum is $N_{\mathrm{vac}}$. The number $|R|$ of cosets times the local factor $\mathrm{N}\mathfrak m^{-ad}$ is $N_{\mathrm{loc}}(\mathfrak m)$, by the count of $\mathrm{GL}_a(\mathcal{O}_w / w^{e_w})$ at each prime $w \mid \mathfrak m$. The product of the three gives the claim. $\square$

**Remark 1.9.5.** The theorem on finite points is the global form of the statement that the Fock model and the Schrödinger model agree on the finite part: the finite adelic group acts only on the finite variable, and the [[Bargmann transform|QPH28QH036]] at infinity is not touched. The normalization by the constant $1$ is the point of the theorem, and it is fixed place by place, at split places by the Schrödinger model and at inert places by the spherical vector.

**Remark 1.9.6 (Formalization).** The theorem on finite points is `GlobalTheory.VacMoveFin.vacuum_move_reads` (WeilDatumFinitePartMovesVacuumAsThetaModel.lean, line 47). Its proof applies `movedVacuum_constant_trivial_finite_pairs`, a wrapper of `GlobalTheory.VacTriv.vacuum_const_trivial`, to four inputs: `VacLine.moved_vacuum_reads` (a constant exists), `mulStep` (line 25 of the same file), `SplitVacMove.reads_om_split` (split places) and `inertIntegralPoints_fix_adelic_classical_vacuum` (inert integral points). We have not opened the proofs of these four inputs or of the induction principle, so the reasons for them above are ours. The reading is `Reads` and the setup is `Setup` (IsCongLevelIntG.lean, lines 29 and 35); `Setup` also carries a field `scale` for $r$. A finite point is `IsFinPt` (IsFinPt.lean, line 21), where the archimedean triviality is membership in `GfC`, the kernel of `infHom`, defined in Formalism/LocalToGlobal/BesselHermitianTheta/IsAutFunDef.lean, line 30. Many hypotheses of `vacuum_move_reads` (the input `hInp`, the torsion point `t0` with `ht0`, the parity `hev` of $ad$, `hodd`, `hfS` and `hfT`) are only passed to the inputs. The second name is a `first | exact ...` wrapper under `maxHeartbeats 1000000` (WeilDatumFinitePartMovesVacuumAsThetaModelStatement.lean, line 18). The finite data theorem is `finite_data` (HeckeLFunctionBottomPair.lean, line 245); the standard datum is `IsStdDatum` (Definitions/Divisors/FinitePrimesUnder.lean, line 49), and the good modulus and the norms are `GoodMod`, `locNorm` and `vacNorm` (GoodModModT.lean, lines 29, 35 and 42). The statement uses `vacNorm D ⊤ δ t0`, with the ideal $\top$ in place of the ideal of the pair. The input `hI` is used only for the sum formula `vac_eq_sum`, and the hypothesis $o + a \leq d$ only for the orthogonality `cosetVector_orthogonal_translate_finite_point`. The proof ends with `norm_arith` on the three computations `thetaCosetIndicatorReading_normSq_eq_absNorm_inv_mul_vacuum`, `thetaLineReading_adelicNorm_eq_torusMeanSquare` and `card_transversal_congruence_mul_norm_eq_localNorm`, whose proofs we have not opened.
