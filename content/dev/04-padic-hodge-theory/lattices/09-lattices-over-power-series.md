---
title: Lattices over power series and the assembled Theorem E
decls:
  - Formalism.ExponentWindows.E.theorem_E_assembled
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattices over power series and the assembled Theorem E

[The final form of Theorem E](/entry/theorem-e-final-form/), used in [Theorem E in lifting form](/entry/crystalline-lifting-second-form/), is a statement about modules over a power series ring with two commuting operators. This section sets up that language: Frobenius bases, lattices over a base with their cocycles, cuts, the good conditions, and extensions. Then it proves the first form of Theorem E, the *assembled form*: if each arc vector of the target lifts at each cut with a bounded exponent, then every cocycle of the target that comes from a good extension lifts up to a coboundary. The next sections replace the lifting hypothesis at the cuts by conditions on the levels of the arcs.

Throughout, $\mathcal{O}$ is a commutative ring and $\mathcal{O}[[X]]$ is the ring of formal power series over $\mathcal{O}$. Indices $i$ run over $\mathbb{Z}/n$ with $n \ge 1$, as the letters of the first section do.

**Definition 8.9.1 (Frobenius base).** A *Frobenius base* over $\mathcal{O}$ is a number $\ell \in \mathbb{N}$ and two $\mathcal{O}$-algebra endomorphisms $\varphi$ and $\gamma$ of $\mathcal{O}[[X]]$ that commute. Put
$$q = X + \ell, \qquad p_s = \varphi^s(q) \quad (s \ge 0).$$

In the application $\mathcal{O}$ is the ring of integers of the coefficient field, $\ell = p$, $\varphi$ is the Frobenius and $\gamma$ a generator of $\Gamma$ acting on $\mathcal{O}[[X]]$, as in [the realisation of the arc data](/entry/realised2-pf/). The elements $p_s$ play the part of the products $\varphi^s(q)$ in $\Lambda_H$.

**Definition 8.9.2 (Lattice over a base).** Let $B$ be a Frobenius base. A *lattice over* $B$ with $n$ letters is an $\mathcal{O}[[X]]$-module $V$ with additive maps $\varphi_i, \gamma_i \colon V \to V$ for $i \in \mathbb{Z}/n$ and submodules $N_i \subseteq V$, such that
$$\varphi_i(a v) = \varphi(a) \varphi_i(v), \qquad \gamma_i(a v) = \gamma(a) \gamma_i(v), \qquad \varphi_i \circ \gamma_{i-1} = \gamma_i \circ \varphi_i$$
for $a \in \mathcal{O}[[X]]$ and $v \in V$. A *map of lattices* $h \colon V \to V'$ over $B$ is an $\mathcal{O}[[X]]$-linear map with $h \circ \varphi_i = \varphi'_i \circ h$, $h \circ \gamma_i = \gamma'_i \circ h$ and $h(N_i) \subseteq N'_i$.

So $V$ plays the part of the coordinates of [the realisation of the arc data](/entry/realised2-pf/), $N_i$ is the Wach module at the letter $i$, and $\varphi_i$ goes from the letter $i - 1$ to the letter $i$. For a submodule $S$ and $a \in \mathcal{O}[[X]]$ write $a S = \{a s : s \in S\}$ and $(S : a) = \{v \in V : a v \in S\}$. The *$k$-fold pull* of $N_c$ is the submodule $\mathrm{Pull}(c, k)$ spanned by the elements $\varphi_{c+k} \circ \dots \circ \varphi_{c+1}(v)$ with $v \in N_c$; it lies over the letter $c + k$. An element $w$ is *$\gamma$-congruent at* $c$ if $\gamma_c(w) - w \in X N_c$.

**Definition 8.9.3 (Cocycles and coboundaries).** For $m \colon \mathbb{Z}/n \to V$ put
$$(d_\varphi m)_i = \varphi_i(m_{i-1}) - m_i, \qquad (d_\gamma m)_i = \gamma_i(m_i) - m_i.$$
A pair $(y, z)$ of maps $\mathbb{Z}/n \to V$ is a *cocycle* if $d_\gamma y = d_\varphi z$, and a *coboundary* if there is $m \colon \mathbb{Z}/n \to V$ with $y = d_\varphi m$ and $z = d_\gamma m$.

This is the Herr complex of a $(\varphi, \Gamma)$-module, written letter by letter: a class of $H^1$ is given by its $\varphi$-part $y$ and its $\gamma$-part $z$. A coboundary is a cocycle, since $\varphi_i \circ \gamma_{i-1} = \gamma_i \circ \varphi_i$.

**Definition 8.9.4 (Cuts).** A *set of cuts* for $n$ is a nonempty finite set $\mathcal{C} \subseteq \mathbb{Z}/n$ with a length $\ell_c$ for each $c \in \mathcal{C}$, such that $1 \le \ell_c \le n$, $c - \ell_c \in \mathcal{C}$, and $c - k \notin \mathcal{C}$ for $1 \le k < \ell_c$.

This is the first condition of the cuts of [Theorem E in lifting form](/entry/crystalline-lifting-second-form/). The arc of $c$ runs from the previous cut $c' = c - \ell_c$ to $c$.

**Definition 8.9.5 (Good base and good lattice).** Fix $j, M, g, \sigma \in \mathbb{N}$ and put $f = X^M \prod_{s < j} p_s^{3g}$. The base is *good* if $\gamma(X) \in (X)$, $\gamma(f) \in (f)$ and $\varphi^j(X)^M \in (f)$. Let $c$ be a cut. A *transport* of $z \in X N_c$ is an element $\tau \in \mathrm{Pull}(c, j)$ such that for some $K$ and some $v \in X N_c$,
$$\begin{aligned} \gamma_c(v) - v - \ell^K z &\in X^M N_c, \\ \ell^K \tau - \ell^\sigma \varphi^j(v) &\in f\, \mathrm{Pull}(c, j). \end{aligned}$$
A lattice is *good* for the cuts $\mathcal{C}$ if:

1. $\gamma_i(v) - v \in X N_i$ for $v \in N_i$;
2. $\varphi_i$ maps $X^M N_{i-1}$ into $X^M N_i$;
3. for every $t$ with $t_i \in X^M N_i$ there is exactly one $z$ with $z_i \in X^M N_i$ and $d_\varphi z = t$;
4. $f\, \mathrm{Pull}(c, j) \subseteq X^M N_{c+j}$ for each cut $c$;
5. every $z \in X N_c$ has a transport, for each cut $c$;
6. if $v \in X N_c$ and $\gamma_c(v) - v \in X^M N_c$, then $\ell^K v \in X^M N_c$ for some $K$;
7. if $v \in \mathrm{Pull}(c, j)$ and $\ell^K v \in f\, \mathrm{Pull}(c, j)$, then $v \in f\, \mathrm{Pull}(c, j)$;
8. $\ell v = 0$ implies $v = 0$.

Condition 3 says that $\varphi - 1$ is invertible deep in the filtration by powers of $X$; condition 5 moves a $\gamma$-part along $j$ steps of the arc with the loss $\ell^\sigma$.

**Definition 8.9.6 ($\rho$-cocycles and arc vectors).** Let $c$ be a cut and $w$ be $\gamma$-congruent at $c$. A pair $(y, z)$ is a *$\rho$-cocycle of* $w$ if there is a transport $\tau$ of $\gamma_c(w) - w$ such that $y$ is zero except at the letter $c + j$, where it is $\ell^\sigma \varphi^j(w) - \tau$, and $(y, z)$ is a cocycle with $z_i \in X^M N_i$ for all $i$. Let $\Lambda \colon \mathbb{Z}/n \to \mathcal{O}[[X]]$. An *arc vector* at $c$ is an element $w$ that is $\gamma$-congruent at $c$ with $w \in (\mathrm{Pull}(c', \ell_c) : \Lambda_c)$, where $c' = c - \ell_c$.

So an arc vector is a vector at $c$ that becomes a pull of the Wach module at the previous cut after multiplication by $\Lambda_c$. In the application $\Lambda_c$ is the element $\Lambda_H$ of the arc data.

**Definition 8.9.7 (Extensions).** Let $V_2$ and $V_0$ be lattices over $B$. An *extension* of $V_0$ by $V_2$ is a lattice $Y$ with maps of lattices $\iota \colon V_2 \to Y$ and $\pi \colon Y \to V_0$ such that $\iota$ is injective and the kernel of $\pi$ is the image of $\iota$. Let $e_0 \in V_0$. The extension *represents* a pair $(y, z)$ for $V_2$ at $e_0$ if there is $E \colon \mathbb{Z}/n \to Y$ with $\pi(E_i) = e_0$, $\iota(y_i) = (d_\varphi E)_i$ and $\iota(z_i) = (d_\gamma E)_i$ for all $i$. It is *good* with exponent $r$ if: for each cut $c$ some element of $N_c(Y)$ maps to $\ell^r e_0$; $Y$ satisfies condition 1 of a good lattice; $\iota(u) \in X^k N_i(Y)$ implies $u \in X^k N_i(V_2)$; $Y$ satisfies conditions 4 and 7 at each cut; $N_c(Y) \subseteq (\mathrm{Pull}_Y(c', \ell_c) : \Lambda_c)$ at each cut; and $\iota(u) \in (\mathrm{Pull}_Y(c', \ell_c) : \Lambda_c)$ implies $u \in (\mathrm{Pull}_{V_2}(c', \ell_c) : \Lambda_c)$.

If $e_0$ is fixed by all $\varphi_i$ and $\gamma_i$, a represented pair is a cocycle, and its class is the class of the extension. This is the usual dictionary between $H^1$ and extensions of the unit object.

The assembled form rests on four results about $\rho$-cocycles and extensions. Fix a good base and a set of cuts, and let $c$ be a cut.

1. *Existence.* In a good lattice, every $w$ that is $\gamma$-congruent at $c$ has a $\rho$-cocycle.
2. *Linearity.* In a good lattice, if $(y, z)$ is a $\rho$-cocycle of $w$, $(y', z')$ is one of $w'$, $m \in \mathcal{O}$ and $w' - m w \in X N_c$, then $(y' - m y, z' - m z)$ is a coboundary.
3. *Functoriality.* A map of lattices $h$ sends a $\rho$-cocycle of $w$ to a $\rho$-cocycle of $h(w)$.
4. *Splitting.* Let $M \ge 1$, let the base be good, $V_2$ be good, $j \le \ell_c$ for all cuts, and let $e_0 \in V_0$ be fixed by all $\varphi_i$ and $\gamma_i$. If a good extension with exponent $r$ represents $(y_0, z_0)$, then there are arc vectors $w_c$ of $V_2$ at each cut, with $\rho$-cocycles $(y_c, z_c)$, such that
$$\Bigl( \ell^{r + 2\sigma} y_0 - \sum_{c \in \mathcal{C}} y_c,\ \ell^{r + 2\sigma} z_0 - \sum_{c \in \mathcal{C}} z_c \Bigr)$$
is a coboundary.

So a class that comes from a good extension is, up to $\ell^{r + 2\sigma}$, a sum of $\rho$-cocycles of arc vectors, one at each cut.

**Theorem 8.9.8 (Assembled form of Theorem E).** Let $B$ be a Frobenius base with $\ell$, let $\mathcal{C}$ be a set of cuts, $\Lambda \colon \mathbb{Z}/n \to \mathcal{O}[[X]]$, and $j, M, g, \sigma, r, a_0, \kappa \in \mathbb{N}$. Let $h \colon V_1 \to V_2$ be a map of lattices, $V_0$ a lattice with $e_0 \in V_0$, and $Z_1$, $Z_2$ additive subgroups of pairs for $V_1$ and $V_2$. Assume:

1. $M \ge 1$, the base is good, $V_1$ and $V_2$ are good, and $j \le \ell_c$ for each cut $c$;
2. $\varphi_i(e_0) = \gamma_i(e_0) = e_0$ for all $i$;
3. $Z_1$ is stable under multiplication by $\mathcal{O}$, and contains every $\rho$-cocycle of every arc vector of $V_1$ at every cut;
4. every $\kappa' \in Z_2$ is represented at $e_0$ by a good extension of $V_0$ by $V_2$ with exponent $r$;
5. (*arc lifting*) for each cut $c$ and each arc vector $w$ of $V_2$ at $c$ there are an arc vector $w'$ of $V_1$ at $c$, a number $k \le 2\kappa$ and a unit $\varepsilon \in \mathcal{O}^\times$ with
$$h(w') - \varepsilon\, \ell^{2\sigma + 2a_0 + r + k} w \in X N_c(V_2).$$

Then for every $\kappa' \in Z_2$ there is $\kappa_1 \in Z_1$ such that $\ell^{2r + 4\sigma + 2a_0 + 2\kappa} \kappa' - h(\kappa_1)$ is a coboundary of $V_2$.

Lean: `Formalism.ExponentWindows.E.theorem_E_assembled`.

*Proof.* Let $\kappa' = (y_0, z_0) \in Z_2$. By hypothesis 4 a good extension represents it, and splitting gives arc vectors $w_c$ of $V_2$ with $\rho$-cocycles $(y_c, z_c)$ such that $\ell^{r+2\sigma} \kappa' - \sum_c (y_c, z_c)$ is a coboundary. At each cut, arc lifting gives $w'_c$, $k_c \le 2\kappa$ and $\varepsilon_c$; put $m_c = \varepsilon_c \ell^{2\sigma + 2a_0 + r + k_c}$. By existence, $w'_c$ has a $\rho$-cocycle $(Y_c, Z'_c)$ in $V_1$, and by functoriality $h(Y_c, Z'_c)$ is a $\rho$-cocycle of $h(w'_c)$. Since $h(w'_c) - m_c w_c \in X N_c$, linearity shows that $h(Y_c, Z'_c) - m_c (y_c, z_c)$ is a coboundary. Put $a_c = \varepsilon_c^{-1} \ell^{2\kappa - k_c}$, so that $a_c m_c = \ell^{r + 2\sigma + 2a_0 + 2\kappa}$, and
$$\kappa_1 = \sum_{c \in \mathcal{C}} a_c (Y_c, Z'_c).$$
By hypothesis 3, $\kappa_1 \in Z_1$. With $E = r + 2\sigma + 2a_0 + 2\kappa$,
$$\begin{aligned} \ell^{E + r + 2\sigma} \kappa' - h(\kappa_1) = {} & \ell^{E} \Bigl( \ell^{r + 2\sigma} \kappa' - \sum_c (y_c, z_c) \Bigr) \\ & - \sum_c a_c \bigl( h(Y_c, Z'_c) - m_c (y_c, z_c) \bigr), \end{aligned}$$
a combination of coboundaries with coefficients in $\mathcal{O}$, hence a coboundary. Finally $E + r + 2\sigma = 2r + 4\sigma + 2a_0 + 2\kappa$. $\square$

The exponent has two halves: $r + 2\sigma$ is lost in splitting the class into arc vectors, and $r + 2\sigma + 2a_0 + 2\kappa$ in lifting each arc vector. The arc lifting hypothesis is the hard one. The next section derives it from a description of each arc by its levels.

**Remark 8.9.9 (Formalization).** The assembled form is a step below the declarations of this chapter; it prepares [the full form](/entry/theorem-e-full-form/). The base is `Base`, lattices are `Lat`, maps are `LatHom` ([IsCocycle.lean](lean:Formalism/DistinguishedUnitIdeals/IsCocycle.lean#L8)); cuts, the good conditions, transports (`IsTr`), $\rho$-cocycles (`IsRho`), arc vectors (`Wc`) and extensions (`Ext`, `Ext.Rep`, `Ext.Good`) are in StatementE.lean, and the assembled form is the statement `ThmEAssembly` there. The four results are `RhoExists`, `RhoLin`, `RhoFun` and `Step1`, proved as `rho_map_exists`, `rho_map_linear`, `rho_map_functorial` and `splitting_of_extension` and combined by `thmE_of` (BaseGamC.lean line 85); we read only the statements of the four results, not their proofs. In the assembled form, $\Lambda$, $Z_1$ and $Z_2$ are free data, and the map $m$ of a coboundary may be any map into $V_2$. The ring $\mathcal{O}$ is any commutative ring here; the next forms ask for a discrete valuation ring.
