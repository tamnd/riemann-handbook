---
title: Determinants of eigenlattices over a valuation ring
decls:
  - GlobalTheory.HerbrandBridge.exForm
  - GlobalTheory.T.latticeDetRelation_herbrand_eigenspace
  - GlobalTheory.FrameModel.det_append_eq_mul_det
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Determinants of eigenlattices over a valuation ring

Let $\mathcal{O}$ be a valuation ring and let $a_s \in \mathcal{O}$ be distinct points, indexed by a finite set $S$. The ring $R = \mathcal{O}[T] / \prod_s (T - a_s)$ sits inside $\mathcal{O}^S$ by evaluation at the points, but it is smaller, and the differences $a_\tau - a_s$ measure the gap. For the Lie algebra of an abelian scheme with an action of a ramified order, the points $a_s$ are the conjugates of a generator of the order, and the Lie algebra and its Hodge filtration are modules over $R$. This section compares, at one point $\tau$, three lattices: the vectors that live only at $\tau$, the $\tau$-part of the Lie quotient, and the $\tau$-part of the filtration. The comparison is a determinant identity, and the valuation of the constant is an explicit sum over $s \ne \tau$ of the differences, weighted by ranks. The result is used in [the determinant of an adapted core](/entry/det-adapted-core/).

Let $C$ be a field with a valuation $w : C \to \mathbb{R}_{\ge 0}$, with valuation ring $\mathcal{O}$, and let $\ell \in C$ with $0 < w(\ell) < 1$. The *normalized additive valuation* is
$$v(c) = \frac{\log w(c)}{\log w(\ell)},$$
so that $v(\ell) = 1$. A family $x_1, \dots, x_n$ in a $C$-vector space is a *lattice basis* of an $\mathcal{O}$-submodule $X$ if it is linearly independent over $C$ and spans $X$ over $\mathcal{O}$.

**Definition 3.20.1 (Free lattice and filtrations).** Let $S$ be finite, $a : S \to \mathcal{O}$ injective and $N \in \mathbb{N}$. The *free lattice* $\Lambda_a \subset \prod_{s \in S} C^N$ is the set of families $(x_s)_s$ such that for each coordinate $i$ there is a polynomial $f \in \mathcal{O}[T]$ with $x_{s,i} = f(a_s)$ for all $s$. A *filtration* is an $\mathcal{O}$-submodule $\mathrm{Fil} \subset \Lambda_a$ such that:

1. it is stable under the map $(x_s)_s \mapsto (a_s x_s)_s$;
2. it is saturated in $\Lambda_a$: if $x \in \Lambda_a$, $c \in \mathcal{O}$, $c \ne 0$ and $c x \in \mathrm{Fil}$, then $x \in \mathrm{Fil}$.

For $s \in S$ let $F_s \subset C^N$ be the $C$-span of the $s$-components of the elements of $\mathrm{Fil}$.

So $\Lambda_a$ is the image of $R^N$ under evaluation, and a filtration is a saturated $R$-submodule of it. The spaces $F_s$ are the fibres of the filtration at the points.

**Definition 3.20.2 (The three lattices at $\tau$).** Fix $\tau \in S$. Put:

1. $X_\tau = \{ y \in C^N : \text{the family with } y \text{ at } \tau \text{ and } 0 \text{ elsewhere lies in } \Lambda_a \}$;
2. $L_\tau$ is the set of $z \in C^N / F_\tau$ such that the family with $z$ at $\tau$ and $0$ elsewhere lies in the image of $\Lambda_a$ in $\prod_s C^N / F_s$;
3. $M_\tau$ is the set of $\tau$-components of the elements of $\mathrm{Fil}$.

A *determinant relation* with exponent $y \in \mathbb{R}$, for $N = p + q$ and $\dim F_\tau = q$, is a lattice basis $x_1, \dots, x_N$ of $X_\tau$, vectors $u_1, \dots, u_p$ whose classes are a lattice basis of $L_\tau$, a lattice basis $m_1, \dots, m_q$ of $M_\tau$ with $m_i \in F_\tau$, and $c \in C^\times$ with $v(c) = y$, such that
$$\det(x_1, \dots, x_N) = c \cdot \det(u_1, \dots, u_p, m_1, \dots, m_q).$$

Here $X_\tau$ is the lattice of the Lie algebra that lives purely at $\tau$, $L_\tau$ is the $\tau$-eigenlattice of the Lie quotient, and $M_\tau$ is the image of the filtration at $\tau$. A determinant relation says that the volume of $X_\tau$ equals the volume of the extension of $L_\tau$ by $M_\tau$, up to a scalar of valuation $y$.

**Theorem 3.20.3 (Determinant relation for eigenlattices).** Let $S$ be finite, $a : S \to \mathcal{O}$ injective, $p, q \in \mathbb{N}$, $\mathrm{Fil}$ a filtration in $\prod_s C^{p+q}$ and $\tau \in S$ with $\dim F_\tau = q$. Then there is a determinant relation at $\tau$ with exponent
$$y = \sum_{s \ne \tau} \dim F_s \cdot v(a_\tau - a_s).$$

Lean: `GlobalTheory.HerbrandBridge.exForm` (also `GlobalTheory.T.latticeDetRelation_herbrand_eigenspace`, a second name).

*Proof.* Put $N = p + q$.

*Change of ring.* The valuation ring $\mathcal{O}$ is the ring of integers of the normalized valuation $v$, by an input lemma. Lift $a$ to this ring; the lift is again injective. Evaluation at the points is an injective map $\mathrm{ev} : R^N \to \prod_s C^N$, and its image is $\Lambda_a$; both facts are input lemmas. Let $\mathrm{Fil}' = \mathrm{ev}^{-1}(\mathrm{Fil})$. Since $\mathrm{Fil}$ is stable under multiplication by the $a_s$, an element lies in $\mathrm{Fil}'$ if and only if its image lies in $\mathrm{Fil}$, and $\mathrm{Fil}'$ is an $R$-submodule.

*Saturation.* Let $c \in \mathcal{O}$, $c \ne 0$, and $x \in R^N$ with $c x \in \mathrm{Fil}'$. Then $\mathrm{ev}(x) \in \Lambda_a$ and $c\, \mathrm{ev}(x) = \mathrm{ev}(c x) \in \mathrm{Fil}$, so $\mathrm{ev}(x) \in \mathrm{Fil}$ by saturation, and $x \in \mathrm{Fil}'$.

*The determinant identity over $R$.* An input lemma on ranks shows that the $\tau$-rank of $\mathrm{Fil}'$ is $\dim F_\tau = q$. An input determinant identity for saturated $R$-submodules of $R^N$ gives an integer $p'$ with $p' + q = N$, so $p' = p$, and lattice bases $h$ of the $\tau$-eigenpart of $R^N$, $l$ of the $\tau$-eigenpart of $R^N/\mathrm{Fil}'$ and $f$ of the $\tau$-part of $\mathrm{Fil}'$. For lifts $x_i$ of the $l_i$ it gives $c$ with
$$v(c) = \sum_{s \ne \tau} \dim F_s \cdot v(a_s - a_\tau),$$
with $\det(u, m) \ne 0$ and $\det X = c \det(u, m)$. Here $X$, $u$ and $m$ are the $\tau$-components of $h$, the $x_i$ and the $f_i$. Since $v(a_s - a_\tau) = v(a_\tau - a_s)$, this is the exponent $y$.

*Translation.* We check that $X$, $u$ and $m$ are lattice bases of $X_\tau$, $L_\tau$ and $M_\tau$. In each case an input lemma describes the lattice as the image of the corresponding eigenpart over $R$: for $X_\tau$ the $\tau$-eigenpart of $R^N$, for $L_\tau$ the $\tau$-eigenpart of the quotient, and for $M_\tau$ the $\tau$-part of $\mathrm{Fil}'$. The images of bases are then spanning families. They are independent since $\det X \ne 0$ and $\det(u, m) \ne 0$; for $u$ this needs that the classes modulo $F_\tau$ stay independent, which holds since the $m_i$ span $F_\tau$ and $(u, m)$ is independent. The $m_i$ lie in $F_\tau$ by definition.

*The constant.* The valuation of $c$ is finite, so $c \ne 0$. $\square$

**Theorem 3.20.4 (Determinant of an adapted basis).** In the setting of the previous theorem, let $x_1, \dots, x_N$ be a lattice basis of the $\tau$-components of $\Lambda_a$, let $u_1, \dots, u_p$ have classes that form a lattice basis of $L_\tau$, and let $m_1, \dots, m_q$ be a lattice basis of $M_\tau$. Then there is $c \in C$ with
$$w(c) = \prod_{s \ne \tau} w(a_\tau - a_s)^{\,p + q - \dim F_s}$$
and
$$\det(u_1, \dots, u_p, m_1, \dots, m_q) = c \cdot \det(x_1, \dots, x_N).$$

Lean: `GlobalTheory.FrameModel.det_append_eq_mul_det`.

The $\tau$-components of $\Lambda_a$ are all of $\mathcal{O}^N$, since a polynomial can take any value at one point. So the theorem compares the adapted basis $(u, m)$ with a basis of the full lattice. Here the hypothesis $\dim F_\tau = q$ is not needed: it follows from the basis $m$.

*Proof.* Put $N = p + q$ and $d = \prod_{s \ne \tau} (a_\tau - a_s)$.

*Rank and $d$.* The $m_i$ are independent and span $M_\tau$ over $\mathcal{O}$, so they span $F_\tau$ over $C$ and $\dim F_\tau = q$. The $a_s$ are distinct, so $d \ne 0$.

*A relation for the full lattice.* The previous theorem gives a determinant relation with exponent $y$ for $X_\tau$. An input lemma shows that $X_\tau = d \cdot \mathcal{O}^N$, the image of the $\tau$-components of $\Lambda_a$ under multiplication by $d$. A second input lemma turns a relation for $d \cdot X'$ into a relation for $X'$ with exponent $y - N v(d)$. This gives bases $x'$, $u'$, $m'$ and $c'$ with $v(c') = y - N v(d)$ and
$$\det x' = c' \det(u', m').$$

*Change of bases.* Two lattice bases of the same lattice differ by a matrix with determinant of valuation $0$. This gives matrices $P$, $A$ and $B$ with $w(\det P) = w(\det A) = w(\det B) = 1$, with $x = P x'$, and with
$$\det(u, m) = \det A \cdot \det B \cdot \det(u', m'),$$
by an input lemma on block changes modulo $F_\tau$. Then $\det x = \det P \cdot c' \cdot \det(u', m')$.

*The constant.* Put $c = \det A \det B\, (\det P\, c')^{-1}$. Then $\det(u, m) = c \det x$ and $w(c) = w(c')^{-1}$. We have
$$v(c') = \sum_{s \ne \tau} \dim F_s \cdot v(a_\tau - a_s) - N \sum_{s \ne \tau} v(a_\tau - a_s),$$
so
$$v(c') = - \sum_{s \ne \tau} (N - \dim F_s)\, v(a_\tau - a_s),$$
since $\dim F_s \le N$. Multiplying by $\log w(\ell)$ and taking exponentials gives the formula for $w(c)$. $\square$

**Remark 3.20.5 (Formalization).** The element $\ell$ enters only through the normalization of the additive valuation; the conclusion of the second theorem does not mention it, and the hypotheses $0 < w(\ell) < 1$ only say that $w$ is not trivial ([DvrAlphaDeterminantOrder.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DvrAlphaDeterminantOrder.lean#L194)). The first theorem works over the quotient ring $R$, written as the ring obtained by adjoining a root of $\prod_s (T - a_s)$, and the bridge to the free lattice is in [LatticeDetRelationHerbrandEigenspace.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LatticeDetRelationHerbrandEigenspace.lean#L223). The lattices, filtrations and determinant relations are defined in [QuotientEigenDifference.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/QuotientEigenDifference.lean#L27). We have not unfolded the input determinant identity over $R$ or the comparison lemmas for bases. The second name is a wrapper.
