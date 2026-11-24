---
title: Unramified Howe duality
decls:
  - GlobalTheory.Hk3.HoweDuality.step
  - GlobalTheory.Hk3.HoweDuality.fixed_mem_span
  - GlobalTheory.Hk3.howeUnram_holds
---
## Unramified Howe duality

This section proves the spherical part of the [local theta correspondence](/learn/theta/#the-local-theta-correspondence) for an unramified unitary dual pair: in the lattice model of the [previous section](/entry/gram-class-orbit-mod-lower/), every vector fixed by the integral points of one member of the pair lies in the span of the orbit of the vacuum under the other member. The proof is an induction on the lattice index, run by an abstract lemma on representations that permute a family of lines. The result is passed by the [literature step](/step/every-character-of-literature/) to the [separation of functionals](/entry/functionals-separate-of-howe-unram-of-siegel-weil/) of the [Bessel seesaw chapter](/proof/bessel-seesaw/), where it is the input at the unramified places.

We keep the notation of the previous section: a local dual pair $(\rho, \omega)$ on $M$ for Hermitian $J_S \in GL_n(\mathcal{O})$ and $J_T \in GL_{n'}(\mathcal{O})$, with $X = M_{n' \times n}(L)$, and we write $K_S$ and $K_T$ for the integral points of $U(J_S)$ and $U(J_T)$.

### An abstract lemma

**Lemma 2.3.1 (Fixed vectors by height).** Let a group $G$ act on a set $I$, let $\pi : G \to \operatorname{End}(M)$ be a homomorphism of monoids, and let $(V_i)_{i \in I}$ be independent subspaces of $M$ that span $M$, each contained in a line, with $\pi(g) V_i \subseteq V_{g i}$. Let $\mu : I \to \mathbb{N}$ be invariant under $G$, and let $S \subseteq M$ be a subspace of $G$-fixed vectors. For $i \in I$ let $W_i = \sum_{g \in G} V_{g i}$. Suppose that for every $i$ such that $W_i$ contains a nonzero $G$-fixed vector there are $v \in S$ and $u \in \sum_{\mu(j) < \mu(i)} V_j$ with $v - u \in W_i$ and $v - u \neq 0$. Then every $G$-fixed vector of $M$ lies in $S$.

Lean: `GlobalTheory.fixed_mem_of_orbit_height` (also `GlobalTheory.T.invariant_mem_of_orbit_height_separation`, a second name)

*Proof.* Every vector of $M$ is a finite sum of components in the $V_i$, and since $\pi(g)$ carries $V_i$ into $V_{g i}$, the part of a $G$-fixed vector lying over one orbit is again $G$-fixed. So it is enough to show that a $G$-fixed $w \in W_i$ lies in $S$, and we do this by strong induction on $\mu(i)$. Since $\pi(g)$ is invertible and maps $V_i$ into $V_{g i}$, a $G$-fixed vector of $W_i$ is determined by its component in $V_i$, which lies in a line; so the $G$-fixed vectors of $W_i$ form at most a line. If $w \neq 0$, take $v$ and $u$ as in the hypothesis. The orbit of $i$ has height $\mu(i)$, so $u$ has no component over it and $v - u$ is the part of $v$ over the orbit of $i$. Hence $v - u$ is $G$-fixed and nonzero, and $w = t(v - u)$ for some $t$. Then $u = v - (v - u)$ is $G$-fixed and lives on orbits of smaller height, so by induction $u \in S$, and $w = t v - t u \in S$. $\square$

### The step and the induction

**Lemma 2.3.2 (Height step).** Let the data form a local dual pair with $L$ of characteristic $0$ and complete, and let $s \neq 0$ be a lattice vacuum such that the vectors $\rho(x) s$ span $M$. Let $x \in X$ and suppose that some nonzero $w \in M$, fixed by $\omega(1, h)$ for every $h \in K_T$, lies in the span of the vectors $\rho(h x) s$ with $h \in K_T$. Then there are $v$ in the span of $\{\omega(g, 1) s : g \in U(J_S)\}$ and $u$ in the span of $\{\rho(y) s : \operatorname{idx}(y) < \operatorname{idx}(x)\}$ with $v - u \neq 0$ and $v - u$ in the span of $\{\rho(h x) s : h \in K_T\}$.

Lean: `GlobalTheory.Hk3.HoweDuality.step`

*Proof.* The fixed vector gives an integral matrix $l \in X(\mathcal{O})$ such that $(x - l) J_S^{-1} (x - l)^*$ is integral: a $K_T$-fixed vector on the orbit of $x$ can only exist when the Gram matrix of $x$ is integral up to an integral translation. Apply the [orbit theorem](/entry/gram-class-orbit-mod-lower/) to $x - l$. The lattice index does not change under integral translation, so $\operatorname{idx}(x - l) = \operatorname{idx}(x)$, and for $h \in K_T$ the matrices $h(x - l)$ and $h x$ differ by an integral matrix, so $\rho(h(x - l)) s$ is a nonzero multiple of $\rho(h x) s$. The vectors $v$ and $u$ given for $x - l$ therefore work for $x$. $\square$

**Theorem 2.3.3 (Spherical vectors of $U(J_T)$).** Let the data form a local dual pair with $L$ of characteristic $0$ and complete, and let $s \neq 0$ be a lattice vacuum such that the vectors $\rho(x) s$ span $M$. If $w \in M$ is fixed by $\omega(1, h)$ for every $h \in K_T$, then
$$w \in \operatorname{span}\{\omega(g, 1) s : g \in U(J_S)\}.$$

Lean: `GlobalTheory.Hk3.HoweDuality.fixed_mem_span`

*Proof.* Apply the lemma on fixed vectors by height with $G = K_T$ acting on the classes $I = X / X(\mathcal{O})$ by left multiplication, $\pi(h) = \omega(1, h)$, $V_c$ the span of the vectors $\rho(x) s$ with $x$ in the class $c$, and $\mu(c) = \operatorname{idx}(x)$ for a representative $x$ of $c$. The $V_c$ are lines by the shift rule for lattice vacua, they are independent and span $M$, and condition 6 of a local dual pair gives $\omega(1, h) V_c \subseteq V_{h c}$. The index is invariant under $K_T$. The subspace $S$ is the span of the $\omega(g, 1) s$, and its vectors are $K_T$-fixed because the two factors of $\omega$ commute and $s$ is fixed by $K_T$ (condition 7). The hypothesis of the lemma is the height step. $\square$

**Theorem 2.3.4 (Unramified Howe duality).** Let the data form a local dual pair with $L$ of characteristic $0$ and complete, and let $s \neq 0$ be a lattice vacuum such that the vectors $\rho(x) s$ with $x \in X$ span $M$. Then:

1. every $w \in M$ fixed by $\omega(g, 1)$ for all $g \in K_S$ lies in the span of $\{\omega(1, h) s : h \in U(J_T)\}$;
2. every $w \in M$ fixed by $\omega(1, h)$ for all $h \in K_T$ lies in the span of $\{\omega(g, 1) s : g \in U(J_S)\}$.

Lean: `GlobalTheory.Hk3.howeUnram_holds`

*Proof.* Part 2 is the previous theorem. For part 1, exchange the roles of the two spaces: the data $\rho'(x') = \rho(J_T^{-1} x'^* J_S)$ for $x' \in M_{n \times n'}(L)$, the Hermitian adjoint for the exchanged pair, and $\omega'(h, g) = \omega(g, h)$ again form a local dual pair for $(J_T, J_S)$ with $\delta$ replaced by $-\delta$, with the same vacuum $s$ and the same spanning property. Part 2 for this pair is part 1. $\square$

In the classical language: in the lattice model of the Weil representation of an unramified dual pair, the $K_T$-spherical vectors are generated by the vacuum under $U(J_S)$, and conversely. Combined with the Satake isomorphism, this gives the unramified theta correspondence; see R. Howe, *θ-series and invariant theory* (1979), and S. Rallis, *Langlands' functoriality and the Weil representation* (1982), where unramified results of this kind appear. The theorem here is only this spherical statement, not the full Howe duality conjecture on irreducible quotients.

**Remark 2.3.5 (Formalization).** The three results are in [RhoMemOfMkEq.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L107) (the step at L107, the induction at L145, the theorem at L250), and the abstract lemma at [FixedMemOfOrbitHeight.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/FixedMemOfOrbitHeight.lean#L205). The statement is the proposition `HoweUnram` at [HoweUnram.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisGeometry₂/HoweUnram.lean#L8); the folder name suggests a cited theorem, but the code proves it. The fixed vector in the height step is used only to make the Gram matrix of $x$ integral after a translation. The swap of the two roles is a separate lemma, `unramifiedLocalDualPair_swap_hermitianAdjoint`. The representation is purely algebraic: $M$ is a complex vector space with no topology, and $U(J_S)$, $U(J_T)$ are abstract groups of matrices.
