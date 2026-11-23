---
title: The local factor at a twist place
decls:
  - GlobalTheory.T.splitPlaceChart_parahoric_level_stabiliser_height
  - GlobalTheory.T.flatIntegrand_localFactor_splits_twistPlace
  - GlobalTheory.ChainTw.OnePlace.local_factor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local factor at a twist place

This section moves the local computation of [the last section](/entry/local-zeta-twisted/) into the global doubling integral of one step of a theta chain. At a twist place, the unitary group is a general linear group, the level group is a parahoric subgroup, and the level character is a tame character. Under this dictionary, right translation at the twist place multiplies the doubling integrand by the local function $\zeta$ of the last section, and the integral of $\zeta$ is an explicit product of local $L$-factors. The result feeds [the peeling of the twist places](/entry/q-peel-holds/) in the next section.

**Setting.** Let $E/F$ be a CM extension of number fields and $\mathbb{A}$ the adeles of $F$. A theta chain gives hermitian spaces $V_0, V_1, \dots, V_m$ over $E$, where $V_j$ has rank $r + jt$, with lattices, level groups and level characters at the finite places. We call the data at the index $j$ a *stage* of the chain. A *step* from the stage $V_k$ to the stage $V_{k+1}$ is a [theta lift](/learn/theta/#the-global-theta-lift) for the dual pair $(U(V_k), U(V_{k+1}))$: a Weil representation $\omega$ of $U(V_k)(\mathbb{A}) \times U(V_{k+1})(\mathbb{A})$ with splitting characters $\chi_{S,k+1}$ and $\chi_{T,k+1}$ of $\mathbb{A}_E^\times$, a test function, and the lift. The *common datum* of the chain fixes, among other things, a finite set $P$ of places of $E$, the splitting characters, and characters $\mu_1, \dots, \mu_m$. A *twist* of the common datum splits $P$ as a disjoint union $P' \sqcup Q$. At each $\mathfrak{P} \in Q$ it gives a nontrivial character $\xi_{\mathfrak{P}}$ of the multiplicative group of the residue field at $\mathfrak{P}$, and the level character of the chain at $\mathfrak{P}$ is $\xi_{\mathfrak{P}}^{-1}$. The places of $Q$ are the *twist places*. A twist place lies over a place $v$ of $F$ that splits in $E$.

Fix a twist place $\mathfrak{P}$ over $v$, and let $F_v$ be the completion, with residue field of $q$ elements. A character $\mu$ of $F_v^\times$ *lifts* $\xi_{\mathfrak{P}}$ if its restriction to $\mathcal{O}_v^\times$ is $\xi_{\mathfrak{P}}$ composed with the reduction map. At the split place $v$, the projection to the factor at $\mathfrak{P}$ identifies $U(V_k)(F_v)$ with a general linear group over $F_v$. A *chart* at $v$ is a homomorphism $\iota \colon \mathrm{GL}_{r+kt}(F_v) \to U(V_k)(\mathbb{A})$ with image in the factor at $v$, such that the matrix of $\iota(y)$ in the frame of the lattice is $y$, up to a reordering of the basis that keeps the first $r$ vectors. Let $G_v$ be the local group $U(V_k)(F_v)$, and $\mathrm{emb}$ its inclusion into the adelic group.

**Theorem 2.3.1 (Charts at a twist place).** Let $V_k$ be a stage of a twisted theta chain, $\mathfrak{P}$ a twist place over $v$, and fix the projection at $\mathfrak{P}$. Then:

1. $v$ is the place of $F$ below $\mathfrak{P}$, and the residue field of $F_v$ has $N(\mathfrak{P})$ elements;
2. every character of $F_v^\times$ that lifts $\xi_{\mathfrak{P}}$ is tame and not unramified;
3. for $k < m$, every character of $F_v^\times$ that matches $\chi_{S,k+1}$ or $\chi_{T,k+1}$ at the place $v$ lifts $\xi_{\mathfrak{P}}$;
4. for every chart $\iota$ there is an isomorphism of topological groups $e \colon \mathrm{GL}_{r+kt}(F_v) \to G_v$ with $\iota = \mathrm{emb} \circ e$, such that $e(y)$ stabilises the local lattice if and only if $y \in \mathrm{GL}_{r+kt}(\mathcal{O}_v)$, and such that the local doubling height composed with $e$ is a height in the sense of [the last section](/entry/local-zeta-twisted/) for every local uniformizer;
5. $\iota(y)$ lies in the level group if and only if $y$ lies in the parahoric subgroup $J$ with blocks $r$ and $kt$;
6. for a character $\xi_l$ that lifts $\xi_{\mathfrak{P}}$ and $y \in J$, the level character at $\iota(y)$ is $\xi_l(\det y_{22})^{-1}$.

Lean: `GlobalTheory.T.splitPlaceChart_parahoric_level_stabiliser_height`.

*Proof.* Claim 1 compares the projection at $\mathfrak{P}$ with the residue field. For claim 2, a lift of $\xi_{\mathfrak{P}}$ is trivial on $1 + \mathfrak{p}_v$, so it is tame, and it is not trivial on $\mathcal{O}_v^\times$ since $\xi_{\mathfrak{P}} \neq 1$. For claim 3, at each place of $P$ the residue characters of $\chi_{S,k+1}$ and $\chi_{T,k+1}$ are the inverse of the level character of the chain. At a twist place this inverse is $\xi_{\mathfrak{P}}$. A character of $F_v^\times$ that matches a splitting character at $v$ lifts its residue character, so it lifts $\xi_{\mathfrak{P}}$. Claims 4 to 6 come from the frame of the stage: the frame is self-dual at $v$, so the chart is an isomorphism onto $G_v$ that carries $\mathrm{GL}_{r+kt}(\mathcal{O}_v)$ to the stabiliser of the lattice, the doubling height to a bi-invariant function with the torus values $q^{-|e|}$, the parahoric to the level group, and the character $\xi_l(\det y_{22})^{-1}$ to the level character. $\square$

**Definition 2.3.2 (Doubling integrand).** Fix a step from $V_k$ to $V_{k+1}$. Let $\Phi$ be the test function of the step for a polynomial $\varphi$, let $a$ be a majorant of $V_k$, and let $F_1, F_2$ be automorphic forms on $U(V_k)$. For real $z$ put
$$\mathcal{I}_z(g) = c_\Phi(g) \cdot H_a(g)^{z - t/2} \cdot \langle R(g)\overline{F_1}, \overline{F_2} \rangle, \qquad g \in U(V_k)(\mathbb{A}).$$
Here $c_\Phi(g)$ is the matrix coefficient $\langle \omega(g,1)\Phi, \Phi \rangle$ of the Weil representation, $H_a$ is the height of the image of $(g, 1)$ in the doubled group, $R$ is right translation, and the last factor is a matrix coefficient of $R$. The shift $t/2$ is half the difference of the ranks of $V_{k+1}$ and $V_k$.

This is the integrand of the doubling zeta integral of the step at the point $s = z$. The [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula) expresses the inner product of two theta lifts by its integral at $z = t/2$.

For $\mathfrak{P} \in Q$ put $\alpha_i = (\mu_i \mu_{k+1}^{-1})(\mathfrak{P})$ and
$$\ell_{\mathfrak{P}} = \prod_{i=1}^{k} \prod_{n=1}^{t} \frac{1}{(1 - \alpha_i q^{-n})(1 - \alpha_i^{-1} q^{-n})} \cdot \prod_{n = t+1}^{(k+1)t} (1 - q^{-n}).$$

We say that $F_1$ *has the twisted type of the chain* if at each twist place, for every lift $\xi_l$ of $\xi_{\mathfrak{P}}$, every local uniformizer and every chart $\iota$, the vector $\overline{F_1}$ is generic of type $\xi_l$, in the sense of [the last section](/entry/local-zeta-twisted/), for the representation $y \mapsto R(\iota(y))$ of $\mathrm{GL}_{r+kt}(F_v)$, with the parameters of the chain at the index $k$. These parameters are defined in [the section on Hecke parameters](/entry/up-q-holds/).

**Theorem 2.3.3 (Local factor at a twist place).** Assume the unramified doubling identity and the rapid decay of cusp forms. Assume the node gap condition. Let $k < m$, take a step from $V_k$ to $V_{k+1}$, a measure of covolume one, a majorant $a$, a polynomial $\varphi$, forms $u_1, u_2$ of the stage with $K$-finite vectors, and let $F_1, F_2$ be their automorphic functions. Assume that $F_1$ has the twisted type of the chain. Let $z > t/2 - 1$ and $\mathfrak{P} \in Q$ over $v$. Then there are an open subgroup $J_v \subseteq G_v$, a Haar measure $\mu$ on $G_v$ with $\mu(J_v) = 1$ and an integrable function $\zeta \colon G_v \to \mathbb{C}$ with $\zeta = 1$ on $J_v$, such that:

1. the component of $g$ at $v$ lies in the level group if and only if the projection of $g$ to $G_v$ lies in $J_v$;
2. if $z = t/2$, then $\int_{G_v} \zeta\, d\mu = \ell_{\mathfrak{P}}$;
3. if $x$ is integral at every place outside the finite set of bad places and $x_v = 1$, then $\mathcal{I}_z(x \cdot \mathrm{emb}(y)) = \zeta(y)\, \mathcal{I}_z(x)$ for all $y \in G_v$.

Lean: `GlobalTheory.ChainTw.OnePlace.local_factor` (also `GlobalTheory.T.flatIntegrand_localFactor_splits_twistPlace`, a second name).

*Proof.* The proof has five steps.

1. *Charts.* At $v$ there are a uniformizer $\varpi$, a character $\mu_T$ of $F_v^\times$ that matches $\chi_{T,k+1}$, and a chart $\iota$. By the theorem on charts, $\iota = \mathrm{emb} \circ e$ for an isomorphism $e$. Under $e$ the level group is the parahoric $J$, the level character comes from $\mu_T$, which lifts $\xi_{\mathfrak{P}}$, and the height is a height $H$. Also $\mu_T$ is tame and not unramified.
2. *The Weil factor.* For $x_v = 1$, the coefficient $c_\Phi$ at $x\iota(y)$ times $\overline{c(1)}$ equals $c_\Phi(x)$ times $\overline{c(y)}$, where $c$ is the coefficient of the local Weil representation of the last section with $\xi = \mu_T$ and $\mu_0 = 1$. The node gap condition enters here.
3. *The automorphic factor.* The function $y \mapsto \langle R(x\iota(y))\overline{F_1}, \overline{F_2}\rangle$ is $\ell(\pi(y)u)$, with $\pi$ right translation on $L^2$, $u = \overline{F_1}$ and a linear form $\ell$. By the hypothesis on $F_1$, the vector $u$ is generic of type $\mu_T$, and $\ell$ has dual type $\mu_T$. The rapid decay of cusp forms puts the forms in $L^2$.
4. *The local integral.* [The theorem on the doubling integral at a twist place](/entry/local-zeta-twisted/), with $\mu_0 = 1$ and $l = k$, gives $c(1) \neq 0$ and a function $\zeta_0$ with $\zeta_0 = 1$ on $J$ and $\overline{c(g)}\,\ell(\pi(g)u) = \overline{c(1)}\,\zeta_0(g)\,\ell(u)$. It also gives $\int \zeta_0 H^{s - t/2} = L(s+\frac12, \alpha)L(s+\frac12, \alpha^{-1})\prod_{i=1}^{kt}(1 - q^{-(2s+i)})$, where $\alpha$ is the multiset of parameters of $F_1$ divided by $\mu_T(\varpi)$. At $s = t/2$ the parameters are the segments of the chain, and this product is $\ell_{\mathfrak{P}}$.
5. *Assembly.* The height splits: $H_a(x \cdot e(y)) = H_a(x)\, H(y)$, and $H = 1$ on $J$. Put $\zeta = (\zeta_0 H^{z - t/2}) \circ e^{-1}$, and let $\mu$ be the image under $e$ of the Haar measure of $\mathrm{GL}_{r+kt}(F_v)$ with $J$ of volume one. Then claim 1 is claim 5 of the theorem on charts, claim 2 is step 4 at $z = t/2$ (where $H^{z - t/2} = 1$), and claim 3 follows from steps 2 to 4 after cancelling $\overline{c(1)} \neq 0$.

This proves the theorem. $\square$

**Remark 2.3.4 (Formalization).** The theorem on charts is a relay to `GlobalTheory.ChartTwist.chart_dict` in [SplitPlaceChartParahoricLevelStabiliserHeight.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SplitPlaceChartParahoricLevelStabiliserHeight.lean#L32). That proof collects eight lemmas, one for each claim; we have read their statements, not their proofs, so the arguments given for claims 1 and 3 to 6 are summaries of those statements. The same holds for the lemmas behind steps 1, 2 and 4 of the second proof, among them the evaluation of the $L$-factors at $s = t/2$. The local factor theorem is at [FlatIntegrandLocalFactorSplitsTwistPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FlatIntegrandLocalFactorSplitsTwistPlace.lean#L164). Claim 2 is stated only at $z = t/2$; for other $z$ the theorem gives only the integrability of $\zeta$. We have not unfolded the Weil coefficient, the doubling height, the matrix coefficient of right translation, the measure of covolume one, the majorant, the level group and the level character; the descriptions above follow their names and the statements of the lemmas that use them.
