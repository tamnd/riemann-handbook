---
title: A finite cover with reduced fibre
decls:
  - GlobalTheory.PD.FibRed.exists_finCover_fibre_reduced
  - GlobalTheory.T.exists_finiteCover_projSpace_reduced_fibre_origin
  - GlobalTheory.T.isReduced_quotient_of_artinian_of_maximal_le'
  - GlobalTheory.isReduced_quotient_of_artinian_of_maximal_le
  - GlobalTheory.T.isArtinianRing_rB_quot_span_tco_of_isFinCover
  - GlobalTheory.PD.isArtinianRing_fib_quot
  - GlobalTheory.T.exists_finiteCover_affineCover_of_forms_no_commonZero
  - GlobalTheory.EtProj.isFinCover_of_forms
  - GlobalTheory.T.exists_forms_transversal_at_complexPoints
  - GlobalTheory.EtProj.Transv.exists_forms_transversal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A finite cover with reduced fibre

The third step of the proof of [the Lefschetz formula in the integral case](/entry/holomorphic-lefschetz-finite-etale-integral/) chooses a finite map $Z \to \mathbb{P}^d$ such that a given finite set of points lies over the origin of chart $0$ and the fibre over the origin is reduced. This section proves that such a map exists (Theorem 5.9.7). The map is given by $d + 1$ forms of one degree in a projective embedding of $Z$. We choose the forms so that the ratios $f_j / f_0$ vanish on the given points and are local parameters at every point where they all vanish. A short argument on Artinian rings then shows that the fibre is reduced.

We keep the notation of Definition 5.6.2. In this section $Z$ is an integral scheme over $\mathbb{C}$, smooth of relative dimension $d$ and projective, and $K$ is its function field, a $\mathbb{C}$-algebra through $Z \to \mathrm{Spec}\, \mathbb{C}$. For an open set $U$ of $Z$ that contains the generic point, the map $\mathcal{O}(U) \to K$ that sends a section to its germ at the generic point is injective, because $Z$ is integral. A *complex point* of $Z$ is a morphism $\mathrm{Spec}\, \mathbb{C} \to Z$ over $\mathbb{C}$. For a complex point $y$ in $U$ and $f \in \mathcal{O}(U)$ we write $f(y) \in \mathbb{C}$ for the value, and $\mathfrak{m}_y \subseteq \mathcal{O}(U)$ for the kernel of $f \mapsto f(y)$. Let $\iota : Z \to \mathbb{P}^N$ be a closed immersion over $\mathbb{C}$. For a homogeneous polynomial $f$ in $N + 1$ variables we put $D(f) = \iota^{-1}(D_+(f))$, the open set of $Z$ where $f$ does not vanish. If $f$ and $g$ are forms of the same degree, then $f/g$ is a function on $D(g)$.

**Definition 5.9.1 (Affine charts).** Let $B_I$ be a $\mathbb{C}$-subalgebra of $K$ for each nonempty set $I \subseteq \{0, \dots, d\}$. Open sets $U_0, \dots, U_d$ of $Z$ are *affine charts* for $(B_I)$ if, with $U_I = \bigcap_{i \in I} U_i$:
1. $U_I$ is affine for each nonempty $I$;
2. $U_0, \dots, U_d$ cover $Z$;
3. each $U_I$ contains the generic point of $Z$;
4. for each nonempty $I$, $B_I$ is the image of $\mathcal{O}(U_I)$ in $K$.

**Example 5.9.2.** Let $Z = \mathbb{P}^d$ with homogeneous coordinates $x_0, \dots, x_d$, let $F = K$ and let $U_i$ be the chart $x_i \neq 0$. Then $\mathcal{O}(U_I) = R_I(F)$, and $R_I(F)$ is integrally closed, so the $U_i$ are affine charts for $(R_I(K))$.

So if the $U_i$ are affine charts for $(R_I(K))$, then $R_I(K) \cong \mathcal{O}(U_I)$, and the rings of Definition 5.6.2 are the rings of the open sets of a cover of $Z$. This is how the Čech groups of Theorem 5.6.3 compute the cohomology of $Z$.

**Lemma 5.9.3 (Reduced Artinian quotients).** Let $A$ be a commutative ring and $I$ an ideal of $A$ such that $A/I$ is an [[Artinian ring|20QEAM8AX2]]. Assume that $\mathfrak{m} \subseteq I + \mathfrak{m}^2$ for every maximal ideal $\mathfrak{m}$ of $A$ with $I \subseteq \mathfrak{m}$. Then $A/I$ is [[reduced|SZHY975FFX]].

Lean: `GlobalTheory.T.isReduced_quotient_of_artinian_of_maximal_le'` (also `GlobalTheory.isReduced_quotient_of_artinian_of_maximal_le`, a second name).

*Proof.* Let $R = A/I$. A maximal ideal $M$ of $R$ is the image of a maximal ideal $\mathfrak{m} \supseteq I$ of $A$, and the image of $\mathfrak{m} \subseteq I + \mathfrak{m}^2$ is $M \subseteq M^2$. So $M = M^2$, and $M^k = M$ for all $k \geq 1$. Since $R$ is Artinian, it has finitely many maximal ideals $M_1, \dots, M_s$. They are pairwise coprime, so their product $J = M_1 \cdots M_s$ is their intersection, the [[Jacobson radical|XA0DCNH7WY]] of $R$. Then $J^k = M_1^k \cdots M_s^k = J$ for all $k \geq 1$. The Jacobson radical of an Artinian ring is nilpotent, so $J^k = 0$ for some $k$, and $J = 0$. A nilpotent element lies in every maximal ideal, so it lies in $J = 0$. $\square$

**Lemma 5.9.4 (The fibre is Artinian).** Let $k$ be a field, and let $F$, $x_0, \dots, x_d$ and $K$ be as in Definition 5.6.2 with $k$ in place of $\mathbb{C}$. If $K$ is a finite cover on charts, then the fibre $R_{\{0\}}(K)/(x_1/x_0, \dots, x_d/x_0)$ is an Artinian ring.

Lean: `GlobalTheory.T.isArtinianRing_rB_quot_span_tco_of_isFinCover` (also `GlobalTheory.PD.isArtinianRing_fib_quot`, a second name).

*Proof.* Let $\mathfrak{a}$ be the ideal $(x_1/x_0, \dots, x_d/x_0)$ of $R_{\{0\}}(K)$. The ring $R_{\{0\}}(F) = k[x_1/x_0, \dots, x_d/x_0]$ maps to $R_{\{0\}}(K)$, and $R_{\{0\}}(K)$ is integral over it by definition. Since $R_{\{0\}}(K)$ is smooth over $k$, it is of finite type over $k$, so it is of finite type and integral over $R_{\{0\}}(F)$, hence a finite module over $R_{\{0\}}(F)$. Each element of $R_{\{0\}}(F)$ is a polynomial in the $x_j/x_0$, so it is congruent to a constant modulo $\mathfrak{a}$. So the images of finitely many module generators span $R_{\{0\}}(K)/\mathfrak{a}$ over $k$. A $k$-algebra of finite dimension is Artinian. $\square$

**Lemma 5.9.5 (A finite cover from forms).** Let $\iota : Z \to \mathbb{P}^N$ be a closed immersion over $\mathbb{C}$. Let $n > 0$ and let $f_0, \dots, f_d$ be forms of degree $n$ in $N + 1$ variables such that $D(f_0), \dots, D(f_d)$ cover $Z$ and each $D(f_i)$ contains the generic point of $Z$. Then there are a subfield $F \subseteq K$ that contains $\mathbb{C}$ and elements $x_0, \dots, x_d \in F$ with these properties:
1. $K$ is a finite cover on charts for $x_0, \dots, x_d$;
2. $D(f_0), \dots, D(f_d)$ are affine charts for $(R_I(K))$;
3. for each $j$, $x_j$ is the image in $K$ of the function $f_j/f_0$ on $D(f_0)$.

Lean: `GlobalTheory.T.exists_finiteCover_affineCover_of_forms_no_commonZero` (also `GlobalTheory.EtProj.isFinCover_of_forms`, a second name).

*Proof.* The forms have no common zero on $Z$, so they define a morphism $\varphi = [f_0 : \dots : f_d] : Z \to \mathbb{P}^d$ over $\mathbb{C}$. The inverse image of the chart $x_i \neq 0$ is $D(f_i)$. Since $n > 0$, $D_+(f_i)$ is affine, and so is its inverse image $D(f_i)$ under the closed immersion $\iota$. So $\varphi$ is affine. It is proper, because $Z$ is proper over $\mathbb{C}$ and $\mathbb{P}^d$ is separated. A morphism that is proper and affine is finite. Let $F$ be the image in $K$ of the function field of $\mathbb{P}^d$, and let $x_j$ be the image of the ratio $x_j/x_0$ of coordinates, which is the function $f_j/f_0$ on $D(f_0)$. So $x_0 = 1$. Since $\varphi$ is finite and $Z$ has dimension $d$, $\varphi$ is dominant, the $x_j/x_0$ are algebraically independent, and $K$ is finite over $F$. It is separable, because the characteristic is $0$. Since $Z$ is smooth, it is normal, so the ring $\mathcal{O}(D(f_I))$ of $\varphi^{-1}(U_I)$ is the integral closure $R_I(K)$ of $R_I(F)$ in $K$. Each $R_{\{i\}}(K) \cong \mathcal{O}(D(f_i))$ is smooth over $\mathbb{C}$, because $D(f_i)$ is open in $Z$. $\square$

**Lemma 5.9.6 (Transversal forms).** Let $\iota : Z \to \mathbb{P}^N$ be a closed immersion over $\mathbb{C}$ and $S$ a finite set of complex points of $Z$. There are $n > 0$ and forms $f_0, \dots, f_d$ of degree $n$ in $N + 1$ variables with these properties. Put $t_j = f_j / f_0 \in \mathcal{O}(D(f_0))$ for $1 \leq j \leq d$.
1. $D(f_0), \dots, D(f_d)$ cover $Z$, and each $D(f_i)$ contains the generic point of $Z$.
2. Each $y \in S$ lies in $D(f_0)$, and $t_j(y) = 0$ for all $j$.
3. If $y$ is a complex point of $D(f_0)$ with $t_j(y) = 0$ for all $j$, then $\mathfrak{m}_y \subseteq (t_1, \dots, t_d) + \mathfrak{m}_y^2$ in $\mathcal{O}(D(f_0))$.

Lean: `GlobalTheory.T.exists_forms_transversal_at_complexPoints` (also `GlobalTheory.EtProj.Transv.exists_forms_transversal`, a second name).

Condition 3 says that $t_1, \dots, t_d$ are local parameters at every common zero in $D(f_0)$.

*Proof.* We give the outline. It uses four facts that we take as given. (a) There are $n > 0$ and forms $h, g_1, \dots, g_d$ of degree $n$ such that each $D(g_j)$ contains the generic point, each $g_j$ vanishes on $S$, every common zero of $h, g_1, \dots, g_d$ lies in $S$, and for each $y \in S$ and each form $f$ of degree $n$ with $y \in D(f)$ we have $h/f \in \mathfrak{m}_y^2$ and $\mathfrak{m}_y \subseteq (g_1/f, \dots, g_d/f) + \mathfrak{m}_y^2$. (b) The algebraic form of Sard's theorem: for an affine open set $U$ of $Z$ and $\phi_1, \dots, \phi_d \in \mathcal{O}(U)$, there is a set $E \subseteq \mathbb{C}^d$ of Lebesgue measure $0$ such that for $c \notin E$, at each complex point $z$ of $U$ with $\phi_j(z) + c_j = 0$ for all $j$, we have $\mathfrak{m}_z \subseteq (\phi_1 + c_1, \dots, \phi_d + c_d) + \mathfrak{m}_z^2$. (c) On an affine open set, the complex points where $\phi_1, \dots, \phi_d$ vanish and are local parameters form a finite set. (d) For each finite set $T$ of complex points there is a form of degree $n$ that does not vanish on $T$ or at the generic point.

Take $h$ and $g_j$ from (a), and apply (b) to $U = D(h)$ and $\phi_j = g_j/h$. For each $j$ there is at most one $a_j \in \mathbb{C}$ such that $g_j + a_j h$ vanishes at the generic point. Choose $c \notin E$ with $c_j \neq a_j$ for all $j$. This is possible, because the excluded set has measure $0$. Put $F_j = g_j + c_j h$. The common zeros of $F_j/h$ in $D(h)$ are local parameters by (b), so they form a finite set $T'$ by (c). Take $f_0$ from (d) for $T = S \cup T'$, and put $f_j = F_j$ for $j \geq 1$.

Now we check the conditions. A point outside all $D(F_j)$ lies in $T'$ if it lies in $D(h)$. Otherwise it is a common zero of $h$ and the $g_j$, so it lies in $S$. In both cases it lies in $D(f_0)$, so the $D(f_i)$ cover $Z$. The generic point lies in $D(F_j)$ because $c_j \neq a_j$. For $y \in S$, $g_j(y) = 0$ and $h(y) = 0$, so $t_j(y) = 0$. For 3, let $y \in D(f_0)$ be a common zero of the $t_j$. If $y \in S$, then $t_j = g_j/f_0 + c_j h/f_0$ with $h/f_0 \in \mathfrak{m}_y^2$, and (a) gives the inclusion. If $y \notin S$, then $y \in D(h)$, and the inclusion for the $F_j/h$ from (b) gives the inclusion for the $t_j = (F_j/h)(h/f_0)$, since $h/f_0$ does not vanish at $y$. $\square$

**Theorem 5.9.7 (A finite cover with reduced fibre over the origin).** Let $Z$ be an integral scheme over $\mathbb{C}$, smooth of relative dimension $d$ and projective, with function field $K$. Let $S$ be a finite set of complex points of $Z$. There are a subfield $F \subseteq K$ that contains $\mathbb{C}$, elements $x_0, \dots, x_d \in F$ and open sets $U_0, \dots, U_d$ of $Z$ with these properties:
1. $K$ is a finite cover on charts for $x_0, \dots, x_d$;
2. $U_0, \dots, U_d$ are affine charts for $(R_I(K))$;
3. the fibre $R_{\{0\}}(K)/(x_1/x_0, \dots, x_d/x_0)$ is reduced;
4. each $y \in S$ lies in $U_0$, and for $1 \leq j \leq d$, every $f \in \mathcal{O}(U_0)$ whose image in $K$ is $x_j/x_0$ has $f(y) = 0$.

Lean: `GlobalTheory.PD.FibRed.exists_finCover_fibre_reduced` (also `GlobalTheory.T.exists_finiteCover_projSpace_reduced_fibre_origin`, a second name).

*Proof.* Since $Z$ is projective, there is a closed immersion $\iota : Z \to \mathbb{P}^N$ over $\mathbb{C}$. The lemma on transversal forms gives $n > 0$ and forms $f_0, \dots, f_d$. The lemma on a finite cover from forms gives $F$ and $x_0, \dots, x_d$ with properties 1 and 2 for $U_i = D(f_i)$, and $x_j = f_j/f_0$ in $K$. In particular $x_0 = 1$, and $t_j = f_j/f_0 \in \mathcal{O}(U_0)$ maps to $x_j/x_0$ in $K$.

The map $\mathcal{O}(U_0) \to K$ is injective, and by property 2 with $I = \{0\}$ its image is $R_{\{0\}}(K)$. It sends $t_j$ to $x_j/x_0$. So it gives an isomorphism
$$
\mathcal{O}(U_0)/(t_1, \dots, t_d) \cong R_{\{0\}}(K)/(x_1/x_0, \dots, x_d/x_0).
$$
By the lemma that the fibre is Artinian, both rings are Artinian. The open set $U_0$ is affine, and $\mathcal{O}(U_0)$ is a finitely generated $\mathbb{C}$-algebra. By Hilbert's Nullstellensatz every maximal ideal of $\mathcal{O}(U_0)$ is $\mathfrak{m}_y$ for a complex point $y$ of $U_0$. If $\mathfrak{m}_y$ contains $t_1, \dots, t_d$, then all $t_j(y) = 0$, and the lemma on transversal forms gives $\mathfrak{m}_y \subseteq (t_1, \dots, t_d) + \mathfrak{m}_y^2$. The lemma on reduced Artinian quotients shows that $\mathcal{O}(U_0)/(t_1, \dots, t_d)$ is reduced, and the isomorphism gives property 3.

For property 4, let $y \in S$. By the lemma on transversal forms, $y \in U_0$ and $t_j(y) = 0$. If $f \in \mathcal{O}(U_0)$ has image $x_j/x_0$ in $K$, then $f = t_j$, because the map to $K$ is injective. So $f(y) = 0$. $\square$

In the proof of Theorem 5.6.4, $S$ is the image in $Z$ of the set $\Phi$ of fixed points under $c_1$. Property 4 puts these images in chart $0$ over the origin, and property 3 is condition 2 of Theorem 5.6.3 for $K$.

**Remark 5.9.8 (Formalization).** The $\mathbb{C}$-algebra structure on $K$ is an argument with a hypothesis that it equals the one given by $Z \to \mathrm{Spec}\, \mathbb{C}$. The second name of Theorem 5.9.7 is proved by a `first` list whose last two alternatives name `GlobalTheory.PD.FibRed.quotEquiv_of_germ`, the isomorphism of the proof, which cannot close the goal; the first alternative succeeds, so they are never tried ([ExistsFiniteCoverProjSpaceReducedFibreOriginStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsFiniteCoverProjSpaceReducedFibreOriginStatement.lean#L9)). That file imports `Mathlib` twice. The theorem proves that the whole fibre over the origin is reduced, which is more than reducedness at the points of $S$. The facts (a) to (d) in the proof of Lemma 5.9.6, and the two facts on pulled back coordinate ratios and chart covers behind Lemma 5.9.5, were read as statements, not proofs. Fact (b) is stated with a set of Lebesgue measure $0$ in $\mathbb{C}^d$.
