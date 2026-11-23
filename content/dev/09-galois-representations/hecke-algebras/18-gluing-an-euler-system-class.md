---
title: Gluing an Euler system class
decls:
  - GlobalTheory.KZ.middle_glue2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gluing an Euler system class

A norm-compatible family of cocycles along the cyclotomic $\mathbb{Z}_\ell$-tower, twisted by a character, has a limit: one global cocycle $y$ for a two-dimensional representation $W$. This section shows that a bounded multiple $\ell^m y$ is an Euler system class: it is integral, unramified away from $\ell$ and has tame classes at the auxiliary primes, provided that the family has tame companions at these primes. The same theorem shows that the second coordinates of the family form an Iwasawa system linked to $y$. It is the last step of the proof of [the norm-compatible system of zeta classes](/entry/k4-top/), which supplies the family and the tame companions.

### Setting

Let $\ell$ be a prime, $\Omega$ an algebraic closure of $\mathbb{Q}$, $G_{\mathbb{Q}} = \mathrm{Gal}(\Omega/\mathbb{Q})$, and $A$ a valuation ring of $\Omega$ with decomposition group $D_A$ and inertia group $I_A$. Let $W : G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ be a representation and $\mathcal{O} \subseteq \overline{\mathbb{Q}}_\ell$ the ring of a coefficient datum. Let $\chi_r$ be the cyclotomic character modulo $\ell^r$ and $\omega$ the Teichmüller character. For a place $q$ of $\mathbb{Q}$ we write $q$ also for its prime number, and $I_B$ for the inertia group of a valuation ring $B$ of $\Omega$ over $q$. For $x \in (\mathbb{Z}/\ell^r)^\times$ let $\langle x\rangle \in \{1, \ldots, \ell^r - 1\}$ be its least positive representative. We write $a \equiv_n b$ when $|a - b| \leq |\ell^n|$, and use it coordinatewise for vectors.

**Definition 6.18.1 (Shapiro cocycle).** Let $X$ be a monoid, $\kappa : G_{\mathbb{Q}} \to X$ a homomorphism and $\rho : G_{\mathbb{Q}} \to M_2(\overline{\mathbb{Q}}_\ell)$. A map $Y : G_{\mathbb{Q}} \times X \to \overline{\mathbb{Q}}_\ell^2$ is a *Shapiro cocycle for $(\rho, \kappa)$* if
$$
Y(st, x) = Y(s, x) + \rho(s)\,Y\bigl(t, x\,\kappa(s)\bigr) \qquad (s, t \in G_{\mathbb{Q}},\ x \in X).
$$
A family $Y_r$ of such maps on $X = (\mathbb{Z}/\ell^r)^\times$ is *norm-compatible* if $Y_r(s, x) = \sum_{x' \mapsto x} Y_{r+1}(s, x')$, the sum over the $x' \in (\mathbb{Z}/\ell^{r+1})^\times$ above $x$.

For $X = (\mathbb{Z}/\ell^r)^\times$ and $\kappa = \chi_r^{-1}$, such a $Y$ is a cocycle of $G_{\mathbb{Q}}$ with values in the functions on $\mathrm{Gal}(\mathbb{Q}(\mu_{\ell^r})/\mathbb{Q})$. By Shapiro's lemma this is a class over $\mathbb{Q}(\mu_{\ell^r})$, and a norm-compatible family is a class in the inverse limit along the cyclotomic tower.

**Definition 6.18.2 (Specialization).** For $\eta : (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell$ and $Y$ as above, put $\mathrm{sp}_\eta(Y)(s) = \sum_x \eta(x)\,Y(s, x)$.

Let $\theta$ be a character with $W = \theta\rho$. If $\eta(x\chi_r(s)) \equiv_r \theta(s)\eta(x)$ for all $s$ and $x$, then for a Shapiro cocycle $Y$ for $(\rho, \chi_r^{-1})$ with integral values,
$$
\mathrm{sp}_\eta(Y)(st) = \mathrm{sp}_\eta(Y)(s) + \rho(s)\sum_x \eta\bigl(x\chi_r(s)\bigr)Y(t, x) \equiv_r \mathrm{sp}_\eta(Y)(s) + W(s)\,\mathrm{sp}_\eta(Y)(t).
$$
So the specialization is a cocycle for $W$ modulo $\ell^r$. This is the twist that turns the Iwasawa class into a class for $W$.

**Definition 6.18.3 (Tame class).** Let $y : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^2$, $n \geq 1$, $w$ a prime with $\ell^n \mid w - 1$, and $\psi : G_{\mathbb{Q}} \to \mathbb{Z}/\ell^n$ a surjective homomorphism that is trivial on $\mathrm{Gal}(\Omega/\mathbb{Q}(\mu_w))$. Then $y$ *has a tame class at $(w, n, \psi)$* if there are a continuous $Y : G_{\mathbb{Q}} \times \mathbb{Z}/\ell^n \to \mathcal{O}^2$, $P \in \mathcal{O}$, $u$ with $|u| = 1$ and $b \in \mathcal{O}^2$ such that:

1. $Y(st, x) = Y(s, x) + W(s)\,Y(t, x - \psi(s))$;
2. $\sum_x Y(s, x) = P\,y(s) + W(s)b - b$ for all $s$;
3. $P \equiv_n u\det\bigl(W(\sigma) - 1\bigr)$ for each Frobenius element $\sigma$ at each place over $w$;
4. for each prime $q \neq w, \ell$ there are a place $B$ over $q$ and $t : \mathbb{Z}/\ell^n \to \mathcal{O}^2$ with $Y(s, x) = W(s)t(x) - t(x)$ for $s \in I_B$.

Here $\psi$ cuts out the subfield of degree $\ell^n$ of $\mathbb{Q}(\mu_w)$. So $Y$ is a class over that field, unramified away from $w$ and $\ell$, whose corestriction to $\mathbb{Q}$ is $P\,y$, with $P$ the value of the Euler factor $\det(1 - W(\mathrm{Frob}_w))$ up to a unit. This is the Euler system relation; see K. Rubin, *Euler Systems*, Chapter 2.

**Definition 6.18.4 (Euler system class).** Let $S'$ be a finite set of places. The map $y$ is an *Euler system class for $W$, $\mathcal{O}$ and $S'$* if the entries of $W$ lie in $\mathcal{O}$, $y$ is a cocycle for $W$ with values in $\mathcal{O}^2$, for each prime $q \neq \ell$ there are a place $B$ over $q$ and $x \in \overline{\mathbb{Q}}_\ell^2$ with $y(s) = W(s)x - x$ on $I_B$, and $y$ has a tame class at $(w, n, \psi)$ for all $n \geq 1$, $w \notin S'$ with $\ell^n \mid w - 1$, and $\psi$ as above.

**Definition 6.18.5 (Iwasawa system, link).** Let $\nu : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^\times$. A family $Z_r : G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \mathcal{O}$ is an *Iwasawa system for $\nu$* if $\nu$ is multiplicative on $D_A$, $Z_r(st, x) = Z_r(s, x) + \nu(s)Z_r(t, x\chi_r(s)^{-1})$ for $s, t \in D_A$, and $Z_r(s, x) = \sum_{x' \mapsto x} Z_{r+1}(s, x')$. Let $e \geq 0$ and $\chi = (\chi'_r)$ a family of functions on $(\mathbb{Z}/\ell^r)^\times$. Then $Z$ is *linked to $y$ with weight $e$* if for each $n$ there is $r_0$ such that for $r \geq r_0$ and $s \in I_A$ with $\omega(s) = 1$,
$$
y(s)_2 \equiv_n \sum_x \langle x\rangle^{-e}\chi'_r(x)\,Z_r(s, x).
$$

These are the notions of [the chapter on Coleman power series](/entry/p-locu/), where the Euler system class is shown to be nonzero on $I_A$.

### The theorem

**Theorem 6.18.6 (Gluing an Euler system class).** Let $e \geq 0$, $S$ a finite set of places, $\chi'_r : (\mathbb{Z}/\ell^r)^\times \to \mathcal{O}$, $\theta : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^\times$ a homomorphism, $\rho : G_{\mathbb{Q}} \to M_2(\overline{\mathbb{Q}}_\ell)$, $\nu : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^\times$, and $Y_r : G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell^2$. Put $\eta_r(x) = \langle x\rangle^{-e}\chi'_r(x)$. Assume:

1. $W$ and $\theta$ are continuous, $W = \theta\rho$, and the entries of $W$ and of $\rho$ lie in $\mathcal{O}$;
2. $\chi'_{r+1}(x) \equiv_r \chi'_r(x \bmod \ell^r)$, and $\eta_r(x\chi_r(s)) \equiv_r \theta(s)\eta_r(x)$ for all $r$, $s$, $x$;
3. the $Y_r$ are norm-compatible Shapiro cocycles for $(\rho, \chi_r^{-1})$, continuous in $s$, with values in $\mathcal{O}^2$;
4. for $s \in D_A$ the second row of $\rho(s)$ is $(0, \nu(s))$;
5. $W$ is trivial on $I_B$ for every place $B$ over a place $w \notin S$, and $\theta$ is trivial on $I_B$ for every $B$ over a prime $q \neq \ell$;
6. (tame companions) for each $n \geq 1$, each $w \notin S$ with $\ell^n \mid w - 1$ and each $\psi$ as in the definition of a tame class, there are norm-compatible Shapiro cocycles $Y^w_r$ on $X = \mathbb{Z}/\ell^n \times (\mathbb{Z}/\ell^r)^\times$ for $\rho$ and $\kappa(s) = (\psi(s), \chi_r(s)^{-1})$, continuous, with values in $\mathcal{O}^2$, and $P \in \mathcal{O}$, $|u| = 1$, $b_r \in \mathcal{O}^2$ with
$$
\sum_{a \in \mathbb{Z}/\ell^n}\mathrm{sp}_{\eta_r}\bigl(Y^w_r(\cdot, (a, \cdot))\bigr)(s) \equiv_r P\,\mathrm{sp}_{\eta_r}(Y_r)(s) + W(s)b_r - b_r
$$
for all $r$ and $s$, and $P \equiv_n u\det(W(\sigma) - 1)$ for each Frobenius $\sigma$ at each place over $w$.

Then there are $m \geq 0$, $y : G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^2$ and a finite set $S'$ such that:

1. $y \equiv_r \mathrm{sp}_{\eta_r}(Y_r)$ for every $r$;
2. $\ell^m y$ is an Euler system class for $W$, $\mathcal{O}$ and $S'$;
3. the second coordinates of $\ell^m Y_r$ form an Iwasawa system for $\nu$;
4. this Iwasawa system is linked to $\ell^m y$ with weight $e$.

Lean: `GlobalTheory.KZ.middle_glue2`.

*Proof.* We take $S' = S$. The proof has four steps.

*Step 1: the limit.* By hypothesis 2, $\eta_{r+1}(x') \equiv_r \eta_r(x)$ for $x'$ above $x$, since $\langle x'\rangle \equiv \langle x\rangle$ modulo $\ell^r$ and both are prime to $\ell$. With the norm relation this gives $\mathrm{sp}_{\eta_{r+1}}(Y_{r+1}) \equiv_r \mathrm{sp}_{\eta_r}(Y_r)$. So the specializations converge to a map $y$ with values in $\mathcal{O}^2$ and $y \equiv_r \mathrm{sp}_{\eta_r}(Y_r)$. By the computation after the definition of the specialization, $y$ is a cocycle for $W$. We use one more fact about this limit: for each prime $q \neq \ell$, $y$ is a coboundary $W(s)x_q - x_q$ on the inertia group of some place over $q$, with $x_q \in \overline{\mathbb{Q}}_\ell^2$. Here hypothesis 5 enters: $\theta$ is unramified at $q$, and the class comes from the cyclotomic tower, in which $q$ is finitely decomposed. The link with weight $e$ follows from $y \equiv_r \mathrm{sp}_{\eta_r}(Y_r)$: take $r_0 = n$.

*Step 2: integrality.* For each prime $q$ and each place $B$ over $q$ there is $m_q$ such that, if an integral cocycle is a coboundary $W(s)v - v$ on $I_B$ with $v \in \overline{\mathbb{Q}}_\ell^2$, then $\ell^{m_q}$ times it is a coboundary $W(s)t - t$ with $t \in \mathcal{O}^2$. This holds because the entries of $W$ lie in $\mathcal{O}$: modulo $I_B$-invariant vectors, $v$ is determined by the values $W(s_i)v - v$ at finitely many $s_i \in I_B$, through a linear map with bounded denominators. Put $m = \max_{q \in S} m_q$. Then $\ell^m y$ is an integral cocycle, unramified away from $\ell$.

*Step 3: tame classes.* Fix $n$, $w \notin S$ and $\psi$. Hypothesis 6 gives $Y^w_r$, $P$, $u$ and $b_r$. Since $|P| \leq 1$ and $y \equiv_r \mathrm{sp}_{\eta_r}(Y_r)$, the congruence of hypothesis 6 holds with $P\,y$ in place of $P\,\mathrm{sp}_{\eta_r}(Y_r)$. A limit argument as in Step 1, now for the Shapiro cocycles $Y^w_r$, gives a continuous cocycle $Y^t$ on $G_{\mathbb{Q}} \times \mathbb{Z}/\ell^n$ for $W$ and the shift by $\psi$, with values in $\mathcal{O}^2$, and $b' \in \mathcal{O}^2$, with $\sum_a Y^t(s, a) = P\,y(s) + W(s)b' - b'$. Then $\ell^m Y^t$, $P$, $u$ and $\ell^m b'$ satisfy conditions 1 to 3 of a tame class for $\ell^m y$. For condition 4, let $q \neq w, \ell$. Since $\psi$ factors through $\mathrm{Gal}(\mathbb{Q}(\mu_w)/\mathbb{Q})$, it is trivial on inertia at $q$, and so is $\theta$. The same limit argument then shows that $Y^t$ is a coboundary on the inertia group at a place over $q$, with rational $v$. If $q \in S$, Step 2 makes $\ell^m Y^t$ an integral coboundary there. If $q \notin S$, $W$ is trivial on that inertia group, so $Y^t = 0$ there and $t = 0$ works.

*Step 4: the Iwasawa system.* Since $W = \theta\rho$ with $W$ a homomorphism and $\theta$ a character, $\rho$ is multiplicative. By hypothesis 4, $\rho(s)$ is upper triangular on $D_A$ with lower right entry $\nu(s)$, so $\nu$ is multiplicative on $D_A$. The second row of the Shapiro relation for $s \in D_A$ reads $Y_r(st, x)_2 = Y_r(s, x)_2 + \nu(s)Y_r(t, x\chi_r(s)^{-1})_2$. The norm relation and integrality pass to the second coordinates, and all of this is preserved by the factor $\ell^m$. The link of Step 1 is also preserved by this factor. $\square$

The constant $m$ depends only on $W$, $\mathcal{O}$ and $S$, not on $w$, $n$ or $\psi$. This is why one multiple $\ell^m y$ has all tame classes at once.

**Remark 6.18.7 (Formalization).** The prime $\ell$ is not assumed to be odd, and the set $S'$ of the conclusion is $S$; the coefficient datum of the Euler system class is the given one. The limit in Step 1, with the cocycle property, the unramified property and the link, is `GlobalTheory.KZ.glob_of_shapiro_system_noLayer` (in [NormSubMulAddLeOfUltrametricReplace.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/NormSubMulAddLeOfUltrametricReplace.lean#L23)), proved from `GlobalTheory.T.isCocycle_of_padic_limit_of_approx_cocycles`, `GlobalTheory.T.unramified_away_from_l_of_twisted_shapiro_limit` and `GlobalTheory.T.kummerScalarLayerLink_of_shapiroSpecialization_approx`. Step 2 is `GlobalTheory.rat_unram_to_int_unram`; Step 3 uses `GlobalTheory.T.tameClass_limit_of_normCompatible_shapiroSystem`, `GlobalTheory.T.tameShapiroSystem_limit_unramified_away_from_l` and `GlobalTheory.KZ.tame_of_shCoc`; Step 4 is `GlobalTheory.KZ.iwSys2_of_shCoc`. None of these is in the outline, and we read them as statements; the reasons given in Steps 1 and 2 for them are ours. The Frobenius condition is the predicate `IsFrob`, which we did not unfold. The file is named after the small helper `norm_sub_mul_add_le_of_ultrametric_replace` (line 116), not after the theorem at line 124.
