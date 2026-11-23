---
title: Surjectivity and the dimension formula
decls:
  - CrystallineSemistableComparison.Onto.parts
  - CrystallineSemistableComparison.Onto.htBij_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Surjectivity and the dimension formula

The [previous section](/entry/hodge-tate-of-etale-side/) gives an injective Hodge-Tate map $\iota : V_n \otimes \mathbb{C}_\ell \to \bigoplus_a \mathrm{Hdg}(a, n) \otimes \mathbb{C}_\ell(-a)$. This section proves that $\iota$ is also surjective, so that it is the Hodge-Tate decomposition, and deduces the formula
$$\dim_{\mathbb{Q}_\ell} V_n = \sum_{a=0}^{n} \dim_K \mathrm{Hdg}(a, n).$$
The proof uses the class of the diagonal in $X \times X$. Its image under $\iota$ is a Hodge class on $X \times X$, and a slant product with it reproduces every Hodge class of $X$ from the image of $\iota$.

We keep the notation of the previous section: $\ell$, $K$, models $\mathfrak{X}$ over $\mathcal{O}_K$ with generic fibre $X$, the spaces $T_n$, $V_n$ and $\mathrm{Hdg}(a, n)$, and a Hodge-Tate pairing $h$.

**Definition 2.4.1 (Surjectivity of a pairing).** A Hodge-Tate pairing $h$ is *surjective in degree $n$* for a model if the following holds. Let $(b_{a,s})_s$ be a $K$-basis of $\mathrm{Hdg}(a, n)$ for each $a \leq n$, with dual basis $(b_{a,s}^*)$, and let $z_{a,s} \in \mathbb{C}_\ell$. If
$$\sum_{a=0}^{n} \sum_s z_{a,s}\, h(v)(b_{a,s}^*) = 0 \quad \text{for all } v \in V_n,$$
then all $z_{a,s}$ are $0$.

In terms of $\iota$ this says that no nonzero $\mathbb{C}_\ell$-linear functional on the target vanishes on the image. So $\iota$ is surjective.

For the surjectivity we need three constructions on the square of a model.

**Definition 2.4.2 (Square with a blown-up diagonal).** Let $\mathfrak{X}$ be a smooth model of relative dimension $d + 1$. A *square* of $\mathfrak{X}$ consists of the following data.

1. A smooth model $\mathfrak{P}$ with projections $p_1, p_2 : \mathfrak{P} \to \mathfrak{X}$ that make $\mathfrak{P}$ the fibre product $\mathfrak{X} \times_{\mathcal{O}_K} \mathfrak{X}$, and the diagonal $\Delta : \mathfrak{X} \to \mathfrak{P}$ with $p_1 \Delta = p_2 \Delta = \mathrm{id}$.
2. A smooth model $\mathfrak{Y}$ with a map $\pi : \mathfrak{Y} \to \mathfrak{P}$ and a line datum $D$ on $\mathfrak{Y}$ whose charts cover $\mathfrak{Y}$.
3. On the generic fibre, a *blow-up structure* of codimension $d + 1$: $\Delta$ is a closed immersion, $\pi$ is an isomorphism over the complement of the diagonal, and $D$ has a section $f$ (an equation of the exceptional divisor) that is a unit over the complement of the diagonal.

**Definition 2.4.3 (Slant products).** Let $X$, $X'$ be smooth proper over a field $K$ of characteristic $0$, with product $P = X \times_K X'$ and projections $p_1$, $p_2$. We say that *slant products exist* if for each $\varphi \in \mathrm{Hdg}_X(a, i)^\vee$ and each bidegree there is a $K$-linear map $\mathrm{sl}_\varphi : \mathrm{Hdg}_P(a + a', i + j) \to \mathrm{Hdg}_{X'}(a', j)$ with
$$\mathrm{sl}_\varphi\big(p_1^* u \cup p_2^* v\big) = \varphi(u)\, v$$
for $u \in \mathrm{Hdg}_X(a, i)$ and $v \in \mathrm{Hdg}_{X'}(a', j)$, and with $\mathrm{sl}_\varphi(p_1^* u \cup p_2^* v) = 0$ when $u$ has a bidegree $(b, i') \neq (a, i)$.

**Definition 2.4.4 (Vanishing along a blow-up).** We say that *classes vanish along blow-ups* if the following holds. Let $Z$ be smooth proper over a field $K$ of characteristic $0$, $i : W \to Z$, $\pi : Y \to Z$ proper and $D$ a line datum on $Y$ with a blow-up structure of positive codimension, and $e \in \mathrm{Hdg}_Y(1, 2)$ a logarithmic first Chern class of $D$. Let $c \in \mathrm{Hdg}_Z(a, n)$ with $\pi^* c = 0$ or $\pi^* c = e \cup w$ for some $w$, and let $y \in \mathrm{Hdg}_Z(a', n')$ with $i^* y = 0$. Then $c \cup y = 0$.

The étale input is a decomposition of the diagonal class.

**Definition 2.4.5 (Étale diagonal).** We say that the *étale diagonal decomposes* if the following holds for each smooth model $\mathfrak{X}$ of relative dimension $d + 1$ with $d \geq 1$, each square of $\mathfrak{X}$ whose line datum has an étale map, and each étale first Chern class $v \in T_2(\mathfrak{Y})$ of $D$. There is a class $c \in T_{2+2d}(\mathfrak{P})$ such that $\pi^* c = v \cup w$ in $V_{2+2d}(\mathfrak{Y})$ for some $w \in T_{2d}(\mathfrak{Y})$, and such that in $V_{2+2d}(\mathfrak{P})$
$$\begin{aligned} c &= \sum_s p_1^* a^0_s \cup p_2^* b^0_s + \sum_s p_1^* a_s \cup p_2^* b_s, \end{aligned}$$
with $a^0_s \in T_{2+2d}(\mathfrak{X})$ linearly independent in $V_{2+2d}$, $b^0_s \in T_0(\mathfrak{X})$ with $\sum_s b^0_s = N \cdot 1$ in $V_0$ for some $N \in \mathbb{Q}_\ell$ with $N \neq 0$, and $b_s$ of positive degree.

So $c$ plays the role of the diagonal class: it pulls back to a multiple of the exceptional class on the blow-up, and its Künneth component of bidegree $(2 + 2d, 0)$ is nonzero.

We can now state the main theorem.

**Theorem 2.4.6 (Hodge-Tate decomposition, surjectivity and dimension).** Assume that $\mathrm{Hdg}$ admits a Hodge-Tate pairing that is injective in every degree and at the top, as in the conclusion of the [Theorem 2.3.6](/entry/hodge-tate-of-etale-side/) on the existence of the Hodge-Tate map. Assume also:

1. every smooth model of relative dimension $d + 1$ with $d \geq 1$ has a square whose line datum has an étale map;
2. the étale diagonal decomposes;
3. $V_n$ is finite-dimensional for every smooth model.

Then for every $\ell$ and every finite $K$ over $\mathbb{Q}_\ell$ there is a Hodge-Tate pairing $h$ such that for every smooth model: $h$ is injective in every degree, injective at the top when the model is connected of dimension $d$, and, when $\mathfrak{X}$ has relative dimension $d$ over $\mathcal{O}_K$, surjective in every degree $n$ with
$$\dim_{\mathbb{Q}_\ell} V_n = \sum_{a=0}^{n} \dim_K \mathrm{Hdg}(a, n).$$

Lean: `CrystallineSemistableComparison.Onto.htBij_of`.

The proof uses a list of facts on Hodge cohomology, forms and étale classes. Most of them are local; the last three are the reductions of the proof. Write $\mathrm{PD}$ for the statement: for every $\ell$, $K$, Hodge-Tate pairing $h$ and smooth model of relative dimension $d + 1$ with $d \geq 1$ on which $h$ is injective in degree $2 + 2d$, $h$ is surjective in every degree.

**Proposition 2.4.7 (The parts of the surjectivity proof).** The following statements hold.

1. *Local facts.* Mayer-Vietoris bijectivity and surjectivity for systems of complexes over finite index sets; descent along covers of the thickening site; the laws of the thickening site under intersection and pullback; bijectivity of restriction to a closed subscheme and to a Zariski cover; the two statements of the [Theorem 2.1.5](/entry/hdg-aff-iso-onto/) on the affine case; the laws of Kähler forms, of the wedge with $df$ and with $d\log f$; a Künneth isomorphism $\bigoplus_a \Omega^a_A \otimes_K \Omega^{c-a}_B \cong \Omega^c_{A \otimes_K B}$; the compatibility of forms with the cup product; the description of the logarithmic first Chern class by a cocycle; a cover of a blow-up by charts with affine intersections on which the exceptional divisor has an equation that is a nonzerodivisor on forms; the laws and the bijectivity of blow-up charts; bijectivity over an open where $\pi$ is an isomorphism; and the bilinearity and associativity of the cup product on $\mathrm{Hdg}$.
2. *Derived facts.* Each of the following follows from the local facts it uses: relative cohomology on Zariski covers and on affine opens, lifting and injectivity of relative classes, vanishing on cones, killing of relative classes, the Künneth formula on affine opens, the existence of slant products, and the vanishing along blow-ups.
3. *Positive dimension.* The cup product laws, slant products, the vanishing along blow-ups and the three assumptions of the theorem imply $\mathrm{PD}$.
4. *Low dimension.* The cup product laws, the retraction and $\mathrm{PD}$ imply that for every $\ell$, $K$ and Hodge-Tate pairing that is injective in every degree, the pairing is surjective in every degree on every smooth model.
5. *Retraction.* For every smooth model $\mathfrak{X}$ of relative dimension $d$ there are a smooth model $\mathfrak{N}$ of relative dimension $d + 2$ and maps $p : \mathfrak{N} \to \mathfrak{X}$ over $\mathcal{O}_K$ and $s : \mathfrak{X} \to \mathfrak{N}$ with $p \circ s = \mathrm{id}$.

Lean: `CrystallineSemistableComparison.Onto.parts`.

*Proof.* We take the local facts as given; they are standard facts on Kähler forms, on Čech cohomology and on blow-ups along smooth centres. Slant products are computed on a coordinate cover of $P = X \times_K X'$ by products of affine opens: by the Künneth formula there, a class of $\mathrm{Hdg}_P$ is a sum of products $p_1^* u \cup p_2^* v$, and $\mathrm{sl}_\varphi$ applies $\varphi$ to the first factor. The vanishing along blow-ups is computed with relative cohomology: $y$ with $i^* y = 0$ lifts to a class relative to $W$, and on the charts of the blow-up the class $e$ has a cocycle given by $d\log$ of the equation of the exceptional divisor, which kills relative classes. For the retraction take $\mathfrak{N} = \mathfrak{X} \times_{\mathcal{O}_K} \mathbb{P}^2$ with a section at a rational point. The reductions are proved in the proof of the theorem below. $\square$

*Proof of the theorem.* Fix $\ell$ and $K$, and take the injective pairing $h$ of the hypothesis. Let $\mathfrak{X}$ be a smooth model.

1. Suppose first that $\mathfrak{X}$ has relative dimension $d + 1$ with $d \geq 1$. Take a square of $\mathfrak{X}$ (hypothesis 1) and the class $c$ of the étale diagonal (hypothesis 2). By the cup product and first Chern class properties of $h$, the image of $\pi^* c = v \cup w$ in Hodge cohomology is divisible by the exceptional class $e$. By the vanishing along blow-ups, the Hodge image of $c$ cups to zero with every class that vanishes on the diagonal. Take the slant product of the Hodge image of $c$ with the dual basis vectors $b_{a,s}^*$. The Künneth decomposition of $c$ and the condition $\sum_s b^0_s = N \cdot 1$ with $N \neq 0$ show that each Hodge class of $\mathfrak{X}$, tensored with $\mathbb{C}_\ell$, lies in the $\mathbb{C}_\ell$-span of the image of $h$. The hypothesis of injectivity in degree $2 + 2d$ enters this step. This is the reduction in positive dimension.
2. If $\mathfrak{X}$ has relative dimension $d$, apply the retraction. The model $\mathfrak{N}$ has relative dimension $d + 2 \geq 2$, so $h$ is surjective on $\mathfrak{N}$ by step 1. Since $s^* p^* = \mathrm{id}$ on both sides and $h$ is natural, surjectivity passes to $\mathfrak{X}$.
3. Now $V_n$ is finite-dimensional (hypothesis 3), and $\iota$ is injective and surjective, so it is an isomorphism of $\mathbb{C}_\ell$-vector spaces $V_n \otimes_{\mathbb{Q}_\ell} \mathbb{C}_\ell \cong \bigoplus_{a \leq n} \mathrm{Hdg}(a, n) \otimes_K \mathbb{C}_\ell$. Comparing dimensions over $\mathbb{C}_\ell$ gives $\dim_{\mathbb{Q}_\ell} V_n = \sum_{a \leq n} \dim_K \mathrm{Hdg}(a, n)$. $\square$

**Remark 2.4.8 (Formalization).** The theorem is the step from the [Theorem 2.3.6](/entry/hodge-tate-of-etale-side/) on the Hodge-Tate map to the [Theorem 3.9 of Volume 9](/entry/ht-bij/) on the Hodge-Tate bijection in the chapter on Galois representations; its pairing is the pairing of the hypothesis. The proposition is the record `CrystallineSemistableComparison.Onto.Parts` of 31 statements, many of them from files under `Development/AutomorphicSpectrum/Proofs/BlockDecomposition`; the list above names them in groups. The file `TowerRallisLemma.lean` holds the statements of a square, of the étale diagonal and of the reduction in positive dimension, and has nothing to do with the Rallis tower. We did not open the proofs of the 31 statements, so the proofs above for slant products, the vanishing along blow-ups and the retraction are the standard arguments.
