---
title: Degeneration data along a trait
decls:
  - GlobalTheory.T.exists_degeneration_data_tautologicalChart_of_trait
  - GlobalTheory.TChart.exists_degFrom_of_trait
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Degeneration data along a trait

A chart at a boundary point is tested on traits: complete discrete valuation rings that map the generic point into the Siegel moduli scheme. Along such a trait the universal abelian scheme degenerates, and Mumford's construction writes the degeneration as the quotient of a semi-abelian group by a lattice of periods. This section proves that, after a finite extension of the trait, the periods are monomials in a few elements of the ring, with exponents given by a cone for the polarization function, and that the whole degeneration datum is pulled back from a [lower base](/entry/exists-low-base-of-trait/). The result is used in the [next sections](/entry/exists-chart-at/) to build a chart at each point of the normalized blowup.

Throughout, $n \ge 3$ is odd, $F$ is a Siegel family of genus $g$ and level $n$ over $\Lambda_n$ with base $X$ and universal datum $(A, P, \ell)$, and a CN domain is as in the section on the lower base. For a domain $R$ we write $K_R$ for its fraction field.

**Definition 9.5.1 (Degeneration data).** Let $R$ be a domain. A *degeneration pre-datum* $D$ over $R$ consists of:

1. a polarized abelian scheme $(B_D, L)$ over $R$, a generator of $0^* L$ that rigidifies $L$, a cubical structure on $L$, and a generator of $(-1)^* L \otimes L^{-1}$ that is $1$ at the zero section;
2. a free $\mathbb{Z}$-module $Y$ of finite rank and an additive map $c : Y \to B_D(R)$;
3. for each $\chi \in Y$ a generator $\psi(\chi)$ of $c(\chi)^* L^{-1}$ over $K_R$.

The *periods* of $D$ are $\tau(a, b) = \psi(a + b)\,\psi(a)^{-1}\psi(b)^{-1}$, divided by the rigidification; they are generators of the inverse of the Mumford bundle of $L$ at $(c(a), c(b))$ over $K_R$. For an ideal $I$ of $R$, *degeneration data* with respect to $I$ are a pre-datum such that $\psi$ is even, $\tau$ is bimultiplicative up to the cubical structure, $\psi(\chi)$ is a section of $I$ times the bundle for each $\chi \ne 0$, and for each $k$ only finitely many $\psi(\chi)$ fail to lie in $I^k$.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.DegData` (also `ReciprocityTheory.ChartRestriction.G.Out.DegPre`).

This is the form of the degeneration data of Faltings and Chai (Degeneration of abelian varieties, Chapters II and III) that we need: the torus part is split, and its character group is identified with the period lattice $Y$, as for a principal polarization ([semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction)).

**Definition 9.5.2 (Trait).** A *trait* for $F$ consists of a complete discrete valuation ring $V$ of characteristic $0$ with a uniformizer $\varpi$, a map $y : \operatorname{Spec} K_V \to X$, a semi-abelian group scheme $G$ over $V$, degeneration data $D$ over $V$ with respect to $\mathfrak{m}_V$, a polarized abelian scheme $(A_K, L_K)$ over $K_V$, a uniformization of $G$ by $D$ and $A_K$, a map $\alpha : A_K \to A$ that makes $A_K$ the group pullback of $A$ along $y$, with $\Lambda(L_K) \cong (\alpha \times \alpha)^* P$, and a symmetric bilinear form $\beta$ on the lattice $Y$ of $D$ such that, for each $\chi \in Y$, $\beta(\chi, \chi) = 2k$ is even and $\psi(\chi)$ is $\varpi^{k}$ times a generator over $V$.

Lean: `GlobalTheory.Poinc.Trait`.

So a trait is a point of $X$ over the fraction field of $V$ together with Mumford's description of the degeneration of $y^* A$ over $V$, whose periods are powers of $\varpi$ with exponents given by $\beta$. The form $\beta$ is the one that a polarization function is evaluated on.

**Definition 9.5.3 (Uniformization along a map).** Let $R$ be a domain, $y : \operatorname{Spec} K_R \to X$, $G_1$ a group scheme over $R$, and $\alpha_1$ a map from the generic fibre of $G_1$ to $A$. Let $\rho : R \to R'$ be a map of domains, $G'$ a group scheme over $R'$ with $\pi : G' \to G_1$, and $U'$ a uniformization of $G'$ by degeneration data $D'$ and a polarized abelian scheme $(A', L')$ over $K_{R'}$. We say that $U'$ is a *uniformization along $\rho$* if $\pi$ makes $G'$ the group pullback of $G_1$ along $\operatorname{Spec}\rho$, and there are $\kappa : \operatorname{Spec} K_{R'} \to \operatorname{Spec} K_R$ over $\rho$ and a map $\pi_K$ of generic fibres over $\pi$, and a group pullback $\alpha : A' \to A$ along $y \circ \kappa$ with $\Lambda(L') \cong (\alpha \times \alpha)^* P$, such that the uniformization of $U'$ followed by $\alpha$ equals $\pi_K$ followed by $\alpha_1$.

Lean: `GlobalTheory.PolDeg.IsUnifAlong`.

**Definition 9.5.4 (Refinement).** Let $Q$ be Mumford data over $R$, with abelian scheme $B_Q$, bundle $M$, lattice $Y_Q$, map $c_Q$ and periods $\tau_Q$, as in the [main section](/entry/siegel-toroidal-integral-holds/). Let $\rho : R \to R'$, let $D$ be a degeneration pre-datum over $R'$ and let $e : Y \to Y_Q$ be an isomorphism. We say that $D$ *refines* $Q$ along $\rho$ and $e$ if there are a group pullback $\beta : B_D \to B_Q$ along $\operatorname{Spec}\rho$ and an isomorphism $w : \Lambda(L) \cong (\beta \times \beta)^*\Lambda(M)$ such that $\beta \circ c(a) = c_Q(e(a))$ over $\operatorname{Spec}\rho$ for each $a$, and $\tau(a, b) = w \cdot \tau_Q(e(a), e(b))$ over $K_{R'}$ for all $a, b$.

Lean: `GlobalTheory.PolDeg.Refines`.

**Definition 9.5.5 (Data from a tautological base).** Let $T = (b, B, M, r, c_0, \tau_0)$ be a tautological base over $W$, let $\iota : W \to V$ be a map to a domain, let $s_1, \dots, s_k \in V$, let $\varepsilon_1, \dots, \varepsilon_k$ be bilinear forms on $\mathbb{Z}^r$, and let $n \ge 1$. Mumford data $Q$ over $V$ with an isomorphism $e : Y_Q \to \mathbb{Z}^r$ *come from $T$* via $(\iota, s, \varepsilon, n)$ if there are a group pullback $\beta : B_Q \to B$ along $\operatorname{Spec}\iota$ and an isomorphism $w : \Lambda(M_Q) \cong (\beta \times \beta)^*\Lambda(M)$ such that $\beta \circ c_Q(a) = c_0(n\,e(a))$ over $\operatorname{Spec}\iota$, and
$$\tau_Q(a, b) = \prod_{i} s_i^{\,n\,\varepsilon_i(e(a), e(b))} \cdot w \cdot \tau_0\big(n\,e(a), n\,e(b)\big)$$
over $K_V$ for all $a, b$. A degeneration pre-datum $D$ over $V$ with $e : Y \to \mathbb{Z}^r$ *comes from $T$* if there are Mumford data $Q$ over $V$ and $e' : Y \to Y_Q$ such that $D$ refines $Q$ along the identity and $e'$, and $Q$ with $e \circ e'^{-1}$ comes from $T$.

Lean: `GlobalTheory.TChart.DegFrom` (also `GlobalTheory.TChart.DataFrom`).

So, up to the isomorphism $w$, the periods of $D$ are the periods of the tautological base times monomials in the $s_i$.

**Theorem 9.5.6 (Degeneration data along a trait).** Let $g \ge 1$, let $\varphi$ be a polarization function of rank $g$, and let $\mathcal{T}$ be a trait for $F$ with ring $V$, group $G$, data $D$, map $y$ and uniformization $U$ with generic map $\alpha$. Let $b : \Lambda_n \to V$ with $s \circ y = \operatorname{Spec} b$ on $\operatorname{Spec} K_V$. Then there are:

- a lower base $L$ of level $n$ over $\Lambda_n$, with ring $W$ and tautological base $T$ of rank $r$;
- integers $m, N$ and a basis $\varepsilon_1, \dots, \varepsilon_{m+N}$ of the symmetric bilinear forms on $\mathbb{Z}^{r}$;
- a CN domain $V'$ that is a discrete valuation ring, an injective, finite, local map $f : V \to V'$, and a local map $\kappa : W \to V'$;
- elements $s_1, \dots, s_{m+N} \in V'$;
- degeneration data $D'$ over $V'$ with respect to $\mathfrak{m}_{V'}$, with an isomorphism $e : Y' \to \mathbb{Z}^r$;
- a group scheme $G'$ over $V'$ with $\pi : G' \to G$, a polarized abelian scheme $A'$ over $K_{V'}$, and a uniformization $U'$ of $G'$ by $D'$ and $A'$,

such that:

1. $h_L + r = g$;
2. $\varepsilon_1, \dots, \varepsilon_m$ is a cone for $\varphi$, and for each $x \ne 0$ in $\mathbb{Z}^r$ there is $i \le m$ with $\varepsilon_i(x, x) > 0$;
3. $\kappa \circ b_T = f \circ b$;
4. $s_1, \dots, s_m$ are nonzero elements of $\mathfrak{m}_{V'}$, and $s_{m+1}, \dots, s_{m+N}$ are units;
5. $U'$ is a uniformization along $f$, with respect to $y$, $G$ and $U$ followed by $\alpha$;
6. $D'$ with $e$ comes from $T$ via $(\kappa, s, \varepsilon, n)$.

Lean: `GlobalTheory.TChart.exists_degFrom_of_trait` (also `GlobalTheory.T.exists_degeneration_data_tautologicalChart_of_trait`, a wrapper).

*Proof.* The ring $V$ is a CN domain: it is noetherian, integrally closed as a discrete valuation ring, complete, and of characteristic $0$. Let $r$ be the rank of the lattice $Y$ of $D$, choose an isomorphism $e_0 : \mathbb{Z}^r \to Y$, and let $(B_D, L_D)$ be the polarized abelian scheme of $D$. The map $a \mapsto c(e_0(a))$ is additive.

1. Apply the theorem on the [lower base for a trait](/entry/exists-low-base-of-trait/) to $V$, $b$, $(B_D, L_D)$ and $c \circ e_0$. It gives a lower base $L$ with tautological base $T$, a CN discrete valuation ring $V_1$ with an injective, finite, local map $f_1 : V \to V_1$, a local map $\kappa_1 : W \to V_1$ with $\kappa_1 \circ b_T = f_1 \circ b$, an isomorphism $e_1 : \mathbb{Z}^{r_T} \to \mathbb{Z}^r$, and a common group pullback $B'$ of $B_D$ and $B$ over $V_1$ with matching Mumford bundles and matching sections. Since $e_1$ is an isomorphism, $r_T = r$. Also $h_L$ is the relative dimension of $B_D$, and a lemma on traits gives that this dimension plus $r$ is $g$.
2. A lemma on pulled-back periods gives $q : \mathbb{Z}^r \times \mathbb{Z}^r \to K_{V_1}^\times$, symmetric and bimultiplicative, with $q(a, a)$ a nonzero element of $\mathfrak{m}_{V_1}$ for $a \ne 0$, and with the following property. Let $f_2 : V_1 \to V_2$ be injective, finite and local, with $V_2$ a CN domain, and let $s_i \in V_2$ and forms $\varepsilon_i$ satisfy $q(a, b) = \prod_i s_i^{n \varepsilon_i(a, b)}$ in $K_{V_2}$. Then each degeneration datum over $V_2$ that is the pullback of $D$ along $f_2 \circ f_1$ comes from $T$ via $(f_2 \circ \kappa_1, s, \varepsilon, n)$. In words, $q$ is the period of $D$ divided by the period of $T$, after the comparison of step 1.
3. Since $r \le g$ and $q$ is symmetric, bimultiplicative and positive, a lemma on roots of periods gives $m$, $N$, a basis $\varepsilon$ of the symmetric forms whose first $m$ members form a cone for $\varphi$ and detect each $x \neq 0$, a CN discrete valuation ring $V_2$ with an injective, finite, local map $f_2 : V_1 \to V_2$, and elements $s_i \in V_2$ with $s_1, \dots, s_m$ nonzero in $\mathfrak{m}_{V_2}$, $s_{m+1}, \dots, s_{m+N}$ units, and $q(a, b) = \prod_i s_i^{n \varepsilon_i(a, b)}$ in $K_{V_2}$.
4. A lemma on uniformizations gives degeneration data $D'$ over $V_2$ that are the pullback of $D$ along $f_2 \circ f_1$, a group scheme $G'$ with $\pi : G' \to G$, a polarized abelian scheme $A'$ and a uniformization $U'$ along $f_2 \circ f_1$.

Put $V' = V_2$, $f = f_2 \circ f_1$ and $\kappa = f_2 \circ \kappa_1$; both are local, and $f$ is injective and finite. Then $\kappa \circ b_T = f_2 \circ f_1 \circ b = f \circ b$. The isomorphism $e$ is the identification of $Y'$ with $Y$ from the pullback, followed by $e_0^{-1}$ and $e_1^{-1}$. Condition 6 is the property of step 2, applied to $f_2$, $s$, $\varepsilon$ and $D'$. $\square$

**Remark 9.5.7 (Formalization).** The hypothesis $s \circ y = \operatorname{Spec} b$ on the generic point is never used in the proof ([ExistsDegenerationDataTautologicalChartOfTrait.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDegenerationDataTautologicalChartOfTrait.lean#L18)). The three lemmas used in steps 2 to 4, and the lemma that the dimension of the abelian part plus the rank of the lattice is $g$, have no entries in this chapter; we describe only what their statements give, and the sentence "$q$ is the period of $D$ divided by the period of $T$" is our reading. We have not unfolded the Lean uniformization `Unif` beyond its name; it is Mumford's construction with the expansion property. In the Lean statement the forms $\varepsilon_i$ are a basis of the "balanced" forms for the identity involution, which are the symmetric bilinear forms on $\mathbb{Z}^r$.
