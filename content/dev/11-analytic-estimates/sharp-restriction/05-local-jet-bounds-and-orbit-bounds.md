---
title: Local jet bounds and orbit bounds
decls:
  - Formalism.MainNotions.DIV.Bridge.DworkPowerSeriesWeights.thmA_of
  - Formalism.MainNotions.DIV.Bridge.DworkPowerSeriesWeights.split_bound_eleven_one
  - Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.entry_divisor_bound_holds
  - Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.orbit_entry_bounds_of_family
  - Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.orbit_entry_bounds_hold
  - Formalism.MainNotions.Pk.sum_over_primes_service
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local jet bounds and orbit bounds

This section turns the kernel bounds of the previous section into lower bounds for the valuation of jet pairings at one prime, and then puts the local bounds together over the orbits of Frobenius on the places of a CM field. The local result is a uniform bound with the constants $C_6 = 11$ and $C_d = 1$. The global result is the "core" of the orbit bounds, and it feeds the sum over primes that gives the service conclusion of [Theorem 3.5.3 of Volume 15](/entry/closed-serv-f-of-serv-t-of-d-gam-size/).

### Local jet data

Let $l \geq 5$ be a prime and let $d \geq 2$ be even. Let $N_0 < N_1$. A theta series is a power series $\Theta$ over $\mathbb{C}_l$ in the variables $X_{s,a,b}$ with $s \in \mathbb{Z}/d$, $a < N_0$, $b < N_1$. For each $s$ let $\nu_s$ be a partition with at most $N_0$ rows, and let $T \subseteq \mathbb{Z}/d$. We call $(l, d, N_0, N_1, \Theta, \nu, T)$ a local jet datum.

**Definition 8.5.1 (Valuation of a jet pairing).** A column choice $I$ assigns to each $s$ and each column $c$ of $\nu_s$ an increasing map $I_{s,c}$ from $\{1, \dots, \nu_s'(c)\}$ into $\{1, \dots, N_1\}$, where $\nu_s'(c)$ is the length of the column. Let
$$G_{\nu,I} = \prod_s \prod_c \det\Big(\sum_{a < N_0} x_{s,i,a}\, z_{s,a,I_{s,c}(k)}\Big)_{i,k},$$
a polynomial in the variables $x$ and $z$. Pair it with $\Theta$ in the $z$ variables: replace each monomial $x^\mu z^\kappa$ by $\kappa!\,\Theta_\kappa\, x^\mu$. For $B \in \mathbb{R}$ we write $\operatorname{val}(\Theta, \nu) \geq B$ if, for all $I$, every coefficient of the result has norm at most $l^{-B}$.

Lean: `Formalism.MainNotions.product_zeroth_first_parts.KvalGe`

This is the jet pairing of Section 4, applied to products of minors. It is monotone: if the bound holds for $B$, it holds for each $B' \leq B$.

Let $A_s$ be the length of the first row of $\nu_s$ and $|\nu_s|$ its size. Put $\operatorname{cap}_s$ equal to the length of the second row if $s \in T$ and to $A_s$ if $s \notin T$. Put $D_s = |\nu_s| - A_s$ for $s \in T$ and $D_s = |\nu_s|$ otherwise. Let $W_s$ be the largest $\operatorname{cap}_{s-i}$ over odd $i$ with $l^i \leq |\nu_{s-i}|$. Put $\rho(l) = 1/(l^2-1)$ and $\gamma(l) = l/(l^2-1)$. For real weights $D = (D_s)$ let
$$F(D) = \gamma(l) \sum_s D_s - \sup \sum_{s} \sum_{i < d} x_{s,i},$$
where the supremum runs over $x_{s,i} \geq 0$, zero unless $i$ is odd, with $\sum_{i<d} l^i x_{s,i} + \sum_{i<d} x_{s-i,i} \leq D_s$ for all $s$. Let $d_{\mathrm{top}}(s)$ be the least odd $e$ with $s + e \in T$. The top term $\operatorname{top}_s$ is the sum over odd $e$ of $\max(A_s/l^e - \operatorname{cap}_{s+e}, 0)$ for $e < d_{\mathrm{top}}(s)$ and of $A_s/l^e$ for $e > d_{\mathrm{top}}(s)$. The base term $\operatorname{base}_s$ is the sum over odd $e \neq d_{\mathrm{top}}(s)$ of $\max((A_s - \nu_{s,2})/l^e - \operatorname{cap}_{s+e}, 0)$, where $\nu_{s,2}$ is the second row length. Each base term is at most the top term.

**Definition 8.5.2 (Admissible local datum).** Let $\ell_{s,b} = \sum_{e \geq 0} l^{-e} X_{s-2e,b}^{l^{2e}}$. The datum is admissible if there are a unit $\varepsilon$ and a series $\beta$ in variables $Y_s$, $s \in \mathbb{Z}/d$, such that the following hold.

1. $\Theta(\varepsilon \ell) = U \cdot \exp\big(\pm \sum_{a,b} \beta(X_{\cdot,a,b})\big)(\ell)$ with $U$ integral.
2. The coefficients of $\beta$ lie in the closure $W$ of the field generated over $\mathbb{Q}_l$ by the roots of unity of order prime to $l$.
3. $\beta$ is fixed by the twists $Y_s \mapsto u^{l^s} Y_s$ ($s$ even) and $Y_s \mapsto u^{-l^s} Y_s$ ($s$ odd), for $u^{l^d - 1} = 1$.
4. Each monomial of $\beta$ has nonzero degree in the even variables and in the odd variables, and its bidegree is not $(1,1)$.
5. The two coboundaries of $\beta$ (in the even and in the odd variables), exponentiated and composed with $\ell$, have coefficients in the integers of $W$ and constant term $1$.

Lean: `Formalism.MainNotions.product_zeroth_first_parts.Loc.AdmB`

For $a \in \mathbb{R}$ the datum is in the Hida setting if $l \leq a$, $|\nu_s| \leq a$ for all $s$, and $2\log_l a + 2 \leq N_0 - 1$.

**Definition 8.5.3 (Theorem A and Corollary 2).** The datum satisfies Theorem A with constant $C$ if, for each $a$ in the Hida setting,
$$\operatorname{val}(\Theta, \nu) \geq \sum_{s \in T}\big(\operatorname{top}_s - \gamma(l) W_s\big) + F(D) - C\, d N_0 N_1 (\log_l a + 1).$$
It satisfies Corollary 2 with constants $C_6, C_d$ if, for each $a$ in the Hida setting, each $k \geq 3$ and all $w_s > 0$ and $0 \leq E_s \leq 4w_s$ with $D_s = (k-1)w_s + E_s$ for $s \notin T$ and $D_s = (k-3)w_s + E_s$ for $s \in T$,
$$\begin{aligned} \operatorname{val}(\Theta, \nu) \geq{} & \sum_{s \in T} \operatorname{base}_s + F((k-1)w) - \frac{C_6}{l}\sum_s w_s \\ & - \gamma(l) \sum_{s \in T} W_s - C_d\, d N_0 N_1 (\log_l a + 1). \end{aligned}$$

Lean: `Formalism.MainNotions.product_zeroth_first_parts.Loc.ThmA` (also `Formalism.MainNotions.product_zeroth_first_parts.Loc.Cor2`)

There is also a one-letter form. It has $d = 1$, one partition $\nu$, and a series $\beta$ in two variables. Its Hida setting is $l \leq a$ and $|\nu| \leq a$. Theorem 1 with constant $C$ says $\operatorname{val}(\Theta, \nu) \geq \rho(l)|\nu| - C N_0 N_1 (\log_l a + 1)$.

### The uniform local bound

**Theorem 8.5.4 (Theorem A with constant one).** Assume the following three statements.

1. For each series $\beta$ with properties 2 to 5, there are an unramified subfield $K_0$ of $\mathbb{C}_l$ and a primitive root of unity $\zeta$ of order $l^d - 1$ that satisfy a fixed condition on $\beta$.
2. For each datum with property 1, $\Theta(\varepsilon X)$ is the explicit theta kernel built from $\beta$, an integral series $U$, a sign, and the inverse $g$ of the entry logarithm.
3. If every coefficient of every frame jet of $\Theta(\varepsilon X)$ has norm at most $l^{-B}$, then $\operatorname{val}(\Theta, \nu) \geq B$.

Then each admissible local datum satisfies Theorem A with constant $1$.

Lean: `Formalism.MainNotions.DIV.Bridge.DworkPowerSeriesWeights.thmA_of`

*Proof (outline).* Let $a$ be in the Hida setting and let $n = \lfloor a \rfloor$. Then $n \geq 1$, $|\nu_s| \leq n$, and $\log_l n \leq \log_l a$, so $n$ satisfies the same inequality on $N_0$. Statement 1 gives $K_0$ and $\zeta$, and statement 2 writes $\Theta(\varepsilon X)$ as the explicit kernel. By statement 3 it is enough to bound the coefficients of the frame jets of this kernel. A bound for the frame jets of the explicit kernel at the integer $n$ gives each coefficient a norm at most $l$ to the power minus the bound of Theorem A with $\log_l n$ in place of $\log_l a$. Since $\log_l n \leq \log_l a$, the bound with $a$ follows. $\square$

**Lemma 8.5.5 (Comparison with eleven).** Let $k \geq 3$, $w_s > 0$ and $0 \leq E_s \leq 4w_s$, with $D_s$ as in Corollary 2. Then
$$F((k-1)w) - \frac{11}{l}\sum_s w_s \leq F(D).$$

Lean: `Formalism.MainNotions.DIV.Bridge.DworkPowerSeriesWeights.local_bound_eleven_comparison`

*Proof (outline).* A comparison bound for the linear program, with $l \geq 3$, gives $F((k-1)w) - (11/l)\sum_s w_s$ minus a sum of odd-level gain terms as a lower bound for $F(D)$. Each gain term is a sum of maxima with $0$, so it is non-negative, and we drop it. $\square$

**Theorem 8.5.6 (Uniform local bound).** Each admissible local datum satisfies Theorem A with constant $1$ and Corollary 2 with constants $11$ and $1$. Each admissible one-letter datum satisfies Theorem 1 with constant $1$.

Lean: `Formalism.MainNotions.DIV.Bridge.DworkPowerSeriesWeights.split_bound_eleven_one`

*Proof.* The three statements of [Theorem 8.5.4](/entry/thm-a-of/) are proved (the second one through [Theorem 8.4.3](/entry/beta-is-g/)), so Theorem A holds with constant $1$. For Corollary 2, take $k$, $w$ and $E$. The bound of Theorem A is at least the bound of Corollary 2. The reason: $\operatorname{base}_s \leq \operatorname{top}_s$ for each $s \in T$, and the Lemma gives $F(D) \geq F((k-1)w) - (11/l)\sum_s w_s$. The pairing bound is monotone in $B$, so Corollary 2 follows. Theorem 1 for one-letter data follows from the one-letter forms of the three statements in the same way. $\square$

### Orbit bounds

Now fix a global datum: a CM host field with the ranks $N_i$, a family of entries $E$ and its error constants. The entries give, for each word $u$, level $i$ and place $z$ of the host, a partition $\nu_{u,i,z}$, and, for each place $w$ of the base, theta series $\Theta_{u,\mu,w,i}$, a unit $\varepsilon_w$ and series $\beta_{w,z}$. Frobenius at the residue prime $p$ of $w$ permutes the places $z$. An orbit of length $n_p$ gives a local jet datum with $d = n_p$. An orbit of length $1$ gives a one-letter datum.

**Definition 8.5.7 (Core of the orbit bounds).** The core with constant $C$ is the conjunction of eight statements.

1. Orbit bounds add: if each orbit representative $r$ has a local bound $\beta_r$, then the full series has $\operatorname{val} \geq \sum_r \beta_r$.
2. The same holds at primes with $n_p = 1$.
3. The restriction of the full series to an orbit is the local datum of that orbit.
4. At primes with $n_p = 1$, the restriction to each place is admissible.
5. The orbit valuation bound: at the representatives of kind B or C the local bound is $g_0 + F_{\mathrm{orb}} - \operatorname{err}$.
6. The entries at the discriminant: at a level-free place over the ramified prime, the entries have valuation at least $-\frac12 \sum_t c_t$.
7. The valuation sum bound: at split primes $p \geq 5$ in the zero residue class with $h_p = 0$, the inert loss minus the error is at most $\rho(p)\sum_z |\nu_{u,i,z}| - C f N_i N_{i+1}(\log_p a^2 + 1)$.
8. The scaled generators: at primes of type C, the entries have valuation at least a lower constant $\operatorname{low}_p$, and the inert loss minus its error is at most $\operatorname{low}_p$ when the error constants are large.

Lean: `Formalism.MainNotions.OrbitPlaces.Core`

The shape condition on $E$ asks ten things: positive weights $w_z$; at each place, $|\nu_{u,i,z}|$ (less the first row at top places) differs from $(k-1)w_z$ (or $(k-3)w_z$ at top places) by an amount in $[0, 4w_z]$; the first row at top places is at least $2w_z$; the sizes are at most $a^2$; $2\log_5 a^2 + 2 \leq k - 1$; and four bounds on the caps and rows. The constants $(C_6, C)$ are large for the error constants $(K, c_e)$ if $C \geq 0$, $C_6 \leq c_6$, $3C \leq 1 + \delta_1$, $\delta_1, \delta_2 \geq 0$ and $3C \leq c_{\mathrm{dig}}$. With $c_6 = 12$, $c_{\mathrm{dig}} = 3$, $\delta_1 = 5$ and $\delta_2 \geq 0$, the pair $(11, 1)$ is large.

**Theorem 8.5.8 (Entries at the discriminant).** Assume that at each level-free place $w$ over the ramified prime the series has the shape
$$\Theta = \exp\Big(-S \sum_t u_t \sum_{a,b} X_{(0,t),a,b}\, X_{(1,t),a,b}\Big)\, \sigma',$$
where $(0,t)$ and $(1,t)$ are the two places over $t$, with $|S| \leq p^{1/2}$, $|u_t| \leq 1$ and $\kappa!\,\sigma'_\kappa$ integral for all $\kappa$. Then statement 6 of the core holds.

Lean: `Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.entry_divisor_bound_holds`

*Proof.* This is [Theorem 6.8.4](/entry/jet-bound-ramified-prime/) applied to the entries of $E$ and the assumed shape. $\square$

**Theorem 8.5.9 (Core from the orbit valuation bound).** Assume statement 5 of the core, the shape at the discriminant, the shape condition, and that $(C_6, C)$ is large. Then the core with constant $C$ holds.

Lean: `Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.orbit_entry_bounds_of_family`

*Proof.* Statements 1 to 4 hold for every entry family, by the orbital bounds of Volume 6. Statement 5 is assumed. Statement 6 is the previous theorem. Statement 7 follows from the shape condition and the size of the constants, by the orbital sum bound of Volume 6. For statement 8, the shape condition gives the lower bound $\operatorname{low}_p$ for the entries, and the size of the constants gives the inequality for the inert loss. $\square$

**Theorem 8.5.10 (Orbit entry bounds).** Assume that every admissible local datum satisfies Theorem A with constant $C$ and Corollary 2 with constants $C_6, C$, and every admissible one-letter datum satisfies Theorem 1 with constant $C$. Assume the shape at the discriminant, the shape condition, and that $(C_6, C)$ is large. Then the core with constant $C$ holds.

Lean: `Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.orbit_entry_bounds_hold`

*Proof.* The local bounds, the shape condition and the size of the constants give statement 5, by the orbit form of the local bounds in Volume 6. Then [Theorem 8.5.9](/entry/orbit-entry-bounds-of-family/) gives the core. $\square$

With [Theorem 8.5.6](/entry/split-bound-eleven-one/) the local hypothesis holds for $(C_6, C) = (11, 1)$.

### The sum over primes

A family class $\mathcal{C}$ is closed for a property $P$ if there is $\varepsilon_1 > 0$ such that for each $\varepsilon \in (0, \varepsilon_1]$ there are thresholds with the following property: $P$ holds for each family in $\mathcal{C}$ with parameter $\varepsilon$ that is large for these thresholds. See [Closed](/step/closed-def/). The size property says $\log \Delta_\Gamma(u) \leq C f N_m \log(f N_m)$. The service property is the conjunction of the size conditions at the type primes, the first conclusion of the jet bounds, and the column valuation away from the type primes.

**Theorem 8.5.11 (Sum over primes).** Let $\mathcal{C}$ be a family class that is closed for the size property and satisfies the sum-over-primes hypotheses: the twist system holds, and for large $x$ each family member has a kernel entry family with the unit, rationality and stability properties, the even conditions, the orbit bound without operator, the jet integrality, the shape at the discriminant and the shape condition. Then $\mathcal{C}$ is closed for the service property.

Lean: `Formalism.MainNotions.Pk.sum_over_primes_service`

*Proof (outline).* We combine four closed properties: the size property, the twist system, the kernel entry families and the count of zeros. A closed property implies a second one on large families, so the second one is closed too. We use this with zero extra thresholds. The fixed error constants are $c_6 = 12$, $c_{\mathrm{dig}} = 3$ and $\delta_1 = 5$, so $(11, 1)$ is large. The size property gives an admissible size constant. The twist system and the count of zeros give the unit bound. For $x$ at least $3^{5/e_z}$ the split bound is at least $3$, so the orbits are admissible. The kernel entry family gives an entry family with the shape at the discriminant and the shape condition. With [Theorem 8.5.6](/entry/split-bound-eleven-one/) and [Theorem 8.5.10](/entry/orbit-entry-bounds-hold/), the entry family is admitted. The four orbit conditions then give the service property. $\square$

**Remark 8.5.12 (Formalization).** Statements 1 to 3 of [Theorem 8.5.4](/entry/thm-a-of/) are inputs. They are proved in [UniformBoundAllData.lean](lean:Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/UniformBoundAllData.lean#L26) and [OneLetterJetKernel.lean](lean:Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/OneLetterJetKernel.lean#L54). The condition on $K_0$ and $\zeta$, the explicit kernel, the frame-jet bound for the kernel and the comparison bound for the linear program are not unfolded here. Corollary 2 is defined twice, in [LocalBoundElevenComparison.lean](lean:Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/LocalBoundElevenComparison.lean#L13) and in [OrbitPlaces.lean](lean:Formalism/SharpRestriction/Divisibility/OrbitPlaces.lean#L315), with the same body. The core ([OrbitPlaces.lean](lean:Formalism/SharpRestriction/Divisibility/OrbitPlaces.lean#L1323)) does not contain $C_6$, which is used only in the hypotheses. The theorem for a family takes the orbit valuation bound for one family, not for a family of data. In the sum over primes, the extra thresholds are zero and the large-family hypothesis is not used. The orbital facts of Volume 6 used in the proofs of the core are not opened here.
