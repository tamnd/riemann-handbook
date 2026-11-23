---
title: The logarithm of the uniformizer
decls:
  - GlobalTheory.LogFlat.exists_log_flat_pow_Bst
  - GlobalTheory.T.exists_log_teichmuller_pow_semistablePeriods
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The logarithm of the uniformizer

Let $K$ be a finite extension of $\mathbb{Q}_\ell$ with a uniformizer $\pi$ of ramification index $e$. The semistable period ring $B_{\mathrm{st}}$ is $B_{\mathrm{cris}}$ with a logarithm of $[\ell^\flat]$ adjoined. To compare semistable representations of $G_K$ with modules over the power series ring $\mathfrak{S} = W[[X]]$, where $X$ maps to $[\pi^\flat]$, we need a logarithm of $[\pi^\flat]$ instead. This section proves that $B_{\mathrm{st}}$ contains an element that behaves like $e \log [\pi^\flat]$: it moves under $G_K$ by multiples of $t$ through a cocycle that vanishes on the stabilizer of $\pi^\flat$, and it is approximated modulo each power of the filtration of $B_{\mathrm{dR}}^+$ by elements of $E\mathfrak{S}$. The result is the first step of the construction of [period matrices over $A_{\mathrm{cris}}$](/entry/sst-periods/) in the next section.

Throughout the chapter, $\ell$ is a prime, $\Omega = \overline{\mathbb{Q}}_\ell$, $C = \mathbb{C}_\ell$ is its completion, and $G = \mathrm{Gal}(\Omega/\mathbb{Q}_\ell)$. A finite extension $K$ of $\mathbb{Q}_\ell$ is taken inside $\Omega$, and $G_K \subset G$ is its Galois group. We use the [period rings](/learn/galois-representations/#period-rings) of the Background ([[Fontaine's period rings|K6HW8YWCQJ]]), with $\ell$ in place of $p$: the tilt $\mathcal{O}_{C^\flat}$ and its fraction field $C^\flat$, the rings $A_{\mathrm{inf}} = W(\mathcal{O}_{C^\flat}) \subset W(C^\flat)$ of [[Witt vectors|6N3X2QX4W9]] with the Frobenius $\varphi$, the map $\theta : A_{\mathrm{inf}} \to \mathcal{O}_C$, the rings $A_{\mathrm{cris}}$, $B_{\mathrm{cris}}$, $B_{\mathrm{dR}}^+$ and $B_{\mathrm{dR}}$. We write $\iota : A_{\mathrm{inf}} \to B_{\mathrm{dR}}^+$ and $j : A_{\mathrm{cris}} \to B_{\mathrm{dR}}^+$ for the natural maps, and $\mathrm{Fil}^m B_{\mathrm{dR}}^+$ for the $m$-th power of the maximal ideal of $B_{\mathrm{dR}}^+$. For $x \in \mathcal{O}_{C^\flat}$ we write $x^{(m)} \in \mathcal{O}_C$ for its $m$-th component, so that $(x^{(m+1)})^\ell = x^{(m)}$ and $x^{(0)} = x^\sharp$.

**Definition 3.1.1 (Normalized periods).** We fix the following data. A sequence $(\zeta_{\ell^m})_{m \geq 0}$ in $\Omega$ with $\zeta_1 = 1$, $\zeta_{\ell^{m+1}}^\ell = \zeta_{\ell^m}$ and $\zeta_\ell \neq 1$. The element $\varepsilon \in \mathcal{O}_{C^\flat}$ with $\varepsilon^{(m)} = \zeta_{\ell^m}$. The period $t \in A_{\mathrm{cris}}$, the logarithm of $[\varepsilon]$, given as the limit of the truncated series $\sum_{k < n} (-1)^k ([\varepsilon] - 1)^{k+1}/(k+1)$. The [[cyclotomic character|XSGB5K2KEG]] $\chi : G \to \mathbb{Z}_\ell^\times$, with $g(\zeta) = \zeta^{\chi(g)}$ for each root of unity $\zeta$ of $\ell$-power order ([the cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules)). Then $g(t) = \chi(g) t$.

We also fix a sequence $(\ell_m)_{m \geq 0}$ in $\Omega$ with $\ell_0 = \ell$ and $\ell_{m+1}^\ell = \ell_m$.

**Definition 3.1.2 (Kummer exponent).** Let $x \in \mathcal{O}_{C^\flat}$, $g \in G$ and $c \in \mathbb{Z}_\ell$. Then $c$ is a *Kummer exponent of $x$ at $g$* if $g(x)^{(m)} = \zeta_{\ell^m}^{c} \, x^{(m)}$ for all $m \geq 0$, where $\zeta_{\ell^m}^c$ means $\zeta_{\ell^m}^{c \bmod \ell^m}$. Equivalently, $g(x) = \varepsilon^c x$ in $\mathcal{O}_{C^\flat}$. The *Kummer cocycle* of $\ell$ is the map $c_\ell : G \to \mathbb{Z}_\ell$ with $g(\ell_m) = \zeta_{\ell^m}^{c_\ell(g)} \ell_m$ for all $m$. It satisfies $c_\ell(gh) = c_\ell(g) + \chi(g) c_\ell(h)$.

The value $c_\ell(g)$ exists and is unique because $g(\ell_m)/\ell_m$ is a root of unity of order dividing $\ell^m$, and these roots are compatible in $m$.

**Definition 3.1.3 (The semistable period ring).** Let $B_{\mathrm{st}} = B_{\mathrm{cris}}[X]$ be the polynomial ring in one variable. An element $g \in G$ acts on $B_{\mathrm{st}}$ as the unique ring map that is $g$ on $B_{\mathrm{cris}}$ and sends $X$ to $X + c_\ell(g) t$. The Frobenius $\varphi$ is $\varphi$ on $B_{\mathrm{cris}}$ and sends $X$ to $\ell X$. The monodromy operator is $N = -d/dX$. For a finite extension $L$ of $\mathbb{Q}_\ell$ and a representation $V$ of $G_K$ on a finite-dimensional $L$-vector space, put $D_{\mathrm{st}}(V) = (V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{st}})^{G_K}$. Then $V$ is *semistable* if $\dim_L D_{\mathrm{st}}(V) = [K_0 : \mathbb{Q}_\ell] \dim_L V$, where $K_0$ is the maximal unramified subfield of $K$.

The cocycle law for $c_\ell$ makes the action a group action. The variable $X$ plays the role of $\log [\ell^\flat]$, where $\ell^\flat \in \mathcal{O}_{C^\flat}$ is the element with $(\ell^\flat)^{(m)} = \ell_m$: both move by $c_\ell(g) t$ under $g$, and $\varphi$ multiplies both by $\ell$. This is the ring of the Background, with $u = X$.

**Definition 3.1.4 (Breuil-Kisin datum).** A *Breuil-Kisin datum* for $K$ consists of the following.

1. An integer $a \geq 1$. Put $W = W(\mathbb{F}_{\ell^a})$ and $\mathfrak{S} = W[[X]]$.
2. A monic polynomial $E \in W[X]$ of degree $e > 0$ whose coefficients of degree below $e$ are divisible by $\ell$, whose constant term is $\ell$ times a unit, and which has a nonzero coefficient in a degree prime to $\ell$.
3. A ring isomorphism $\mathcal{O}_K \cong \mathfrak{S}/(E)$.
4. Let $\varphi$ on $\mathfrak{S}$ be the Frobenius of $W$ on coefficients with $\varphi(X) = X^\ell$, and $\delta$ the fixed $\delta$-structure on $\mathfrak{S}$. Then $\delta(E)$ is a unit and $\mathfrak{S}$ is complete for the ideal $(\ell, E)$.
5. An element $\pi^\flat \in \mathcal{O}_{C^\flat}$ and a ring map $\mathrm{ev} : \mathfrak{S} \to A_{\mathrm{inf}}$ with $\mathrm{ev}(X) = [\pi^\flat]$, which on $W$ is the map $W(\mathbb{F}_{\ell^a}) \to W(\mathcal{O}_{C^\flat})$ induced by a fixed embedding of $\mathbb{F}_{\ell^a}$ into $\mathcal{O}_{C^\flat}$, and with $\mathrm{ev} \circ \varphi = \varphi \circ \mathrm{ev}$.
6. The kernel of $\theta$ is generated by $\mathrm{ev}(E)$, and $\theta(\mathrm{ev}(x))$ is the image of $r \in \mathcal{O}_K$ whenever $x \bmod E$ corresponds to $r$.
7. $G_K$ fixes $\mathrm{ev}(W)$.

Let $\pi \in \mathcal{O}_K$ correspond to the class of $X$. Since $E$ is Eisenstein, the class of $X$ generates the maximal ideal of $\mathfrak{S}/(E)$, so $\pi$ is a uniformizer, and $e$ is the ramification index of $K$ over its subfield $W[1/\ell]$. By 6, $\theta([\pi^\flat]) = (\pi^\flat)^\sharp = \pi$. So $\pi^\flat$ is a tilt of the uniformizer. Put $G_\infty = \{ g \in G_K : g(\pi^\flat) = \pi^\flat \}$. This is the Galois group of the field generated over $K$ by a compatible system of $\ell$-power roots of $\pi$.

**Lemma 3.1.5 (Existence of Breuil-Kisin data).** Every finite extension $K$ of $\mathbb{Q}_\ell$ in $\Omega$ has a Breuil-Kisin datum.

Lean: `GlobalTheory.BSP.nonempty_bk_of_finExt`.

**Theorem 3.1.6 (A logarithm of a power of $[\pi^\flat]$).** Fix a Breuil-Kisin datum for $K$ and let $e = \deg E$. There are $b \in B_{\mathrm{cris}}$ and a map $c : G_K \to \mathbb{Z}_\ell$ with the following properties.

1. For all $g \in G_K$, $g(X + b) = X + b + c(g) t$ in $B_{\mathrm{st}}$, and $\varphi(X + b) = \ell (X + b)$.
2. $c(g) = 0$ for $g \in G_\infty$.
3. For each $m \geq 0$ there are $k \in \mathbb{N}$ and $s \in \mathfrak{S}$ with $E \mid s$ such that, for all $g \in G_K$,
$$\iota\big(g(\mathrm{ev}(s)) - \mathrm{ev}(s)\big) - \ell^k c(g) \, j(t) \in \mathrm{Fil}^m B_{\mathrm{dR}}^+.$$

Lean: `GlobalTheory.LogFlat.exists_log_flat_pow_Bst` (also `GlobalTheory.T.exists_log_teichmuller_pow_semistablePeriods`, a second name).

The proof combines five facts about $\mathcal{O}_{C^\flat}$ and $B_{\mathrm{cris}}$. We state them as lemmas and use them without proof here.

**Lemma 3.1.7 (The tilt of $\ell$).** There is $\varpi \in \mathcal{O}_{C^\flat}$ with $\varpi^{(m)} = \ell_m$ for all $m$. In particular $\varpi^\sharp = \ell$.

Lean: `GlobalTheory.Pst.NoLog.exists_tilt`.

**Lemma 3.1.8 (Power of the tilt of the uniformizer).** If $\varpi \in \mathcal{O}_{C^\flat}$ and $\varpi^\sharp = \ell$, then $(\pi^\flat)^e = \varpi x$ for a unit $x$ of $\mathcal{O}_{C^\flat}$.

Lean: `GlobalTheory.T.tilt_uniformizer_pow_eq_mul_unit`.

The reason is that $\pi^e$ and $\ell$ have the same absolute value, and $|y| = |y^\sharp|$ on $C^\flat$.

**Lemma 3.1.9 (Kummer cocycle of $\pi^\flat$).** There is $c_\pi : G_K \to \mathbb{Z}_\ell$ such that $c_\pi(g)$ is a Kummer exponent of $\pi^\flat$ at $g$ for each $g \in G_K$, and $c_\pi(g) = 0$ for $g \in G_\infty$.

Lean: `GlobalTheory.T.exists_kummer_cocycle_tilt_uniformizer`.

**Lemma 3.1.10 (Logarithm of a unit).** Let $x$ be a unit of $\mathcal{O}_{C^\flat}$. There is $b_x \in B_{\mathrm{cris}}$ with $\varphi(b_x) = \ell b_x$ such that $g(b_x) = b_x + c t$ whenever $g \in G$ and $c$ is a Kummer exponent of $x$ at $g$.

Lean: `GlobalTheory.T.exists_teichmuller_log_unit_bcris`.

One thinks of $b_x$ as $\log [x]$. Then $\varphi(\log [x]) = \log [x^\ell] = \ell \log [x]$ and $g(\log [x]) = \log [\varepsilon^c x] = \log[x] + c t$.

**Lemma 3.1.11 (Truncated logarithm).** Let $c_\pi$ be as in the lemma on the Kummer cocycle of $\pi^\flat$. For each $m \geq 0$ there are $k \in \mathbb{N}$ and $s \in \mathfrak{S}$ with $E \mid s$ such that $\iota(g(\mathrm{ev}(s)) - \mathrm{ev}(s)) - \ell^k e \, c_\pi(g) \, j(t) \in \mathrm{Fil}^m B_{\mathrm{dR}}^+$ for all $g \in G_K$.

Lean: `GlobalTheory.T.exists_truncLog_gal_mod_filP`.

The last lemma is elementary.

**Lemma 3.1.12 (Exponents of a product).** Let $y, \varpi, x \in \mathcal{O}_{C^\flat}$ and $n \in \mathbb{N}$ with $y^n = \varpi x$ and $\varpi^\sharp \neq 0$. Let $g \in G$. If $a$ is a Kummer exponent of $y$ at $g$ and $b$ is a Kummer exponent of $\varpi$ at $g$, then $n a - b$ is a Kummer exponent of $x$ at $g$.

Lean: `GlobalTheory.LogFlat.rootT_cocycle_of_pow_eq_mul`.

*Proof.* The map $z \mapsto z^{(m)}$ is multiplicative and commutes with $g$. So $g(x)^{(m)} \varpi^{(m)} \zeta_{\ell^m}^{b} = g(\varpi x)^{(m)} = g(y^n)^{(m)} = \zeta_{\ell^m}^{n a} (y^{(m)})^n = \zeta_{\ell^m}^{na} \varpi^{(m)} x^{(m)}$. Since $\varpi^\sharp \neq 0$, also $\varpi^{(m)} \neq 0$, and we can cancel it. $\square$

**Lemma 3.1.13 (The cocycle of $\ell^\flat$).** Let $\varpi$ be as in the lemma on the tilt of $\ell$. Then $c_\ell(g)$ is a Kummer exponent of $\varpi$ at $g$ for each $g \in G$.

Lean: `GlobalTheory.LogFlat.rootT_σF_tilt_l`.

*Proof.* We have $g(\varpi)^{(m)} = g(\varpi^{(m)}) = g(\ell_m) = \zeta_{\ell^m}^{c_\ell(g)} \ell_m = \zeta_{\ell^m}^{c_\ell(g)} \varpi^{(m)}$. $\square$

*Proof of the theorem.* Take $\varpi$ with $\varpi^{(m)} = \ell_m$ (the tilt of $\ell$). Then $(\pi^\flat)^e = \varpi x$ with $x$ a unit (power of the tilt of the uniformizer). Take $c_\pi$ from the lemma on the Kummer cocycle of $\pi^\flat$ and $b_x$ from the lemma on the logarithm of a unit. Put $b = b_x$ and $c(g) = e \, c_\pi(g)$.

Let $g \in G_K$. The element $c_\pi(g)$ is a Kummer exponent of $\pi^\flat$ at $g$, and $c_\ell(g)$ is one of $\varpi$ (the cocycle of $\ell^\flat$). By the lemma on exponents of a product, with $y = \pi^\flat$ and $n = e$, the element $e c_\pi(g) - c_\ell(g)$ is a Kummer exponent of $x$ at $g$. Hence $g(b) = b + (e c_\pi(g) - c_\ell(g)) t$. With $g(X) = X + c_\ell(g) t$ this gives
$$g(X + b) = X + c_\ell(g) t + b + (e c_\pi(g) - c_\ell(g)) t = X + b + c(g) t.$$
Also $\varphi(X + b) = \ell X + \ell b$. This proves 1. Property 2 holds because $c_\pi(g) = 0$ on $G_\infty$. Property 3 is the lemma on the truncated logarithm, since $c(g) = e c_\pi(g)$. $\square$

In terms of logarithms, $X + b$ is $\log [\ell^\flat] + \log [x] = \log [(\pi^\flat)^e] = e \log [\pi^\flat]$, and $c(g) t$ is $e \log [\varepsilon^{c_\pi(g)}]$.

**Remark 3.1.14 (Formalization).** The theorem takes a hypothesis `True`, which carries no information. The ring $B_{\mathrm{cris}}$ of the statement is the abstract crystalline ring of a fixed set of period data, and $B_{\mathrm{st}}$ is the polynomial ring over it. The element $b$ is the image of $b_x$ under the inverse of a fixed isomorphism from that abstract ring to the concrete ring $B_{\mathrm{cris}}$ (a datum `LocTied`), and a compatibility datum `Fits` matches $t$, $\zeta$ and $\chi$ of the two models. The five input lemmas (`exists_tilt`, `tilt_uniformizer_pow_eq_mul_unit`, `exists_kummer_cocycle_tilt_uniformizer`, `exists_teichmuller_log_unit_bcris`, `exists_truncLog_gal_mod_filP`) are not unfolded in this chapter. The reading of $X + b$ as $e \log[\pi^\flat]$ is ours; it is not a statement of the theorem.
