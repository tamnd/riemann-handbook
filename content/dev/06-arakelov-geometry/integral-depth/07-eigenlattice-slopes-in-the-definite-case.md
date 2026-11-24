---
title: Eigenlattice slopes in the definite case
decls:
  - GlobalTheory.DefFibre.fibreAt_defCase
  - GlobalTheory.T.definiteCase_cuspForm_fibre_slope_ge_bound
  - GlobalTheory.DefPt.eigLat_slope_definite
  - GlobalTheory.T.eigenlattice_slope_lower_bound_definite_case
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Eigenlattice slopes in the definite case

This section gives a lower bound for the slope of the lattice of integral cusp forms on which a finite group of level operators acts through a character, when the signature is definite. On each component, the cusp forms of a theta weight are the image of a dual Weyl tensor lattice at a rational point, and its slope is bounded below by the degrees of Lie lines, which [the previous section](/entry/frame-deg-def/) computes through flat sections. A level move lemma then passes from the components to the eigenlattice. The bound is the input of the low defect bound of [the previous chapter](/entry/defect-bound-of-connected-alt/) in the definite case.

Let $X$ be the moduli space of a datum of signature $(s, t)$ over its coefficient field $F$, $U$ a family of uniformizations at level $r$ over the complex embeddings of $F$, and $\xi \in \mathbb{R}$. For a weight $a$ on factors and $n$ columns, $G(a, n)$ is the theta weight. For a factor weight, $\mathrm{part}(a, \tau)$ is the partition of $a$ at $\tau$, with a size and the dimension of the associated representation. Let $\mathrm{lrd}(E)$ be the logarithm of the root discriminant of $E$. For a lattice $L$ in an $F$-vector space with norms $N_\sigma$ at the complex embeddings $\sigma$, $\mu(N, L)$ is the slope of $L$ for the hermitian metrics with squared norms $N_\sigma$ ([hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes)); it is $0$ if the norms do not come from hermitian forms.

**Definition 3.7.1 (The definite case).** The *definite case* holds for $U$ and $\xi$ if $t = 0$, $s \ge 1$, the level is good at every prime and has $A = 1$, $F$ is algebraically closed in the function field of the moduli space, each uniformization at a good embedding is unfolded, and each base point $\xi_0$ of each chart has $|\tau(\xi_0)| = \xi$ for all $\tau$.

**Definition 3.7.2 (Flat sections of constant degree).** For $c_1 \in \mathbb{R}$, *flat sections of degree $-c_1$ exist* if for each component $Z$ and each $\tau \in \Psi$ there is a flat section of the flat weight of $\tau$ on $Z$, and every such flat section has degree $-c_1$.

**Definition 3.7.3 (Definite bound).** For a weight $a$, $n \in \mathbb{N}$ and $c_1 \in \mathbb{R}$ put
$$\begin{aligned}
\beta_{\mathrm{def}} &= \sum_{\tau \in \Psi} \Bigl( \Bigl(\frac{\lvert \mathrm{part}(a, \tau) \rvert}{s} + \frac{n}{2}\Bigr) c_1 - \frac{\log \dim \mathrm{part}(a, \tau)}{2} \Bigr) \\
&\quad + n\, |\Psi|\, s\, \Bigl(\frac{\log 2\pi}{4} - \frac{\mathrm{lrd}(E)}{2}\Bigr).
\end{aligned}$$

**Definition 3.7.4 (Fibre bound).** Let $Z$ be a component, $G$ a weight and $\beta \in \mathbb{R}$. The *fibre bound* $\beta$ holds at $Z$ for $G$ if there are a nonempty finite set $\iota$, a lattice $L \subseteq F^\iota$, invertible complex matrices $Y_\sigma$ indexed by $\iota$ for each embedding $\sigma$ of $F$, and an injective $F$-linear map $\varphi$ from $F^\iota$ to the rational functions on the moduli space, with:

1. the image of $\varphi$ is the space of cusp forms of weight $G$ on $Z$;
2. $\beta \le \tfrac12 \mu(N_Y, L)$, where $N_{Y,\sigma}(x) = \|Y_\sigma x\|$;
3. $\varphi(L)$ is integral: every valuation in the valuation set of each finite place is $\ge 0$ on $\varphi(x)$ for $x \in L$;
4. for each $\sigma$, $x$ and each frame $z$ on $Z$ for the uniformization at $\sigma$, the norm of $\varphi(x)$ at $z$ for the weight $G$ and the parameter $\xi$ is at most $\|Y_\sigma x\|$.

**Theorem 3.7.5 (Fibre bound in the definite case).** Assume the definite case. Let $a$ be a weight in the domain for $n$ columns, and assume that flat sections of degree $-c_1$ exist. Then for every component $Z$ the fibre bound $\beta_{\mathrm{def}}$ holds at $Z$ for $G(a, n)$.

Lean: `GlobalTheory.DefFibre.fibreAt_defCase` (also `GlobalTheory.T.definiteCase_cuspForm_fibre_slope_ge_bound`, a second name).

*Proof.* An input gives rational point data $P$ on $Z$: a point over a totally complex field with a frame, Lie lines and a matrix family. A second input gives an injective map $\varphi$ from a dual Weyl tensor space to the cusp forms of weight $G(a, n)$ at $P$, with image the cusp forms on $Z$. A third input gives the integrality of the coordinates and the norm bound for the fibre, that is, parts 3 and 4. The lattice $L$ is the lattice of the local matrix family of $P$ for $a$ and $n$, and the matrices $Y_\sigma$ have nonzero determinant.

For the slope, a lemma on dual Weyl fibre lattices, an input, gives
$$\tfrac12 \mu(N_Y, L) \ge \sum_{\tau} \Bigl(\frac{\lvert \mathrm{part}(a, \tau) \rvert}{\mathrm{mult}(\tau)}\, \deg_\tau - \frac{\log \dim \mathrm{part}(a, \tau)}{2}\Bigr) + \Theta,$$
summed over all complex embeddings $\tau$ of $E$, where $\deg_\tau$ is the degree of the determinant of the Lie line at $\tau$ and $\Theta$ is $n$ times the degree of the theta line. For $\tau \notin \Psi$ we have $\mathrm{mult}(\tau) = t = 0$, so the partition at $\tau$ is empty, its dimension is $1$, and the term is $0$. For $\tau \in \Psi$, the degree of the dual determinant of the Lie line is minus the degree of a flat section, so $\deg_\tau = c_1$. A further input bounds the theta line from below by half the determinant of the Lie lines at the definite point, which gives the terms $\tfrac{n}{2} c_1$ and the constant term $n |\Psi| s (\tfrac14 \log 2\pi - \tfrac12 \mathrm{lrd}(E))$. Adding the inequalities gives $\beta_{\mathrm{def}} \le \tfrac12 \mu(N_Y, L)$. $\square$

Now let $\Gamma_0$ be a finite group with a map $\mathrm{lev}$ to pairs of $\mathcal{O}_E$-linear endomorphisms of the lattice of the datum, which acts on the rational functions of the moduli space by level operators, and $\chi \colon \Gamma_0 \to F^\times$ a character. The *eigenlattice* $\mathcal{E}_\chi(G)$ is the intersection of the lattice of integral cusp forms of weight $G$ with the $\chi$-eigenspace of $\Gamma_0$. The norms $N_W$ on cusp forms are the Petersson norms at the embeddings of $F$ through the dictionary of frames.

**Theorem 3.7.6 (Eigenlattice slope in the definite case).** Assume the definite case. Assume that the moduli space has finitely many components, at least one, that the dictionary of frames lands in the chart domains, that $\Gamma_0$ acts by level operators and acts freely on points (if $g$ maps a point $y$ to a point $y'$ over the same point, then $g = 1$). Let $a$ be a weight in the domain for $n$ columns such that the weight $G(a, n)$ is good (the Petersson norms are hermitian, and the lattice of integral cusp forms is finitely generated and spans), and assume that flat sections of degree $-c_1$ exist. Then $\mathcal{E}_\chi(G(a, n)) \ne 0$ and
$$\beta_{\mathrm{def}} \le \tfrac12\, \mu\bigl(N_W, \mathcal{E}_\chi(G(a, n))\bigr).$$

Lean: `GlobalTheory.DefPt.eigLat_slope_definite` (also `GlobalTheory.T.eigenlattice_slope_lower_bound_definite_case`, a second name).

*Proof.* This is the level move lemma for eigenlattices in the definite case, an input, applied with the bound $\beta_{\mathrm{def}}$ and with the fibre bound at every component from the previous theorem. $\square$

**Remark 3.7.7 (Formalization).** In the theorem on fibres, the terms of the slope lemma for $\tau \notin \Psi$ vanish because $\mathrm{mult}(\tau) = 0$ and division by zero gives $0$, together with a lemma that the dimension of an empty partition is $1$ ([DefiniteCaseCuspFormFibreSlopeGeBound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DefiniteCaseCuspFormFibreSlopeGeBound.lean#L36)). The theorem on eigenlattices is a single application of the level move lemma ([EigenlatticeSlopeLowerBoundDefiniteCase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EigenlatticeSlopeLowerBoundDefiniteCase.lean#L11)). The slope $\mu$ is defined as $0$ when the norms do not come from hermitian forms. The rational point data, the dual Weyl tensor map, the integrality and norm bounds, the degree of the dual determinant of the Lie line, the theta line bound, the slope lemma and the level move lemma are known to us by their statements. We have not unfolded the components, the partitions, the flat sections, the Petersson norms or the level operators.
