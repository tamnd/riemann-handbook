---
title: The crystalline period map
decls:
  - CrystallineSemistableComparison.Pb.rhoSys_ex'
  - CrystallineSemistableComparison.Pb.crystalline_deRham_firstChern_exists
  - CrystallineSemistableComparison.Pb.pmap
  - CrystallineSemistableComparison.Pb.pSeam
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The crystalline period map

The Hodge-Tate map of the [earlier sections](/entry/hodge-tate-of-etale-side/) pairs étale classes with Hodge classes and takes values in $\mathbb{C}_\ell$. The crystalline comparison needs a finer pairing. It pairs crystalline classes over Fontaine's ring $A_{\mathrm{cris}}$ with de Rham classes of the generic fibre, and it takes values in $B_{\mathrm{dR}}$ (see [[Fontaine's period rings|K6HW8YWCQJ]] and the Background on [period rings](/learn/galois-representations/#period-rings)). This section builds that pairing for smooth models. We call it the *period map*. Its last property is the one with content: the top power of a first Chern class pairs to a unit of $B_{\mathrm{dR}}^+$. The proof of that property uses the [nonvanishing of the top power](/entry/pow-k-ne-zero/) of the de Rham first Chern class. At the end we collect the period map with three simpler facts into one statement, which the [geometric steps](/entry/steps-holds/) use.

We keep the notation of the earlier sections. So $\ell$ is a prime, $K$ is a finite extension of $\mathbb{Q}_\ell$ inside $\overline{\mathbb{Q}}_\ell$, and a model $\mathfrak{X}$ is a scheme over $\mathcal{O}_K$ with generic fibre $X$. A model is *smooth* when it is projective, strictly semistable and smooth over $\mathcal{O}_K$. We write $H^j_{\mathrm{dR}}(X)$ for the de Rham cohomology of $X$ on the thickening site, with its Hodge filtration $\mathrm{Fil}^r$ (see the Background on [de Rham cohomology](/learn/geometry/#de-rham-cohomology-and-deformations) and [[algebraic de Rham cohomology|13F5JZPDD0]]). We write $\check{H}^j = \mathrm{Hom}_K(H^j_{\mathrm{dR}}(X), K)$ for its dual.

**Definition 2.5.1 (Period data).** The *period data* of $K$ consist of the ring $A_{\mathrm{cris}}$, the field $B_{\mathrm{dR}}$, the subring $B_{\mathrm{dR}}^+$, the element $t \in B_{\mathrm{dR}}^+$ that generates the kernel of $\theta$, the maps $i : A_{\mathrm{cris}} \to B_{\mathrm{dR}}$ and $o : K \to B_{\mathrm{dR}}$, and the action of $G_K = \mathrm{Gal}(\overline{\mathbb{Q}}_\ell / K)$ on these rings. An element $u \in B_{\mathrm{dR}}$ is a *unit* when $u \in B_{\mathrm{dR}}^+$ and $uv = 1$ for some $v \in B_{\mathrm{dR}}^+$.

**Definition 2.5.2 (The crystalline family of a line).** Let $\mathfrak{X}$ be a model and $D$ a line datum on $\mathfrak{X}$ that is tautological, that is, it comes from $\mathcal{O}(1)$ of an embedding of $\mathfrak{X}$ in a projective space over $\mathcal{O}_K$. The *crystalline family* of $D$ is the system of $A_{\mathrm{cris}}$-modules
$$H^j(D) = \varprojlim_n H^j\big(\mathfrak{X}_{\mathcal{O}_{\mathbb{C}_\ell}/\ell^n},\, A_{\mathrm{cris}}/\ell^n\big),$$
the limit over $n$ of the cohomology of the thickening site of $\mathfrak{X}$ over $A_{\mathrm{cris}}/\ell^n$. It carries an action of $G_K$, a cup product, a unit class, and pullbacks along maps of models. A class $x \in H^2(D)$ is a *first Chern class* of $D$ when its component at each level $n$ is the first Chern class of $D$ at that level. A class $x \in H^j(D)$ lies in *filtration step $r$* when at each level it lies in the image of the $r$-th divided power of the ideal of the thickening.

**Definition 2.5.3 (Period map).** A *period map* for smooth models consists of additive maps
$$\kappa_D : H^j(D) \to \mathrm{Hom}\big(\check{H}^j,\ B_{\mathrm{dR}}\big)$$
for each model and each tautological line datum $D$, and a $K$-bilinear cup product $\cup$ on $H^\bullet_{\mathrm{dR}}(X)$, with the following properties on smooth models.

1. *Finiteness.* Each $H^j_{\mathrm{dR}}(X)$ is finite-dimensional and $\mathrm{Fil}^{j+1} H^j_{\mathrm{dR}}(X) = 0$. If $\mathfrak{X}$ is connected of dimension $d$, then $\mathrm{Fil}^{d+1} H^j_{\mathrm{dR}}(X) = 0$.
2. *Filtration of the cup product.* The cup product takes $\mathrm{Fil}^r \times \mathrm{Fil}^s$ into $\mathrm{Fil}^{r+s}$.
3. *Linearity.* $\kappa(cx)(\varphi) = i(c)\, \kappa(x)(\varphi)$ for $c \in A_{\mathrm{cris}}$, and $\kappa(x)(k\varphi) = o(k)\, \kappa(x)(\varphi)$ for $k \in K$.
4. *Galois.* $\kappa(\sigma x)(\varphi) = \sigma(\kappa(x)(\varphi))$ for $\sigma \in G_K$.
5. *Naturality.* $\kappa$ commutes with pullback along maps of models over $\mathcal{O}_K$.
6. *Filtration.* If $x$ lies in filtration step $n$ and $\varphi$ vanishes on $\mathrm{Fil}^{r+1}$, then $t^r \kappa(x)(\varphi) = t^n y$ for some $y \in B_{\mathrm{dR}}^+$.
7. *Cup product.* For $z = x \cup y$ and bases $(b_s)$, $(b'_{s'})$ of $H^i_{\mathrm{dR}}$ and $H^j_{\mathrm{dR}}$,
$$\kappa(z)(\varphi) = \sum_{s, s'} \kappa(x)(b_s^*)\, \kappa(y)(b'^*_{s'})\, o\big(\varphi(b_s \cup b'_{s'})\big).$$
8. *Top power.* If $\mathfrak{X}$ is connected of dimension $d$, then there are a first Chern class $x$ of $D$, the power $z = x^d$, and $\varphi \in \check{H}^{2d}$ such that $\kappa(z)(\varphi)$ is a unit.

A period map is the $B_{\mathrm{dR}}$ form of a de Rham comparison: property 6 says that $\kappa$ is strict for the filtrations up to powers of $t$, and property 8 says that $\kappa$ is not degenerate at the top.

We build $\kappa$ one level at a time. A *level* of index $m \geq 1$ is a divided power thickening $A_m \to B_m$ with a surjection $B_{\mathrm{dR}}^+ \to B_m$ whose kernel is $t^m B_{\mathrm{dR}}^+$, and with compatible actions of $G_K$. A *good level system* is a sequence of levels of index $m + 1$ for $m = 0, 1, \ldots$ with transition maps $A_{m+1} \to A_m$ and $B_{m+1} \to B_m$ that respect all the data, such that each compatible family $(y_m)$ with $y_m \in B_m$ comes from exactly one element of $B_{\mathrm{dR}}^+$. A level is *compatible with $A_{\mathrm{cris}}$* when the image of $\xi$ lies in the divided power ideal $I$ of $A_m$, and when $a - \lambda(w) \in I$ for every $a \in \mathcal{O}_K$ and every $w \in A_{\mathrm{inf}}$ with $\theta(w) = a$. Here $\lambda : A_{\mathrm{cris}} \to A_m$ is the map that comes with the level.

A *$\rho$-system* on a level system is a relation $\rho(x, m, f)$ between a class $x \in H^j(D)$ and an additive map $f : \check{H}^j \to B_m$. It says that $f$ is the value of $\kappa(x)$ modulo $t^{m+1}$. On smooth models it has these properties: for each $x$ and $m$ there is exactly one such $f$; $\rho$ is additive, linear over $A_{\mathrm{cris}}$ and $K$, and Galois equivariant; it is compatible with the transition maps and with pullbacks; if $x$ lies in filtration step $n$ with $n \leq m$ and $\varphi$ vanishes on $\mathrm{Fil}^{r+1}$, then $f(\varphi)$ lies in the $(n - r)$-th divided power ideal of $B_m$; it satisfies the cup product formula of property 7 and the unit formula $f(\varphi) = \varphi(1)$; and on a first Chern class $x$ of $D$ and a de Rham first Chern class $c$ of the line on $X$ it gives $f(\varphi) = \varphi(c)$.

**Lemma 2.5.4 (Existence of a $\rho$-system).** Let $(L_m)$ be a good level system such that each level is compatible with $A_{\mathrm{cris}}$. Then there is a $\rho$-system on $(L_m)$ for smooth models, with tautological lines as line data and the de Rham first Chern class of the line on the generic fibre.

Lean: `CrystallineSemistableComparison.Pb.rhoSys_ex'` (a second name for `CrystallineSemistableComparison.Pb.Kap.Mo.rhoSys_ex`).

*Proof.* This is the [existence of $\rho$-systems](/entry/rho-sys-ex/), which is proved in a later part of this chapter. At each level $m$ it realizes crystalline classes as classes on a thickening over $A_m$, and it reads them as maps on $\check{H}^j$ with values in $B_m$. $\square$

**Proposition 2.5.5 (Period pairing on first Chern classes).** There is a family of maps $\kappa_D$ with properties 3 to 7 of a period map, and with the unit property $\kappa(1)(\varphi) = o(\varphi(1))$, such that for every smooth model, every tautological line datum $D$, every first Chern class $x \in H^2(D)$ and every de Rham first Chern class $c \in H^2_{\mathrm{dR}}(X)$ of the line on $X$,
$$\kappa(x)(\varphi) = o(\varphi(c)) \quad \text{for all } \varphi \in \check{H}^2.$$

Lean: `CrystallineSemistableComparison.Pb.crystalline_deRham_firstChern_exists`.

*Proof.* The [existence of level systems](/entry/lev-sys-ex/) gives a good level system $(L_m)$ in which every level is compatible with $A_{\mathrm{cris}}$. The lemma above gives a $\rho$-system on it. For a class $x$ and $\varphi \in \check{H}^j$, the values $f_m(\varphi) \in B_m$ with $\rho(x, m, f_m)$ form a compatible family, because $\rho$ is compatible with the transition maps and $f_m$ is unique. Since $B_{\mathrm{dR}}^+$ is the limit of the $B_m$, there is a unique $\kappa(x)(\varphi) \in B_{\mathrm{dR}}^+$ with image $f_m(\varphi)$ at every level. Each property of the $\rho$-system passes to this limit and gives the matching property of $\kappa$. For property 6, an element of $B_{\mathrm{dR}}^+$ whose images in all $B_m$ lie in the divided power ideals of index $n - r$ is $t^{n-r}$ times an element of $B_{\mathrm{dR}}^+$. The property on first Chern classes gives $\kappa(x)(\varphi) = o(\varphi(c))$. $\square$

For the top power we need one fact on powers. We call it (P). Let $\kappa$ be as in the proposition, $\mathfrak{X}$ smooth, $x \in H^2(D)$ and $c \in H^2_{\mathrm{dR}}(X)$ with $\kappa(x)(\varphi) = o(\varphi(c))$ for all $\varphi$. Then for every $k \geq 0$ and every $k$-th power $z$ of $x$,
$$\kappa(z)(\varphi) = o\big(\varphi(c^k)\big) \quad \text{for all } \varphi \in \check{H}^{2k}.$$

*Proof.* We use induction on $k$. For $k = 0$ the class $z$ is the unit, and the unit property gives the claim. Let $z = y \cup x$ with $y$ a $k$-th power. Choose bases $(b_s)$ of $H^{2k}_{\mathrm{dR}}$ and $(b'_{s'})$ of $H^2_{\mathrm{dR}}$. By property 7, the induction hypothesis and the hypothesis on $x$,
$$\begin{aligned} \kappa(z)(\varphi) &= \sum_{s, s'} o\big(b_s^*(c^k)\big)\, o\big(b'^*_{s'}(c)\big)\, o\big(\varphi(b_s \cup b'_{s'})\big) \\ &= o\Big(\varphi\Big(\sum_s b_s^*(c^k)\, b_s \cup \sum_{s'} b'^*_{s'}(c)\, b'_{s'}\Big)\Big) = o\big(\varphi(c^k \cup c)\big). \end{aligned}$$
Here we use that $o$ is a ring map and that the cup product is bilinear. $\square$

Statement (P) is a step inside the proof of the next theorem. It is not a separate result of the chapter.

**Theorem 2.5.6 (The crystalline period map).** For every prime $\ell$ and every finite extension $K$ of $\mathbb{Q}_\ell$, a period map for smooth models exists, with tautological lines as line data.

Lean: `CrystallineSemistableComparison.Pb.pmap`.

*Proof.* Take $\kappa$ from the [proposition on first Chern classes](/entry/crystalline-de-rham-first-chern-exists/). Properties 3 to 7 are the properties of $\kappa$ there. Take for $\cup$ the cup product of de Rham cohomology. Properties 1 and 2 are the finiteness of de Rham cohomology of a smooth proper variety, the bounds on its Hodge filtration, and the compatibility of the cup product with the filtration. It remains to prove property 8. Let $\mathfrak{X}$ be connected of dimension $d$ and $D$ a tautological line datum on $\mathfrak{X}$.

1. The pullback of $D$ to $X$ is a tautological line on $X$.
2. There is a first Chern class $x \in H^2(D)$, and there is a de Rham first Chern class $c \in H^2_{\mathrm{dR}}(X)$ of the line on $X$.
3. Let $z \in H^{2d}(D)$ be the $d$-th power of $x$. It exists by induction on $d$, with the unit class for $d = 0$.
4. By the [nonvanishing of the top power](/entry/pow-k-ne-zero/), $c^d \neq 0$. A finite-dimensional vector space is projective, so there is $\varphi \in \check{H}^{2d}$ with $\varphi(c^d) = 1$.
5. By the proposition, $\kappa(x)(\psi) = o(\psi(c))$ for all $\psi$. Statement (P) then gives $\kappa(z)(\varphi) = o(\varphi(c^d)) = o(1) = 1$.

The element $1$ is a unit of $B_{\mathrm{dR}}^+$, with inverse $1$. So $x$, $z$ and $\varphi$ satisfy property 8. $\square$

The next statement collects the data that the crystalline comparison takes as input. It also needs a Frobenius map. A *residue datum* is a perfect field $k$ of characteristic $\ell$ with a surjection $\rho : \mathcal{O}_K \to k$ and a ring map $s$ from $k$ to the tilt of $\mathcal{O}_{\mathbb{C}_\ell}$ such that $|s(\rho(x))^\sharp - x| < 1$ for all $x \in \mathcal{O}_K$. Let $K_0 = W(k)[1/\ell]$ be the fraction field of the [[Witt vectors|6N3X2QX4W9]] of $k$. Let $D^j(\mathfrak{X})$ be the crystalline cohomology of the reduction of $\mathfrak{X}$, a $K_0$-vector space with a Frobenius $\phi_D$, and let $C$ be a period ring with a Frobenius $\phi_C$ and a map $\iota_C : C \to B_{\mathrm{dR}}$. Let $H'^j(D)$ be a second crystalline family, with a Frobenius $\phi$. A *Frobenius map* consists of an integer $e \geq 0$ and additive maps
$$\psi : H'^j(D) \to \mathrm{Hom}\big(\mathrm{Hom}_{K_0}(D^j(\mathfrak{X}), K_0),\ C\big)$$
with these properties on smooth models: $D^j(\mathfrak{X})$ is finite-dimensional; $\psi(cx) = \phi^e(c)\,\psi(x)$ for $c \in A_{\mathrm{cris}}$, and $\psi$ is $K_0$-linear in the second variable; $\psi$ is Galois equivariant and natural; for a basis $(b_s)$ of $D^j$, $\psi(\phi x)(f) = \sum_s \phi_C(\psi(x)(b_s^*))\, f(\phi_D b_s)$; and for every $G_K$-equivariant $A_{\mathrm{cris}}$-linear map $g : H'^j(D) \to B_{\mathrm{dR}}$ there are $G_K$-invariant elements $w_s(g)$ with $g(\phi^e x) = \sum_s \iota_C(\psi(x)(b_s^*))\, w_s(g)$.

**Theorem 2.5.7 (The data for the crystalline comparison).** Let $\ell$ be a prime and $K$ a finite extension of $\mathbb{Q}_\ell$. There is a property $\mathrm{Amp}$ of line data on models such that:

1. if $\mathrm{Amp}(\mathfrak{X}, D)$ holds, then the map $f$ of the line datum $D$ is étale;
2. every smooth model $\mathfrak{X}$ has a line datum $D$ with $\mathrm{Amp}(\mathfrak{X}, D)$;
3. there is a period map for smooth models with line data in $\mathrm{Amp}$;
4. for every residue datum $k$, there is a Frobenius map for smooth models with line data in $\mathrm{Amp}$.

Lean: `CrystallineSemistableComparison.Pb.pSeam`.

*Proof.* Let $\mathrm{Amp}(\mathfrak{X}, D)$ say that $D$ is a tautological line on $\mathfrak{X}$. The map $f$ of a tautological line datum is étale, which gives part 1. A smooth model is projective over $\mathcal{O}_K$, so it has a tautological line, which gives part 2. The [crystalline period map](/entry/pmap/) gives part 3. For part 4, fix a residue datum. The Frobenius map is built from the crystalline cohomology of the reduction over $K_0$ and from the [Theorem 2.12.6](/entry/fac-ex/) on the Frobenius factorisation, which gives the integer $e$ and the elements $w_s$. We take this as given here; it is proved in a later section. $\square$

**Remark 2.5.8 (Formalization).** The last theorem proves the statement `BocksteinBaseChangeP` in [BocksteinBaseChangeP.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/BocksteinBaseChangeP.lean#L27), which has neither a Bockstein map nor a base change; part 4 is `CrystallineSemistableComparison.Pb.fmap`, and a Frobenius map is `FMap`. The property $\kappa(x)(\varphi) = o(\varphi(c))$ of the proposition is `LieComplementChartContDiffAt`, whose name has no relation to its content. The lemma `levSys_ex'` is a second name for `CrystallineSemistableComparison.HT.levSys_ex`. The passage to the limit is `kap_abs`, which sets $\kappa = 0$ on models that are not smooth, and statement (P) is `kap_pow`. The families $H^j(D)$ and $H'^j(D)$ are `M.HA false` and `M.HA true`; we did not check how they differ.
