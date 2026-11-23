---
title: The Hodge-Tate pairing
decls:
  - CrystallineSemistableComparison.HT.half1
  - CrystallineSemistableComparison.HT.half2
  - CrystallineSemistableComparison.HT.ht_of
  - CrystallineSemistableComparison.HT.hodgeTate_of_etale_side
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hodge-Tate pairing

This section constructs the Hodge-Tate map from the étale cohomology of a smooth projective variety over an $\ell$-adic field to its Hodge cohomology, and proves that it is injective after extension of scalars to $\mathbb{C}_\ell$. The first half of the construction lifts an étale class, times a power of Fontaine's element $t$, to a family in the divided-power filtration over $A_{\mathrm{cris}}$; the second half reads off a Hodge class from it. Injectivity comes from the [nonvanishing of the top power of the first Chern class](/entry/pow-k-ne-zero/) and from Poincaré duality on the étale side.

Throughout, $\ell$ is a prime, $\overline{\mathbb{Q}}_\ell$ an algebraic closure of $\mathbb{Q}_\ell$, $\mathbb{C}_\ell$ its completion, and $K \subseteq \overline{\mathbb{Q}}_\ell$ a finite extension of $\mathbb{Q}_\ell$ with ring of integers $\mathcal{O}_K$ and Galois group $G_K = \operatorname{Gal}(\overline{\mathbb{Q}}_\ell / K)$. Let $\chi : G_K \to \mathbb{Z}_\ell^\times$ be the [cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules). For the period rings $A_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$, the map $\theta$ and the element $t$ see [period rings](/learn/galois-representations/#period-rings).

**Definition 2.3.1 (Models).** A *model* over $\mathcal{O}_K$ is a scheme $\mathfrak{X}$ with a map $p : \mathfrak{X} \to \operatorname{Spec} \mathcal{O}_K$. Its generic fibre is $X = \mathfrak{X} \times_{\mathcal{O}_K} K$, with $q : X \to \operatorname{Spec} K$. The model is *good* if $p$ is projective and strictly semistable. It is *smooth* if it is good and $p$ is smooth. For $d \geq 0$ the model is *connected of dimension $d$* if $X$ is connected and $q$ is smooth of relative dimension $d$.

**Definition 2.3.2 (Étale cohomology).** For a model with generic fibre $X$, let $T_n = \varprojlim_k H^n_{\mathrm{et}}(X_{\overline{\mathbb{Q}}_\ell}, \mathbb{Z}/\ell^k)$ and $V_n = \mathbb{Q}_\ell \otimes_{\mathbb{Z}_\ell} T_n$, the [étale cohomology](/learn/geometry/#tale-cohomology) of the geometric generic fibre. They carry an action of $G_K$, pullbacks along maps of models, and a cup product defined at each finite level.

We write $\mathrm{Hdg}(a, n)$ for the [Hodge cohomology on the thickening site](/entry/hodge-affine-iso-sign/) of the generic fibre $X$ over $K$. By the [Čech comparison](/entry/hodge-iso-natural-cech/), $\mathrm{Hdg}(a, n) \cong H^{n-a}(X, \Omega^a)$ when $X$ is smooth and proper.

**Definition 2.3.3 (Hodge-Tate pairing).** A *Hodge-Tate pairing* over $K$ is a family of additive maps
$$h : V_n \to \operatorname{Hom}\big(\mathrm{Hdg}(a, n)^\vee, \mathbb{C}_\ell\big),$$
one for each model and all $a, n \geq 0$, with these properties. In each property the model is smooth.

1. *Linearity.* $h(zv)(\varphi) = z\, h(v)(\varphi)$ for $z \in \mathbb{Q}_\ell$, and $h(v)(k\varphi) = k\, h(v)(\varphi)$ for $k \in K$.
2. *Finiteness.* $\mathrm{Hdg}(a, n)$ is finite-dimensional over $K$, and it is $0$ for $n < a$.
3. *Galois equivariance.* $\chi(\sigma)^a\, h(\sigma v)(\varphi) = \sigma\big(h(v)(\varphi)\big)$ for $\sigma \in G_K$.
4. *Naturality.* $h(u^* v)(\varphi) = h(v)(\varphi \circ u^*)$ for each map $u$ of smooth models over $\mathcal{O}_K$.
5. *Cup products.* If $z$ is the cup product of $x \in T_i$ and $y \in T_j$, then for bases $(b_{a,s})$ of $\mathrm{Hdg}(a, i)$ and $(b'_{a',s'})$ of $\mathrm{Hdg}(a', j)$ and $\varphi \in \mathrm{Hdg}(c, i+j)^\vee$,
$$h(z)(\varphi) = \sum_{a + a' = c} \sum_{s, s'} h(x)(b_{a,s}^*)\, h(y)(b_{a',s'}^*)\, \varphi\big(b_{a,s} \cup b'_{a',s'}\big).$$
6. *Unit.* $h(1)(\varphi) = \varphi(1)$ in degree $0$.
7. *First Chern class.* For a line datum $D$ with étale structure map whose charts cover $X$, the étale first Chern class $v \in T_2$ and the logarithmic first Chern class $c \in \mathrm{Hdg}(1, 2)$ exist, $c$ is unique, and $h(v)(\varphi) = \varphi(c)$ in weight $a = 1$, while $h(v) = 0$ in the weights $a \neq 1$.

The pairing is *injective in degree $n$* if for a $\mathbb{Q}_\ell$-basis $(v_i)$ of $V_n$ and $z_i \in \mathbb{C}_\ell$, the equations $\sum_i z_i\, h(v_i)(\varphi) = 0$ for all $a$ and all $\varphi \in \mathrm{Hdg}(a, n)^\vee$ imply $z = 0$. It is *injective at the top* for a model connected of dimension $d$ if the same holds in degree $2d$ with only the weight $a = d$.

Since $\mathrm{Hdg}(a, n)$ is finite-dimensional, $h$ is the same as a $\mathbb{C}_\ell$-linear map
$$\iota : V_n \otimes_{\mathbb{Q}_\ell} \mathbb{C}_\ell \to \bigoplus_{a=0}^{n} \mathrm{Hdg}(a, n) \otimes_K \mathbb{C}_\ell(-a),$$
and equivariance says that $\iota$ commutes with $G_K$, acting on $\mathbb{C}_\ell(-a)$ by $\chi^{-a} \sigma$. Injectivity in degree $n$ says that $\iota$ is injective.

**Theorem 2.3.4 (Hodge-Tate decomposition; Faltings, 1988).** Let $X$ be a proper smooth variety over $K$. There is a canonical $G_K$-equivariant isomorphism
$$H^n_{\mathrm{et}}(X_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell) \otimes_{\mathbb{Q}_\ell} \mathbb{C}_\ell \cong \bigoplus_{a=0}^{n} H^{n-a}(X, \Omega^a) \otimes_K \mathbb{C}_\ell(-a).$$

This section constructs an injective map with the properties above; the [next section](/entry/ht-bij-of/) proves that it is surjective.

**Definition 2.3.5 (Étale side).** We say that the *étale side holds* over $K$ if the following four statements hold for smooth models.

1. Every pair $x \in T_i$, $y \in T_j$ has a cup product in $T_{i+j}$.
2. Each $V_n$ is finite-dimensional over $\mathbb{Q}_\ell$.
3. *Duality.* If the model is connected of dimension $d$, then $V_i = 0$ for $i > 2d$. For $i + j = 2d$ there are vectors $g_1, \dots, g_r$ that span $V_{2d}$, such that $G_K$ moves each $g_s$ to a nonzero multiple of each $g_{s'}$, and such that the functionals $x \mapsto$ (coefficient of $g_s$ in $x \cup y$), for $y \in T_j$, span the dual of $V_i$.
4. *Reduction to connected models.* For each smooth model there are finitely many smooth models $\mathfrak{P}_1, \dots, \mathfrak{P}_r$, each connected of some dimension, with maps $u_k : \mathfrak{P}_k \to \mathfrak{X}$, such that a class $v \in V_n$ with $u_k^* v = 0$ for all $k$ is $0$.

**Theorem 2.3.6 (Existence of the Hodge-Tate map).** Assume that the étale side holds over every finite extension $K$ of $\mathbb{Q}_\ell$, for every $\ell$. Then for every $\ell$ and $K$ there is a Hodge-Tate pairing over $K$ that is injective in every degree for every smooth model, and injective at the top for every smooth model that is connected of dimension $d$.

Lean: `CrystallineSemistableComparison.HT.hodgeTate_of_etale_side`.

The proof uses cohomology over $A_{\mathrm{cris}}$. For a model $\mathfrak{X}$ and $r, j, k \geq 0$ let $F^r H^j_k$ be the $j$-th cohomology of the $r$-th divided-power filtration $J^{[r]}$ of the sheaf $T \mapsto \mathcal{O}(T)$ on the site of divided-power thickenings of $\mathfrak{X}$ over $A_{\mathrm{cris}}/\ell^k$.

**Definition 2.3.7 (Crystalline families).** A *family* of filtration $r$ in degree $j$ is a sequence $x = (x_k)_{k \geq 0}$ with $x_k \in F^r H^j_k$. It is *compatible* if $x_{k+1}$ reduces to $x_k$ for all $k$. The families form an $A_{\mathrm{cris}}$-module with a Galois action, pullbacks, cup products and a shift $F^r \to F^{r+k}$, multiplication by $t^k$.

**Definition 2.3.8 (Lift).** Let $e = (e_k)$ be a family of additive maps from $H^j_{\mathrm{et}}(X_{\overline{\mathbb{Q}}_\ell}, \mathbb{Z}/\ell^k)$ to the cohomology $H^j_k$ of the sheaf $\mathcal{O}$ over $A_{\mathrm{cris}}/\ell^k$. A family $x$ of filtration $r$ is a *lift* of $v \in T_j$ if $x$ is compatible and the image of $x_k$ in $H^j_k$ is $t^r e_k(v_k)$ for all $k$.

**Proposition 2.3.9 (First half: lifts).** Assume that the image of $t$ in $A_{\mathrm{cris}}/\ell^k$ lies in the divided-power ideal for every $k$. Let $e$ be a family of maps as above that is compatible with sums, Galois actions, pullbacks, cup products and units, such that $T_0$ has a unit class and every line datum has an étale first Chern class, and such that $e$ sends an étale first Chern class to the class of a cocycle of lifted transition units. Then lifts have these properties.

1. A lift is a compatible family.
2. For each smooth model and each $j$ there is $r$ such that every $v \in T_j$ has a lift of filtration $r$.
3. For each smooth model and each $j$ there is $k$ such that, for all $r$, two lifts of filtration $r$ of the same $v$ agree after the shift by $t^k$.
4. If $x$ lifts $v$ and $x'$ lifts $v'$, then $x + x'$ lifts $v + v'$, and $z x$ lifts $z v$ for $z \in \mathbb{Z}_\ell$. The shift by $t^k$ of a lift of filtration $r$ is a lift of filtration $r + k$.
5. If $x$ lifts $v$ with filtration $r$, then $\sigma(x)$ lifts $\chi(\sigma)^r \sigma(v)$ for $\sigma \in G_K$, and $u^* x$ lifts $u^* v$ for a map $u$ of models.
6. If $w$ is a cup product of $v$ and $v'$, and $x$, $x'$ lift $v$, $v'$ with filtrations $r$, $r'$, then $x \cup x'$ lifts $w$ with filtration $r + r'$. The unit of $T_0$ lifts to $1$ with filtration $0$.
7. Every line datum has an étale first Chern class. If $D$ has étale map and charts that cover $X$, each étale first Chern class of $D$ has a lift of filtration $1$ that is a crystalline first Chern class.

Lean: `CrystallineSemistableComparison.HT.half1`.

*Proof.* Property 1 holds by definition, and property 4 because the condition $\bar x_k = t^r e_k(v_k)$ is linear in $(v, x)$. For property 5, $\sigma(t) = \chi(\sigma) t$ gives $\overline{\sigma(x)}_k = t^r e_k(\chi(\sigma)^r \sigma(v)_k)$ by the Galois compatibility of $e$; pullback is the same computation. Property 6 is the compatibility of $e$ with cup products and units. For property 7, the truncated logarithms of the cocycle of lifted transition units give a family in $J^{[1]}$ with image $t\, e(v)$. We take as given properties 2 and 3: the obstruction to lifting $t^r e_k(v_k)$ to $F^r H^j_k$, and the difference of two lifts, are killed by a power of $t$ that depends only on the model and $j$. $\square$

**Proposition 2.3.10 (Second half: the Hodge part of a family).** Let $\ell$ be a prime and $K$ a finite extension of $\mathbb{Q}_\ell$. Assume that a level system exists over $K$, and that for every field $F$ of characteristic $0$ and every smooth proper $X$ over $F$ the spaces $\mathrm{Hdg}(a, n)$ are finite-dimensional, with $\mathrm{Hdg}(a, n) = 0$ for $n < a$. Then there is a family of maps
$$\gamma : (\text{families of filtration } r \text{ in degree } j) \to \operatorname{Hom}\big(\mathrm{Hdg}(a, j)^\vee, \mathbb{C}_\ell\big),$$
additive in $\varphi$, with these properties on compatible families $x, y$ over smooth models.

1. $\gamma(x + y) = \gamma(x) + \gamma(y)$, $\gamma(cx)(\varphi) = \theta(c)\gamma(x)(\varphi)$ for $c \in A_{\mathrm{cris}}$, and $\gamma(x)(k\varphi) = k\, \gamma(x)(\varphi)$ for $k \in K$.
2. $\gamma$ does not change under the shift by $t^k$.
3. $\chi(\sigma)^a\, \gamma(\sigma x)(\varphi) = \chi(\sigma)^r \sigma(\gamma(x)(\varphi))$ for $\sigma \in G_K$, in weight $a$.
4. $\gamma(u^* x)(\varphi) = \gamma(x)(\varphi \circ u^*)$ for a map $u$ of smooth models.
5. $\gamma$ satisfies the cup product formula of the definition of a Hodge-Tate pairing, for all bases of the $\mathrm{Hdg}(a, i)$ and $\mathrm{Hdg}(a', j)$, and $\gamma(1)(\varphi) = \varphi(1)$ in weight $0$.
6. If $D$ is a line datum whose charts cover $X$, $x$ is a crystalline first Chern class of $D$ of filtration $1$ in degree $2$ and $c \in \mathrm{Hdg}(1, 2)$ is a logarithmic first Chern class of $D$, then $\gamma(x)(\varphi) = \varphi(c)$ in weight $1$ and $\gamma(x) = 0$ in the weights $a \neq 1$.

Lean: `CrystallineSemistableComparison.HT.half2`.

*Proof.* We take as given the construction of $\gamma$ from a level system: through the level system, a compatible family is read as a map from the dual of de Rham cohomology to $B_{\mathrm{dR}}^+/t^m$, and $\gamma$ is its leading coefficient in weight $a$ followed by $\theta$. The properties come from the surjectivity of $A_{\mathrm{cris}}$ onto its reductions, the compatibility of the level maps with products and first Chern classes, and the cup product laws on $\mathrm{Hdg}$. $\square$

**Theorem 2.3.11 (Existence from five inputs).** Assume these five statements.

1. A level system exists over every finite extension $K$ of $\mathbb{Q}_\ell$, for every $\ell$.
2. For a smooth proper scheme over a field of characteristic $0$, each $\mathrm{Hdg}(a, n)$ is finite-dimensional, and $\mathrm{Hdg}(a, n) = 0$ for $n < a$.
3. If $X$ is a scheme over a field of characteristic $0$ and the charts of a line datum $D$ cover $X$, then $D$ has exactly one logarithmic first Chern class in $\mathrm{Hdg}(1, 2)$.
4. If $X$ is connected and smooth of relative dimension $d$ over a field of characteristic $0$, $D$ is a tautological line on $X$ and $c$ is a logarithmic first Chern class of $D$, then $c^d \neq 0$ in $\mathrm{Hdg}(d, 2d)$.
5. The étale side holds over every finite extension $K$ of $\mathbb{Q}_\ell$, for every $\ell$.

Then the conclusion of the [Theorem 2.3.6](/entry/hodge-tate-of-etale-side/) on the existence of the Hodge-Tate map holds.

Lean: `CrystallineSemistableComparison.HT.ht_of`.

*Proof.* Fix $\ell$ and $K$. We take as given a family $e$ of maps from étale cohomology to cohomology over $A_{\mathrm{cris}}/\ell^k$ that satisfies the hypothesis of the [Proposition 2.3.9](/entry/half1/) on lifts. Inputs 1 and 2 and the [Proposition 2.3.10](/entry/half2/) on the Hodge part give $\gamma$. For a smooth model and $v \in T_n$ choose a lift $x$ of some filtration $r$ and put $h(v) = \gamma(x)$, extended to $V_n$ by linearity. This does not depend on the choice: two lifts agree after a shift, and $\gamma$ does not change under the shift. In the Galois property the twists $\chi^r$ of the two halves cancel. The other properties of a Hodge-Tate pairing follow from the matching properties of the two halves, with inputs 2 and 3 for finiteness and for the first Chern class. On models that are not smooth put $h = 0$.

Injectivity is proved in three steps.

1. *At the top.* Let the model be connected of dimension $d$, and let $D$ be a tautological line. Input 4 gives $c^d \neq 0$ in $\mathrm{Hdg}(d, 2d)$. By the first Chern class property and the cup product formula, $h(v^d)(\varphi) = \varphi(c^d)$ for the étale class $v$ of $D$. Choose $\varphi$ with $\varphi(c^d) \neq 0$. The vectors $g_s$ of the duality statement span $V_{2d}$, and $G_K$ moves each to a multiple of each other. With the equivariance of $h$, this gives injectivity at the top.
2. *Connected models.* Let $n \leq 2d$. If $\sum_i z_i h(v_i) = 0$, cup with classes $y \in T_{2d-n}$ and use the cup product formula and injectivity at the top. Since the functionals $x \mapsto$ (coefficient of $g_s$ in $x \cup y$) span the dual of $V_n$, all $z_i$ vanish. For $n > 2d$ the space $V_n$ is $0$.
3. *All smooth models.* Use the reduction to connected models and the naturality of $h$. $\square$

*Proof of the existence theorem.* Apply the [Theorem 2.3.11](/entry/ht-of/) with five inputs. Input 5 is the hypothesis, and input 1 follows from the [Theorem 2.9.7](/entry/lev-sys-ex/) on level systems. We take as given inputs 2 and 3: input 2 is the finiteness of coherent cohomology of a proper scheme (EGA III, Théorème 3.2.1) read through the [Theorem 2.1.9](/entry/hodge-iso-natural-cech/), and input 3 holds because the logarithmic class is the class of the cocycle $d\log$ of the transition units. Input 4 comes from the [Theorem 2.2.4](/entry/pow-k-ne-zero/) on the top power, since the logarithmic class and the de Rham class agree on the thickenings over a coordinate cover. $\square$

**Remark 2.3.12 (Formalization).** The finiteness hypothesis of the second half is passed to a construction that does not use it ([HalfGaloisOfCompatible.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/HalfGaloisOfCompatible.lean#L56)). We did not open the level system or the proofs of the inputs taken as given. The pairing is $0$ on models that are not smooth ([GTSmul.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/GTSmul.lean#L104)). A smooth model is strictly semistable and smooth, so semistable bad reduction is not covered, and the statement asks neither that $h$ is canonical nor that it is surjective.
